# L2 — Retrieval / Context (RAG) Testing

## Purpose

This layer focuses on validating how the system retrieves, prepares, and provides context to the model.

Retrieval / Context Testing ensures that:
- The right information is selected
- The information is relevant to the request
- The information is correctly structured and usable
- The model is grounded in appropriate context

This layer evaluates whether the system supplies the model with the correct inputs required to generate reliable responses.

---

## Layer Summary

| Dimension | Description |
|---|---|
| Layer | L2 — Retrieval / Context (RAG) |
| Primary Question | Did we give the model the right information to answer correctly? |
| Testing Focus | Retrieval quality, context selection, grounding, and source alignment |
| Main Risk | The model produces incorrect or misleading outputs due to poor or missing context |
| Output of This Layer | Confidence that the model is operating on accurate, relevant, and sufficient context |

---

## What This Layer Tests

This layer tests how context is selected and supplied to the model.

It includes validation of:

- Retrieval quality (precision and relevance)
- Context completeness
- Context relevance to the query
- Groundedness of responses in source material
- Source selection correctness
- Embedding effectiveness
- Chunking strategies
- Context window utilization
- Redundancy or noise in retrieved context
- Alignment between retrieved data and user intent

---

## What This Layer Does Not Test

This layer does not validate:

- Whether the model itself reasons correctly (L1)
- Whether prompt structure is correct (L1)
- Whether agents choose the correct tools (L3)
- Whether workflows execute correctly (L3)
- Whether systems behave correctly end-to-end (L4)
- Whether governance, compliance, or safety policies are enforced (L5)

This layer assumes:
- The model is already capable of generating appropriate responses (L1)
- The data exists and is valid (L0)

---

## Where This Layer Sits in the AI Testing Model

```text
L5 — Governance / Responsible AI
L4 — System Integration / Experience
L3 — Agentic Systems
L2 — Retrieval / Context (RAG)
L1 — Model / LLM
L0 — Data Foundation

L2 sits between the model and the broader system, providing context that directly influences model output.

Why This Layer Matters
In most AI systems, especially enterprise applications, the model does not operate purely on its pretrained knowledge.
Instead, it relies on retrieved context such as:

Internal documentation
Knowledge bases
Policies
Customer data
Operational data

If the context is wrong, incomplete, outdated, or irrelevant:

The model may produce correct answers based on incorrect context
The model may appear accurate but be grounded in the wrong source
The system may return misleading or unsafe outputs

Many issues labeled as “model problems” are actually retrieval problems.

Core Risk
The core risk at this layer is that the model receives incorrect, incomplete, irrelevant, or misleading context.
This can result in:

Confident but incorrect answers
Hallucination-like behavior grounded in wrong data
Use of outdated or invalid information
Ignoring the most relevant source
Misalignment with user intent


Layer Responsibility
This layer is responsible for answering:

Did we retrieve the right documents or data?
Is the retrieved content relevant to the request?
Did we retrieve enough information to answer the question?
Is the information current and valid?
Is the content free of unnecessary noise or irrelevant detail?
Is the content structured in a way the model can use?
Does the system prefer correct sources over irrelevant ones?


Contract Boundary
Input: User query, intent, or request
Output: Retrieved context supplied to the model
This layer validates the transformation between a request and the context selected to support that request.
The contract is:

Given a request, the system retrieves and prepares context that is sufficient, relevant, and appropriate for the model to produce a correct response.


Relationship to Other Layers
Relationship to L0 — Data Foundation
L2 depends on L0 for:

Data quality
Data completeness
Data freshness
Data accuracy
Data structure

If the underlying data is incorrect, retrieval will also be incorrect.

Relationship to L1 — Model / LLM
L1 validates model behavior in isolation.
L2 validates whether the model is given the correct context.
A model may perform well in L1 testing but still produce poor results in L2 scenarios due to bad context.

Relationship to L3 — Agentic Systems
L2 focuses on retrieving information.
L3 focuses on how that information is used within workflows, decisions, and tool interactions.
Agentic systems may depend on retrieval results as part of multi-step processes.

Relationship to L4 — System Integration / Experience
L4 validates how the full system behaves with real users.
L2 contributes to L4 by determining whether the system provides correct context during real usage.

Relationship to L5 — Governance / Responsible AI
L2 impacts governance concerns such as:

Use of approved sources
Avoidance of restricted or sensitive data
Correct sourcing and attribution
Data compliance

However, governance controls are validated more broadly at L5.

Test Types
The following Test Types define validation at this layer:

Retrieval Quality Testing
Retrieval Precision & Recall Testing
Context Relevance Testing
Context Completeness Testing
Groundedness Testing
Source Attribution & Traceability Testing
Embedding Effectiveness Testing
Chunking Strategy Testing
Context Window Utilization Testing
Context Noise & Redundancy Testing
Data Freshness in Retrieval Testing
Query Understanding & Mapping Testing


Characteristics of Testing at This Layer
Testing at this layer is:

Semi-deterministic (more structured than L3+, less than L0/L1)
Dependent on data quality and indexing strategies
Dependent on ranking, similarity, and retrieval logic
Sensitive to user query phrasing
Often evaluated using datasets, scoring, and human review
Critical for minimizing hallucination and improving accuracy


Examples of What is Validated
Examples include:

Did the system retrieve the correct documents for a query?
Were the most relevant sections of content included?
Was important information missing?
Was irrelevant content included?
Did the model response align with retrieved context?
Were the correct sources used?
Did retrieval favor outdated information over current data?
Was the retrieved content structured appropriately for the model?
Did the system retrieve enough context to answer the question?


Common Failure Patterns
Common failures at this layer include:

Retrieving irrelevant documents
Missing critical information
Returning incomplete context
Including too much irrelevant content
Selecting outdated content
Incorrect ranking of results
Poor embedding or similarity matching
Ineffective chunking leading to loss of meaning
Context window overflow causing important data to be dropped
Misalignment between query intent and retrieved results


Key Implications

Many “model errors” are actually retrieval errors
Improving retrieval often improves system accuracy without changing the model
Context quality directly impacts model output quality
Retrieval must be tested independently from model behavior
Testing must simulate real queries and real content usage
Retrieval effectiveness depends on both data and indexing strategy


Human Oversight
Human review is often required at this layer, especially when:

Determining relevance requires domain judgment
Evaluating whether important context was omitted
Reviewing complex or ambiguous queries
Validating source selection
Assessing whether retrieval aligns with user intent

Human evaluation complements automated scoring but cannot be fully replaced in complex cases.

Navigation
Proceed to Test Types within this layer:

Retrieval Quality Testing
Retrieval Precision & Recall Testing
Context Relevance Testing
Context Completeness Testing
Groundedness Testing
Source Attribution & Traceability Testing
Embedding Effectiveness Testing
Chunking Strategy Testing
Context Window Utilization Testing
Context Noise & Redundancy Testing
Data Freshness in Retrieval Testing
Query Understanding & Mapping Testing