# Skill Taxonomy — Universal Quality Skill System

## Purpose

This document defines the complete set of skills that make up the Universal Quality Operating Layer for AI Work.

Each skill represents a discrete, reusable capability that an AI agent can apply to:

- Understand the governing principles
- Define work correctly
- Execute work to a high standard
- Verify outputs against expectations

This taxonomy is the authoritative index of all skills in the system.
All other artifacts (library files, views, schemas, prompts) must align to this structure.

---

## Structure

Skills are organized into layers based on their role in the system:

- Layer 0 — Principle Understanding
- Layer 1 — Contract Definition
- Layer 2 — Risk & Verification
- Layer 3 — Execution
- Layer 4 — Review & Feedback

Each layer represents a stage in the quality lifecycle.

---

# Layer 0 — Principle Understanding

---

### L0.S1 — Interpret Principles
Understand each principle in operational terms and apply it to the current context.

---

### L0.S2 — Apply Fractal Contract Logic
Apply the consumer-provider model at all levels of a system, ensuring every unit has a defined consumer and contract.

---

### L0.S3 — Resolve Principle Tension
Resolve conflicts between principles using defined priority rules.

---

### L0.S4 — Detect Principle Violations
Identify when behavior, decisions, or outputs violate governing principles.

---

### L0.S5 — Trace Decisions to Principles
Map decisions and outputs back to the principles that justify them.

---

### L0.S6 — Operationalize Principles
Convert abstract principles into concrete actions within a task.

---

# Layer 1 — Contract Definition

---

### L1.S1 — Define Contract
Explicitly define the expectations between producer and consumer.

---

### L1.S2 — Identify Consumers
Determine all entities that depend on the output.

---

### L1.S3 — Apply Quality Questions

Answer the six quality questions:

- Outcome
- Consumers
- Constraints
- Structure
- Failure Modes
- Verification

---

### L1.S4 — Define Constraints
Specify what must be true for the output to be considered valid.

---

### L1.S5 — Define Structure
Define what the correct output should look like before building it.

---

# Layer 2 — Risk & Verification

---

### L2.S1 — Identify Failure Modes
Determine how the work or system can fail.

---

### L2.S2 — Bound Risk
Ensure all unknowns are either resolved or explicitly bounded.

---

### L2.S3 — Define Verification
Specify how the output will be proven correct.

---

### L2.S4 — Classify Uncertainty

Distinguish between:

- Resolved
- Bounded
- Unbounded uncertainty

---

### L2.S5 — Determine Execution Readiness

Decide whether to:

- Proceed
- Proceed with caveats
- Pause / escalate

---

# Layer 3 — Execution

---

### L3.S1 — Execute Work
Perform the task based on the defined contract and constraints.

---

### L3.S2 — Maintain Contract Alignment
Ensure output remains consistent with defined expectations during execution.

---

### L3.S3 — Apply Structured Decision Model
Use WHY / WHAT / WHERE / HOW to guide execution decisions.

---

### L3.S4 — Generate Output
Produce the final artifact (writing, code, plan, etc.).

---

### L3.S5 — Surface Assumptions
Make all assumptions visible when operating under bounded uncertainty.

---

### L3.S6 — Handle Ambiguity
Proceed appropriately when ambiguity exists without blocking progress unnecessarily.

---

# Layer 4 — Review & Feedback

---

### L4.S1 — Diagnose Failure
Identify mismatches between expected and actual outcomes.

---

### L4.S2 — Trace Failure to Contract
Determine where the breakdown occurred in the contract chain.

---

### L4.S3 — Validate Output Quality
Evaluate whether the output meets defined expectations.

---

### L4.S4 — Verify Output
Apply defined verification methods to confirm correctness.

---

### L4.S5 — Capture Learnings
Document improvements for future iterations.

---

### L4.S6 — Support Human Override
Allow human decision to override system decisions or gates.

---

## Governing Rule

Every skill must support the system’s core requirement:

All work must be explainable in terms of:

- Defined contract
- Identified risks
- Verification method

If a skill does not support this,
it does not belong in this system.

---

## Final Reduction

The full system of skills exists to ensure that any unit of work can answer:

- What is it supposed to do?
- Who does it serve?
- How can it fail?
- How do we prove it works?

If a task cannot be expressed in these terms,
the system is not being applied correctly.
