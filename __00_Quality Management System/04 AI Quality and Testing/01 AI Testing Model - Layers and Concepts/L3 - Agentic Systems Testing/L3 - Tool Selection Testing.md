# L3 — Tool Selection Testing

## What

Tool Selection Testing validates whether an agent chooses the correct tool, API, function, or capability for a given task.

This test type focuses on the agent’s decision about which tool should be used.

---

## Why

Agentic systems may have access to multiple tools that appear similar or overlap in capability.

Even if a tool call is technically valid, the system can fail if the wrong tool was selected.

Tool Selection Testing helps bound the risk of:
- Incorrect action path
- Wrong system being used
- Unnecessary tool calls
- Missed tool calls
- Unsafe or inefficient workflows
- Incorrect results caused by using the wrong capability

---

## Where

Tool Selection Testing applies when an agent has access to more than one possible action or tool.

It may apply to:
- Multi-tool agents
- MCP-based systems
- Workflow agents
- Search-and-action agents
- Business process agents
- Customer or employee support agents
- Agents that choose between read, write, update, or execute actions

This test type belongs at L3 because it validates the agent’s decision to use a tool, not the tool execution itself.

---

## When

Tool Selection Testing may occur:
- During agent design
- During tool catalog design
- During workflow testing
- Before enabling tool access
- Before production release
- After tools are added, removed, or changed
- After prompt or routing changes
- During regression testing

---

## How

Tool selection may be validated through:
- Scenario-based testing
- Intent-to-tool mapping validation
- Comparing chosen tools against expected tools
- Testing ambiguous requests
- Testing similar tools with different purposes
- Testing no-tool scenarios
- Reviewing traces of tool decisioning
- Human review of decision appropriateness

Tool Selection Testing should include scenarios where the correct behavior is to ask for clarification, refuse, or avoid tool use.

---

## Failure Modes

Common failure modes include:
- Wrong tool selected
- Tool selected when no tool was needed
- No tool selected when a tool was required
- Read tool used when update tool was required
- Update tool used when only read access was appropriate
- Tool selected based on keyword match rather than intent
- Agent chooses a tool outside the allowed scope
- Agent fails to distinguish between similar capabilities

---

## Verification / Signals

Verification signals may include:
- Correct tool selection rate
- No-tool decision accuracy
- Incorrect tool selection count
- Unnecessary tool call count
- Missed tool call count
- Human decision review score
- Trace-based decision validation
- Improvement after tool description or instruction refinement

---

## Key Note

Tool descriptions are part of the quality boundary.

If an agent selects the wrong tool because tool descriptions are unclear, that is a system design issue, not just a model issue.