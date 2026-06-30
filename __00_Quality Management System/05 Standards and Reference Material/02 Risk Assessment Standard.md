# Risk Assessment Standard

## Purpose

This standard establishes how delivery teams identify, communicate, assess, and manage quality risk throughout the solution lifecycle.

Risk management exists to reduce uncertainty and enable informed delivery decisions.

---

# Definition of Risk

Risk is the combination of:

- Likelihood
- Impact
- Detectability

A risk represents uncertainty regarding expected outcomes.

---

# Risk Assessment Timing

Risk assessment should occur during:

- Discovery
- Design
- Estimation
- Development
- Testing
- Release preparation

---

# Quality Risk Categories

## Functional Risk

Failure to meet expected business behavior.

## Integration Risk

Failure between systems or services.

## Data Risk

Incorrect, incomplete, or unavailable data.

## Performance Risk

Degradation under workload.

## Security Risk

Unauthorized access or data exposure.

## Operational Risk

Monitoring, support, recovery, or maintenance concerns.

## AI Risk

Bias, hallucination, drift, misuse, or unreliable outputs.

---

# Risk Scoring

Organizations may use local scoring models.

At minimum teams should assess:

| Factor | Description |
|----------|-------------|
| Likelihood | Probability of failure |
| Impact | Business impact |
| Visibility | Ability to detect issues |
| Recovery Difficulty | Complexity of correction |

---

# Risk Response

Risks may be:

- Mitigated
- Accepted
- Avoided
- Escalated

Unresolved risks exceeding agreed tolerance must be visible prior to release.

---

# Risk Based Testing

Testing depth should increase with risk.

High risk areas require:

- Greater coverage
- Deeper validation
- Earlier testing
- More automation
- Stronger diagnostics

---

# Risk Governance

Quality signals should support:

- Release discussions
- Coverage decisions
- Automation prioritization
- Escalation discussions

Hidden risk is unacceptable.

Visible risk is manageable.