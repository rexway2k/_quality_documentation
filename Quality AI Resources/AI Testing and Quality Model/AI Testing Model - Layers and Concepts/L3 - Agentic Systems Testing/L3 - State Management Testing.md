# L3 — State Management Testing

## What

State Management Testing validates whether an agent correctly tracks and uses the current state of a task, workflow, session, or interaction.

State includes what has happened, what is currently true, what remains to be done, and what decisions have already been made.

---

## Why

Agentic workflows depend on changing state over time.

If state is incorrect or lost, the agent may:
- Repeat completed steps
- Skip required steps
- Use outdated information
- Make decisions based on conditions that are no longer true
- Fail to complete the workflow correctly

State Management Testing helps ensure the agent understands its current position in the workflow.

---

## Where

State Management Testing applies to:
- Multi-step workflows
- Conversational agents
- Task execution agents
- Long-running processes
- Agents with session context
- Agents that handle approvals, decisions, or branching paths
- Systems where prior actions affect future actions

This test type belongs at L3 because it validates the agent’s awareness and use of state during execution.

---

## When

State Management Testing may occur:
- During workflow development
- During agent orchestration design
- Before production release
- After changing memory, session, or state handling
- During regression testing
- During replay of failed workflows
- During testing of interrupted or resumed tasks

---

## How

State management may be validated through:
- Scenario-based workflow testing
- State transition checks
- Trace review
- Session continuity testing
- Testing paused and resumed workflows
- Testing branching workflows
- Testing repeated user inputs
- Comparing expected state to actual state after each step
- Validating that state updates occur after tool calls or decisions

Testing should validate both state storage and state interpretation.

---

## Failure Modes

Common failure modes include:
- State lost between steps
- Incorrect state retained
- Completed step repeated
- Required step skipped
- Agent acts on outdated state
- User correction not reflected in state
- Tool result not incorporated into state
- Session resume starts from wrong point
- Branching decision based on incorrect state
- State becomes inconsistent across components

---

## Verification / Signals

Verification signals may include:
- State transition accuracy
- Session continuity success rate
- State mismatch count
- Workflow replay accuracy
- Correct resume rate
- Step repeat or skip count
- Human trace review results
- Reduction in state-related defects after design improvements

---

## Key Note

State is not the same as memory.

State is the current operational condition of the workflow.

Memory is information retained and reused across time.