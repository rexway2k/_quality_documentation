# L2 — Retrieval Precision & Recall Testing

## What

Retrieval Precision & Recall Testing evaluates whether the retrieval system returns the right amount of relevant information.

Precision focuses on whether retrieved results are relevant.

Recall focuses on whether all needed relevant information was retrieved.

---

## Why

A retrieval system can fail in two different ways:

- It can return too much irrelevant content
- It can miss important relevant content

Both failure patterns create risk.

Low precision introduces noise and may confuse the model.

Low recall omits important information and may cause incomplete or incorrect responses.

---

## Where

Retrieval Precision & Recall Testing applies to:
- Vector search
- Keyword search
- Hybrid search
- RAG pipelines
- Enterprise knowledge retrieval
- Document retrieval
- Search-ranking systems

This test type belongs at L2 because it evaluates the retrieval result set before generation.

---

## When

Retrieval Precision & Recall Testing may occur:
- During retrieval system design
- During search configuration
- During embedding model selection
- During index tuning
- Before release
- After content updates
- After search or ranking changes
- During regression testing of known query sets

---

## How

Precision and recall may be validated through:
- Known query-to-source mappings
- Golden query datasets
- Human labeling of relevant documents or chunks
- Top-k result evaluation
- Measuring whether the expected source appears in retrieved results
- Measuring whether irrelevant results appear in retrieved results
- Comparing retrieval results across configurations

Precision and recall should be evaluated using realistic queries, not only ideal or perfectly worded questions.

---

## Failure Modes

Common failure modes include:
- Relevant source missing from retrieved results
- Relevant source appears too low in ranking
- Irrelevant sources appear above relevant ones
- Too many unrelated chunks returned
- Search retrieves keyword matches without meaning relevance
- Search retrieves semantically similar but incorrect content
- Important secondary sources are omitted
- Retrieval returns partial context when full context is needed

---

## Verification / Signals

Verification signals may include:
- Precision score
- Recall score
- Top-k accuracy
- Expected source included rate
- Irrelevant result rate
- Missed source count
- Human relevance rating
- Retrieval regression score

---

## Key Note

Precision and recall often require tradeoffs.

High recall may bring in more noise. High precision may omit useful supporting information.

The appropriate balance depends on the use case risk and expected answer behavior.