# L1 — Output Format Testing

## What

Output Format Testing validates whether the model produces responses in the required structure, format, schema, tone, or presentation style.

It ensures the response is not only meaningful, but usable in the expected workflow.

---

## Why

AI outputs often need to be consumed by humans, systems, downstream prompts, workflows, or automation.

Even when the content is correct, the output may fail if it does not follow the expected structure.

Output Format Testing helps bound the risk of:
- Unusable responses
- Broken downstream processing
- Manual rework
- Formatting drift
- Inconsistent structure
- Failure to follow requested templates
- Outputs that cannot be parsed or reviewed reliably

---

## Where

Output Format Testing applies to direct model responses.

It is used when evaluating:
- Structured responses
- JSON or schema-like outputs
- Tables
- Summaries
- Templates
- Generated documentation
- Prompt output used by another workflow
- AI-generated content requiring a consistent format

This test type belongs at L1 when evaluating whether the model follows output instructions. If the output is passed into tools, APIs, or workflow systems, related validation also belongs to L3 or L4.

---

## When

Output Format Testing may occur:
- During prompt design
- During reusable prompt template creation
- Before workflow integration
- Before production release
- After prompt or model changes
- During regression testing
- During monitoring of structured outputs

---

## How

Output format may be validated through:
- Schema validation
- Template comparison
- Human review
- Automated parsing checks
- Required section checks
- Field presence validation
- Format consistency testing
- Testing repeated outputs for structural stability

Where output is intended for machine consumption, stricter validation is required.

---

## Failure Modes

Common failure modes include:
- Missing required section
- Incorrect structure
- Invalid JSON or schema output
- Format drift
- Extra text where structured-only output was required
- Inconsistent tone
- Incorrect heading structure
- Output cannot be parsed
- Output requires excessive manual cleanup

---

## Verification / Signals

Verification signals may include:
- Format adherence rate
- Schema validation pass rate
- Parse success rate
- Required field completion rate
- Template compliance score
- Manual cleanup effort
- Number of format-related failures

---

## Key Note

Output Format Testing is not cosmetic.

For AI-enabled workflows, structure is often part of the contract between the model and the next consumer of the output.