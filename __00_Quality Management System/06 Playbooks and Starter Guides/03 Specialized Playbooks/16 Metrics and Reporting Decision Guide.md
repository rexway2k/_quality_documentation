# Metrics and Reporting Decision Guide

## Purpose

This guide helps teams decide what to measure, when to measure it, where to look for the information, and how to use it.

## When to Use This Guide

Use this during planning, review, release decision-making, and quality improvement conversations.

## Core Idea

Metrics should support learning and decision-making. They should not become a scoreboard or a substitute for context.

## What to Measure

Choose measures that help answer:
- what risk is present
- what confidence do we have
- where are we seeing recurring issues
- what needs attention now

Useful areas include:
- defect trends and severity
- release readiness outcomes
- test coverage for critical risks
- automation reliability and feedback speed
- escaped defects and recurring issues

## When to Measure

- at the end of a sprint or delivery increment
- before a release decision
- during recurring quality reviews
- after incidents or production issues

## Where to Get the Information

The repository points to common sources such as:
- Jira for defects, issues, and root cause data
- qTest for test cases, executions, coverage, and automation outcomes

## How to Use the Metrics

Use metrics to:
- identify risk and emerging patterns
- guide improvement actions
- support release decisions
- inform conversations about quality and delivery confidence

Do not use metrics in isolation. Always interpret them with context, risk, and delivery reality.

## Common Mistakes

- measuring for reporting rather than learning
- overemphasizing volume over value
- using metrics without context
- treating metrics as a performance target

## Quick Checklist

- [ ] The metric is tied to a real quality concern
- [ ] The team knows why it matters
- [ ] The data source is understood
- [ ] The metric is interpreted with context
- [ ] The result drives action or decision-making

## Source Materials

- [Metrics and Reporting Standard](../../05 Standards and Reference Material/04 Metrics and Reporting Standard.md)
- [Test Automation Strategy](../../03 Test Automation/00 Test Automation Strategy.md)
- [Defect Triage and Root Cause Playbook](../01 Core Team Playbooks/06 Defect Triage and Root Cause Playbook.md)
