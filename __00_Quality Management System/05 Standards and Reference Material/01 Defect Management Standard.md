# Defect Management Standard

## Purpose

This standard establishes the enterprise approach for identifying, documenting, prioritizing, resolving, and learning from defects.

This standard supports:

- Q10.2 Defect Management
- Q10.3 Production Defects
- Q10.4 Root Cause Analysis
- Q11 Measurement and Governance

Defect management exists to reduce uncertainty, improve solution quality, and create organizational learning.

Defect management is not intended to assign blame.

---

# Core Principles

## Defects Represent Information

A defect is any deviation between expected and observed behavior.

Defects provide information about:

- Requirement misunderstandings
- Implementation mistakes
- Contract mismatches
- Data issues
- Environmental inconsistencies
- Process weaknesses

---

## Focus on Learning

The goal of defect management is:

- Understanding
- Risk reduction
- Prevention of recurrence

The goal is not:

- Individual performance evaluation
- Team comparison
- Blame assignment

---

# Systems of Record

## Jira

Jira is the authoritative system of record for:

- Defect identification
- Defect lifecycle management
- Defect prioritization
- Resolution tracking
- Root cause information

---

# Minimum Defect Content

Every defect must include:

## Summary

Clear description of observed issue.

## Expected Behavior

What should have occurred.

## Actual Behavior

What occurred.

## Reproduction Information

Steps necessary to reproduce.

## Environment Information

Including:

- Environment
- Version
- Build
- Data conditions

## Severity

Impact to solution behavior.

## Root Cause

When known.

---

# Defect Lifecycle

## Open

Defect identified.

## Triaged

Impact and priority evaluated.

## In Progress

Active resolution underway.

## Resolved

Correction implemented.

## Verified

Retesting confirms resolution.

## Closed

No additional work required.

---

# Production Defects

Production defects represent realized risk.

For production defects teams must evaluate:

- Why existing testing did not identify the issue
- Whether coverage should be expanded
- Whether automation should be added
- Whether monitoring should be enhanced

---

# Root Cause Expectations

Root cause analysis should investigate:

- Technical causes
- Architectural causes
- Process contributors
- Data contributors
- Environment contributors

Depth should be proportional to:

- Risk
- Business impact
- Frequency
- Recurrence

---

# Quality Signals

The following are reviewed regularly:

- Defect escape rate
- Defect aging
- Open defect backlog
- Production defect patterns
- Defect root cause trends

These signals inform decisions but do not serve as individual performance metrics.
