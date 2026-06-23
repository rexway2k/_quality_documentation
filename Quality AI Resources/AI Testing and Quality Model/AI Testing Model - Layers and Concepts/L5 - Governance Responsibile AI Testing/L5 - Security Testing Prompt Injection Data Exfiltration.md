# L5 — Security Testing (Prompt Injection & Data Exfiltration)

## What

Security Testing validates whether the AI system is resistant to manipulation, misuse, or unauthorized access through prompts, inputs, or interactions.

This includes prompt injection and attempts to extract restricted or sensitive data.

---

## Why

AI systems can be manipulated through inputs.

Failures at this layer can expose sensitive data or cause unintended behavior.

---

## Where

- User inputs
- Prompt handling
- Retrieval pipelines
- Tool invocation flows
- System boundaries

---

## When

- Pre-release
- Red-team testing
- Security validation cycles
- Post-update validation

---

## How

- Adversarial prompt testing
- Injection simulation
- Data exfiltration attempts
- Boundary condition testing

---

## Failure Modes

- System follows malicious instructions
- Sensitive data exposed
- System ignores guardrails
- Unauthorized access enabled

---

## Verification / Signals

- Injection resistance rate
- Data leak incidents
- Security test pass rate