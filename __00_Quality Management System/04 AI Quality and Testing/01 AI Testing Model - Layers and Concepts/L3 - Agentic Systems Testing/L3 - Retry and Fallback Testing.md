# L3 — Retry & Fallback Testing

## What

Retry & Fallback Testing validates whether an agent retries failed actions appropriately and uses fallback behavior when primary paths fail or are unavailable.

This test type focuses on resilience patterns within agentic workflows.

---

## Why

Agents often operate in environments where tools, services, or context may fail.

Retries and fallbacks can improve reliability, but they can also create risk if uncontrolled.

Retry & Fallback Testing helps bound the risk of:
- Infinite retry loops
- Duplicate actions
- Unsafe fallback behavior
- Excessive cost or token usage
- Latency issues
- Masked failures
- Incorrect success reporting

---

## Where

Retry & Fallback Testing applies to:
- Tool calls
- API calls
- Retrieval attempts
- Workflow steps
- External dependency use
- Agent recovery paths
- Long-running or multi-step actions

This test type belongs at L3 because it validates agent behavior when execution does not proceed normally.

---

## When

Retry & Fallback Testing may occur:
- During workflow design
- During tool integration testing
- Before release
- During resilience testing
- After dependency changes
- After retry policy changes
- During incident review

---

## How

Retry and fallback behavior may be validated through:
- Simulated service failures
- Forced timeout scenarios
- Rate-limit scenarios
- Temporary failure scenarios
- Permanent failure scenarios
- Duplicate action checks
- Trace review
- Testing maximum retry limits
- Testing fallback path correctness
- Testing user communication when fallback occurs

Retry behavior should be bounded by clear limits and stopping conditions.

---

## Failure Modes

Common failure modes include:
- Infinite retry loop
- Retrying when retry is unsafe
- Fallback used when primary path succeeded
- Fallback produces incorrect result
- Duplicate downstream action
- Excessive latency
- Excessive token or tool consumption
- Failure hidden by fallback
- User not informed fallback occurred
- Agent reports completion when fallback only partially succeeded

---

## Verification / Signals

Verification signals may include:
- Retry limit adherence
- Fallback success rate
- Duplicate action count
- Retry loop detection
- Failure transparency score
- Token/tool cost during retries
- Latency impact
- Correct stop condition rate
- Human review of retry/fallback traces

---

## Key Note

Retries and fallbacks should reduce risk, not hide it.

A fallback path is still a controlled workflow that must be tested.