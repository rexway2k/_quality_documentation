# Engineer Starter Guide

## Purpose

This guide helps engineers apply quality thinking in day-to-day development work.

## What You Need to Know

Good engineering quality is not just about writing code that compiles. It includes making the work understandable, testable, observable, and safe to change.

## What You Should Do

- build for clarity and maintainability
- understand the acceptance criteria before implementation
- identify the highest-risk behaviors early
- choose appropriate validation for the change
- capture evidence and defects clearly

## Questions to Ask

- What could break?
- What is the critical behavior here?
- How will I know it works?
- What should be automated versus checked manually?
- What should be monitored after release?

## Common Mistakes to Avoid

- coding without a clear understanding of the expected behavior
- relying only on manual validation for repetitive checks
- skipping edge cases and failure paths
- treating automation as a substitute for thinking

## Quick Checklist

- [ ] The expected behavior is clear
- [ ] Key risks are considered
- [ ] The change has a validation approach
- [ ] Important edge cases are covered
- [ ] The work is observable and supportable

## Source Materials

- [Test Automation Strategy](../../03 Test Automation/00 Test Automation Strategy.md)
- [What to Test, Where, When, and How Playbook](../01 Core Team Playbooks/02 What to Test, Where, When, and How Playbook.md)
- [Quality Engagement During Development and Validation](../../01 SDLC Quality Engagement/05 Quality Engagement During Development and Validation.md)
