# L2.S2 — Bound Risk

## Purpose

Ensure that all uncertainty is either resolved or explicitly bounded so that work can proceed without hidden or compounding risk.

## Governing Basis

Every open variable is a risk.
Unbounded risks compound.
Completeness is not required before progress.
Bounded uncertainty is required before progress.

“Unknown” is not acceptable.
“Unknown but bounded by scope and impact” is acceptable.

## When to Use

Use this skill:

- before starting work
- when new information is introduced
- when dependencies are unclear
- when assumptions are required
- at major decision points
- whenever ambiguity exists

## Inputs Required

- The defined or partially defined contract
- Known unknowns, assumptions, and dependencies
- Context of what the work affects

## Process

1. Identify all open variables
   - unknowns
   - assumptions
   - unresolved dependencies
   - unclear expectations

2. Classify each item as:
   - **Resolved** — fully known and verified
   - **Bounded** — unknown but limited in scope and impact
   - **Unbounded** — unknown with unclear or potentially large impact

3. For each bounded item:
   - define what it affects
   - define what it does not affect
   - define the acceptable impact range

4. For each unbounded item:
   - determine whether execution must pause
   - identify whether scope can be reduced to avoid dependency
   - escalate if necessary

5. Replace all vague unknowns with explicit statements:
   - define scope
   - define impact
   - define limitations

6. Re-evaluate whether work can proceed safely

## Outputs Produced

- A list of identified risks and unknowns
- A classification of each risk (resolved, bounded, unbounded)
- A defined blast radius for each bounded risk
- A decision on execution readiness

## Failure Signals

- “Unknown” is used without qualification
- Dependencies are acknowledged but not analyzed
- Work proceeds as if missing information does not matter
- Risk impact is unclear or undefined
- Open variables are hidden or ignored

## Escalation Rule

If any critical dependency is unbounded:

- Do not proceed as if the system is stable
- Either:
  - bound the uncertainty explicitly
  - reduce scope to isolate the risk
  - or pause and surface the issue

Work may proceed only when uncertainty is sufficiently bounded.

## Completion Criteria

This skill is complete when:

- all unknowns are either resolved or bounded
- the impact of each open item is understood
- no hidden or unacknowledged uncertainty remains
- a clear decision to proceed, proceed with caveats, or pause is made
