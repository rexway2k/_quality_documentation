# L1.S3 — Apply Quality Questions

## Purpose

Use the six quality questions to fully define a task, decision, artifact, system component, or relational dependency so that work is built on explicit understanding rather than assumptions.

## Governing Basis

The six quality questions apply to every relational dependency, architectural decision, system component, document, deliverable, interaction, and transaction at every layer.

They define:

- outcome
- consumers
- constraints
- structure
- failure modes
- verification

If any of these are undefined, the work is incomplete.

## When to Use

Use this skill:

- when a request is received
- when clarifying requirements
- when designing a solution
- when evaluating completeness
- when breaking down complex work
- when diagnosing confusion or ambiguity

Apply it to:

- entire tasks
- sub-components of tasks
- dependencies between units of work

## Inputs Required

- The task, request, or work item
- Any known context, requirements, or stakeholder information

## Process

1. Define **Outcome**
   - State what is true when the work is complete
   - Do not describe process or activity
   - Describe the end state

2. Identify **Consumers**
   - Name the immediate consumer
   - Identify downstream consumers
   - Include any system, role, or process that depends on the output

3. Define **Constraints**
   - Identify what must be true for the output to work
   - Include boundaries, limitations, and non-negotiables
   - Include technical, logical, and contextual constraints

4. Define **Structure**
   - Describe what the correct output should look like
   - Define shape before content
   - Identify required components or organization

5. Identify **Failure Modes**
   - Determine how the work can fail
   - Identify common and high-impact failure paths
   - Include mismatch scenarios between expectation and delivery

6. Define **Verification**
   - Specify how correctness will be proven
   - Define observable pass/fail criteria
   - Prefer automation where possible
   - Define human review where required

## Outputs Produced

- A complete six-question definition of the work
- A clarified and structured specification
- A visible set of risks and constraints
- A defined method of verification

## Failure Signals

- Any question cannot be answered clearly
- Outcome is confused with process
- Consumers are assumed rather than identified
- Constraints are missing or incomplete
- Structure is not defined before execution
- Failure modes are ignored
- Verification cannot be described

## Escalation Rule

If one or more questions cannot be answered:

- Proceed only if uncertainty is bounded and visible
- Reduce scope to a smaller, well-defined subset
- Or stop and surface the missing information explicitly

Do not proceed with hidden ambiguity.

## Completion Criteria

This skill is complete when all six questions are answered clearly enough to:

- support execution
- support verification
- prevent expectation mismatch

If verification cannot be defined, the work is not defined.
