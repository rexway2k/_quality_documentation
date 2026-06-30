# L2 — Chunking Strategy Testing

## What

Chunking Strategy Testing validates whether source content is divided into pieces that preserve meaning and support effective retrieval.

Chunking determines what portions of content are retrieved and passed to the model.

---

## Why

Poor chunking can break context.

If content is split incorrectly, the retrieval system may return fragments that:
- Lack necessary surrounding detail
- Omit definitions or exceptions
- Separate related steps
- Lose meaning
- Create misleading context

Chunking Strategy Testing helps ensure retrieved content remains meaningful and usable.

---

## Where

Chunking Strategy Testing applies to:
- Document ingestion pipelines
- Knowledge base indexing
- Vector database content preparation
- RAG systems
- Policy and procedure documents
- Long-form documentation
- Structured and semi-structured content

This test type belongs at L2 because chunking directly affects retrieved context quality.

---

## When

Chunking Strategy Testing may occur:
- During content ingestion design
- During RAG pipeline setup
- Before indexing large document sets
- Before production release
- After changing chunk size or overlap
- After adding new document types
- During investigation of incomplete or misleading answers

---

## How

Chunking may be validated through:
- Reviewing chunk boundaries
- Testing known questions against expected source sections
- Checking whether chunks preserve complete ideas
- Evaluating chunk overlap
- Comparing answer quality across chunking strategies
- Testing documents with headings, tables, lists, procedures, and exceptions
- Human review of retrieved chunks

Chunking should be evaluated based on whether retrieved chunks provide enough meaning to support correct answers.

---

## Failure Modes

Common failure modes include:
- Critical information split across chunks
- Definitions separated from terms
- Exceptions separated from rules
- Procedure steps separated from sequence
- Chunk too small to preserve meaning
- Chunk too large and noisy
- Headings detached from content
- Tables or lists split incorrectly
- Related context omitted due to chunk boundaries

---

## Verification / Signals

Verification signals may include:
- Chunk usefulness score
- Retrieval success by source section
- Answer completeness score
- Human review of chunk coherence
- Number of boundary-related failures
- Reduction in incomplete answers after chunking changes
- Comparison of answer quality across chunking configurations

---

## Key Note

Chunking is not just a technical preprocessing step.

It defines what the model is able to “see” when answering a question.