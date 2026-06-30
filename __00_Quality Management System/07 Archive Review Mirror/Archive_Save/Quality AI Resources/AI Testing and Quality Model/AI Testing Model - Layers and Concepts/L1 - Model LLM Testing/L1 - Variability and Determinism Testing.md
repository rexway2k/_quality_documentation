# L1 — Variability & Determinism Testing

## What

Variability & Determinism Testing evaluates how consistently the model responds to the same or similar prompts over repeated runs.

It examines whether output variation stays within acceptable boundaries for the intended use.

---

## Why

AI models are probabilistic and may produce different answers across repeated executions.

Some variation may be acceptable or even useful. Too much variation can create risk, confusion, rework, or inconsistent user experiences.

This test type helps bound the risk of:
- Inconsistent answers
- Unstable behavior
- Unrepeatable validation
- Conflicting recommendations
- Regression failures that are difficult to reproduce
- Overconfidence in one-off successful outputs

---

## Where

Variability & Determinism Testing applies to repeated model responses.

It is used when evaluating:
- Same prompt repeated multiple times
- Similar prompts with small wording changes
- Expected response consistency
- Regression prompt suites
- Structured output generation
- Decision-support prompts
- High-risk or high-control use cases

This test type belongs at L1 when evaluating model response stability itself. Variability caused by changing retrieved context, memory, tools, or workflows involves higher layers.

---

## When

Variability & Determinism Testing may occur:
- During model selection
- During prompt design
- Before using AI in repeatable workflows
- Before automation or workflow integration
- After changing model parameters
- After model upgrades
- During regression evaluation

---

## How

Variability may be validated through:
- Repeated prompt execution
- Prompt paraphrase testing
- Comparing response similarity
- Measuring format consistency
- Evaluating answer consistency across runs
- Testing with different model settings where applicable
- Reviewing whether variation changes meaning or outcome

The goal is not always identical output.

The goal is acceptable variation within defined risk boundaries.

---

## Failure Modes

Common failure modes include:
- Different answers to the same question
- Conflicting recommendations
- Format inconsistency
- Meaning changes across runs
- Inconsistent refusal behavior
- Unstable reasoning path
- High sensitivity to minor wording changes
- Regression test results that cannot be reproduced

---

## Verification / Signals

Verification signals may include:
- Response consistency score
- Semantic similarity score
- Format consistency rate
- Repeated-run agreement rate
- Prompt paraphrase agreement rate
- Number of conflicting outputs
- Variation range across repeated executions

---

## Key Note

AI testing should not assume deterministic behavior.

For AI systems, “acceptable consistency” must be defined based on use case risk, not assumed from traditional automated testing expectations.