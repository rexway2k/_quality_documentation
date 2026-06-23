# Universal Quality Skill System — Operating Guide

## Purpose

This document explains how the Universal Quality Skill System is used in practice.

It defines:

- how the system works end-to-end
- how artifacts relate to each other
- how to apply the system in real tasks
- how to integrate the system into AI agents and workflows

This is the operational layer of the system.

---

## What This System Is

This system is a reusable quality operating layer that ensures:

- outputs align to consumer expectations
- ambiguity is reduced before execution
- uncertainty is bounded
- verification is defined and applied
- work progresses without unnecessary blocking

This system applies to any relational task:

- writing
- coding
- planning
- analysis
- decision-making
- system design
- AI agent behavior

---

## Core Operating Model

All work follows the same flow:

1. Define the contract
2. Clarify the work using quality questions
3. Bound uncertainty
4. Define verification
5. Execute the work
6. Validate the output
7. Diagnose and improve if needed

This flow is recursive and applies at every level of the system.

---

## System Components

This system is composed of multiple artifact types.

### 1. System Specification

File:

00_system_specification.md

Purpose:

- defines the system contract
- defines constraints, structure, and verification model
- serves as the governing source of truth

Dependency:

- all other artifacts must align to this

---

### 2. Skill Taxonomy

File:

skills/00_skill_taxonomy.md

Purpose:

- defines all skills in the system
- organizes skills into layers
- provides unique identifiers for traceability

Dependency:

- all skill definitions, views, prompts, and schemas must map to this

---

### 3. Skill Library

Location:

skills/library/

Purpose:

- defines each skill in detail
- describes how each skill behaves
- provides execution guidance

Dependency:

- each file maps to one taxonomy skill

---

### 4. Skill Views

Location:

skills/views/

Purpose:

- group skills by function (definition, execution, governance, verification)
- provide human-friendly navigation
- help users select the right skills

Dependency:

- derived from taxonomy
- do not redefine skills

---

### 5. Prompt Blocks

File:

skills/prompts/modular_blocks.md

Purpose:

- provides reusable execution units
- maps skills to prompt-level behavior
- enables dynamic use inside AI workflows

Dependency:

- directly maps to skills
- used to compose system prompt

---

### 6. System Prompt

File:

skills/prompts/system_prompt.md

Purpose:

- defines full agent behavior
- integrates all skills into a single operating model
- adapts rigor based on task complexity

Dependency:

- built from prompt blocks + skills

---

### 7. Schemas

Location:

skills/schemas/

Files:

- skills.json
- skills.yaml

Purpose:

- provide machine-readable representation of the system
- enable integration with agent frameworks
- support orchestration and automation

Dependency:

- must match taxonomy and skills

---

## How The System Works Together

### Flow of Control

Specification → Taxonomy → Skills → Prompts → Execution → Verification

### Interpretation

- Specification defines what must be true
- Taxonomy defines capabilities
- Skills define behavior
- Prompts enable execution
- Outputs are validated through verification

---

## Execution Modes

The system operates in three modes:

### 1. Definition Mode

Used when a task is unclear.

Skills used:

- Define Contract
- Apply Quality Questions
- Define Constraints
- Define Structure

---

### 2. Execution Mode

Used when producing output.

Skills used:

- Execute Work
- Maintain Contract Alignment
- Surface Assumptions
- Handle Ambiguity

---

### 3. Verification Mode

Used when validating or correcting output.

Skills used:

- Define Verification
- Bound Risk
- Diagnose Failure
- Validate Output

---

## Adaptive Rigor

The system adjusts its level of rigor based on task complexity.

### Low Complexity

- minimal structure
- fast execution
- light validation

### Moderate Complexity

- explicit contract
- partial quality question application
- visible assumptions

### High Complexity

- full six-question definition
- risk analysis
- explicit verification
- structured execution

### Critical Work

- full system applied
- strict validation
- escalation when needed

---

## Execution States

At any point, the system must determine:

### Proceed

- risk is low or bounded

### Proceed with Caveats

- uncertainty exists but is controlled

### Pause / Escalate

- uncertainty is unbounded
- contract is unclear
- verification is not possible

### Override

- human decision overrides system gating

---

## Key Operating Rules

1. Do not execute without understanding expectations
2. Do not hide assumptions
3. Do not proceed with unbounded risk
4. Do not produce unverifiable output
5. Do not block progress unnecessarily
6. Always align output to consumer needs

---

## How To Use This System

### For Human Use

1. Start with definition skills
2. Clarify the task
3. Execute with awareness of constraints
4. Validate outputs explicitly
5. Refine based on feedback

---

### For AI Agent Use

1. Apply system prompt
2. Use modular blocks dynamically
3. Adjust rigor based on complexity
4. Ensure outputs are structured and verifiable

---

### For System Builders

1. Use schemas for integration
2. Use prompts for behavior control
3. Use skills for modular design
4. Use taxonomy for orchestration logic

---

## Extending The System

When adding new capabilities:

- add to taxonomy first
- create corresponding skill
- update prompt blocks if needed
- update schema definitions
- ensure alignment with system specification

Do not add isolated functionality.

All additions must:

- align to system principles
- support contract-risk-verification model
- be traceable and composable

---

## Failure Signals

The system is not working correctly if:

- outputs are not traceable to a contract
- ambiguity is hidden instead of surfaced
- risk is ignored or undefined
- outputs cannot be verified
- behavior is inconsistent across tasks
- system blocks progress unnecessarily

---

## Final Reduction

All work must be explainable as:

- What is expected?
- Who is the consumer?
- What can go wrong?
- How do we prove it works?

If these cannot be answered, the system is not being applied correctly.
