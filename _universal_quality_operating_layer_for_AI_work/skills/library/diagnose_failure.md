# L4.S1 — Diagnose Failure

## Purpose

Identify the root cause of a failure by locating the mismatch between expected outcome and actual outcome, and tracing that mismatch back to the contract.

## Governing Basis

Failures are mismatched expectations.
The root cause of failure is not the symptom, but the gap between what was expected and what was delivered.
Fixing failure requires identifying and correcting the expectation mismatch at the contract level, not just resolving the immediate issue.

## When to Use

Use this skill:

- when an output is incorrect, incomplete, or misaligned
- when validation fails
- when stakeholders report issues or dissatisfaction
- during debugging, testing, or review
- when unexpected behavior occurs
- when outcomes do not match expectations

## Inputs Required

- The expected outcome (contract)
- The actual outcome (observed result)
- Available context, inputs, and system behavior
- Any defined constraints, structure, or verification criteria

## Process

1. Define the expected outcome
   - restate what should have been true
   - reference the contract explicitly

2. Define the actual outcome
   - describe what actually occurred
   - avoid interpretation, focus on observable behavior

3. Identify the mismatch
   - compare expected vs actual
   - determine where and how they diverge

4. Trace the mismatch upstream
   - determine where the expectation originated
   - identify where the breakdown occurred:
     - missing expectation
     - incorrect expectation
     - misinterpreted expectation
     - incomplete specification
     - implementation error

5. Classify the failure type
   - contract definition failure
   - constraint violation
   - structure misunderstanding
   - missed failure mode
   - verification gap
   - execution defect

6. Determine corrective action
   - fix the contract if expectations were wrong
   - fix the specification if incomplete
   - fix the implementation if incorrect
   - fix the verification if it failed to detect the issue

7. Validate resolution path
   - ensure correction addresses the root cause
   - confirm that repeat failure is prevented

## Outputs Produced

- A clear definition of expected vs actual outcome
- Identified mismatch point
- Root cause classification
- A corrective action aligned to the contract level
- A recommendation to prevent recurrence

## Failure Signals

- Fixing symptoms without identifying expectation mismatch
- Blaming execution without validating the contract
- Lack of traceability to the originating expectation
- Repeated failures of the same type
- Vague or subjective explanations of failure

## Escalation Rule

If the root cause cannot be traced:

- do not assume execution failure by default
- move upstream in the contract chain
- re-evaluate:
  - outcome definition
  - consumer expectations
  - constraints
  - structure
  - verification

If the contract cannot explain the failure, the contract is incomplete.

## Completion Criteria

This skill is complete when:

- the mismatch between expected and actual outcome is explicitly defined
- the root cause is traced to a specific point in the contract chain
- corrective action addresses the source of failure
- the likelihood of recurrence is reduced through improved contract, execution, or verification
