# Release Readiness Playbook

## Purpose

This guide helps teams decide whether a change is ready to release.

It focuses on the minimum evidence and decision points that matter most.

## When to Use This Guide

Use this before deployment, before a major release, or before handing work to support and operations.

## Key Questions

Before release, the team should be able to answer:
- what changed
- what risk remains
- what validation was completed
- what is known and unknown
- what happens if something fails

## Minimum Readiness Evidence

A release is more ready when the team can show:
- the intended outcome is understood
- key validation was completed
- major risks were reviewed
- defects and known issues were assessed
- monitoring or support plans are in place
- rollback or recovery options are understood

## Simple Go/No-Go Approach

### Go
Release when the core risk is understood and the evidence is sufficient for the change.

### No-Go
Pause when there is major ambiguity, unresolved critical issues, or insufficient validation for the release risk.

## Common Release Readiness Mistakes

- treating release as only a deployment activity
- assuming the work is safe because it built successfully
- skipping post-deployment monitoring
- failing to review known issues and support readiness

## Quick Checklist

- [ ] Business outcome is clear
- [ ] Key validation is complete
- [ ] Major risks are reviewed
- [ ] Known issues are understood
- [ ] Support and monitoring are ready
- [ ] Rollback approach is clear

## Source Materials

- [Release Readiness Standard](../../05 Standards and Reference Material/03 Release Readiness Standard.md)
- [Quality Engagement During Release Planning and Deployment](../../01 SDLC Quality Engagement/06 Quality Engagement During Release Planning and Deployment.md)
- [Testing Strategy Overview](../../02 Test Strategy/00 Testing Strategy Overview.md)
