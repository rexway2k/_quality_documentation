# L3 — Error Handling & Recovery Testing

## What

Error Handling & Recovery Testing validates whether an agent responds appropriately when something goes wrong.

This includes how the agent detects failures, communicates them, recovers from them, retries, escalates, or safely stops.

---

## Why

Agentic systems must be expected to encounter errors.

Errors may come from:
- Tool failures
- Missing data
- Timeout conditions
- Invalid responses
- User corrections
- Conflicting information
- Workflow interruptions

Error Handling & Recovery Testing helps prevent small failures from becoming larger system or user-impacting failures.

---

## Where

Error Handling & Recovery Testing applies to:
- Tool-using agents
- Multi-step workflows
- Long-running tasks
- Systems with external dependencies
- Agents that interact with APIs or services
- Agents that may need to retry, fallback, or escalate

This test type belongs at L3 because it validates how the agent responds to failure during agentic execution.

---

## When

Error Handling & Recovery Testing may occur:
- During workflow design
- During tool integration testing
- Before production release
- After adding or changing tools
- During resilience testing
- During regression testing
- During incident analysis

---

## How

Error handling may be validated through:
- Simulated tool failures
- Timeout testing
- Invalid response testing
- Missing data scenarios
- Conflicting information scenarios
- Retry behavior validation
- Fallback path validation
- Escalation testing
- Trace review of failure handling

Testing should include both recoverable and non-recoverable failures.

---

## Failure Modes

Common failure modes include:
- Agent ignores error
- Agent hides error from user
- Agent retries endlessly
- Agent repeats failed action without change
- Agent proceeds after failed prerequisite
- Agent gives false success message
- Agent fails to escalate
- Agent loses workflow state after error
- Agent provides misleading recovery guidance
- Agent takes unsafe fallback action

---

## Verification / Signals

Verification signals may include:
- Error detection rate
- Correct recovery rate
- Retry success rate
- Escalation correctness
- False success count
- Unhandled error count
- Recovery path pass rate
- Human review of failure traces

---

## Key Note

Good agentic systems do not only succeed correctly.

They must also fail safely, visibly, and recoverably.