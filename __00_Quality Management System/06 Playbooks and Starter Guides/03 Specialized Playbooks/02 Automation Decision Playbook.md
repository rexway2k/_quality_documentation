# Automation Decision Playbook

## Purpose

This guide helps teams decide when automation is worthwhile and when it is not.

It is meant to keep automation focused on confidence and feedback rather than creating noise or unnecessary maintenance.

## When to Use This Guide

Use this when choosing what to automate, reviewing current automation, or debating whether a test should remain manual or exploratory.

## Good Automation Candidates

Automation is usually a strong fit when:
- the check is repetitive
- the behavior is stable and important
- the validation needs to be repeated often
- regression protection is valuable
- the feedback should be fast

## Automation Should Not Replace Thinking

Automation is not a substitute for:
- clear requirements
- thoughtful risk analysis
- exploratory testing
- judgment in complex scenarios

## Simple Decision Questions

Ask:
- is this check repeated often
- is the outcome important
- is the behavior stable enough to automate
- will the automation add confidence or just noise
- is there a better manual or exploratory approach

## Practical Rule of Thumb

Automate the checks that provide repeatable confidence and are worth maintaining over time.

Do not automate everything simply because it is possible.

## Common Mistakes

- automating unstable or poorly understood behavior
- automating without a clear purpose
- creating brittle tests that break often
- using automation as a substitute for risk discussion

## Quick Checklist

- [ ] The check is important
- [ ] The behavior is stable enough to automate
- [ ] The test will be repeated or reused
- [ ] The automation adds confidence
- [ ] The maintenance cost is acceptable

## Source Materials

- [Test Automation Strategy](../../03 Test Automation/00 Test Automation Strategy.md)
- [Automation Design Principles](../../03 Test Automation/03 Automation Design Principles.md)
- [What to Test, Where, When, and How Playbook](../01 Core Team Playbooks/02 What to Test, Where, When, and How Playbook.md)
