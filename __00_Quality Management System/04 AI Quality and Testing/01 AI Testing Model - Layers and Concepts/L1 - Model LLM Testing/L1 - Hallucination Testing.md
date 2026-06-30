# L1 — Hallucination Testing

## What

Hallucination Testing validates whether the model generates unsupported, fabricated, or invented information.

A hallucination occurs when the model produces content that appears plausible but is not grounded in known facts, provided context, approved sources, or expected domain knowledge.

---

## Why

Hallucinations are one of the most significant risks in AI-enabled systems because they can be difficult for users to detect.

A hallucinated response may sound professional, confident, and specific, even when it is false.

Hallucination Testing helps bound the risk of:
- Fabricated facts
- Unsupported claims
- Invented policies, procedures, or technical details
- False references
- Misleading explanations
- User trust in incorrect information

---

## Where

Hallucination Testing applies to direct model outputs.

It is used when evaluating:
- Open-ended answers
- Summaries
- Explanations
- Recommendations
- Generated procedures
- Generated documentation
- Answers to questions where the model may not know the truth

This test type belongs at L1 when the focus is the model’s tendency to invent information without considering retrieval quality. If hallucination is caused by bad or missing retrieved context, that concern also involves L2.

---

## When

Hallucination Testing may occur:
- During model selection
- During prompt engineering
- During safety and reliability evaluation
- Before releasing user-facing AI capabilities
- After changing prompts, system instructions, model versions, or model settings
- During periodic regression testing
- During production sampling and review

---

## How

Hallucination may be tested through:
- Asking questions with known answers
- Asking questions with no valid answer
- Testing whether the model admits uncertainty
- Comparing responses to known source material
- Reviewing generated citations or source claims
- Using adversarial prompts designed to provoke invention
- Evaluating whether the model distinguishes fact from assumption
- Repeating prompts to observe whether unsupported details appear

Hallucination Testing should include scenarios where the correct response is “I don’t know,” “not enough information,” or “this cannot be determined from the provided context.”

---

## Failure Modes

Common failure modes include:
- Fabricated answer
- Invented source
- Invented business rule
- Invented technical capability
- Unsupported procedural step
- False citation
- Overconfident answer when uncertain
- Mixing true and false details
- Filling gaps instead of identifying missing information

---

## Verification / Signals

Verification signals may include:
- Hallucination rate
- Unsupported claim count
- False citation count
- Correct uncertainty response rate
- Human review results
- Number of fabricated details detected
- Reduction in hallucinations after prompt or guardrail improvements

---

## Key Note

Hallucination Testing is not only about detecting false statements.

It is also about validating whether the model behaves appropriately when it lacks sufficient information.