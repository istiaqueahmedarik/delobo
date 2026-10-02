# de-lobotomy

A portable agent skill that keeps you involved in software design and implementation: understand the task, approve the abstract design, then build in small, explained, verified steps.

The repository contains one shared skill plus compatible manifests for Codex, Claude Code, and Agent Plugins hosts. It has no runtime dependencies, credentials, hooks, or network services.

## Install on another PC

Requirements: Git and Python 3.9 or newer.

```bash
git clone https://github.com/istiaqueahmedarik/delobo.git
cd delobo
python3 install.py --user
```

This installs the skill at `~/.agents/skills/de-lobotomy`, the user-level location discovered by Codex. Restart Codex if it is already running, then invoke:

```text
$de-lobotomy Help me add a todo-list feature.
```

To make it available only inside one project:

```bash
python3 install.py --project /path/to/project
```

That installs it at `/path/to/project/.agents/skills/de-lobotomy`.

## Update an installation

```bash
git pull --ff-only
python3 install.py --user --upgrade
```

Use `--project /path/to/project --upgrade` for a project-scoped copy. Without `--upgrade`, the installer refuses to replace a different existing copy. Re-running it against an identical copy is a safe no-op.

## Use with Claude Code

Clone the repository, then load the repository itself as a plugin:

```bash
claude --plugin-dir /absolute/path/to/delobo
```

Invoke it as:

```text
/de-lobotomy:de-lobotomy Help me add a todo-list feature.
```

## Validate locally

```bash
python3 install.py --check
python3 -m unittest discover -s tests -v
```

The installer uses only the Python standard library, stages and verifies files before installation, refuses symbolic-link destinations, and does not modify application source code.

See [GUIDE.md](GUIDE.md) for the workflow, checkpoints, resume behavior, help modes, and design rationale.
