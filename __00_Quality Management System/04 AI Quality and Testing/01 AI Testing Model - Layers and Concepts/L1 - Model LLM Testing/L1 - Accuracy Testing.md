# L1 — Accuracy Testing

## What

Accuracy Testing validates whether the model produces correct responses for the intended task, prompt, or use case.

Accuracy is concerned with whether the response is factually, logically, or operationally correct based on the expected answer, business rule, known source of truth, or domain expectation.

---

## Why

AI models can produce responses that sound confident, complete, and well-written while still being incorrect.

Accuracy Testing helps determine whether the model can be trusted for the intended use before it is connected to retrieval systems, agents, tools, workflows, or user-facing applications.

This test type bounds the risk of:
- Incorrect answers
- Misleading recommendations
- False confidence
- Business rule misinterpretation
- Downstream decisions based on wrong information

---

## Where

Accuracy Testing applies at the direct model response layer.

It is used when validating:
- Prompt-response behavior
- Question-answer scenarios
- Classification tasks
- Summarization outputs
- Reasoning tasks
- Domain-specific answer generation
- Model selection or comparison

This test type belongs at L1 because it evaluates the model’s response itself, not retrieval quality, tool execution, workflow completion, or system integration.

---

## When

Accuracy Testing may occur:
- During model selection
- During prompt design
- During proof-of-concept evaluation
- Before production release
- After model upgrades or configuration changes
- During regression evaluation
- During ongoing monitoring when outputs can be scored or sampled

---

## How

Accuracy may be validated through:
- Comparison against known correct answers
- Evaluation against curated golden datasets
- Review by domain experts
- Automated scoring where expected outputs are well-defined
- Human review where answers require judgment
- Spot-checking outputs against trusted references
- Regression testing across repeated prompt sets

Accuracy Testing should define what “correct” means before evaluation begins.

---

## Failure Modes

Common failure modes include:
- Incorrect factual statement
- Incorrect calculation
- Incorrect interpretation of business rules
- Incorrect classification
- Incorrect summary
- Confident but wrong answer
- Partially correct answer that omits critical context
- Answer that is technically true but not appropriate for the use case

---

## Verification / Signals

Verification signals may include:
- Accuracy score
- Percent of correct responses
- Human review rating
- Domain expert approval rate
- Regression pass rate
- Number of critical accuracy failures
- Number of responses requiring correction
- Accuracy trend over time

---

## Key Note

Accuracy does not prove the full AI system is ready.

A model may be accurate in isolation but still fail when paired with poor retrieval, weak prompts, agentic workflows, tool calls, or production system constraints.