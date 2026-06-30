# Testing Levels vs Testing Types

## Purpose

Testing discussions often become confusing because teams use the terms "testing level" and "testing type" interchangeably.

These concepts describe different dimensions of testing and should be considered independently when designing testing strategies.

Understanding this distinction helps teams select appropriate validation approaches and improve overall quality coverage.

---

## Testing Levels

Testing levels describe where testing occurs within the system and how much of the system is involved.

Testing levels typically progress from smaller scopes to larger scopes.

### Examples of Testing Levels

| Level | Scope |
|----------|----------|
| L0 | Reviews and Analysis |
| L1 | Unit and Component Validation |
| L2 | System Validation |
| L3 | Integration Validation |
| L4 | End-to-End Validation |
| L5 | Production Validation |

Testing levels primarily answer:

> Where are we testing?

---

## Testing Types

Testing types describe what characteristic or quality attribute is being evaluated.

Testing types are independent of system level.

### Examples of Testing Types

| Testing Type |
|----------|
| Functional |
| Performance |
| Security |
| Accessibility |
| Operational |
| Regression |
| Exploratory |

Testing types primarily answer:

> What are we evaluating?

---

## Example

Performance Testing can occur at:

- L1 Component
- L2 Application
- L3 Integration
- L4 End-to-End
- L5 Production

Functional Testing can occur at:

- L1 Unit
- L2 System
- L3 Integration
- L4 End-to-End

The testing type remains the same while the testing level changes.

---

## Why This Matters

Testing strategies should include consideration of both:

- Appropriate testing levels
- Appropriate testing types

A testing strategy that only focuses on functional testing may miss security concerns.

A testing strategy that only focuses on system testing may miss integration concerns.

Both dimensions are necessary to establish confidence.

---

## Summary

Testing Levels define:

> Where testing occurs.

Testing Types define:

> What is being evaluated.

Both are required for effective quality validation.