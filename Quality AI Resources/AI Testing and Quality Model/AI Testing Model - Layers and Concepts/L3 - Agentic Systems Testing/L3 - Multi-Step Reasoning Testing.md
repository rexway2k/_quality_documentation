# L3 — Multi-Step Reasoning Testing

## What

Multi-Step Reasoning Testing validates whether an agent can reason across multiple steps, intermediate results, and changing context.

This test type evaluates whether reasoning remains coherent as the agent progresses through a task.

---

## Why

An agent may reason correctly in a single response but fail when reasoning must continue across multiple actions.

Multi-Step Reasoning Testing helps bound the risk of:
- Broken logic across steps
- Incorrect use of intermediate results
- Loss of task intent
- Poor adaptation to new information
- Invalid conclusions after tool results
- Compounding errors across a workflow

---

## Where

Multi-Step Reasoning Testing applies to tasks requiring sequential reasoning or iterative decision-making.

It may apply to:
- Research agents
- Planning agents
- Troubleshooting agents
- Decision-support agents
- Agents that call tools and interpret results
- Agents that decompose tasks into subtasks
- Agents that revise a plan based on new information

This test type belongs at L3 because it validates reasoning across a process, not just a single model response.

---

## When

Multi-Step Reasoning Testing may occur:
- During agent design
- During workflow design
- Before release of agentic capabilities
- After prompt or orchestration changes
- After tool integration changes
- During regression testing
- During incident analysis

---

## How

Multi-step reasoning may be validated through:
- Multi-step scenario tests
- Trace analysis
- Reviewing intermediate reasoning checkpoints
- Comparing actual reasoning path to expected logic
- Testing tasks with changing information
- Testing tasks requiring conditional branching
- Testing whether tool results are interpreted correctly
- Human review of reasoning quality across the full process

Testing should evaluate whether the agent’s reasoning remains aligned from start to finish.

---

## Failure Modes

Common failure modes include:
- Correct first step but incorrect later step
- Intermediate result misinterpreted
- Original goal lost
- Tool output used incorrectly
- Agent fails to update reasoning after new information
- Agent repeats earlier reasoning despite changed context
- One error compounds into larger failure
- Final action does not follow from prior steps
- Reasoning appears plausible but violates task constraints

---

## Verification / Signals

Verification signals may include:
- Multi-step scenario pass rate
- Intermediate reasoning review score
- Tool-result interpretation accuracy
- Goal retention score
- Branching decision accuracy
- Error propagation count
- Human review of reasoning trace
- Reduction in reasoning failures after prompt or orchestration improvements

---

## Key Note

Multi-Step Reasoning Testing differs from L1 Reasoning Quality Testing.

L1 evaluates reasoning inside a single response.

L3 evaluates reasoning across actions, steps, tools, and changing state.