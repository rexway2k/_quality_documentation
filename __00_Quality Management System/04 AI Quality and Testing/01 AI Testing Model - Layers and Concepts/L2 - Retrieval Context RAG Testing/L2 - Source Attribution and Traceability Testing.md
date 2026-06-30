# L2 — Source Attribution & Traceability Testing

## What

Source Attribution & Traceability Testing validates whether AI responses can be traced back to the sources used to generate them.

It evaluates whether the system identifies, preserves, and presents source information accurately.

---

## Why

Enterprise AI systems often need users to understand where an answer came from.

Poor attribution creates risk because users may:
- Trust unsupported answers
- Be unable to verify information
- Misunderstand the source of a response
- Use outdated or unauthorized information
- Lose confidence in the system

Traceability helps support trust, auditability, and governance.

---

## Where

Source Attribution & Traceability Testing applies to:
- RAG pipelines
- Citation systems
- Knowledge base references
- Retrieved document metadata
- Source links
- Answer explanations
- Audit logs involving retrieved context

This test type belongs at L2 because it validates the connection between retrieved context and source identity.

---

## When

Source Attribution & Traceability Testing may occur:
- During retrieval pipeline design
- During citation feature validation
- During governance review
- Before release
- After content migration
- After source metadata changes
- During audits or production sampling

---

## How

Source attribution may be validated through:
- Checking whether retrieved context retains source metadata
- Verifying citations point to the correct document or passage
- Comparing answer claims to cited sources
- Reviewing source links
- Testing source display behavior
- Validating audit records
- Confirming that source identity is not lost during chunking or transformation

Source traceability should include enough information for a user or reviewer to verify the basis of the response.

---

## Failure Modes

Common failure modes include:
- Missing citation
- Incorrect citation
- Citation points to unrelated content
- Source metadata lost during indexing
- Source link broken
- Answer references a source not used
- Source appears authoritative but is outdated or invalid
- User cannot verify response origin

---

## Verification / Signals

Verification signals may include:
- Source attribution accuracy
- Citation correctness rate
- Traceability completeness
- Broken source link count
- Claim-to-source alignment score
- Audit trace completeness
- Human source verification results

---

## Key Note

Source attribution is not the same as groundedness.

Groundedness asks whether the answer is supported.

Attribution asks whether the support can be identified, traced, and verified.