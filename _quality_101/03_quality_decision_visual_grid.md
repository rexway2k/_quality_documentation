# QUALITY DECISION VISUAL GRID  
### Companion to Core Quality Working and Testing Principles

---

## PURPOSE

Use this one-page grid to turn the quality principles into a clear decision path.

This is not a replacement for the core document.
It is a visual operating sheet for daily use.

---

## START WITH THE CONTRACT

Before choosing tests, levels, automation, or detail:

- What outcome must be true?
- Who depends on it?
- What constraints must hold?
- What can fail?
- How will we verify it?

If these are unclear, stop.
The testing plan is not ready yet.

---

## THE DECISION GRID

| DIMENSION | QUESTION | DECIDES | FAILURE IF UNCLEAR |
|---|---|---|---|
| **WHY** | What decision are we trying to make? | Testing intent | Testing has no purpose |
| **WHAT** | What kind of risk matters most? | Quality attribute | Risk is not targeted |
| **WHERE** | Where should confidence be built? | Test level | Validation is misplaced |
| **HOW** | How should we validate efficiently? | Execution mode | Effort is inefficient |
| **WHEN** | When must risk be reduced? | Lifecycle timing | Risk is discovered too late |

---

## RISK FLOW

All five dimensions are driven by risk.

- **WHY** defines the decision being made
- **WHAT** defines the type of risk
- **WHERE** defines where it is validated
- **HOW** defines how it is reduced
- **WHEN** defines when it must be reduced

---

## THE SIX QUALITY QUESTIONS UNDERNEATH THE GRID

Every decision above must trace back to these:

1. What is the desired outcome?
2. Who are the consumers?
3. What constraints are required?
4. What is the final structure?
5. What are the failure modes?
6. How will it be verified?

---

## WHAT “ENOUGH” LOOKS LIKE

Stop analysis and proceed when:

- Critical risks are identified
- Failure modes are understood
- Verification proves those risks are controlled

Do not keep analyzing only to increase volume, coverage, or comfort.
Enough means risk is bounded.

---

## FAST CHECK

A plan is ready only if it can be explained in one line:

**Intent | Attribute | Level | Execution Mode | Timing**

Example shape:

**Change Impact | Functional | Service | Automated | Build**

---

## FINAL REDUCTION

Define the contract  
Identify how it can fail  
Choose where and how to prove it holds  
Do it as early as possible  
Stop when risk is bounded
