# CORE WORKING PRINCIPLES

## Foundation Document — Universal Application

### Version 1.5

---

## PURPOSE

These principles govern the quality of any transactional relational deliverable —
any work product exchanged between a producer and a consumer,
in any context, at any scale.

Following these principles produces one outcome:
work that does what its consumers need it to do,
with risk explicitly bounded and verification aligned to the contract.

---

## QUALITY PRINCIPLES

**Quality = Expectations**
Quality is not a property of output. It is the degree to which output matches
the expectations of its consumers. A thing is high quality when it does exactly
what its consumers need it to do. Nothing more is required. Nothing less is acceptable.

**Contracts Exist Even When Unnamed**
Every system, document, conversation, and relationship operates under contracts —
explicit or implicit. Implicit contracts are the primary source of failure.
The work is to name them, make them explicit, and get them agreed upon
before work begins. If you cannot name the contract, you do not understand
the system well enough to build it.

**Failures Are Mismatched Expectations**
When something fails, the root cause is almost always a mismatch between
what one party expected and what another delivered.
Debugging a failure means finding the expectation mismatch, not just fixing the symptom.
Future prevention means closing the gap at the contract level.

**Risks Must Be Bounded**
Every open variable is a risk. Unbounded risks compound.
Before proceeding on any work, every dependency must be either resolved
or explicitly flagged with its blast radius defined —
what does it affect, how far does it reach, what is blocked until it resolves.
Nothing proceeds on an unbounded dependency.

**Enough = Bounded Uncertainty**
Completeness is not required before progress. Bounded uncertainty is.
Every open item must be either resolved or explicitly flagged with its scope of impact defined.
"Unknown" is not acceptable.
"Unknown but does not affect X, Y, Z and is bounded by W" is acceptable.
The goal is not to eliminate uncertainty — it is to contain it.

**Human Effort Is a Quality Signal**
Wherever human judgment, review, or intervention is required,
that is a signal that the specification is incomplete or the automation is insufficient.
Every instance of required human effort must be named, owned, and resolved —
either by tightening the spec, building automation, or explicitly deciding
that human judgment is appropriate here and building the review step into the process.
Unacknowledged human effort is hidden risk.

**System Speed Over Local Speed**
Optimizing a single component at the expense of the system is false progress.
The highest-dependency items must be resolved first even when they are harder,
because everything downstream accelerates once they are locked.
Local progress on unresolved upstream dependencies is work that will be redone.

**Early Conflict Over Late Surprises**
Disagreements, mismatches, and incompatibilities discovered early are cheap to resolve.
The same conflicts discovered late are expensive, sometimes catastrophic.
Surface conflicts immediately. Do not defer uncomfortable questions.
A conflict named early is a feature. A conflict discovered in final output is a failure.

**Quality Enables Progress — It Does Not Block It**
Quality work is not slow work.
A well-specified system moves faster than an under-specified one
because it eliminates rework, misalignment, and late surprises.
Quality investment at the front end is the fastest path to completion.
Quality is the accelerator, not the brake.

**Automation Preserves Clarity**
Wherever repetitive judgment, verification, or consistency-checking is required,
automation is preferred over human repetition.
Scripted and programmatic verification reduces human judgment burden,
catches drift that human review misses,
and resolves the human effort quality signal.
Automation does not replace judgment —
it preserves human judgment capacity for decisions that actually require it.

---

## FRACTAL CONTRACT PRINCIPLE

Every dependency is simultaneously a consumer of what is above it
and a provider to what is below it.

The consumer-provider contract does not exist only at the top level.
It exists at every relational transaction layer, all the way to the smallest unit of interaction.
The same principles apply whether the transaction is between:

**In systems and software:**

- Business goal and system capability
- System and its subsystems
- Architecture and implementation
- Spec and design
- Design and development
- Development and testing
- Testing and release
- Release and user

**In team and organizational interactions:**

- Stakeholder and product owner
- Product owner and business analyst
- Business analyst and solutions architect
- Solutions architect and engineering
- Engineering and QA
- QA and QE
- Any producer role and any consumer role at any layer

**In content and communication:**

- Argument and the system it describes
- Document and its reader
- Section and its parent document
- Paragraph and its section
- Sentence and its paragraph
- Word and the precision it must carry

**In AI and prompt engineering:**

- Objective and prompt design
- Prompt and model instruction
- Instruction and output
- Output and downstream consumer
- Session and session handoff

**In any transactional relationship:**
Every unit has a consumer above it whose contract it must fulfill.
Every unit has a provider below it whose output it depends on.
Quality at any layer requires the contract chain to be intact at every layer.

Drift occurs when a lower-level unit breaks its contract with the unit above it.
Small breaks accumulate. The system appears locally correct but fails globally.
The prevention is the same at every scale:
name the consumer, name the contract, verify fulfillment.

The six quality questions apply at every layer of every system.
Not just at the top. At every relational transaction.

---

## THE SIX QUALITY QUESTIONS

Apply to every relational dependency, architectural decision, system component,
document, deliverable, interaction, and transaction — at every layer.

**1. What is the desired outcome?**
Define the end state precisely. Not the process. Not the output.
The outcome — what is true when this is done that was not true before.

**2. Who are the consumers?**
Name every entity that depends on this output.
Internal consumers, external consumers, downstream consumers.
Consumer needs drive contract definition.

**3. What are the constraints required?**
What must be true for this to work?
What cannot be violated?
What boundaries exist — technical, logical, resource, timeline, quality?
Constraints are not obstacles. They are the shape of the solution space.

**4. What is the final structure?**
What does the complete, correct output look like?
Define the shape before building the content.
Structure first, population second.

**5. What are the failure modes?**
How does this break?
What are the most likely failure paths?
What are the highest-impact failure paths?
Pre-mortem every significant decision and deliverable.
Name the failure modes before they occur.

**6. How will it be verified?**
If you cannot answer this question, the spec is incomplete.
Every outcome needs a verification method —
automated where possible, explicit human review where not.
Unverifiable outputs are undefined outputs.

---

## GOVERNING CONTRACT PRINCIPLES

**Consumer-Driven Contract Testing**
The consumer defines the expectations.
The consumer decides the contracts.
When there is ambiguity about what something needs to be,
the answer comes from the consumer's requirements, not the producer's assumptions.

**Spec-Driven Development**
No work begins without a complete specification of the outcome,
the constraints, and the verification method.
Incomplete specs produce incomplete and misaligned output.
The spec is not overhead — it is the work.

**Test-Driven Mindset**
Define verification before building.
Know how you will confirm something is correct before you build it.
If you cannot define verification, return to the spec.
The inability to verify is a signal that the outcome is not yet clearly enough defined.

---

## APPLICATION TO TEST PLANNING AND QUALITY DECISIONS

The six quality questions produce all testing decisions.
They are not separate from test planning — they are its source.

Every decision about what to test, why to test, when to test, where to test, and how to test
is derived from the contract defined by these questions.

### DERIVATION MODEL

Each testing decision dimension maps directly to the quality questions.
They are not “types of testing” — they are distinct decision lenses.

Confusion occurs when terms like regression, performance, or UI testing
are used interchangeably across different dimensions.

Each dimension answers a different question.
Mixing them results in unclear plans, redundant effort, and unbounded risk.

**WHY → Testing Intent (Decision Being Supported)**
Derived from:

- Outcome
- Consumers
- Failure Modes

Testing intent defines the decision being made and the risk being bounded.
It is not a test type — it is the reason the test exists.
If the decision is unclear, the intent is undefined.

---

**WHAT → Quality Attribute (Type of Risk)**
Derived from:

- Constraints
- Failure Modes

Quality attributes describe what kind of failure matters most
(functional, performance, security, reliability, usability, compliance).
They are dimensions of risk — not levels or test types.
If the risk is unclear, the attribute focus is incorrect.

---

**WHERE → Test Level (Where Confidence Is Built)**
Derived from:

- Structure
- Dependency boundaries

Test levels define where validation occurs within the system:
unit, service, integration, UI, end‑to‑end, and business validation.
They are locations where risk is validated — not intents or attributes.

If the system boundaries are unclear, test placement is incorrect.

---

**HOW → Execution Mode (How Validation Occurs)**
Derived from:

- Verification

Execution mode defines how validation is performed
(manual, automated, monitored, synthetic).
It defines how risk is efficiently validated — not what is being tested.

If verification is unclear, execution mode cannot be chosen correctly.

---

**WHEN → Lifecycle Timing (When Decisions and Execution Occur)**
Testing is not a phase.
It is a continuous expression of contract definition and verification across the lifecycle.

- Test intent is defined at the start, when outcomes and expectations are clarified
- Test levels are decided during design
- Test details are defined during refinement
- Execution occurs primarily during build and deploy
- Business validation occurs at release

Timing decisions determine when risk is reduced.
Delaying risk reduction increases cost, impact, and likelihood of system failure.

---

### GOVERNING RULE

A test plan is not a list of tests.
It is a set of intentional choices across five dimensions:

- WHY are we testing (intent)?
- WHAT risk matters (attribute)?
- WHERE do we build confidence (level)?
- HOW do we validate (execution mode)?
- WHEN do we decide and execute?

If these cannot be explained, the contract is incomplete.

---

All five dimensions are driven by risk.

- WHY defines the decision being made
- WHAT defines the type of risk
- WHERE defines where it is validated
- HOW defines how it is reduced
- WHEN defines when it must be reduced

The completeness of testing is not determined by coverage.
It is determined by whether risk is sufficiently bounded.

“Enough” is reached when:

- critical risks are identified
- failure modes are understood
- verification proves those risks are controlled

Anything beyond this is unbounded analysis or unnecessary effort.

Anything short of this leaves the system exposed to failure.

---

### FINAL TEST DECISION REDUCTION

All quality and testing decisions reduce to this:

- Define the contract
- Identify how it can fail
- Choose where and how to prove it holds
- Do it as early as possible

---

The purpose of analysis is not completeness.
It is to bound risk sufficiently to act with confidence.

Over-analysis occurs when effort continues after risk is already bounded.
Under-analysis occurs when decisions are made with unbounded uncertainty.

The target is bounded, explainable risk at every decision point.

---

## CONSISTENCY AND TRACEABILITY OF QUALITY DECISIONS

All quality and testing decisions must be expressible in a consistent and explainable form.

Every test, validation, or quality activity must be describable using the same structure:

- WHY (Testing Intent)
- WHAT (Quality Attribute)
- WHERE (Test Level)
- HOW (Execution Mode)

And must be traceable back to:

- The defined outcome
- The identified consumers
- The constraints and failure modes
- The defined verification method

---

### STRUCTURAL RULE

Every quality decision must be:

- Explainable — the decision and its purpose are clear
- Traceable — it maps back to a defined contract
- Composable — it can be combined with other decisions to form a system
- Consistent — it follows the same structure across all levels

If a decision cannot be expressed in this form, it is not fully defined.

---

### SYSTEM BEHAVIOR

This structure ensures:

- No testing exists without purpose
- No validation exists without defined risk
- No effort exists without contract alignment
- No gap exists between specification and verification

All quality work becomes:

- Comparable across systems and teams
- Reusable across contexts
- Explainable to both technical and business audiences

---

### FAILURE SIGNAL

The following are indicators of an incomplete system:

- Tests that cannot be described in WHY / WHAT / WHERE / HOW terms
- Decisions that cannot be traced to a contract
- Validation effort that does not map to defined risk
- Testing activities that exist without a clear consumer

When these occur, return to the contract definition.

---

### FINAL QUALITY REDUCTION

All quality systems must produce:

- Contracts that are explicitly defined
- Decisions that are structurally consistent
- Verification that is traceable to intent

Quality is achieved when every layer of the system can explain:

- What it exists to do
- Who it serves
- How it can fail
- How we prove it works

---

## PRINCIPLE TENSION RESOLUTION

When two principles appear to conflict, apply this resolution order:

1. Consumer contracts win over process preferences.
2. System integrity wins over local speed.
3. Early conflict wins over deferred comfort.
4. Bounded uncertainty wins over false completeness.
5. Automation wins over repeated human judgment.

When conflict remains unresolved after applying this order:
stop, name the conflict explicitly, and resolve it as an architectural decision
before proceeding.

---

*When in doubt: name the consumer, name the contract, name the verification method.*

---

## CHANGE LOG

- v1.0: Initial draft

- v1.1: Stripped operational and project-specific content to Document 2.
        Restored universal scope. Tightened purpose statement.

- v1.2: Expanded Fractal Contract Principle to full universal scope —
        covers SDLC workflow, team interactions, content architecture,
        AI and prompt engineering, and all transactional relationships.
        Removed all project-specific references from this document.

- v1.3: Introduced explicit application layer for test planning and quality decisions.
        Established derivation model linking the Six Quality Questions to:
        testing intent (WHY), quality attributes (WHAT), test levels (WHERE),
        execution modes (HOW), and lifecycle timing (WHEN).
        Defined testing as a direct expression of contract definition and verification.

- v1.4: Introduced consistency and traceability model for all quality decisions.
        Formalized requirement that all testing and validation work be:
        explainable, traceable to contract, structurally consistent, and composable.
        Established a single decision structure (WHY / WHAT / WHERE / HOW)
        as the governing form for all quality and testing activity.

- v1.5: Tightened derivation and governing rule sections for clarity and readability.
        Reinforced risk as the central driver across all decision dimensions.
        Reduced redundancy and improved flow without expanding scope.
