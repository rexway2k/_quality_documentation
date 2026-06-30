# L3 — Decision Logic Testing

## What

Decision Logic Testing validates whether an agent makes correct decisions based on available inputs, context, rules, constraints, and workflow state.

This test type focuses on the agent’s choice among possible paths, actions, or conclusions.

---

## Why

Agentic systems often decide what should happen next.

Incorrect decisions can lead to:
- Wrong actions
- Missed escalation
- Incorrect routing
- Unsafe automation
- Misapplied business rules
- Inconsistent outcomes across similar scenarios

Decision Logic Testing helps ensure the agent’s choices are appropriate and bounded.

---

## Where

Decision Logic Testing applies where agents choose between options.

It may apply to:
- Routing decisions
- Escalation decisions
- Tool-use decisions
- Workflow branch decisions
- Recommendation decisions
- Approval or stop/go decisions
- Next-best-action workflows
- Multi-agent coordination decisions

This test type belongs at L3 because it validates decision behavior inside an agentic process.

---

## When

Decision Logic Testing may occur:
- During workflow design
- During agent prompt and policy design
- Before release
- After business rule changes
- After model or prompt changes
- During regression testing
- During review of unexpected agent behavior

---

## How

Decision logic may be validated through:
- Scenario-based testing
- Decision table review
- Expected decision comparison
- Boundary condition testing
- Constraint testing
- Trace review
- Human review of decision rationale
- Testing similar scenarios for consistent decisions
- Testing edge cases and exception conditions

Decision Logic Testing should include cases where the correct decision is to stop, ask for clarification, or escalate.

---

## Failure Modes

Common failure modes include:
- Wrong decision selected
- Similar cases handled inconsistently
- Business rule ignored
- Constraint ignored
- Escalation missed
- Agent proceeds when it should stop
- Agent stops when it should proceed
- Incorrect branch selected
- Decision based on incomplete information
- Decision rationale does not support the selected action

---

## Verification / Signals

Verification signals may include:
- Decision accuracy rate
- Scenario pass rate
- Branch selection accuracy
- Escalation correctness
- Constraint adherence score
- Human review of decision rationale
- Inconsistent decision count
- Reduction in decision-related failures after tuning

---

## Key Note

Decision Logic Testing should not assume that a fluent explanation means the decision was correct.

The selected decision must be validated against expected rules, risks, and constraints.