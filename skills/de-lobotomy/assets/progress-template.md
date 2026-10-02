---
workflow: de-lobotomy
task_id: <name>
artifact: progress
revision: 1
spec_revision: <number or unavailable>
abstract_revision: <number or unavailable>
stage: understand
status: active
updated_at: <actual UTC timestamp or unknown>
---

# <Task title> — progress

## Resume capsule

- Goal/scope: <approved snapshot or not yet approved>
- Location: <stage, sequence item, sector, microtask>
- Implementation started: <yes/no>
- Last completed decision/action: <actual result>
- Exact next question/action: <one next step>
- Blockers/unknowns: <actual items>
- Pace/delegation: <guided default; exact bounded delegation if any>
- Tests: <undecided/user-authored/agent-authored/mixed; chosen order>
- Companions: [spec](<name>_spec.md), [abstract](<name>_abstract.md)
- Learning record: [learning](learning.md), if created

## Approved sequence

| ID/order | Sector and goal | Prerequisite | Status | Evidence |
| --- | --- | --- | --- | --- |
| S1 | <goal> | <dependency> | <pending/in_progress/blocked/done> | <actual evidence or none> |

## Sector decisions

### <Sector ID and name>

Where we are: <sequence location>

Goal: <observable result>

Help mode: <unselected/verify/research/answer>

User proposal/research topic: <actual input>

Evidence/validation: <facts, sources, checks, uncertainty>

Decision and alternatives: <actual choice, reason, tradeoff>

Microtask-order approval: <actual reply, revision, scope, time or pending>

| Microtask | Goal/scope | Dependency | Status | Agreed check | Actual result |
| --- | --- | --- | --- | --- | --- |
| S1.M1 | <small coherent purpose> | <dependency> | pending | <observable check> | not run |

## Gate ledger

| Gate | Revision/scope | Presented summary | Actual user reply | Time | State |
| --- | --- | --- | --- | --- | --- |
| <gate ID> | <revision/scope> | <summary> | <reply or pending> | <time/unknown> | <pending/approved/stale> |

## Edit and verification history

| Microtask | Change and why | Check/cases | Actual result | Remaining limit |
| --- | --- | --- | --- | --- |
| <ID> | <meaningful change> | <check actually run> | <pass/fail/not run and evidence> | <limit> |

Record project paths and identifiers here only after implementation begins. Unavailable checks are not passed checks.

## Revisions, risks, and drift

<Actual changes, affected approvals marked stale, new risks/acknowledgments, and checked drift. Preserve prior decisions.>

## Completion

Acceptance results: <per-case evidence or incomplete>

Knowledge run: <pending/completed/explicitly declined>

Learning record review: <actual correction/approval/explicit opt-out or pending>

Unresolved limitations: <actual limits>
