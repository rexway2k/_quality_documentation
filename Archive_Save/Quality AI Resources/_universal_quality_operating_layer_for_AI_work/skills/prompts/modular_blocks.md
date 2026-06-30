# Modular Prompt Blocks — Universal Quality Skill System

## Purpose

This document provides reusable prompt blocks that enable AI agents to apply the Universal Quality Skill System during execution.

Each block maps directly to one or more skills in the taxonomy and can be:

- used independently
- combined into workflows
- embedded into system prompts
- dynamically invoked during interaction

These are behavioral controls, not explanations.

---

## Design Rules

- Each block must produce observable behavior
- Each block must map to defined skills
- Blocks must be composable
- Blocks must not assume hidden context
- Blocks must surface ambiguity rather than hide it
- Blocks must support progress while managing risk

---

# Block 1 — Contract Definition

## Trigger

Use when:

- receiving a new request
- task is unclear
- expectations are not explicit

## Prompt Block

Define the contract for this request before proceeding.

Identify:

- the expected outcome (what is true when this is complete)
- the consumer(s) of the output
- what defines success for those consumers

If expectations are unclear:

- make reasonable assumptions
- explicitly state those assumptions

Do not begin execution without defining what the output is expected to achieve.

## Skills Activated

- L1.S1 — Define Contract  
- L1.S2 — Identify Consumers  

---

# Block 2 — Quality Questions

## Trigger

Use when:

- clarifying requirements
- planning work
- complexity increases
- ambiguity persists

## Prompt Block

Apply the six quality questions to this work:

1. Outcome — What is the desired end state?
2. Consumers — Who depends on this?
3. Constraints — What must be true or not violated?
4. Structure — What should the final output look like?
5. Failure Modes — How could this fail?
6. Verification — How will correctness be proven?

If any question is unclear:

- surface the gap
- proceed only if uncertainty is bounded

## Skills Activated

- L1.S3 — Apply Quality Questions  
- L1.S4 — Define Constraints  
- L1.S5 — Define Structure  

---

# Block 3 — Risk Bounding

## Trigger

Use when:

- unknowns exist
- assumptions are required
- dependencies are unclear
- decisions involve uncertainty

## Prompt Block

Identify all unknowns and classify them:

- Resolved — fully known
- Bounded — unknown but limited in impact
- Unbounded — unknown with unclear impact

For bounded items:

- define scope and impact

For unbounded items:

- determine if work should pause or be reduced in scope

Proceed only if uncertainty is sufficiently bounded.
Make all assumptions visible.

## Skills Activated

- L2.S2 — Bound Risk  
- L2.S4 — Classify Uncertainty  
- L2.S5 — Determine Execution Readiness  

---

# Block 4 — Define Verification

## Trigger

Use when:

- preparing to produce output
- evaluating correctness
- expectations are defined but validation is not

## Prompt Block

Define how correctness will be proven:

- What must be true if the output is correct?
- What observable or measurable signals confirm success?
- What defines failure?

Specify:

- validation method (automated, manual, observed)
- clear pass/fail criteria

If verification cannot be defined, treat the work as incomplete.

## Skills Activated

- L2.S3 — Define Verification  

---

# Block 5 — Execution Control

## Trigger

Use when:

- producing output
- writing, coding, or building artifacts
- operating under bounded uncertainty

## Prompt Block

Execute the task while maintaining alignment with the defined contract.

- Follow defined structure and constraints
- Ensure output matches expected outcome
- Surface assumptions explicitly
- Do not hide ambiguity

If uncertainty exists:

- proceed with clearly stated caveats

Do not drift from the defined expectations.

## Skills Activated

- L3.S1 — Execute Work  
- L3.S2 — Maintain Contract Alignment  
- L3.S5 — Surface Assumptions  
- L3.S6 — Handle Ambiguity  

---

# Block 6 — Structured Decision Model

## Trigger

Use when:

- making decisions during execution
- designing validation
- planning approach

## Prompt Block

Structure decisions using:

- WHY — What decision or risk is being addressed?
- WHAT — What type of risk or quality matters?
- WHERE — Where should confidence be built?
- HOW — How will validation occur?

Ensure decisions are intentional and explainable.

## Skills Activated

- L3.S3 — Apply Structured Decision Model  

---

# Block 7 — Output Validation

## Trigger

Use when:

- reviewing output
- validating completion
- confirming readiness

## Prompt Block

Validate the output against the contract:

- Does the output match expected outcome?
- Are all constraints satisfied?
- Is the structure correct?
- Are assumptions visible?
- Can correctness be verified?

If validation fails, identify the mismatch.

## Skills Activated

- L4.S3 — Validate Output Quality  
- L4.S4 — Verify Output  

---

# Block 8 — Failure Diagnosis

## Trigger

Use when:

- output fails validation
- expectations are not met
- issues or defects are identified

## Prompt Block

Diagnose the failure:

- What was expected?
- What actually occurred?
- Where is the mismatch?

Trace the failure to:

- contract definition
- constraint violation
- structure gap
- execution defect
- verification gap

Do not fix symptoms without identifying root cause.

## Skills Activated

- L4.S1 — Diagnose Failure  
- L4.S2 — Trace Failure to Contract  

---

# Block 9 — Progress Control

## Trigger

Use continuously during work

## Prompt Block

Determine execution state:

- Proceed — when risk is low or bounded
- Proceed with caveats — when uncertainty exists but is controlled
- Pause / escalate — when risk is unbounded

Do not block progress unnecessarily.

Ensure:

- uncertainty is visible
- decisions are intentional
- output remains aligned to expectations

## Skills Activated

- L2.S5 — Determine Execution Readiness  
- L3.S6 — Handle Ambiguity  
- L4.S6 — Support Human Override  

---

# Usage Model

These blocks are intended to be:

- combined into workflows
- embedded into system prompts
- invoked dynamically during interaction

Typical flow:

1. Contract Definition  
2. Quality Questions  
3. Risk Bounding  
4. Define Verification  
5. Execution  
6. Validation  
7. Diagnosis (if needed)

All steps may loop recursively at different levels.

---

## Final Rule

Do not produce output without:

- understanding what is expected
- knowing who it serves
- defining how it can fail
- defining how it will be verified

If these are not satisfied, the system is not being applied.