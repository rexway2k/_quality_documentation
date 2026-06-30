# L2 — Query Understanding & Mapping Testing

## What

Query Understanding & Mapping Testing validates whether the retrieval system correctly interprets the user’s request and maps it to the right sources, terms, concepts, or retrieval strategy.

It evaluates whether the system understands what the user is asking well enough to retrieve useful context.

---

## Why

Users rarely ask questions using the exact language found in source documents.

If the retrieval system does not correctly interpret the query:
- Relevant sources may be missed
- Wrong sources may be retrieved
- Conceptual matches may fail
- Ambiguous requests may be mishandled
- The model may receive context for the wrong intent

This test type helps ensure retrieval works with realistic user language.

---

## Where

Query Understanding & Mapping Testing applies to:
- Search query processing
- Semantic retrieval
- Hybrid retrieval
- Query rewriting
- Intent mapping
- Synonym handling
- Domain terminology mapping
- RAG pipelines

This test type belongs at L2 because it validates how a user request becomes a retrieval operation.

---

## When

Query Understanding & Mapping Testing may occur:
- During retrieval design
- During query preprocessing design
- During prompt/retrieval integration
- Before release
- After adding new terminology or source domains
- After changing retrieval logic
- During production query analysis

---

## How

Query understanding may be validated through:
- Testing realistic user queries
- Testing synonyms and alternate phrasing
- Testing acronyms and internal terminology
- Testing ambiguous queries
- Testing short and incomplete queries
- Comparing retrieved results against expected sources
- Reviewing whether query rewrites preserve intent
- Human review of query-to-result alignment

Test sets should include how people actually ask questions, not only idealized search phrases.

---

## Failure Modes

Common failure modes include:
- User intent misunderstood
- Acronym mapped incorrectly
- Internal term not recognized
- Query rewritten incorrectly
- Ambiguous query retrieves wrong context
- Conceptual match fails
- Exact keyword matching misses relevant content
- Search retrieves based on surface words instead of meaning

---

## Verification / Signals

Verification signals may include:
- Query interpretation success rate
- Expected source retrieval rate
- Acronym or terminology match rate
- Query rewrite accuracy
- Human query alignment score
- Failed-query analysis
- Improvement after synonym, taxonomy, or query mapping updates

---

## Key Note

Query understanding is often where enterprise AI systems succeed or fail.

If the system misunderstands the question, even high-quality documents and a strong model may produce a poor answer.