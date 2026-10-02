---
workflow: de-lobotomy
task_id: <name>
artifact: spec
revision: 1
status: draft
updated_at: <actual UTC timestamp or unknown>
---

# <Task title> — specification

## Input and AI interpretation

Input source: <ticket/task/prompt; minimal necessary reference>

My understanding: <actor, current behavior, desired change, observable outcome>

## First principles

- Outcome and why it matters: <goal>
- Actors and needs: <who and what>
- Necessary constraints: <evidenced constraints>
- Smallest useful change: <behavior, no implementation>
- Could existing capabilities solve it? <decision and reason>

## Scope and success

In scope: <agreed behavior>

Out of scope: <boundaries>

| Case | Situation/input | Observable expected result |
| --- | --- | --- |
| A1 | <normal case> | <result> |
| A2 | <important failure/edge> | <safe useful behavior> |

## Evidence, assumptions, and interview decisions

| ID | Fact/assumption/unknown | Source or reasoning | Actual user answer/status |
| --- | --- | --- | --- |
| Q1 | <item> | <source or unverified> | <reply or unanswered> |

## Inversion and existing behavior

| Risk | Existing behavior/failure mode | Consequence | Protection/alternative | User acknowledgment |
| --- | --- | --- | --- | --- |
| R1 | <concrete case; mark hypothesis if unverified> | <effect> | <decision> | <actual reply or pending> |

## HCI review

| Finding/dimension | Actor | Severity/protection | Resolution or reason not applicable |
| --- | --- | --- | --- |
| <finding> | <actor> | <impact and protection> | <resolved/accepted/open/NA with reason> |

## Open blockers

<Actual unanswered blockers, otherwise none.>

## Spec gate

Gate/revision/scope: <spec approval and scope>

Presented summary: <what was actually shown>

User reply: <verbatim relevant reply or pending>

Recorded at: <timestamp or unknown>

State: <pending/approved/stale>

Next step: <architecture if approved, otherwise exact pending question>

Companions: [progress](progress.md), [abstract](<name>_abstract.md)
