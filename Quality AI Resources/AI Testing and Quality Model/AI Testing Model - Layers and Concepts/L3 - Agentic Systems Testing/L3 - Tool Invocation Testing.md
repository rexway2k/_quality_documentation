# L3 — Tool Invocation Testing

## What

Tool Invocation Testing validates whether an agent correctly calls a tool, API, function, service, or system capability.

This test type focuses on whether the invocation itself is correct, including the tool name, parameters, required inputs, request structure, and expected usage pattern.

---

## Why

Agentic systems often depend on tools to perform real work.

Even if the model understands the task correctly, the system can fail if it calls the tool incorrectly.

Tool Invocation Testing helps bound the risk of:
- Incorrect API calls
- Invalid parameters
- Missing required fields
- Incorrect field mapping
- Tool misuse
- Failed downstream execution
- Unintended system behavior caused by malformed requests

---

## Where

Tool Invocation Testing applies at the point where the agent attempts to use an external or internal capability.

It may apply to:
- Function calling
- API calls
- MCP tools
- Workflow tools
- Database lookup tools
- Search tools
- Business system actions
- Automation tools
- Agent-accessible services

This test type belongs at L3 because it validates the agent’s action request, not the tool’s internal implementation or the downstream system behavior.

---

## When

Tool Invocation Testing may occur:
- During agent design
- During tool schema definition
- During function calling validation
- Before enabling new tools
- Before production release
- After tool schema changes
- After prompt or instruction changes
- During regression testing of agent workflows

---

## How

Tool invocation may be validated through:
- Schema validation
- Parameter validation
- Required field checks
- Mock tool execution
- Test harnesses
- Trace review
- Scenario-based testing
- Negative testing with missing or invalid inputs
- Reviewing whether the invocation matches the user’s intent

Testing should verify that the agent calls the tool correctly before evaluating whether the tool itself performs correctly.

---

## Failure Modes

Common failure modes include:
- Wrong tool called
- Correct tool called with wrong parameters
- Required parameter omitted
- Invalid parameter value
- Incorrect enum or option selected
- Hallucinated parameter
- Unsupported tool argument
- Tool called prematurely
- Tool called when no tool should have been used
- Tool call does not match user intent

---

## Verification / Signals

Verification signals may include:
- Tool invocation success rate
- Schema validation pass rate
- Parameter accuracy score
- Invalid tool call count
- Missing field count
- Tool call trace review results
- Mock execution pass rate
- Reduction in malformed tool calls after prompt or schema tuning

---

## Key Note

Tool Invocation Testing is not the same as Tool Selection Testing.

Tool Selection asks whether the agent chose the right tool.

Tool Invocation asks whether the agent called that tool correctly.