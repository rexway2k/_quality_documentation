# What to Test, Where, When, and How Playbook

## Purpose

This is the most practical guide for teams that ask, “What should we test for this change?”

It helps teams decide what to validate, where to validate it, when to do it, and how much effort is appropriate.

## When to Use This Guide

Use this when planning work, reviewing a story, preparing a release, or deciding how much validation is needed for a change.

## The Simple Decision Model

Start with four questions:
1. What could go wrong?
2. How important is the outcome?
3. How much change is involved?
4. How risky is the integration or dependency?

If the answer suggests high impact or high uncertainty, validation should be broader and earlier.

## What to Test by Change Type

### UI or user experience changes
- validate the visible behavior
- verify the core workflow end to end
- check usability and critical paths

### API or service changes
- test the contract and behavior at the service boundary
- verify integration and error handling
- check backward compatibility when relevant

### Data or workflow changes
- verify data transformation and business rules
- test edge cases and failure modes
- validate downstream impact

### Integration or dependency changes
- focus on interface behavior and contract stability
- test real integration points where possible
- include release and rollback considerations

### Platform or infrastructure changes
- validate deployment readiness and recovery paths
- test operational behavior and monitoring
- confirm the platform still supports the intended workflow

### AI or LLM-based features
- test the behavior at the relevant layer
- validate prompt, retrieval, workflow, and governance concerns as appropriate
- include evaluation and monitoring plans

## Where to Test

Common choices include:
- unit validation for logic in isolation
- service or API validation at boundaries
- integration validation for connected systems
- end-to-end validation for real user workflows
- production validation for live confidence and monitoring

## When to Test

- early during planning and refinement for risks and expectations
- during development for fast feedback
- before release for confidence and readiness
- after deployment for live validation and monitoring

## How to Test

Choose the method that fits the risk:
- automated for repeatable checks and regression protection
- manual or exploratory for judgment, usability, and complex scenarios
- monitoring or synthetic checks for live confidence

## Quick Examples

### Small UI change
- validate the changed screen and a core user path
- test at the UI and service level if needed
- perform quick regression checks

### New business rule
- test the rule directly and through the relevant workflow
- verify data behavior and edge cases
- check downstream impact

### High-risk release
- broaden validation across levels
- include regression, integration, and release checks
- review readiness and rollback strategy

## Quick Checklist

- [ ] The main risk is known
- [ ] The right level of validation is chosen
- [ ] Validation happens early enough
- [ ] The team knows how success will be observed
- [ ] The release plan includes follow-up monitoring

## Source Materials

- [Testing Strategy Overview](../../02 Test Strategy/00 Testing Strategy Overview.md)
- [Test Automation Strategy](../../03 Test Automation/00 Test Automation Strategy.md)
- [AI Testing Model Layers & Concepts](../../04 AI Quality and Testing/01 AI Testing Model - Layers and Concepts/00 AI Testing Model Layers & Concepts.md)
