# L1 — Reasoning Quality Testing

## What

Reasoning Quality Testing evaluates whether the model’s response demonstrates acceptable logic, interpretation, and problem-solving for the intended task.

It focuses on whether the model reaches a reasonable conclusion using appropriate reasoning, even when the final answer is not a simple factual lookup.

---

## Why

AI models may produce answers that appear correct but are based on weak, incomplete, circular, or invalid reasoning.

Reasoning Quality Testing helps bound the risk of:
- Unsupported conclusions
- Incorrect logic
- Missing assumptions
- Poor tradeoff analysis
- Misinterpreted constraints
- Confident conclusions without sufficient basis
- Recommendations that do not follow from the stated facts

---

## Where

Reasoning Quality Testing applies to model responses requiring interpretation, judgment, or multi-step thinking.

It is used when evaluating:
- Analytical responses
- Recommendations
- Decision support
- Test case generation rationale
- Risk analysis
- Summaries with conclusions
- Scenario interpretation
- Planning or prioritization outputs

This test type belongs at L1 when evaluating reasoning expressed in a direct model response. Multi-step execution, agent planning, tool orchestration, and autonomous decisioning belong to L3.

---

## When

Reasoning Quality Testing may occur:
- During prompt design
- During model evaluation
- During use-case validation
- Before AI is used for decision support
- Before AI is used for risk analysis or planning
- During human review cycles
- After prompt or model changes

---

## How

Reasoning quality may be validated through:
- Human review
- Domain expert evaluation
- Scenario-based testing
- Checking whether conclusions follow from inputs
- Reviewing assumptions
- Testing edge cases
- Comparing reasoning against expected evaluation criteria
- Evaluating whether the model acknowledges uncertainty

Reasoning Quality Testing should focus on whether the logic is acceptable for the intended use, not whether the model imitates a preferred writing style.

---

## Failure Modes

Common failure modes include:
- Invalid conclusion
- Missing assumptions
- Circular reasoning
- Oversimplified analysis
- Ignored constraints
- Poor prioritization
- Incomplete tradeoff evaluation
- Recommendation not supported by evidence
- Reasoning that sounds plausible but does not hold up under review

---

## Verification / Signals

Verification signals may include:
- Human reasoning quality score
- Domain expert approval rate
- Number of unsupported conclusions
- Number of missed assumptions
- Number of reasoning defects
- Scenario pass rate
- Improvement after prompt refinement

---

## Key Note

Reasoning Quality Testing is especially important when AI is used to support planning, analysis, prioritization, risk identification, or quality evaluation.

A useful answer is not only about what the model says.

It is also about whether the answer is logically supportable.