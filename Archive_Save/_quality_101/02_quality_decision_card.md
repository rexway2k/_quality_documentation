# QUALITY DECISION CARD  

## Daily Use Companion to Core Quality Working and Testing Principles

---

## USE THIS CARD BEFORE TEST PLANNING, REVIEW, OR ESTIMATION

### 1) DEFINE THE CONTRACT

- What outcome must be true?
- Who depends on it?
- What constraints must hold?
- What can fail?
- How will we prove it works?

If any answer is unclear, return to the contract.

---

## 2) MAKE THE FIVE DECISIONS

### WHY

What decision are we making?
What risk are we trying to reduce?

### WHAT

What kind of risk matters most?

- Functional
- Performance
- Security
- Reliability
- Usability
- Compliance

### WHERE

Where should confidence be built?

- Unit
- Service
- Integration
- UI / End-to-End
- Business / UAT

### HOW

How should we validate?

- Manual
- Automated
- Semi-automated
- Monitored
- Synthetic

### WHEN

When must this risk be reduced?

- Discovery
- Design
- Refinement
- Build
- Deploy
- Release / Production

---

## 3) CHECK FOR CLARITY

If these are being used interchangeably as “test types,” stop and separate them.

- Intent is not level
- Attribute is not intent
- Level is not execution mode
- Execution mode is not what is being tested
- Timing is not a test type

---

## 4) DEFINE “ENOUGH”

Enough is reached when:

- Critical risks are identified
- Failure modes are understood
- Verification proves those risks are controlled

Anything beyond this may be over-analysis.
Anything short of this leaves risk unbounded.

---

## 5) FINAL CHECK

Can the plan be expressed in this form?

### Intent | Attribute | Level | Execution Mode | Timing

If not, the plan is not clear enough yet.
