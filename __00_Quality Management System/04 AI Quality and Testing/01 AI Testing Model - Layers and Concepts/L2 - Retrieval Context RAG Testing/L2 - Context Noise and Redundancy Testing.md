# L2 — Context Noise & Redundancy Testing

## What

Context Noise & Redundancy Testing validates whether retrieved context contains unnecessary, repetitive, conflicting, or distracting information.

It evaluates whether context is clean enough for the model to use effectively.

---

## Why

Too much irrelevant or repetitive context can degrade model performance.

Noise and redundancy can cause:
- Confused answers
- Longer responses
- Higher token consumption
- Increased latency
- Incorrect prioritization
- Contradictory output
- Important information being diluted by less useful content

This testing helps ensure retrieved context is focused and useful.

---

## Where

Context Noise & Redundancy Testing applies to:
- Retrieved chunks
- Context assembly
- Prompt construction
- Multi-document search results
- Knowledge base retrieval
- RAG pipelines

This test type belongs at L2 because it validates the quality of context before generation.

---

## When

Context Noise & Redundancy Testing may occur:
- During retrieval tuning
- During prompt assembly design
- Before release
- After changes to retrieval limits
- After adding new document sources
- During analysis of poor or verbose answers
- During cost and latency optimization

---

## How

Noise and redundancy may be validated through:
- Human review of retrieved context
- Measuring duplicate or near-duplicate content
- Reviewing irrelevant context ratio
- Comparing response quality with and without noisy context
- Testing queries that retrieve overlapping documents
- Evaluating conflict or contradiction in retrieved sources
- Reviewing token usage caused by redundant content

---

## Failure Modes

Common failure modes include:
- Duplicate chunks returned
- Multiple versions of the same content retrieved
- Irrelevant content included
- Context includes conflicting source material
- Important content buried under noise
- Excessive tokens consumed by repeated information
- Model focuses on irrelevant detail
- Response becomes longer but less useful

---

## Verification / Signals

Verification signals may include:
- Noise ratio
- Redundancy score
- Duplicate content count
- Context usefulness score
- Token waste indicator
- Human review rating
- Answer quality improvement after filtering
- Reduced latency or cost after context cleanup

---

## Key Note

Noise is not harmless.

Irrelevant or repeated context can actively reduce answer quality and increase operational cost.