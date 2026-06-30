# L3 — Agentic Systems Testing

## Purpose

This layer focuses on validating how AI systems act, decide, and operate across multi-step processes.

Agentic Systems Testing evaluates:
- How AI systems plan and execute tasks
- How they interact with tools, APIs, and external systems
- How they maintain state and memory
- How they make decisions within defined constraints

This layer ensures that AI capabilities behave correctly when operating beyond single prompt-response interactions.

---

## Layer Summary

| Dimension | Description |
|---|---|
| Layer | L3 — Agentic Systems |
| Primary Question | Does the system take the right actions and make the right decisions over time? |
| Testing Focus | Orchestration, workflows, tool usage, memory, planning, and decision-making |
| Main Risk | The system performs incorrect, unsafe, or unintended actions despite correct inputs |
| Output of This Layer | Confidence that AI-driven workflows behave correctly and reliably |

---

## What This Layer Tests

This layer tests how AI systems operate over multiple steps and interactions.

It includes validation of:

- Tool selection and invocation
- Workflow execution
- Multi-step reasoning across actions
- Planning and task decomposition
- State management
- Memory usage and persistence
- Decision-making behavior
- Error handling and recovery
- Retry and fallback mechanisms
- Sequence correctness
- Action-result alignment

This layer focuses on what the system does, not just what it says.

---

## What This Layer Does Not Test

This layer does not validate:

- Raw model response quality (L1)
- Retrieval or source selection quality (L2)
- User interface behavior (L4)
- System-level integration correctness across applications (L4)
- Governance, compliance, or policy enforcement (L5)

This layer assumes:
- The model can produce reasonable outputs (L1)
- The system can retrieve appropriate context (L2)

---

## Where This Layer Sits in the AI Testing Model

```text
L5 — Governance / Responsible AI
L4 — System Integration / Experience
L3 — Agentic Systems
L2 — Retrieval / Context (RAG)
L1 — Model / LLM
L0 — Data Foundation

L3 sits between reasoning (L1/L2) and execution within systems (L4).

Why This Layer Matters
Agentic systems introduce a new category of risk:

The system can take action, not just generate output.

Even if:

The model is accurate (L1)
The context is correct (L2)

The system may still fail by:

Choosing the wrong tool
Executing steps in the wrong order
Making incorrect decisions
Misinterpreting state
Losing context across steps
Failing to recover from errors
Performing unintended or unauthorized actions

This layer ensures that AI systems behave correctly over time and across interactions.

Core Risk
The core risk at this layer is that the system performs incorrect or unsafe actions despite receiving correct inputs and context.
This includes:

Incorrect decisions
Invalid tool usage
Broken workflows
Unintended side effects
Failure to complete tasks
Escalation of small errors into larger failures


Layer Responsibility
This layer is responsible for answering:

Does the system choose the correct action?
Does the system use the correct tool?
Does the system follow the correct sequence of steps?
Does the system maintain valid state across interactions?
Does the system remember what it should remember?
Does the system forget what it should forget?
Does the system recover correctly from failure?
Does the system stop when it should stop?
Does the system stay within defined constraints?


Contract Boundary
Input: Intent, task, or system request
Output: Actions taken and resulting system state
This layer validates:

Given a goal or task, the system performs the correct sequence of actions within defined constraints.

This is a shift from:

L1 contract: prompt → response
L2 contract: query → context

to:

L3 contract: intent → actions → outcomes


Relationship to Other Layers
Relationship to L0 — Data Foundation
L3 depends on L0 for:

Input data driving decisions
Structured payloads used in tools
Data correctness influencing actions

Incorrect data can cause incorrect decisions or actions.

Relationship to L1 — Model / LLM
L1 provides:

Reasoning
Language understanding
Instruction-following

L3 depends on L1 for decision-making inputs, but L3 evaluates whether those decisions are executed correctly.

Relationship to L2 — Retrieval / Context
L2 provides context used by agents.
L3 evaluates:

Whether the agent uses that context correctly
Whether retrieved information is applied to decisions and actions


Relationship to L4 — System Integration / Experience
L3 determines what actions should occur.
L4 determines whether those actions actually succeed in the real system.
Example:

L3: selects correct API to call ✅
L4: validates API call actually worked correctly ✅


Relationship to L5 — Governance / Responsible AI
L3 contributes to governance risk by enabling action.
Even safe outputs (L1) and correct context (L2) can create risk if:

The system executes actions incorrectly
The system performs actions it should not perform
The system bypasses constraints

Governance enforcement and policy controls are validated fully at L5.

Test Types
The following Test Types define validation at this layer:

Tool Invocation Testing
Tool Selection Testing
Workflow Execution Testing
Multi-Step Reasoning Testing
Planning & Task Decomposition Testing
State Management Testing
Memory Testing
Decision Logic Testing
Error Handling & Recovery Testing
Retry & Fallback Testing
Action Outcome Validation Testing
Constraint Adherence Testing


Characteristics of Testing at This Layer
Testing at this layer is:

Less deterministic than L1 and L2
Stateful (depends on history and sequence)
Temporal (changes over time)
Sensitive to branching logic and decision paths
Harder to validate with simple assertions
Often requiring scenario-based testing
Often requiring simulation and replay
Often requiring observability and trace analysis


Examples of What is Validated
Examples include:

Did the system select the correct tool?
Did the system call the tool with correct parameters?
Did the system follow the correct sequence of steps?
Did the system correctly interpret the result of a tool call?
Did the system maintain correct state across steps?
Did the system remember relevant context across interactions?
Did the system appropriately recover from failure?
Did the system stop when appropriate?
Did the system avoid unnecessary actions?
Did the system produce the intended outcome?


Common Failure Patterns
Common failures at this layer include:

Selecting the wrong tool
Calling the correct tool incorrectly
Executing steps in the wrong order
Infinite loops or repeated actions
Loss of state between steps
Memory pollution (incorrect memory retained)
Ignoring constraints or instructions
Failing to recover from errors
Escalating small errors into larger failures
Producing correct reasoning but incorrect actions
Taking actions that were not requested
Stopping prematurely or failing to complete tasks


Key Implications

Correct answers do not guarantee correct actions
Agentic systems introduce execution risk beyond reasoning risk
Validation must consider sequences, not just single interactions
Testing must include success, failure, and edge-case scenarios
Observability is critical to understand behavior over time
L3 testing is required before trust can be established in automated workflows


Human Oversight
Human oversight is often required at this layer, especially when:

Reviewing decision logic
Validating complex workflows
Assessing edge-case handling
Monitoring high-impact actions
Evaluating system behavior across multiple steps
Reviewing failures and unexpected behaviors

Human oversight complements automated testing but cannot be eliminated in complex systems.

Navigation
Proceed to Test Types within this layer:

Tool Invocation Testing
Tool Selection Testing
Workflow Execution Testing
Multi-Step Reasoning Testing
Planning & Task Decomposition Testing
State Management Testing
Memory Testing
Decision Logic Testing
Error Handling & Recovery Testing
Retry & Fallback Testing
Action Outcome Validation Testing
Constraint Adherence Testing