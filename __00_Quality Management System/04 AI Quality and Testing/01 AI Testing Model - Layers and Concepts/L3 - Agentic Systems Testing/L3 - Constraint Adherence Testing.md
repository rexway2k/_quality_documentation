# L3 — Constraint Adherence Testing

## What

Constraint Adherence Testing validates whether an agent stays within defined rules, boundaries, permissions, scope, and operating constraints while completing a task.

This test type evaluates whether the agent respects the limits placed on its behavior.

---

## Why

Agentic systems can drift beyond the intended scope of a task.

Constraints are necessary to prevent unintended, unsafe, unauthorized, or excessive actions.

Constraint Adherence Testing helps bound the risk of:
- Scope drift
- Unauthorized action
- Policy violation
- Excessive autonomy
- Unsafe workflow behavior
- Ignoring user or system limits
- Acting beyond intended authority

---

## Where

Constraint Adherence Testing applies across agentic workflows where the system has rules or limits.

It may apply to:
- Tool access boundaries
- User permission boundaries
- Workflow scope
- Approved action lists
- System prompts
- Business rules
- Safety boundaries
- Escalation rules
- Human-in-the-loop requirements

This test type belongs at L3 because it validates whether the agent behaves within its operating boundaries during action and decision-making.

---

## When

Constraint Adherence Testing may occur:
- During agent design
- During prompt and tool configuration
- Before enabling autonomous actions
- Before production release
- After permission or policy changes
- After tool access changes
- During regression testing
- During governance review

---

## How

Constraint adherence may be validated through:
- Scenario-based testing
- Negative testing
- Permission boundary testing
- Scope boundary testing
- Attempts to trigger unauthorized actions
- Testing ambiguous user requests
- Testing conflicting instructions
- Trace review
- Human review of boundary behavior
- Validation of stop, refuse, or escalate behavior

Testing should include both normal requests and requests that attempt to push the agent beyond its intended limits.

---

## Failure Modes

Common failure modes include:
- Agent acts outside allowed scope
- Agent ignores system constraints
- Agent follows user request over policy boundary
- Agent uses tool without required permission
- Agent performs action requiring human approval
- Agent continues after stop condition
- Agent expands task beyond user intent
- Agent bypasses escalation requirement
- Agent treats suggestion as authorization
- Agent fails to refuse or clarify unsafe requests

---

## Verification / Signals

Verification signals may include:
- Constraint adherence rate
- Unauthorized action count
- Correct refusal rate
- Correct escalation rate
- Boundary test pass rate
- Scope drift incident count
- Human review of constrained scenarios
- Reduction in out-of-scope behavior after guardrail improvements

---

## Key Note

Constraint Adherence Testing is one of the most important test types for agentic systems.

The more autonomy an agent has, the more explicit and testable its constraints must be.