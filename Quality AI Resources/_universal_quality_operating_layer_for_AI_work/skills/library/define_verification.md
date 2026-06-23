# L2.S3 — Define Verification

## Purpose

Define how the output of work will be proven correct so that quality can be validated explicitly rather than assumed.

## Governing Basis

If verification cannot be defined, the specification is incomplete.
Unverifiable outputs are undefined outputs.
Verification must be defined before or during execution, not after completion.

## When to Use

Use this skill:

- before execution begins
- when defining requirements or specifications
- when validating output readiness
- when refining ambiguous tasks
- whenever correctness must be proven

## Inputs Required

- The defined or partially defined contract
- The expected outcome
- The constraints and structure of the output
- Known risks or failure modes

## Process

1. Define what “correct” means in observable terms
   - specify what must be true if the output is correct
   - avoid subjective or vague language

2. Identify measurable indicators of correctness
   - define what can be observed, tested, or checked
   - ensure criteria can distinguish pass vs fail

3. Define validation methods
   - automated checks where possible
   - explicit human review where required
   - monitoring or observation if applicable

4. Define pass/fail criteria
   - specify what constitutes success
   - specify what constitutes failure or defect

5. Align verification to the contract
   - ensure verification checks what the consumer expects
   - ensure all critical expectations are covered

6. Confirm verification feasibility
   - ensure verification can actually be executed
   - remove reliance on intuition or undefined judgment

## Outputs Produced

- A defined verification method for the output
- Observable success criteria
- Explicit pass/fail conditions
- A clear link between expectations and validation

## Failure Signals

- Verification is not defined before execution
- Correctness is described subjectively (“looks good”, “seems right”)
- No measurable or observable criteria exist
- Validation depends entirely on informal review
- Verification does not map to consumer expectations

## Escalation Rule

If verification cannot be defined:

- treat the work as undefined
- return to contract definition or quality questions
- reduce scope to something that can be verified
- or proceed only with explicitly stated limitations

Do not proceed as if correctness can be determined later.

## Completion Criteria

This skill is complete when:

- correctness is explicitly defined
- success and failure can be observed and distinguished
- a clear validation method exists
- verification aligns directly with the contract
