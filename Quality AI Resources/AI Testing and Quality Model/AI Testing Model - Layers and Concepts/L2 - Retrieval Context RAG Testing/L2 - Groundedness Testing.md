# L2 — Groundedness Testing

## What

Groundedness Testing validates whether the model’s response is supported by the retrieved context.

A grounded response is one where claims made by the model can be traced back to the information supplied to it.

---

## Why

A response may be fluent and relevant but still not grounded in the provided sources.

Groundedness Testing helps bound the risk of:
- Unsupported claims
- Fabricated details
- Misuse of retrieved context
- Answers that go beyond available evidence
- Model assumptions presented as facts
- Loss of trust in AI outputs

---

## Where

Groundedness Testing applies at the connection point between retrieved context and generated response.

It is used when evaluating:
- RAG-generated answers
- Source-supported summaries
- Policy or procedure responses
- Knowledge-base answers
- Responses requiring citations or source backing

This test type sits at L2 because it validates whether generation is properly supported by retrieved context. It also depends on L1 model behavior.

---

## When

Groundedness Testing may occur:
- During RAG response evaluation
- During prompt and retrieval design
- Before release
- After retrieval changes
- After prompt changes
- During production response sampling
- During investigation of hallucination-like failures

---

## How

Groundedness may be validated through:
- Comparing each response claim against retrieved context
- Checking whether citations support the answer
- Human review of source alignment
- Automated claim-source matching where available
- Testing questions where the answer is not present in context
- Evaluating whether the model refuses or qualifies answers when context is insufficient
- Reviewing whether conclusions are supported by retrieved evidence

Groundedness Testing should separate unsupported model behavior from missing or poor retrieval.

---

## Failure Modes

Common failure modes include:
- Response makes claims not present in context
- Response contradicts retrieved context
- Response exaggerates or overstates source material
- Response combines unrelated pieces of context incorrectly
- Response cites a source that does not support the claim
- Response answers despite insufficient context
- Response fails to indicate uncertainty

---

## Verification / Signals

Verification signals may include:
- Groundedness score
- Unsupported claim count
- Citation support rate
- Claim-source match rate
- Human source alignment rating
- Contradiction count
- Correct insufficient-context handling rate

---

## Key Note

Groundedness is one of the most important tests in RAG systems.

It answers the question:

> “Can this response be justified by the context we provided?”