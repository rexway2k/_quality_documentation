# Agent Build & Test Guide — Universal Quality Skill System

## Purpose

This guide explains how to:

1. Build an AI agent using the Universal Quality Skill System
2. Apply it to real tasks
3. Execute test scenarios
4. Score results using the evaluation rubric
5. Refine the system based on observed failures

This is the practical implementation layer of the system.

---

# Part 1 — Building an Agent (Tool Agnostic)

## What You Are Building

You are building an agent that uses:

- System prompt → governs behavior
- Modular prompt blocks → drive execution
- Skills → define capabilities
- Schema → structured representation (optional but useful)

---

## Minimal Agent Configuration

You only need **two things to start**:

### 1. System Prompt
From:

skills/prompts/system_prompt.md

This becomes your agent’s core instruction set.

---

### 2. Input Interface

This can be:
- Chat interface (Copilot, ChatGPT, Claude, etc.)
- API interface
- Script-based runner

---

## How to Instantiate an Agent

### Generic Pattern (works anywhere)

**System Prompt**
→ paste contents of `system_prompt.md`

**User Input**
→ any task, request, or scenario

---

## Optional Enhancements

You may optionally add:

### Modular Blocks

From:

Use these to:
- inject specific behaviors
- force structured execution steps

---

### Schema

From:

skills/schemas/skills.yaml


Use if:
- building orchestration logic
- mapping skills programmatically
- integrating with multi-agent systems

---

# Part 2 — Running Test Scenarios

## Goal

Evaluate whether the agent behaves according to the quality system.

---

## Step-by-Step Process

### Step 1 — Load the Agent

- Apply the system prompt
- Ensure no external instructions override it

---

### Step 2 — Select a Scenario

From:

verification/test_scenarios.md

Pick one scenario at a time.

---

### Step 3 — Execute the Scenario

- Provide the **Input Prompt** to the agent
- Capture the full response

Do not guide or assist the agent during execution.

---

### Step 4 — Record Output

Save:
- full response
- any intermediate reasoning (if available)

---

# Part 3 — Scoring the Agent

## Use:

verification/evaluation_rubric.md

---

## Step-by-Step

For each scenario:

### 1. Evaluate Each Category

Score from 1–5:

- Contract Clarity
- Ambiguity Handling
- Risk Management
- Execution Quality
- Verification Alignment
- Decision Structure
- Adaptive Rigor
- Failure Diagnosis
- Consistency
- Progress Enablement

---

### 2. Record Scores

Example:

| Category | Score |
|--------|------|
| Contract Clarity | 4 |
| Ambiguity Handling | 5 |
| Execution Quality | 3 |

---

### 3. Identify Weak Areas

Focus on:
- categories scoring ≤ 3
- repeated weaknesses across scenarios

---

# Part 4 — Diagnosing Failures

## Rule

Do not treat failures as isolated issues.

Always trace to:

- contract definition
- risk handling
- execution behavior
- verification gap

---

## Method

For each failure:

1. What was expected?
2. What actually happened?
3. Where is the mismatch?
4. Which skill failed?
5. Which layer failed?

---

## Example

Failure:
- Agent produces generic output

Root cause:
- L1.S1 Define Contract was not applied
- Consumer not identified
- Outcome was unclear

---

# Part 5 — Refining the System

## What You Can Change

Only refine these:

- skill definitions
- prompt blocks
- system prompt language
- evaluation rubric clarity

---

## What You Do NOT Change Lightly

- core principles
- system structure
- taxonomy layering

---

## Refinement Loop

1. Run scenario
2. Score results
3. Identify weak skills
4. Update corresponding artifact
5. Re-run scenario
6. Compare scores

---

# Part 6 — Scaling This

Once validated, you can:

## 1. Embed in tools

- Copilot agents
- prompt engines
- workflow automation

---

## 2. Build reusable agents

- writing agent
- coding agent
- planning agent
- QA agent

All powered by the same system

---

## 3. Create test suites

- expand scenario catalog
- build domain-specific cases
- automate evaluation

---

# Part 7 — Success Criteria

The system is working when:

- behavior is consistent across scenarios
- outputs align to expectations
- ambiguity is surfaced or bounded
- outputs are executable and useful
- verification is always considered
- system does not block progress unnecessarily

---

# Final Rule

This system is not validated by design.

It is validated by behavior.

Run it.
Score it.
Find where it breaks.
Fix the system, not the symptom.
