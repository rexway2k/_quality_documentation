# L1 — Faithfulness Testing

## What

Faithfulness Testing validates whether the model stays true to the information, instructions, context, or constraints it was given.

At L1, faithfulness focuses on whether the model follows the provided prompt, instruction, or supplied information without adding unsupported assumptions or changing the meaning.

---

## Why

A model may produce fluent responses while subtly changing, expanding, weakening, or distorting the original instruction or source material.

Faithfulness Testing helps bound the risk of:
- Misstated information
- Changed meaning
- Added assumptions
- Unsupported interpretation
- Ignored constraints
- Instruction drift
- Output that appears aligned but is not actually faithful to the input

---

## Where

Faithfulness Testing applies to model responses where the model is expected to preserve meaning or obey constraints.

It is used when evaluating:
- Summarization
- Rewriting
- Transformation of text
- Structured extraction
- Instruction-following
- Constraint-based response generation
- Responses based on provided prompt context

This test type belongs at L1 when faithfulness is measured against the prompt or supplied input. In RAG systems, faithfulness to retrieved sources also involves L2.

---

## When

Faithfulness Testing may occur:
- During prompt design
- During content transformation validation
- During summarization evaluation
- During model comparison
- Before releasing AI-assisted documentation or analysis features
- After model, prompt, or instruction changes
- During regression testing

---

## How

Faithfulness may be validated through:
- Comparing output against the original input
- Checking whether meaning was preserved
- Reviewing whether constraints were followed
- Identifying added assumptions
- Identifying omitted critical details
- Testing with prompts that include explicit rules
- Evaluating summaries against source text
- Human review where meaning preservation requires judgment

Faithfulness Testing should define what must be preserved and what may be changed.

---

## Failure Modes

Common failure modes include:
- Added unsupported information
- Omitted critical information
- Changed meaning
- Weakened or strengthened claims
- Ignored constraints
- Reframed the user’s request incorrectly
- Summarized in a way that distorts priority or intent
- Treated assumptions as facts

---

## Verification / Signals

Verification signals may include:
- Faithfulness score
- Constraint adherence rate
- Unsupported addition count
- Critical omission count
- Human review approval rate
- Number of meaning-changing errors
- Regression results across known prompt sets

---

## Key Note

Faithfulness is especially important when AI is used to summarize, rewrite, transform, or interpret existing information.

The goal is not just that the response sounds good.

The goal is that it preserves the intended meaning and constraints.