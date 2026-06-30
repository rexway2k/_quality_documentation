# L3 — Workflow Execution Testing

## What

Workflow Execution Testing validates whether an agent correctly performs a defined sequence of steps to complete a task.

This test type evaluates whether the process is executed in the correct order, with correct transitions, dependencies, and outcomes.

---

## Why

Agentic capabilities often involve more than one step.

A workflow may fail even when individual steps seem correct.

Workflow Execution Testing helps bound the risk of:
- Steps executed out of order
- Required steps skipped
- Duplicate steps performed
- Workflow stopping too early
- Workflow continuing too long
- Invalid transitions
- Incomplete task completion
- Incorrect state changes across the process

---

## Where

Workflow Execution Testing applies to agentic processes involving multiple steps.

It may apply to:
- Multi-step task agents
- Approval workflows
- Research workflows
- Data lookup and response workflows
- Planning and execution workflows
- Support agents
- Process automation agents
- Multi-tool orchestration patterns

This test type belongs at L3 because it validates agent-driven process flow before validating full external system integration at L4.

---

## When

Workflow Execution Testing may occur:
- During workflow design
- During agent orchestration development
- Before production release
- After workflow changes
- After tool or prompt changes
- During regression testing
- During replay analysis of failed workflows

---

## How

Workflow execution may be validated through:
- Scenario-based testing
- Step trace review
- Expected workflow path comparison
- State transition validation
- Mock workflow execution
- Replay testing
- Testing success paths
- Testing failure paths
- Testing edge cases and alternate paths

Testing should confirm both the final outcome and the steps taken to reach that outcome.

---

## Failure Modes

Common failure modes include:
- Required step skipped
- Step repeated unnecessarily
- Wrong sequence
- Workflow stops prematurely
- Workflow continues after completion
- Invalid branch selected
- Dependency ignored
- Agent loses track of progress
- Workflow outcome does not match requested task
- Process appears complete but missed required validation

---

## Verification / Signals

Verification signals may include:
- Workflow completion rate
- Step sequence accuracy
- Required step coverage
- Invalid transition count
- Workflow trace review results
- Scenario pass rate
- Failure path handling score
- Number of incomplete or incorrectly completed workflows

---

## Key Note

Workflow Execution Testing must validate the path, not just the final answer.

A correct-looking final response may hide an invalid or incomplete workflow.