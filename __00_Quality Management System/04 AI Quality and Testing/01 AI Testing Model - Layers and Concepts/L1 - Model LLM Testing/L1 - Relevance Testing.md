# L1 — Relevance Testing

## What

Relevance Testing validates whether the model’s response directly addresses the user’s prompt, task, or intended outcome.

A response may be accurate but still not useful if it does not answer the question that was asked or does not align with the user’s need.

---

## Why

AI models can produce responses that are well-written but misaligned with the actual request.

Relevance Testing helps bound the risk of:
- Off-topic outputs
- Overly broad responses
- Technically correct but unusable answers
- Ignoring user intent
- Answering a different question than the one asked
- Excessive or irrelevant detail

---

## Where

Relevance Testing applies to direct prompt-response interactions.

It is used when evaluating:
- User questions
- Task instructions
- Summaries
- Recommendations
- Drafted content
- Generated analysis
- Model behavior in role-based or task-based prompts

This test type belongs at L1 when the issue is the model’s response alignment to the prompt itself. If relevance depends on whether the correct context was retrieved, that also involves L2.

---

## When

Relevance Testing may occur:
- During prompt design
- During model evaluation
- During workflow design
- Before release of user-facing AI features
- During regression testing after prompt or model changes
- During production output sampling

---

## How

Relevance may be validated through:
- Human review of response alignment
- Scoring response usefulness against the prompt
- Comparing output to expected answer criteria
- Testing with a variety of prompt phrasings
- Evaluating whether the model follows the stated task
- Measuring whether unnecessary unrelated content is included
- Reviewing whether the response satisfies the user’s intended outcome

Relevance criteria should define what a good answer must include and what it should avoid.

---

## Failure Modes

Common failure modes include:
- Response does not answer the question
- Response answers only part of the question
- Response adds unnecessary unrelated content
- Response shifts scope without reason
- Response ignores key constraints
- Response overgeneralizes
- Response provides generic content instead of task-specific content
- Response follows a related but incorrect interpretation of the prompt

---

## Verification / Signals

Verification signals may include:
- Relevance score
- Human usefulness rating
- % of responses aligned to prompt intent
- Number of off-topic responses
- Number of incomplete responses
- Number of responses requiring re-prompting
- Reduction in irrelevant content after prompt refinement

---

## Key Note

Relevance is not the same as accuracy.

A response can be accurate and still fail if it does not satisfy the specific user request or business need.