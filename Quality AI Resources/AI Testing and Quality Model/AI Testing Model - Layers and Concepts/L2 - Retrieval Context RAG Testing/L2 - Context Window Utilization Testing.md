# L2 — Context Window Utilization Testing

## What

Context Window Utilization Testing validates whether the system uses the available model context window effectively.

It evaluates what information is included, excluded, prioritized, or dropped when preparing context for the model.

---

## Why

Models have limits on how much context they can process.

If the system uses the context window poorly:
- Important information may be omitted
- Irrelevant information may crowd out relevant content
- The model may ignore critical details
- Responses may become incomplete or incorrect
- Cost and latency may increase unnecessarily

Context Window Utilization Testing ensures that the most useful information is included in the prompt context.

---

## Where

Context Window Utilization Testing applies to:
- Prompt assembly
- RAG context packaging
- Multi-document retrieval
- Long-context workflows
- Summarization pipelines
- Systems that include documents, chat history, metadata, or instructions in the model request

This test type belongs at L2 because it validates context preparation before model generation.

---

## When

Context Window Utilization Testing may occur:
- During prompt and context design
- During RAG pipeline development
- Before production release
- After retrieval limit changes
- After prompt template changes
- After adding new source types
- During cost, latency, or response quality analysis

---

## How

Context window utilization may be validated through:
- Reviewing assembled prompts
- Measuring token usage
- Checking whether required context is included
- Checking whether irrelevant context is excluded
- Testing long or complex queries
- Testing multi-source questions
- Reviewing truncation behavior
- Comparing response quality against different context packaging strategies

The goal is effective context use, not maximum context use.

---

## Failure Modes

Common failure modes include:
- Critical content excluded
- Important context truncated
- Irrelevant content included
- Too many retrieved chunks included
- Instructions pushed out by retrieved content
- Source order causes poor attention to important context
- Excessive token usage
- Increased latency or cost without quality improvement

---

## Verification / Signals

Verification signals may include:
- Token usage
- Required context inclusion rate
- Truncation occurrence rate
- Context relevance ratio
- Answer quality by context size
- Latency and cost impact
- Human review of assembled context
- Improvement after context selection tuning

---

## Key Note

More context is not automatically better.

The system should provide the model with the right context, not simply the most context.