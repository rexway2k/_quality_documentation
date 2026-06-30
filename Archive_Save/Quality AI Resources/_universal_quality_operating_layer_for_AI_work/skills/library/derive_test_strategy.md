# L2.S6 — Derive Test Strategy

## Purpose

Translate the defined contract, risks, and verification requirements into a structured testing approach based on intent, risk, scope, and execution method.

## Governing Basis

A test plan is not a list of tests.
It is a set of intentional decisions derived from:

- WHY (testing intent)
- WHAT (risk type)
- WHERE (validation layer)
- HOW (execution mode)
- WHEN (lifecycle timing)

Testing decisions are driven by:

- outcome
- consumers
- constraints
- failure modes
- verification

## When to Use

Use this skill:

- after contract and risk are defined
- when planning validation approach
- when designing testing strategy for any output
- when evaluating coverage and completeness
- when structuring how risk will be reduced

## Inputs Required

- Defined outcome and contract
- Identified consumers
- Constraints and structure
- Failure modes and risks
- Defined verification approach

## Process

1. Define **WHY (Testing Intent)**
   - identify the decision being supported
   - define what risk is being reduced
   - ensure the purpose of testing is explicit

2. Define **WHAT (Quality Attribute)**
   - determine the type of risk:
     - functional
     - performance
     - reliability
     - security
     - usability
     - compliance
   - align attribute with identified failure modes

3. Define **WHERE (Test Level)**
   - determine where validation occurs:
     - unit
     - component
     - integration
     - system
     - end-to-end
     - business-level validation
   - align with system boundaries and structure

4. Define **HOW (Execution Mode)**
   - determine how validation is performed:
     - automated
     - manual
     - monitored
     - synthetic
   - optimize for efficiency and consistency

5. Define **WHEN (Timing)**
   - determine when validation occurs:
     - during definition
     - during design
     - during development
     - during release
     - post-release monitoring

6. Validate completeness
   - ensure all significant risks are addressed
   - ensure no redundancy or gaps
   - confirm strategy aligns with contract and constraints

## Outputs Produced

- A structured testing strategy
- Defined testing intent for each validation path
- Clear mapping of risk to validation
- Defined levels, methods, and timing of testing

## Failure Signals

- Testing exists without clear purpose (WHY is undefined)
- Risk types are unclear or mixed incorrectly
- Validation is applied at the wrong level
- Execution mode is chosen without considering verification
- Timing of testing is delayed unnecessarily
- Testing is treated as a checklist instead of decisions

## Escalation Rule

If testing decisions cannot be clearly explained:

- return to the contract or failure modes
- clarify risk before defining tests
- remove unnecessary or redundant testing
- ensure all validation is tied to a defined purpose

Do not proceed with unstructured or unexplained testing effort.

## Completion Criteria

This skill is complete when:

- every testing decision can be explained using WHY / WHAT / WHERE / HOW / WHEN
- all critical risks have corresponding validation
- testing effort is intentional and not redundant
- verification is integrated into the execution strategy
