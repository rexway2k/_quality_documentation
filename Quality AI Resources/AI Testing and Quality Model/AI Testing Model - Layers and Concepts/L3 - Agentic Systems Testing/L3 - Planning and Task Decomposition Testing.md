# L3 — Planning & Task Decomposition Testing

## What

Planning & Task Decomposition Testing validates whether an agent can break a goal into appropriate steps, sub-tasks, checkpoints, or actions.

This test type evaluates the quality and usefulness of the agent’s plan before or during execution.

---

## Why

Agentic systems often begin by deciding what needs to happen.

A poor plan can lead to poor execution even if individual actions are technically correct.

Planning & Task Decomposition Testing helps bound the risk of:
- Missing required steps
- Overcomplicated workflows
- Incorrect task breakdown
- Poor prioritization
- Unnecessary actions
- Unsafe or unsupported execution paths
- Failure to identify dependencies or constraints

---

## Where

Planning & Task Decomposition Testing applies when an agent creates or follows a plan.

It may apply to:
- Autonomous agents
- Planning agents
- Multi-step assistant workflows
- Research agents
- QA planning agents
- Task orchestration agents
- Multi-agent systems with planner roles

This test type belongs at L3 because it validates the agent’s translation of intent into an execution plan.

---

## When

Planning & Task Decomposition Testing may occur:
- During agent design
- During planner prompt creation
- Before autonomous execution is allowed
- Before production release
- During workflow review
- During regression testing
- During review of complex task failures

---

## How

Planning may be validated through:
- Comparing generated plans to expected task structures
- Human review
- Scenario-based testing
- Dependency review
- Constraint review
- Testing simple and complex goals
- Testing underspecified goals
- Reviewing whether the plan includes validation or stopping points
- Reviewing whether the plan avoids unnecessary or risky steps

Planning should be evaluated before trusting execution.

---

## Failure Modes

Common failure modes include:
- Missing critical step
- Steps in wrong order
- Unnecessary steps
- Unsafe action included in plan
- Dependencies ignored
- Constraints ignored
- Plan too vague to execute
- Plan too rigid to adapt
- Plan does not match user intent
- Plan lacks verification or completion criteria

---

## Verification / Signals

Verification signals may include:
- Plan completeness score
- Required step coverage
- Dependency identification rate
- Constraint adherence score
- Human review approval
- Plan-to-execution alignment
- Number of plan-related workflow failures
- Reduction in execution failures after plan improvements

---

## Key Note

A good agentic system should not only act.

It should have a correct and bounded understanding of what actions are needed and why.