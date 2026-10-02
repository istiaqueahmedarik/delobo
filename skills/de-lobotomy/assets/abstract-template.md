---
workflow: de-lobotomy
task_id: <name>
artifact: abstract
revision: 1
spec_revision: <approved spec revision>
status: draft
updated_at: <actual UTC timestamp or unknown>
---

# <Task title> — abstract architecture

## Standalone scope snapshot

Actor/goal: <approved intent>

Current/desired behavior: <approved change>

Scope/non-goals: <boundaries>

Constraints/assumptions: <agreed items>

Acceptance cases: <situations and observable results, including important failure cases>

Spec approval evidence: <actual reply, revision, scope, time or pending>

## Big picture

<Conceptual diagram: necessary components, responsibilities, boundaries, and data movement. No code or implementation identifiers.>

| Component/sector | Responsibility | Receives/produces | Existing behavior affected |
| --- | --- | --- | --- |
| <role> | <purpose> | <conceptual data> | <effect> |

## Sequence alternatives and choice

| Option | Conceptual order | Benefit | Dependency/cost |
| --- | --- | --- | --- |
| A | <feasible order> | <benefit> | <tradeoff> |
| B | <alternative only if feasible> | <benefit> | <tradeoff> |

Chosen option/reason: <actual user choice>

| Order/ID | Sector and goal | Prerequisite | Observable exit criterion |
| --- | --- | --- | --- |
| S1 | <responsibility> | <dependency> | <when ready> |

## Protections and unknowns

Risk/acknowledgment snapshot: <behavior, consequence, protection, actual acknowledgment>

HCI findings/protections: <agreed human and operator experience>

Unknowns: <low-impact assumptions or blockers>

## Gate ledger

| Gate | Revision/scope | Presented summary | Actual user reply | Time | State |
| --- | --- | --- | --- | --- | --- |
| Big picture | <revision/scope> | <summary> | <reply or pending> | <time/unknown> | <pending/approved/stale> |
| Sequence | <revision/scope> | <summary> | <reply or pending> | <time/unknown> | <pending/approved/stale> |
| Abstract document | <revision/scope> | <summary> | <reply or pending> | <time/unknown> | <pending/approved/stale> |

## Resume

Stage: <architecture or sector_planning>

Next unresolved question: <exact question or sector help-mode choice>

Implementation has not started unless progress documents actual work.

Companions: [spec](<name>_spec.md), [progress](progress.md)
