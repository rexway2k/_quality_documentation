# AI Testing Model Layers & Concepts

## Purpose

This page defines how to interpret and apply the AI Testing Model.

It establishes:

- How AI testing is structured across system layers
- How testing responsibilities are separated and defined
- How to understand the relationship between **where**, **what**, **why**, **how**, and **when** in AI testing

This page provides the conceptual foundation required to correctly use all downstream testing guidance.

---

# The Core Problem

“AI Testing” is often treated as a single activity.

This creates ambiguity:

- Testing is inconsistently applied
- Responsibilities are unclear
- Risks are not fully understood or bounded
- Validation approaches vary across teams

Without structure, teams may test the same thing multiple times while missing critical areas entirely.

---

# The Core Concept

AI Testing is not one thing.

AI Testing is the composition of five distinct dimensions:

| Dimension | Question Answered |
|------------|-------------------|
| **WHERE** | System Layers |
| **WHAT** | Test Types |
| **WHY** | Risk & Failure Modes |
| **HOW** | Validation Methods |
| **WHEN** | Lifecycle Timing |

This model separates these concerns to eliminate ambiguity and enable repeatable, scalable quality practices.

---

# The Layered Model (WHERE We Test)

AI systems are composed of multiple layers.

Each layer:

- Represents a distinct system responsibility
- Defines a boundary of behavior
- Introduces unique risks
- Requires specific testing approaches

## Layers

| Layer | Domain | Description |
|---------|---------|-------------|
| **L0** | Data Foundation | Input data quality, structure, and origin |
| **L1** | Model / LLM | Raw model behavior and response generation |
| **L2** | Retrieval / Context (RAG) | Context sourcing, retrieval, and grounding |
| **L3** | Agentic Systems | Decision-making, workflows, and orchestration |
| **L4** | System Integration / Experience | Application behavior and system interactions |
| **L5** | Governance / Responsible AI | Oversight, risk, compliance, and ethics |

---

# Why Layers Matter

Failures originate at specific layers and propagate upward through the system.

### Examples

- Incorrect data (**L0**) leads to incorrect model behavior (**L1**)
- Poor retrieval (**L2**) leads to grounded but incorrect outputs
- Faulty agent logic (**L3**) leads to incorrect or unsafe actions
- Integration failures (**L4**) lead to poor user experience
- Governance gaps (**L5**) expose the organization to risk

Testing must occur at the correct layer to effectively identify and bound risk.

---

# Understanding WHERE (Layers)

Layers define:

- The location of validation within the system
- The responsibility being tested
- The system boundary where behavior occurs

Each layer answers:

> **"Where in the system are we validating behavior?"**

---

# Understanding WHAT (Test Types)

Within each layer, testing is further defined by **Test Types**.

A Test Type represents:

- A specific category of validation
- A clearly defined quality concern
- A repeatable testing focus

### Examples

- Accuracy Testing (L1)
- Retrieval Quality Testing (L2)
- Tool Invocation Testing (L3)
- Privacy Testing (L5)

Each test type answers:

> **"What specifically are we validating within this layer?"**

---

# Understanding WHY (Risk & Failure Modes)

Every test exists to bound risk.

Each test type must define:

- The failure it is designed to detect
- The risk it is intended to reduce
- The impact of failure if left unaddressed

This ensures testing is intentional and aligned to business and system risk.

Each test answers:

> **"Why does this validation exist?"**

---

# Understanding HOW (Validation Methods)

Each test type includes defined methods of validation.

These may include:

- Automated evaluation
- Human review
- Benchmark testing
- Scenario-based validation
- Adversarial testing

Each test type answers:

> **"How do we validate this behavior?"**

---

# Understanding WHEN (Lifecycle Timing)

Testing occurs across the entire lifecycle.

Validation is not limited to a single phase and may occur:

- During design and planning
- During development
- During pre-release validation
- During runtime execution
- During post-release monitoring

Each test type answers:

> **"When should this validation occur?"**

---

# Relationship Between Layers and Test Types

- **Layers** define **WHERE** testing occurs
- **Test Types** define **WHAT** is tested at that layer
- **Methods** define **HOW** validation is performed
- **Failure Modes** define **WHY** testing exists
- **Lifecycle** defines **WHEN** testing is applied

This structure ensures:

- Clear separation of concerns
- No overlap in responsibility
- Consistent application of testing practices

---

# How This Model Differs from Traditional Testing

## Traditional Testing

- Focuses on deterministic systems
- Relies on predefined expected results
- Primarily validates system behavior at defined interfaces

## AI Testing

- Operates in probabilistic systems
- Requires evaluation rather than strict assertion
- Must validate behavior across multiple layers simultaneously
- Relies on both automated and human validation

---

# Key Implications

- AI systems cannot be validated with a single test strategy
- Testing must occur across multiple layers concurrently
- Validation must account for variability and uncertainty
- Observability and evaluation are required across all layers
- Human oversight is required for higher-risk layers

---

# Common Misconception

> “We tested the AI.”

This statement is incomplete.

Correct interpretation requires identifying:

- Which layer(s) were tested
- Which test types were applied
- What risks were addressed
- How validation was performed

Without this detail, testing cannot be verified or trusted.

---

# Evaluation & Observability (Cross-Cutting)

Evaluation is **not a layer**.

It exists across all layers to:

- Measure outcomes
- Detect failures
- Track performance over time
- Enable continuous improvement

Evaluation connects all testing activities into a coherent system.

---

# Summary

AI Testing is a structured system composed of:

- **Layers (WHERE)**
- **Test Types (WHAT)**
- **Risk (WHY)**
- **Methods (HOW)**
- **Lifecycle (WHEN)**

Understanding this structure is required to:

- Apply testing consistently
- Bound risk effectively
- Validate AI systems with confidence

---

# Navigation

Proceed to the system layers:

- **L0 — Data Foundation**
- **L1 — Model / LLM**
- **L2 — Retrieval / Context (RAG)**
- **L3 — Agentic Systems**
- **L4 — System Integration / Experience**
- **L5 — Governance / Responsible AI**

Each layer expands into detailed test types and validation approaches.
