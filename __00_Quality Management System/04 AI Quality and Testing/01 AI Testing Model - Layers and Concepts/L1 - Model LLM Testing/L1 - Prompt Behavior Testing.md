# L1 — Prompt Behavior Testing

## What

Prompt Behavior Testing validates how the model responds to prompts, instructions, roles, constraints, examples, and formatting requirements.

It evaluates whether the model behaves as intended when given specific instructions.

---

## Why

AI model behavior is highly influenced by prompt design.

Small changes in wording, structure, examples, or constraints can significantly change the output.

Prompt Behavior Testing helps bound the risk of:
- Prompt sensitivity
- Instruction drift
- Misinterpreted intent
- Ignored constraints
- Inconsistent behavior
- Overreliance on unclear prompts
- Outputs that vary too much based on phrasing

---

## Where

Prompt Behavior Testing applies to direct interaction between prompts and model responses.

It is used when evaluating:
- System prompts
- User prompts
- Role prompts
- Prompt templates
- Few-shot examples
- Structured output instructions
- Reusable prompt patterns
- AI assistant or copilot behavior

This test type belongs at L1 because it validates model response behavior driven by prompt construction.

---

## When

Prompt Behavior Testing may occur:
- During prompt design
- During prompt template creation
- During model selection
- Before reuse of prompts in production workflows
- After prompt updates
- After model changes
- During regression testing of known prompts

---

## How

Prompt behavior may be tested through:
- Testing multiple prompt variations
- Testing boundary prompts
- Testing unclear or incomplete prompts
- Testing prompts with explicit constraints
- Testing prompts with conflicting instructions
- Testing prompts with examples and without examples
- Comparing output stability across prompt versions
- Reviewing whether the response follows role, tone, structure, and format requirements

Prompt Behavior Testing should include both expected-use prompts and likely user variations.

---

## Failure Modes

Common failure modes include:
- Ignored instructions
- Misinterpreted prompt intent
- Output format drift
- Role drift
- Tone drift
- Overly broad response
- Unwanted assumptions
- Failure to follow constraints
- Response changes significantly with minor prompt wording changes
- Prompt template does not produce repeatable behavior

---

## Verification / Signals

Verification signals may include:
- Instruction-following score
- Prompt variation pass rate
- Format adherence rate
- Constraint adherence rate
- Human review score
- Number of prompt-induced failures
- Regression comparison across prompt versions

---

## Key Note

Prompt quality is part of the quality boundary.

If an AI capability depends on a prompt, that prompt should be treated as a testable artifact, not casual wording.