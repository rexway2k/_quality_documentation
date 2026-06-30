# L2 — Data Freshness in Retrieval Testing

## What

Data Freshness in Retrieval Testing validates whether retrieval uses current, valid, and appropriate source information.

It focuses on whether the retrieval layer selects fresh information when multiple versions or time-sensitive sources exist.

---

## Why

AI systems may produce incorrect answers if retrieval surfaces outdated information.

Freshness issues can cause:
- Use of obsolete policies or procedures
- Incorrect operational guidance
- Misleading answers
- Compliance risk
- Conflicting outputs depending on which source is retrieved

This test type ensures retrieval respects the currency and validity of source material.

---

## Where

Data Freshness in Retrieval Testing applies to:
- Knowledge bases
- Policy repositories
- Procedure documentation
- Versioned documents
- Indexed enterprise content
- Cached retrieval results
- RAG systems using time-sensitive information

This test type belongs at L2 because it validates source selection during retrieval. Data freshness as a property of the underlying data also belongs to L0.

---

## When

Data Freshness in Retrieval Testing may occur:
- During source content onboarding
- During indexing validation
- Before release
- After document updates
- After policy or procedure changes
- During periodic content review
- During production monitoring
- When users report outdated answers

---

## How

Freshness may be validated through:
- Checking source timestamps
- Comparing retrieved sources against current approved versions
- Testing known outdated-versus-current document scenarios
- Reviewing cache behavior
- Validating source ranking preferences
- Confirming deprecated content is excluded or de-prioritized
- Human review of retrieved source currency

---

## Failure Modes

Common failure modes include:
- Outdated document retrieved
- Deprecated source ranked above current source
- Old version included in context
- Cached content used beyond acceptable period
- Current source not indexed
- Conflicting versions retrieved together
- Model response grounded in stale information

---

## Verification / Signals

Verification signals may include:
- Current source retrieval rate
- Outdated source retrieval count
- Version accuracy score
- Cache freshness compliance
- Deprecated content exclusion rate
- Human review of source currency
- Reduction in stale-answer incidents

---

## Key Note

Fresh retrieval depends on both L0 data freshness and L2 retrieval logic.

A source may be current in the repository but still fail if the retrieval system selects an older version.