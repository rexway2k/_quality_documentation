# QUALITY DECISION FIELD GUIDE

## Companion to Core Quality Working and Testing Principles

---

## PURPOSE

This guide translates the core principles into a practical decision tool.

Use this to:

- Plan testing  
- Evaluate quality decisions  
- Align teams  
- Prevent over-testing and under-testing  

This is not a framework.
It is a way to make decisions consistently and explain them clearly.

---

## START HERE — DEFINE THE CONTRACT

Before any testing or planning:

- What outcome must be true?
- Who depends on it?
- What constraints must hold?
- How can it fail?
- How will we prove it works?

If these are unclear, stop.
Testing decisions will be incorrect.

---

## THE FIVE DECISION DIMENSIONS

Every test must be defined using all five:

---

### WHY — Decision / Intent

**What decision are we trying to make?**  
**What risk are we trying to reduce?**

Examples:

- Can we release this?
- Did this change break anything?
- Can consumers rely on this?
- Does the workflow actually work?

If this is unclear → testing has no purpose

---

### WHAT — Type of Risk

**What type of failure matters most?**

Common dimensions:

- Functional (correctness)
- Performance (speed / scale)
- Security (protection)
- Reliability (failure / recovery)
- Usability (human effectiveness)
- Compliance (rules / constraints)

If this is unclear → risk is not properly targeted

---

### WHERE — Location of Validation

**Where in the system should confidence be built?**

Levels:

- Unit (logic in isolation)
- Service (behavior at boundaries)
- Integration (systems working together)
- UI / End-to-End (workflow validation)
- Business (real-world usage / UAT)

If this is unclear → validation is misplaced or redundant

---

### HOW — Execution Method

**How will we validate efficiently?**

Options:

- Manual (judgment / exploration)
- Automated (repeatable, stable validation)
- Semi-automated (complex scenarios)
- Monitored (real-time observation)
- Synthetic (simulated probing)

If this is unclear → effort is inefficient or inconsistent

---

### WHEN — Timing of Validation

**When must this risk be reduced?**

- Defined early (Discovery / Design)
- Refined before build
- Executed during build / deploy
- Validated in real use (Release / Production)

If delayed → cost and risk increase

---

## GOVERNING RULE

A test plan is not a list of tests.

It must answer:

- WHY are we testing?
- WHAT risk matters?
- WHERE do we validate?
- HOW do we validate?
- WHEN does it happen?

If you cannot explain all five → the plan is incomplete

---

## RISK DRIVES EVERYTHING

All decisions are driven by risk:

- WHY defines the decision
- WHAT defines the type of risk
- WHERE defines where it is validated
- HOW defines how it is reduced
- WHEN defines when it must be reduced

---

## WHAT “ENOUGH” LOOKS LIKE

Testing is complete when:

- Critical risks are identified  
- Failure modes are understood  
- Verification proves those risks are controlled  

Not when:

- All possible tests are written  
- All scenarios are explored  
- Coverage feels “high enough”  

---

## AVOID THESE FAILURE MODES

- “Run regression” with no defined intent  
- Mixing levels, attributes, and intent as “test types”  
- Testing everything without defining risk  
- Late discovery of contract mismatches  
- Over-analysis after risk is already bounded  

When these occur → return to the contract

---

## FINAL CHECK

Before executing:

Can you explain, in one line:

### Intent | Attribute | Level | Execution Mode

Example format:

- Change Impact | Functional | Service | Automated  

If not → the decision is not yet clear

---

## FINAL REDUCTION

Define the contract  
Identify how it can fail  
Choose where and how to prove it works  
Do it as early as possible  

Stop when risk is bounded  
Proceed when decisions are clear
