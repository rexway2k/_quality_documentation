# L3 — Memory Testing

## What

Memory Testing validates whether an agent correctly stores, retrieves, updates, uses, and forgets information over time.

Memory may include user preferences, prior interactions, task history, system context, or long-lived knowledge used by the agent.

---

## Why

Memory can improve agent usefulness, but it also introduces serious quality and risk concerns.

Incorrect memory can cause:
- Wrong personalization
- Repeated mistakes
- Privacy issues
- Outdated assumptions
- Cross-user contamination
- Incorrect decisions based on stale information

Memory Testing helps ensure retained information is accurate, appropriate, and used only when valid.

---

## Where

Memory Testing applies to:
- Agents with persistent memory
- Session memory
- User preference storage
- Long-term context stores
- Conversation history
- Workflow memory
- Multi-agent coordination memory
- Systems that retrieve or reuse prior information

This test type belongs at L3 because memory influences agent decisions and behavior over time.

---

## When

Memory Testing may occur:
- During memory design
- Before enabling persistent memory
- Before production release
- After memory schema changes
- After changes to retention policies
- During privacy review
- During regression testing
- During production monitoring and incident review

---

## How

Memory may be validated through:
- Testing what is stored
- Testing what is retrieved
- Testing memory updates
- Testing memory deletion or forgetting
- Testing cross-session behavior
- Testing user correction handling
- Testing whether stale memory is ignored or updated
- Testing whether memory is scoped correctly to the user, task, or context
- Reviewing memory traces and stored records

Memory Testing should include both positive and negative scenarios.

---

## Failure Modes

Common failure modes include:
- Incorrect memory stored
- Sensitive information stored improperly
- Memory retrieved for the wrong user
- Outdated memory reused
- User correction ignored
- Conflicting memories retained
- Memory used outside intended scope
- Memory not deleted when required
- Agent over-personalizes based on weak memory
- Agent treats inferred information as confirmed fact

---

## Verification / Signals

Verification signals may include:
- Memory accuracy rate
- Correct memory retrieval rate
- Memory deletion success rate
- User-scope isolation success
- Stale memory detection rate
- Memory correction success rate
- Sensitive memory incident count
- Human review of memory usage

---

## Key Note

Memory increases the importance of governance.

An agent that remembers incorrectly may become less reliable over time, not more useful.