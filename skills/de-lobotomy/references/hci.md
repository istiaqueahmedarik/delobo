# Proportionate HCI review

Review real human interaction. For backend-only work, consider API consumers, administrators, support staff, and people affected by failures. Record reasons for non-applicable dimensions.

| Dimension | Questions | Possible acceptance evidence |
| --- | --- | --- |
| Goal/context | Can the actor find and understand the action? What knowledge is assumed? | Actor identifies action and outcome |
| Feedback/state | Are pending, success, failure, and partial completion distinct? | Slow or failed action has observable state |
| Error prevention | Can invalid, duplicate, unauthorized, or accidental actions be prevented? | Invalid/repeated input case |
| Recovery/control | Can the person cancel, retry, recover, or undo where appropriate? | Recovery preserves prior valid state |
| Consistency | Does behavior contradict established terms, defaults, or mental models? | Existing behavior compatible or change explained |
| Accessibility | Are applicable keyboard, assistive-technology, contrast, language, and cognitive needs met? | Relevant action works without pointer; errors understandable |
| Trust/privacy | Is consequential data use, permission, permanence, or uncertainty apparent? | Actor understands consequence before commitment |
| Operators | Can consumers distinguish validation, permission, service, and retryable failures? | Actionable errors without secret disclosure |

Record affected actor, severity, protection, and resolved/accepted/open state. Resolve blockers before spec approval. Carry protections into acceptance cases and architecture; check them during implementation. Keep small-task reviews brief and do not claim this replaces user testing.
