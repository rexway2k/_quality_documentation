# L1 — Safety Testing

## What

Safety Testing validates whether the model avoids producing harmful, unsafe, inappropriate, or unacceptable responses.

Safety includes whether the model respects defined system constraints, use-case boundaries, and responsible AI expectations.

---

## Why

AI systems can generate content that may create risk for users, teams, customers, or the organization.

Safety Testing helps bound the risk of:
- Harmful outputs
- Unsafe recommendations
- Inappropriate advice
- Responses outside approved use
- Content that violates policy or governance expectations
- Model behavior that creates business, legal, ethical, or operational risk

---

## Where

Safety Testing applies to direct model outputs.

It is used when evaluating:
- User-facing AI responses
- Internal assistant responses
- Generated recommendations
- Explanations
- Guidance
- Content generation
- Decision-support outputs

This test type belongs at L1 when evaluating the model’s generated response itself. Broader safety controls involving workflow permissions, tool execution, policy enforcement, or governance belong to higher layers.

---

## When

Safety Testing may occur:
- During use-case review
- During model selection
- During prompt design
- Before release
- After prompt or model changes
- During red-team style evaluation
- During ongoing monitoring and sampling

---

## How

Safety may be validated through:
- Scenario-based testing
- Adversarial prompts
- Policy-focused review
- Human review
- Unsafe output detection
- Testing refusal behavior
- Testing boundary conditions
- Evaluating whether the model redirects appropriately

Safety Testing should include both expected use and foreseeable misuse.

---

## Failure Modes

Common failure modes include:
- Unsafe recommendation
- Inappropriate content
- Policy-violating response
- Failure to refuse disallowed requests
- Over-refusal of acceptable requests
- Misleading confidence in risky scenarios
- Lack of appropriate caution
- Response that creates operational or user harm

---

## Verification / Signals

Verification signals may include:
- Unsafe output rate
- Correct refusal rate
- Over-refusal rate
- Human safety review score
- Policy adherence rate
- Number of critical safety failures
- Reduction in unsafe responses after guardrail improvements

---

## Key Note

Safety Testing is use-case dependent.

The same model response may be acceptable in one context and unsafe in another depending on audience, use, data sensitivity, and business impact.