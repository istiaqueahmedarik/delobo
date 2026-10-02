# de-lobotomy

A portable plugin for understanding a task together, agreeing on its design, and learning through small implementation steps.

Version: 1.0.0

## Set it up

Clone the repository on the computer where you want to use it. The installer requires Python 3.9 or newer and uses only the standard library.

```bash
git clone https://github.com/istiaqueahmedarik/delobo.git
cd delobo
```

For **Codex**, install it for your user account:

```bash
python3 install.py --user
```

Or install it only for one project:

```bash
python3 install.py --project /path/to/your/project
```

Restart Codex if needed, then invoke:

```text
$de-lobotomy Add a button to create a todo list.
```

For **Claude Code**, load the cloned repository directly:

```bash
claude --plugin-dir /absolute/path/to/delobo
```

Then invoke its skill:

```text
/de-lobotomy:de-lobotomy Add a button to create a todo list.
```

For another **Agent Plugins-compatible host**, import the cloned repository using that host's documented method. The root manifest uses Agent Plugins 1.0.0. For an **Agent Skills-compatible host**, install the `skills/de-lobotomy/` folder in its documented skill directory. For an agent without either format, provide `SKILL.md`, the references, and templates and explicitly ask it to follow the workflow. A host without file writing can output the checkpoint documents for manual saving.

The repository includes a root portable manifest, Codex and Claude Code compatibility manifests, and one shared skill. The installer stages and verifies the skill before copying it. It does not add hooks, launch a server, obtain credentials, or change application code.

To update an installed copy, pull the repository and opt in to replacement:

```bash
git pull --ff-only
python3 install.py --user --upgrade
```

Use the corresponding `--project` command for a project-scoped installation. Without `--upgrade`, a different existing copy is preserved.

## Start

```text
Use de-lobotomy for this ticket: <paste ticket, task, or prompt>.
Guide me through understanding, architecture, and implementation.
```

The first response explains what the agent understood and asks a small set of consequential questions. The agent should not dump the entire questionnaire or begin implementing.

## Workflow

| Step | What happens | Checkpoint |
| --- | --- | --- |
| Understand | Explain actor, current behavior, desired outcome; interview; distinguish facts and assumptions | Draft progress |
| Review | Examine regression risks through inversion; review human interaction, including backend operators | `<name>_spec.md` |
| Approve spec | Show the actual specification and obtain a scoped approval | Approved spec revision |
| Big picture | Explain only the necessary conceptual components and data flow; confirm the idea | Architecture draft |
| Sequence | Compare feasible orders; user chooses or amends one | `<name>_abstract.md` |
| Sector planning | State location and goal; user selects verify, research, or answer; agree on microtask order | `progress.md` |
| Test role | Ask whether the user will author tests or the agent will | Test preference in progress |
| Implement | Explain purpose and small approach; make the approved coherent edit; run relevant checks; pause before next step | Edit/check evidence in progress |
| Knowledge run | Brief teach-back, corrections, and reviewed learning preferences | `learning.md` |

Each task gets a separate folder and a unique name such as `todo-lists-20261002-a19f7c`. `progress.md` stays inside that folder, so parallel tasks do not overwrite one another.

No implementation identifiers, source code, test code, concrete schemas, or exact endpoints belong in the spec and abstract design. Authorized read-only inspection can inform them. Implementation details become appropriate after the architecture and sector planning gates pass.

## The three help modes

At each sector, the agent first states where you are and the goal, then asks how to help without giving away a solution:

1. **Verify my answer:** you propose; it checks against requirements and evidence.
2. **Research so I can answer:** it supplies sourced facts and uncertainty; you decide.
3. **Answer and explain:** it proposes a solution with brief reasons; you approve or challenge it.

You may explicitly choose one mode for the whole task. Guided mode still pauses at substantive decisions. You may also approve a bounded batch of already-agreed minor steps. New scope or material risks reopen the affected decision.

## Resume in a new session

Supply one of the task's documents and say:

```text
Use de-lobotomy. Resume from this checkpoint at its next unresolved decision.
Preserve approvals for unchanged scope and check actual project state where relevant.
```

- An approved **spec** resumes at architecture.
- An approved **abstract** includes the scope snapshot and resumes at sector planning.
- **Progress**, with available companions, resumes the current decision or microtask.
- A **draft** resumes its unanswered gate. Merely having a file is not approval.

When available, carry all companions together. Include the reviewed learning file in future tasks if you want the agent to use those preferences. The plugin does not guarantee hidden memory across agents or sessions.

## Critique of the original process

Your strongest ideas are explaining the task back to the user, separating design from implementation, surfacing damage to existing behavior, and preserving portable checkpoints. Those make the user an active decision-maker.

Six points need correction:

1. **“No confusion” has no achievable proof.** Stop when consequential blockers are resolved, assumptions are explicit, and the user approves observable acceptance cases. Keep room to discover new information later.
2. **Relentless questioning can exhaust the user.** Be persistent about decisions that affect behavior or architecture; ask one to three questions at a time and never repeat settled ones. Use a teach-back for a consequential misunderstanding, not every detail.
3. **“Developers never write imports first” is false.** Coding order varies with language and person. Teach behavior first and explain the dependency as it becomes relevant, while writing valid code in the project's style. The order of an explanation need not be the literal file-editing order.
4. **The smallest possible fraction is not always the best learning unit.** A useful microtask has one purpose and a checkable result. Half a statement or an invalid function fragment adds friction without a useful checkpoint.
5. **Sequence options must respect real dependencies.** A storage-first order can be valid, and a UI-first prototype can be valid; neither is always best. Explain when only one order is feasible instead of inventing choices.
6. **A universal package cannot guarantee universal obedience.** This uses common formats and native manifests, but model behavior, tools, permissions, and host support vary. The gates are workflow instructions, not a security boundary. HCI review likewise identifies design issues; it does not prove usability without evidence from real users.

The knowledge run checks demonstrated understanding and records preferences you confirm. It should not claim to read your thought process, assign an intelligence score, or store inferred personal traits.

## Compatibility and verification

The shared skill uses only standard name/description frontmatter, Markdown, and templates. The workflow does not require a particular UI widget, shell, external account, or paid API. Research and test execution depend on the host's available tools.

Validate the checkout with `python3 install.py --check` and `python3 -m unittest discover -s tests -v`. Claude Code and Codex native loading must still be checked in those applications on your machine. Use `claude plugin validate /absolute/path/to/delobo` where available, and verify Codex lists `$de-lobotomy` after installation.

## Format references

- [Agent Skills specification](https://agentskills.io/specification)
- [Portable plugin packaging and Codex compatibility](https://developers.openai.com/plugins/build/plugins)
- [Codex local skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code plugin creation and loading](https://code.claude.com/docs/en/plugins/create)

These references establish packaging and discovery conventions. The de-lobotomy interview, gates, learning flow, and checkpoint design are custom behavior in this plugin.
