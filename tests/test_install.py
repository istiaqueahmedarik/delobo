from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "install.py"
SOURCE = ROOT / "skills" / "de-lobotomy"


def run_installer(
    *arguments: str, env: Optional[dict] = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), *arguments],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def file_bytes(directory: Path) -> dict[str, bytes]:
    return {
        path.relative_to(directory).as_posix(): path.read_bytes()
        for path in directory.rglob("*")
        if path.is_file()
    }


class InstallerTests(unittest.TestCase):
    def test_checkout_validation(self) -> None:
        result = run_installer("--check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Package validation passed", result.stdout)

    def test_project_install_and_repeat_are_safe(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            first = run_installer("--project", str(project))
            self.assertEqual(first.returncode, 0, first.stderr)
            destination = project / ".agents" / "skills" / "de-lobotomy"
            self.assertEqual(file_bytes(destination), file_bytes(SOURCE))

            second = run_installer("--project", str(project))
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("Already installed and up to date", second.stdout)

    def test_conflict_is_preserved_without_upgrade(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            self.assertEqual(run_installer("--project", str(project)).returncode, 0)
            skill_file = project / ".agents" / "skills" / "de-lobotomy" / "SKILL.md"
            skill_file.write_text("local change\n", encoding="utf-8")

            result = run_installer("--project", str(project))
            self.assertEqual(result.returncode, 2)
            self.assertIn("--upgrade", result.stderr)
            self.assertEqual(skill_file.read_text(encoding="utf-8"), "local change\n")

    def test_upgrade_replaces_a_different_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            self.assertEqual(run_installer("--project", str(project)).returncode, 0)
            destination = project / ".agents" / "skills" / "de-lobotomy"
            (destination / "SKILL.md").write_text("old copy\n", encoding="utf-8")

            result = run_installer("--project", str(project), "--upgrade")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Upgraded", result.stdout)
            self.assertEqual(file_bytes(destination), file_bytes(SOURCE))

    def test_user_install_respects_home_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            environment = os.environ.copy()
            environment["HOME"] = temporary
            result = run_installer("--user", env=environment)
            self.assertEqual(result.returncode, 0, result.stderr)
            destination = Path(temporary) / ".agents" / "skills" / "de-lobotomy"
            self.assertEqual(file_bytes(destination), file_bytes(SOURCE))


if __name__ == "__main__":
    unittest.main()
