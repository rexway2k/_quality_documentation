# L2 — Context Completeness Testing

## What

Context Completeness Testing validates whether the retrieved context includes enough information for the model to answer correctly.

It evaluates whether critical information is missing from the context supplied to the model.

---

## Why

A model may fail not because it received wrong information, but because it received incomplete information.

Incomplete context can lead to:
- Partial answers
- Unsupported assumptions
- Incorrect conclusions
- Overgeneralization
- Missing constraints
- Failure to identify exceptions or edge cases

Context Completeness Testing helps ensure the model has sufficient information to respond responsibly.

---

## Where

Context Completeness Testing applies to:
- Retrieved context sets
- Document chunks
- Knowledge base passages
- Multi-document retrieval
- Policy or procedure retrieval
- Context windows assembled for generation

This test type belongs at L2 because it validates whether the retrieved material is sufficient before response generation.

---

## When

Context Completeness Testing may occur:
- During RAG design
- During document chunking validation
- During retrieval evaluation
- Before release
- After adding or changing source content
- After changing retrieval limits or ranking rules
- During analysis of incomplete or incorrect responses

---

## How

Context completeness may be validated through:
- Comparing retrieved context to known answer requirements
- Human review
- Golden question datasets
- Checklist-based source coverage review
- Testing questions requiring multiple documents or sections
- Reviewing whether required constraints, exceptions, and definitions are included
- Evaluating whether the model can answer using only the retrieved context

Completeness should be judged against the information needed to answer, not the total amount of available content.

---

## Failure Modes

Common failure modes include:
- Missing critical policy exception
- Missing required definition
- Missing procedural step
- Missing dependency or constraint
- Only part of a multi-part answer retrieved
- Related document retrieved but wrong section selected
- Context is too narrow
- Chunking separates related information needed together

---

## Verification / Signals

Verification signals may include:
- Required context coverage score
- Missing context count
- Human completeness rating
- Multi-source retrieval success rate
- Answer support coverage
- Number of incomplete responses linked to missing context
- Reduction in incomplete answers after retrieval tuning

---

## Key Note

More context is not always better.

The goal is sufficient context, not maximum context.

Complete context should include what is needed to answer correctly without overwhelming the model with unnecessary noise.