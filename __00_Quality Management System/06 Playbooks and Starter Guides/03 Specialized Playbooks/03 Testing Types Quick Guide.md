# Testing Types Quick Guide

## Purpose

This guide helps teams understand the common difference between testing levels and testing types.

## The Simple Difference

### Testing levels answer: where is the testing happening?
Examples:
- unit testing
- service testing
- integration testing
- end-to-end testing
- production validation

### Testing types answer: what are we trying to evaluate?
Examples:
- functional testing
- performance testing
- security testing
- accessibility testing
- usability testing

## Why This Matters

A team can test the same feature in different ways for different reasons. For example, a workflow may be validated at the UI level for user behavior and at the service level for logic and contract behavior.

## Simple Example

A new checkout flow may need:
- functional validation for business behavior
- integration validation for payment and inventory services
- end-to-end validation for the full workflow
- performance validation for scale and reliability

## Quick Checklist

- [ ] The team knows where the validation is happening
- [ ] The team knows what quality concern is being checked
- [ ] The validation approach matches the risk

## Source Materials

- [Testing Strategy Overview](../../02 Test Strategy/00 Testing Strategy Overview.md)
- [What to Test, Where, When, and How Playbook](../01 Core Team Playbooks/02 What to Test, Where, When, and How Playbook.md)
- [Quality Decision Playbook](../01 Core Team Playbooks/05 Quality Decision Playbook.md)
