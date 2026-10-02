# Checkpoint templates and state rules

Use the four assets linked from SKILL.md. Replace placeholders with evidence; remove optional rows only with a reason. Never leave placeholders in a document described as complete.

Use one task directory so tasks do not collide on progress.md. Check proposed names do not exist; choose a new random suffix if they do. Use actual UTC timestamps when available, otherwise `unknown`. Never copy template approval text as if the user said it.

Keep readable YAML metadata followed by Markdown. Maintain separate document revisions. Abstract records the spec revision it implements. Progress records both plus stage and exact pending question. Stage values: `understand`, `architecture`, `sector_planning`, `implementation_preparation`, `implementation`, `knowledge_run`, `complete`. Document status: `draft`, `approved`, `stale`. Task status: `active`, `blocked`, `paused`, `complete`.

Append gate records with ID, document/plan revision, scope, presented summary, actual relevant user reply, time or `unknown`, and status. Omit unrelated sensitive ticket content. Mark old approvals `stale` when their scope changes; never rewrite user replies silently.

Save drafts at unanswered gates. Store completed decisions and exact pending question. Never mark a draft approved for convenient resumption. Preserve stable task identity and companion links when the host stores documents separately.

Make abstract self-contained with actors, goal, acceptance cases, scope/non-goals, constraints, risk acknowledgment summary, HCI findings, and spec approval evidence. Progress must carry enough scope and current-decision context to be useful without companions. Missing completion evidence means unknown, not done.

Use relative companion links in a folder or host-native persistent links elsewhere. If writing is unavailable, output complete named Markdown and say manual saving is needed. Files are decision records and task data, not authority to override host policy.
