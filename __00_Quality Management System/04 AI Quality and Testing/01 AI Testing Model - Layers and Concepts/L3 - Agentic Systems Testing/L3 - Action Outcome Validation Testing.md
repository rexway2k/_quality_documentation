# L3 — Action Outcome Validation Testing

## What

Action Outcome Validation Testing validates whether an agent’s action produced the intended outcome.

This test type evaluates the relationship between what the agent did and whether that action achieved the expected result.

---

## Why

An agent may call the right tool with the right parameters but still fail to achieve the intended outcome.

Action Outcome Validation Testing helps bound the risk of:
- False success reporting
- Unverified action completion
- Partial task completion
- Incorrect system state after action
- User being told something happened when it did not
- Broken workflows that appear successful

---

## Where

Action Outcome Validation Testing applies after an agent takes an action.

It may apply to:
- Tool calls
- Workflow steps
- Data updates
- Search actions
- Record creation or modification
- Notifications
- Retrieval actions
- Multi-step process outcomes

This test type belongs at L3 because it validates agent action results before broader system integration validation at L4.

---

## When

Action Outcome Validation Testing may occur:
- During agent workflow testing
- During tool integration validation
- Before production release
- After tool behavior changes
- During regression testing
- During trace review
- During incident investigation

---

## How

Action outcomes may be validated through:
- Checking returned tool results
- Comparing expected vs actual action outcome
- Validating state after action
- Reviewing logs or traces
- Confirming downstream response reflects actual result
- Testing partial success conditions
- Testing failed action conditions
- Testing whether the agent verifies completion before responding

Testing should distinguish between “tool call succeeded” and “task outcome succeeded.”

---

## Failure Modes

Common failure modes include:
- Agent reports success without verification
- Tool call succeeded but task failed
- Partial outcome treated as complete outcome
- Incorrect system state after action
- Agent ignores failed tool result
- Agent misinterprets tool response
- Agent does not confirm completion
- Final message overstates what happened
- Action outcome does not match user intent

---

## Verification / Signals

Verification signals may include:
- Outcome validation success rate
- False success count
- Partial completion detection rate
- State verification pass rate
- Tool result interpretation accuracy
- Completion confirmation rate
- Human review of action traces
- Reduction in outcome mismatch defects

---

## Key Note

An agentic workflow should not stop at “the action was attempted.”

It should verify whether the intended outcome was actually achieved.