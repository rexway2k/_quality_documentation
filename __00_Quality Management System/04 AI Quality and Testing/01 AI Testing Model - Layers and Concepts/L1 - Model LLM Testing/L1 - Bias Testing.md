# L1 — Bias Testing

## What

Bias Testing validates whether the model produces outputs that reflect unfair, inappropriate, or unsupported assumptions.

Bias may appear in how the model describes people, options, risks, recommendations, success criteria, or decisions.

---

## Why

AI models learn patterns from large datasets and may reproduce or amplify biased patterns.

Bias Testing helps bound the risk of:
- Unfair outcomes
- Stereotyped assumptions
- Unequal treatment
- Proxy discrimination
- Skewed recommendations
- Outputs that appear neutral but disadvantage certain people or groups

---

## Where

Bias Testing applies to direct model outputs.

It is used when evaluating:
- Recommendations
- Prioritization
- Classification
- Summaries involving people or groups
- Generated personas or examples
- Decision-support outputs
- Prompts involving evaluation criteria

This test type belongs at L1 when evaluating the model’s response behavior. Bias caused by unrepresentative datasets also involves L0. Bias caused by workflow or business rule design may involve higher layers.

---

## When

Bias Testing may occur:
- During dataset and prompt design
- During model selection
- During evaluation of sensitive use cases
- Before production release
- During responsible AI review
- After model or prompt changes
- During ongoing monitoring and sampling

---

## How

Bias may be validated through:
- Scenario testing
- Counterfactual prompt testing
- Review of outputs across different user profiles or conditions
- Analysis of recommendation patterns
- Human review
- Testing for proxy variables
- Comparing outputs across equivalent scenarios
- Evaluating whether criteria are explicit and fair

Bias Testing should inspect both obvious bias and subtle bias introduced through apparently neutral criteria.

---

## Failure Modes

Common failure modes include:
- Stereotyped assumptions
- Unequal recommendation quality
- Proxy bias
- Skewed prioritization
- Different treatment for equivalent scenarios
- Biased framing
- Unfair criteria embedded in the prompt or response
- Outputs that reinforce historical disadvantage

---

## Verification / Signals

Verification signals may include:
- Bias finding count
- Counterfactual consistency score
- Human responsible AI review results
- Difference in output patterns across equivalent scenarios
- Proxy bias indicators
- Reduction in biased outputs after prompt, model, or dataset changes

---

## Key Note

Bias Testing is not limited to protected characteristics.

Bias can also appear through proxies, assumptions, framing, incomplete criteria, or definitions of success that appear neutral but produce unfair outcomes.