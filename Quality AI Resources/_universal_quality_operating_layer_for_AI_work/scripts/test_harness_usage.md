# Test Harness Usage Guide — Universal Quality Skill System

## Purpose

This guide provides step-by-step instructions for using the test harness to:

* Run evaluation scenarios
* Capture agent outputs
* Score behavior using the evaluation rubric
* Generate reports
* Refine the system based on observed failures

This document represents the practical validation workflow for the entire system.

***

## Overview

The test harness enables a complete validation loop:

1. Generate a test scenario set
2. Run your agent against those scenarios
3. Manually score results using a structured rubric
4. Generate a report highlighting weaknesses
5. Refine the system based on evidence

This is how the system proves its value through behavior, not design.

***

## Folder Structure

After initialization, you will have:

verification/
├── scenarios.json
├── results.json
├── evaluation_report.md   (generated later)

***

## Step 1 — Initialize Test Files

Run:

```bash
python test_harness.py init --outdir verification
```

This creates:

* `verification/scenarios.json`
* `verification/results.json`

***

## Step 2 — Run Scenarios Against Your Agent

For each scenario in `verification/scenarios.json`:

1. Copy the `input_prompt`
2. Run it through your agent using your system prompt
3. Capture the full agent response

Paste the response into the matching scenario in `verification/results.json`:

```json
{
  "agent_response": "PASTE FULL RESPONSE HERE"
}
```

Repeat for all scenarios.

***

## Step 3 — Score the Results

Run:

```bash
python test_harness.py score --results verification/results.json
```

You will be prompted to score each scenario using:

* Contract Clarity
* Ambiguity Handling
* Risk Management
* Execution Quality
* Verification Alignment
* Decision Structure
* Adaptive Rigor
* Failure Diagnosis
* Consistency
* Progress Enablement

***

## Scoring Scale

1 — Fails  
2 — Weak  
3 — Acceptable  
4 — Strong  
5 — Fully aligned  

***

## Additional Inputs

You can also record:

* **Notes** — what you observed
* **Root Cause Hypothesis** — why it failed
* **Artifacts to Refine** — which files need updates

Example:

Root cause: Contract not defined clearly  
Artifacts: define_contract.md, system_prompt.md  

***

## Step 4 — Generate Evaluation Report

Run:

```bash
python test_harness.py report --results verification/results.json
```

This creates:

verification/evaluation_report.md

***

## Report Contents

The report includes:

* Category averages
* Scenario-level summaries
* Weak categories
* Weak scenarios
* Repeated refinement targets
* Recommended next steps

***

## Step 5 — Diagnose Failures

### Core Rule

Do not fix outputs directly.  
Fix the system that produced them.

***

## Diagnosis Method

For each failure:

1. What was expected
2. What actually happened
3. Where the mismatch exists
4. Which skill failed
5. Which system layer failed

***

## Failure Mapping Guide

| Failure Type          | Likely Artifact              |
| --------------------- | ---------------------------- |
| Missing expectations  | `define_contract.md`         |
| Ambiguity ignored     | `apply_quality_questions.md` |
| Risk ignored          | `bound_risk.md`              |
| Output incomplete     | execution skills             |
| No validation         | `define_verification.md`     |
| Poor decisions        | `derive_test_strategy.md`    |
| Incorrect diagnosis   | `diagnose_failure.md`        |
| Inconsistent behavior | `system_prompt.md`           |

***

## Step 6 — Refine the System

### Allowed Changes

* Skill definitions (`skills/library/`)
* Modular prompt blocks
* System prompt
* Evaluation rubric clarity

### Do NOT Change Lightly

* System specification
* Core principles
* Taxonomy structure

***

## Refinement Loop

1. Run scenario
2. Score behavior
3. Identify failure
4. Trace failure to artifact
5. Update artifact
6. Re-run affected scenarios
7. Compare results

***

## Step 7 — Iterate Efficiently

Avoid rerunning everything every time.

Instead:

1. Fix one issue
2. Re-run only affected scenarios
3. Validate improvement
4. Then expand testing

***

## Example Workflow

1. Run SCN-02 (Ambiguous Request)
2. Score shows low Contract Clarity and Ambiguity Handling
3. Diagnose: contract definition was skipped
4. Update `system_prompt.md` to enforce contract definition
5. Re-run SCN-02
6. Score improves
7. Continue to next weakness

***

## Success Criteria

The system is working when:

* Most scores are 4–5
* No category consistently scores below 3
* Behavior is consistent across scenarios
* The agent performs work (not just analysis)
* Verification is always considered
* The system does not block progress unnecessarily

***

## Common Failure Patterns

### Over-processing Simple Tasks

Fix: reduce rigor in system prompt

### Under-defining Complex Tasks

Fix: strengthen quality questions and contract definition

### Ignoring Risk

Fix: reinforce risk bounding logic

### Missing Verification

Fix: strengthen define\_verification behavior

### Inconsistent Behavior

Fix: tighten system prompt and adaptive rigor rules

***

## Key Principle

The system is NOT validated by:

* Documentation
* Design
* Intent

The system IS validated by:

→ Observable behavior across scenarios

***

## Final Workflow Summary

Initialize → Run → Score → Diagnose → Refine → Repeat

***

## Final Rule

Do not optimize for perfect outputs.

Optimize for:

* Consistent behavior
* Explicit contracts
* Bounded uncertainty
* Verifiable outcomes

The system improves through **iteration, not perfection**.
