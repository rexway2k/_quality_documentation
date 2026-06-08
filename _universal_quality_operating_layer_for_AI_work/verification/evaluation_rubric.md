# Verification — Evaluation Rubric

## Purpose

This rubric defines how to evaluate whether the Universal Quality Skill System is functioning correctly when applied to test scenarios.

It measures system behavior across key dimensions of quality.

Each dimension is scored independently.

---

## Scoring Model

Score each category from 1 to 5:

1 — Fails consistently  
2 — Weak / inconsistent  
3 — Acceptable but incomplete  
4 — Strong and consistent  
5 — Fully aligned and reliable  

---

# Evaluation Categories

---

## 1. Contract Clarity

### What This Measures
- defines expected outcome
- identifies consumer(s)
- makes expectations explicit

### Strong Signals (4–5)
- contract is clear and usable
- assumptions are explicit when needed

### Weak Signals (1–2)
- output is based on hidden assumptions
- consumer is unclear or ignored

---

## 2. Ambiguity Handling

### What This Measures
- ability to detect missing information
- appropriate handling of uncertainty

### Strong Signals
- ambiguity is surfaced
- assumptions are clearly stated
- proceeds when risk is bounded

### Weak Signals
- silent assumption-making
- ignores missing information
- blocks unnecessarily or proceeds blindly

---

## 3. Risk Management

### What This Measures
- identification of risk and uncertainty
- classification of unknowns

### Strong Signals
- distinguishes bounded vs unbounded uncertainty
- defines impact of risks

### Weak Signals
- ignores risk
- uses vague “unknowns” with no scope

---

## 4. Execution Quality

### What This Measures
- ability to perform work, not just describe it

### Strong Signals
- produces complete, usable output
- aligns output to expectations

### Weak Signals
- stops at explanation
- produces incomplete output

---

## 5. Verification Alignment

### What This Measures
- ability to define and apply validation

### Strong Signals
- defines how correctness is measured
- aligns validation to expectations

### Weak Signals
- no verification thinking
- subjective or vague validation

---

## 6. Decision Structure

### What This Measures
- clarity and structure of reasoning

### Strong Signals
- reasoning is explainable
- decisions align to intent and risk

### Weak Signals
- reasoning is unclear or inconsistent
- decisions appear arbitrary

---

## 7. Adaptive Rigor

### What This Measures
- correct level of system application

### Strong Signals
- applies light touch for simple tasks
- applies deep rigor for complex tasks

### Weak Signals
- over-processes simple work
- under-processes complex work

---

## 8. Failure Diagnosis

### What This Measures
- ability to identify root cause correctly

### Strong Signals
- identifies expectation mismatch
- traces failure to correct layer

### Weak Signals
- guesses root cause
- treats symptoms instead of cause

---

## 9. Consistency

### What This Measures
- system behaves the same across similar scenarios

### Strong Signals
- produces repeatable structure and reasoning

### Weak Signals
- behavior varies unpredictably

---

## 10. Progress Enablement

### What This Measures
- whether system supports forward movement

### Strong Signals
- progresses with bounded uncertainty
- avoids unnecessary blocking

### Weak Signals
- blocks prematurely
- ignores risk in favor of speed

---

# Evaluation Output

For each scenario:

- assign score (1–5) for each category
- provide short explanation for low scores
- identify patterns across scenarios

---

# Success Criteria

The system is considered effective when:

- most scores are 4 or 5 across scenarios
- no category consistently scores below 3
- failures are explainable and correctable

---

# Failure Indicators

The system is not functioning correctly if:

- contract clarity is consistently weak
- ambiguity is ignored or mishandled
- outputs are not executable
- verification is missing
- behavior lacks consistency
- system either blocks too often or ignores risk