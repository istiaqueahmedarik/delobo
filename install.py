#!/usr/bin/env python3
"""Install the de-lobotomy skill for Codex from this repository checkout."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from typing import Dict, Iterable, Tuple


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "skills" / "de-lobotomy"
MANIFESTS = (
    ROOT / "plugin.json",
    ROOT / ".codex-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "plugin.json",
)


class InstallError(RuntimeError):
    """A user-facing validation or installation error."""


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inventory(directory: Path) -> Dict[str, Tuple[int, str]]:
    """Return a stable inventory and reject links that could escape the package."""
    result: Dict[str, Tuple[int, str]] = {}
    for path in sorted(directory.rglob("*")):
        relative = path.relative_to(directory).as_posix()
        if path.is_symlink():
            raise InstallError(f"Symbolic links are not allowed in the skill: {relative}")
        if path.is_file():
            result[relative] = (path.stat().st_size, file_digest(path))
    return result


def load_manifest(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise InstallError(f"Invalid manifest {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(data, dict):
        raise InstallError(f"Manifest must contain a JSON object: {path.relative_to(ROOT)}")
    return data


def referenced_local_files(skill_markdown: str) -> Iterable[str]:
    """Extract simple relative Markdown links used by this skill."""
    position = 0
    while True:
        start = skill_markdown.find("](", position)
        if start == -1:
            return
        end = skill_markdown.find(")", start + 2)
        if end == -1:
            return
        target = skill_markdown[start + 2 : end].strip()
        position = end + 1
        if target and "://" not in target and not target.startswith("#"):
            yield target.split("#", 1)[0]


def validate_package() -> None:
    if not SOURCE.is_dir():
        raise InstallError(f"Skill source is missing: {SOURCE}")

    skill_file = SOURCE / "SKILL.md"
    if not skill_file.is_file():
        raise InstallError("skills/de-lobotomy/SKILL.md is missing")

    skill_text = skill_file.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        raise InstallError("SKILL.md must start with YAML frontmatter")
    for required_line in ("name: de-lobotomy", "description:"):
        if required_line not in skill_text:
            raise InstallError(f"SKILL.md frontmatter is missing {required_line!r}")

    for relative in referenced_local_files(skill_text):
        candidate = (SOURCE / relative).resolve()
        try:
            candidate.relative_to(SOURCE.resolve())
        except ValueError as exc:
            raise InstallError(f"SKILL.md link escapes the skill directory: {relative}") from exc
        if not candidate.is_file():
            raise InstallError(f"SKILL.md references a missing file: {relative}")

    manifests = [load_manifest(path) for path in MANIFESTS]
    versions = {manifest.get("version") for manifest in manifests}
    names = {manifest.get("name") for manifest in manifests}
    if versions != {"1.0.0"}:
        raise InstallError(f"Manifest versions do not match 1.0.0: {sorted(map(str, versions))}")
    if names != {"de-lobotomy"}:
        raise InstallError(f"Manifest names do not match de-lobotomy: {sorted(map(str, names))}")
    if manifests[1].get("skills") != "./skills/":
        raise InstallError(".codex-plugin/plugin.json must declare skills as ./skills/")

    files = inventory(SOURCE)
    if len(files) < 8:
        raise InstallError("Skill package appears incomplete")


def copy_to_staging(parent: Path) -> Tuple[Path, Path]:
    temporary = Path(tempfile.mkdtemp(prefix=".de-lobotomy-install-", dir=str(parent)))
    staged = temporary / "de-lobotomy"
    try:
        shutil.copytree(SOURCE, staged)
        if inventory(staged) != inventory(SOURCE):
            raise InstallError("The staged copy does not match the source package")
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return temporary, staged


def install(destination: Path, upgrade: bool) -> str:
    validate_package()
    destination = destination.expanduser().resolve()

    if destination.is_symlink():
        raise InstallError(f"Refusing to replace symbolic-link destination: {destination}")
    if destination.exists() and not destination.is_dir():
        raise InstallError(f"Destination exists and is not a directory: {destination}")
    if destination.is_dir():
        if inventory(destination) == inventory(SOURCE):
            return f"Already installed and up to date: {destination}"
        if not upgrade:
            raise InstallError(
                f"A different installation already exists at {destination}. "
                "Re-run with --upgrade to replace it safely."
            )

    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary, staged = copy_to_staging(destination.parent)
    backup = temporary / "previous"
    had_previous = destination.exists()

    try:
        if had_previous:
            os.replace(destination, backup)
        try:
            os.replace(staged, destination)
        except Exception:
            if had_previous and backup.exists() and not destination.exists():
                os.replace(backup, destination)
            raise
    finally:
        shutil.rmtree(temporary, ignore_errors=True)

    action = "Upgraded" if had_previous else "Installed"
    return f"{action} de-lobotomy at {destination}"


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the de-lobotomy skill for Codex without network access."
    )
    target = parser.add_mutually_exclusive_group()
    target.add_argument(
        "--user",
        action="store_true",
        help="install for the current user in ~/.agents/skills/de-lobotomy",
    )
    target.add_argument(
        "--project",
        metavar="PATH",
        type=Path,
        help="install for one project in PATH/.agents/skills/de-lobotomy",
    )
    target.add_argument(
        "--check",
        action="store_true",
        help="validate this checkout without installing anything",
    )
    parser.add_argument(
        "--upgrade",
        action="store_true",
        help="replace a different existing installation after staging a verified copy",
    )
    args = parser.parse_args(list(argv))
    if not (args.user or args.project or args.check):
        parser.error("one of --user, --project, or --check is required")
    if args.check and args.upgrade:
        parser.error("--upgrade cannot be used with --check")
    return args


def main(argv: Iterable[str] = ()) -> int:
    args = parse_args(argv)
    try:
        if args.check:
            validate_package()
            print("Package validation passed.")
            return 0

        if args.user:
            destination = Path.home() / ".agents" / "skills" / "de-lobotomy"
        else:
            project = args.project.expanduser().resolve()
            if not project.is_dir():
                raise InstallError(f"Project directory does not exist: {project}")
            destination = project / ".agents" / "skills" / "de-lobotomy"

        print(install(destination, upgrade=args.upgrade))
        print("Restart Codex if the skill does not appear, then invoke $de-lobotomy.")
        return 0
    except (InstallError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
