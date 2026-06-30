# Quality Decision Quick Filter

## Purpose

This quick filter helps teams decide how much validation is appropriate for a change.

## Use this when

Use this when planning a change, reviewing a story, or deciding how much confidence is needed before release.

## Quick Filter

### If the change is small and low risk
- use lighter validation
- focus on the main behavior
- check for obvious regressions

### If the change is moderate and meaningful
- validate the changed behavior directly
- cover the most important integration points
- review the risk and known dependencies

### If the change is high risk or broad impact
- use broader validation across levels
- include regression and integration checks where appropriate
- review release readiness and support plans

### If the change affects AI behavior or critical workflows
- include the relevant quality layer review
- consider evaluation, monitoring, and governance concerns
- involve the right stakeholders in readiness review

## Quick Checklist

- [ ] The change size and impact are understood
- [ ] The main risk is known
- [ ] The validation level matches the risk
- [ ] The team knows when to stop and review further
