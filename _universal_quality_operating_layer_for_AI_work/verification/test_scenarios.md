# Verification — Test Scenarios

## Purpose

This document defines a set of test scenarios used to evaluate whether the Universal Quality Skill System behaves correctly across different types of work.

Scenarios are designed to test:

- contract definition
- ambiguity handling
- risk management
- execution quality
- verification alignment
- failure diagnosis

Each scenario provides:

- input
- expected system behavior
- failure risks being tested

---

## Scenario Structure

Each scenario includes:

- Scenario ID
- Scenario Type
- Input Prompt
- What This Tests
- Expected Behaviors
- Failure Signals

---

# Scenario Set

---

## SCN-01 — Simple Direct Task

### Scenario Type

Low complexity / Low ambiguity

### Input Prompt

"Write a short summary of the benefits of exercise."

### What This Tests

- adaptive rigor
- execution without over-processing

### Expected Behaviors

- does not over-apply full framework
- produces useful output quickly
- maintains clarity and correctness

### Failure Signals

- over-analysis before writing
- unnecessary contract breakdown
- excessive verbosity

---

## SCN-02 — Ambiguous Request

### Scenario Type

Moderate ambiguity

### Input Prompt

"Create a plan for improving team performance."

### What This Tests

- contract definition
- assumption surfacing

### Expected Behaviors

- identifies missing context (team type, goals, constraints)
- defines assumptions explicitly
- proceeds with structured plan

### Failure Signals

- assumes context silently
- produces generic output with no framing
- fails to clarify consumer or outcome

---

## SCN-03 — Execution Task (Build Something)

### Scenario Type

Execution-heavy

### Input Prompt

"Write a Python script that reads a CSV file and summarizes the data."

### What This Tests

- execution capability
- not stopping at analysis

### Expected Behaviors

- produces actual working script
- defines assumptions (file format, structure)
- aligns output to expected outcome

### Failure Signals

- explains what to do without writing code
- produces incomplete or non-functional code
- ignores assumptions

---

## SCN-04 — Missing Critical Information

### Scenario Type

High ambiguity / potential unbounded risk

### Input Prompt

"Design a secure system for handling customer data."

### What This Tests

- bounding risk
- escalation behavior
- structured definition

### Expected Behaviors

- identifies critical unknowns (data type, scale, compliance)
- avoids pretending system is fully defined
- defines a bounded approach or outlines assumptions clearly

### Failure Signals

- proceeds as if requirements are complete
- produces overconfident full design with no caveats
- ignores constraints and failure modes

---

## SCN-05 — Validation Required

### Scenario Type

Verification-focused

### Input Prompt

"Here is a test plan. Review it and tell me if it's complete."

### What This Tests

- verification thinking
- structured evaluation

### Expected Behaviors

- evaluates based on:
  - intent (WHY)
  - risk (WHAT)
  - scope (WHERE)
  - execution (HOW)
- identifies gaps
- avoids subjective judgment

### Failure Signals

- vague feedback ("looks good")
- no structured reasoning
- no identification of missing elements

---

## SCN-06 — Failure Diagnosis

### Scenario Type

Debug / issue analysis

### Input Prompt

"This feature is failing in production. Help figure out why."

### What This Tests

- failure diagnosis
- contract tracing

### Expected Behaviors

- asks or defines:
  - expected behavior
  - actual behavior
  - mismatch
- traces root cause categories
- avoids guessing

### Failure Signals

- jumps to conclusions
- suggests fixes without diagnosis
- ignores expectation mismatch

---

## SCN-07 — Conflicting Constraints

### Scenario Type

Governance / tension

### Input Prompt

"We need to move fast, but also ensure this is fully secure. What should we do?"

### What This Tests

- principle tension resolution
- decision justification

### Expected Behaviors

- acknowledges conflict
- balances:
  - system speed
  - risk
  - constraints
- proposes a bounded approach

### Failure Signals

- ignores one side of conflict
- provides generic advice
- fails to justify decision

---

## SCN-08 — Multi-Consumer Scenario

### Scenario Type

Complex dependency system

### Input Prompt

"Design a reporting dashboard used by executives, analysts, and operations teams."

### What This Tests

- consumer identification
- fractal contract logic

### Expected Behaviors

- identifies multiple consumers
- differentiates needs
- reflects in structure/design

### Failure Signals

- treats all users as identical
- ignores downstream needs
- produces shallow design

---

## SCN-09 — Over-Constraint / Rigidity Risk

### Scenario Type

System behavior check

### Input Prompt

"Write a short email to confirm a meeting."

### What This Tests

- adaptive rigor
- non-blocking behavior

### Expected Behaviors

- executes immediately
- avoids unnecessary structure
- keeps response lightweight

### Failure Signals

- over-applies framework
- delays execution
- adds unnecessary complexity

---

## SCN-10 — Verification Gap

### Scenario Type

Validation weakness

### Input Prompt

"Build a solution for managing inventory."

### What This Tests

- verification definition
- completeness thinking

### Expected Behaviors

- defines how success would be measured
- identifies risks and failure modes
- ensures solution is testable

### Failure Signals

- no mention of verification
- produces design without validation
- ignores failure modes
