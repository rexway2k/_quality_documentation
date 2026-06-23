# L2 — Context Relevance Testing

## What

Context Relevance Testing validates whether the retrieved context is relevant to the user’s request, task, or question.

It evaluates whether the content supplied to the model is aligned with the actual intent of the request.

---

## Why

The model may receive context that is technically related but not actually useful for answering the user’s question.

Irrelevant context can cause:
- Confusing responses
- Incorrect emphasis
- Overly broad answers
- Unsupported conclusions
- Hallucination-like behavior
- Poor user experience

Context Relevance Testing ensures that retrieved information is not merely similar, but meaningfully useful.

---

## Where

Context Relevance Testing applies to:
- Retrieved document chunks
- Search result snippets
- Source passages
- Knowledge base excerpts
- Context assemblies passed into prompts
- RAG response pipelines

This test type belongs at L2 because it validates the usefulness of context selected for the model.

---

## When

Context Relevance Testing may occur:
- During retrieval tuning
- During prompt-context assembly design
- During RAG evaluation
- Before release
- After content updates
- After indexing changes
- After changes to query understanding logic
- During production query sampling

---

## How

Context relevance may be validated through:
- Human review of retrieved context
- Query-to-context scoring
- Comparing context against expected answer needs
- Evaluating whether context supports the user’s actual intent
- Testing user query variations
- Reviewing context included in failed responses
- Measuring relevance across top-k retrieved passages

Context Relevance Testing should consider both literal query terms and implied intent.

---

## Failure Modes

Common failure modes include:
- Context is topically related but not answer-supporting
- Context answers a different question
- Context is too general
- Context misses the user’s intended meaning
- Context is outdated for the specific request
- Context includes irrelevant sections from otherwise relevant documents
- Context causes the model to focus on the wrong topic

---

## Verification / Signals

Verification signals may include:
- Context relevance score
- Human relevance rating
- Query-to-context alignment score
- Irrelevant context count
- Context rejection rate
- Failed answer analysis linked to irrelevant context
- Improvement in answer quality after context filtering

---

## Key Note

Context relevance is not the same as retrieval quality overall.

A retrieval system may find a related document, but the exact content passed to the model may still fail relevance expectations.