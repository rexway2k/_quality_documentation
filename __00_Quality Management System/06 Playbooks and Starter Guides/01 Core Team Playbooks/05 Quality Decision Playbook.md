# Quality Decision Playbook

## Purpose

This guide helps teams make quality decisions quickly and consistently.

It is a practical companion to the broader quality and testing content and is meant to answer the question: “What do we need to do to build enough confidence for this change?”

## When to Use This Guide

Use this during planning, refinement, delivery, and release conversations when the team needs to decide how much validation is enough.

## The Five Questions

Every quality decision should be grounded in five simple questions:

1. Why are we doing this?
2. What risk matters most?
3. Where should we build confidence?
4. How will we validate it?
5. When do we need the confidence?

## Practical Guidance

### Why
Clarify the decision being made. Is the goal to release, to reduce risk, to validate a change, or to understand impact?

### What risk matters most
Focus on the main failure mode. Examples include correctness, usability, reliability, performance, security, compliance, or workflow impact.

### Where
Choose the right level of validation. Common options include unit, service, integration, end-to-end, and production monitoring.

### How
Use the method that fits the risk. This may include automation, manual validation, exploratory testing, or monitoring.

### When
Validation should happen early enough to reduce cost and uncertainty. The earlier the risk can be understood, the better.

## Simple Decision Pattern

- Low risk and small change: lighter validation, faster feedback
- Medium risk and meaningful change: target the key behavior and relevant integration points
- High risk or broad impact: wider validation, earlier review, more explicit readiness checks

## Common Mistakes

- testing without a clear decision or purpose
- treating all risks as equal
- validating at the wrong level
- delaying validation until the end

## Quick Checklist

- [ ] The decision purpose is clear
- [ ] The key risk is known
- [ ] The validation level is appropriate
- [ ] The team knows how and when to validate
- [ ] The decision is documented or discussed clearly

## Source Materials

- [Quality Decision Field Guide](../../../Archive_Save/_quality_101/01_quality_decision_field_guide.md)
- [Testing Strategy Overview](../../02 Test Strategy/00 Testing Strategy Overview.md)
- [What to Test, Where, When, and How Playbook](02 What to Test, Where, When, and How Playbook.md)
