# AI Test Type → Metric → Signal Mapping

## Purpose

This document maps AI Test Types to:
- Metrics (how we measure)
- Signals (what we observe)

It connects:
- Testing model (Layers & Test Types)
- Evaluation system (Eval Spine)
- Real-world operational monitoring

---

## Core Principle

Testing defines:
- What we validate

Evaluation defines:
- How we measure it

This mapping connects both.

---

## L1 — Model / LLM

| Test Type | Metric | Signals |
|----------|--------|--------|
| Accuracy | % correct | Answer correctness rate |
| Hallucination | % unsupported claims | Hallucination rate |
| Relevance | relevance score | User usefulness rating |
| Faithfulness | alignment score | Missing/added info |
| Prompt Behavior | instruction adherence | Prompt failure rate |
| Safety | unsafe output rate | Refusal correctness |
| Bias | fairness score | Outcome variance |
| Toxicity | toxicity score | Harmful language count |
| Variability | consistency score | Output variance |
| Reasoning | reasoning score | Logical error count |
| Output Format | format adherence | Parse success rate |

---

## L2 — Retrieval / Context

| Test Type | Metric | Signals |
|----------|--------|--------|
| Retrieval Quality | success rate | Correct doc retrieved |
| Precision / Recall | precision %, recall % | Missed vs irrelevant |
| Context Relevance | relevance score | Context usefulness |
| Completeness | coverage score | Missing content |
| Groundedness | claim support % | Unsupported claims |
| Source Attribution | citation accuracy | Traceability rate |
| Embedding | semantic match score | Match relevance |
| Chunking | chunk coherence | Context usability |
| Context Window | utilization ratio | Token efficiency |
| Noise | noise ratio | Redundant tokens |
| Freshness | freshness score | Stale content rate |
| Query Mapping | intent match | Query success rate |

---

## L3 — Agentic Systems

| Test Type | Metric | Signals |
|----------|--------|--------|
| Tool Invocation | parameter accuracy | Invalid calls |
| Tool Selection | correct tool rate | Wrong tool usage |
| Workflow Execution | completion rate | Step failures |
| Multi-step Reasoning | step consistency | Drift over steps |
| Planning | plan completeness | Missing steps |
| State Mgmt | state accuracy | State mismatch |
| Memory | memory accuracy | Stale memory |
| Decision Logic | decision accuracy | Incorrect branch |
| Error Handling | recovery rate | Failure escalation |
| Retry / Fallback | retry success | Loop detection |
| Action Outcome | outcome match rate | False success |
| Constraint Adherence | compliance rate | Policy violations |

---

## L4 — System Integration

| Test Type | Metric | Signals |
|----------|--------|--------|
| API Integration | success rate | API failures |
| End-to-End | completion rate | Flow breakdown |
| UI/UX | usability score | User friction |
| I/O Handling | validation rate | Input error rate |
| Auth | access success | Unauthorized actions |
| Data Mapping | mapping accuracy | Data mismatch |
| Error Handling | error clarity | User confusion |
| Performance | latency p95 | Slow responses |
| Scalability | throughput | System degradation |
| Session | session continuity | Session loss |
| Reliability | uptime | Failure rate |
| Environment | parity score | Env mismatch |

---

## L5 — Governance

| Test Type | Metric | Signals |
|----------|--------|--------|
| Security | attack success rate | Injection success |
| Privacy | exposure incidents | PII leaks |
| Compliance | compliance score | Audit failures |
| Bias Outcomes | fairness parity | Outcome variance |
| Ethical Use | approval status | Use-case rejection |
| Responsible AI | policy adherence | Policy violations |
| Drift | drift score | Behavior change |
| Observability | trace completeness | Missing logs |
| HITL | approval rate | Bypassed approvals |
| Access Control | violation rate | Unauthorized use |
| Risk Acceptance | risk score | Unmanaged risk |

---

## How to Use This Table

Use this mapping to:

- Design evaluation pipelines
- Define KPIs
- Build dashboards
- Support governance decisions
- Align testing with measurable outcomes

---

## Key Insight

Every test type must map to a measurable signal.

If it cannot be measured:
- It cannot be validated
- It cannot be governed