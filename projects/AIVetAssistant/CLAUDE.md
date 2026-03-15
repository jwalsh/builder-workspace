# AIVetAssistant

You are a coding agent working on AIVetAssistant -- An AI system that assists veterinarians in diagnosing pet ailments and recommending treatments.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AIVetAssistant makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data ingestion and preprocessing
- User interface: define project scope and requirements (revised)
- Data layer: implement data ingestion and preprocessing

## Anti-Goals

- **General-purpose platform**: AIVetAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3)
4. Implement Data Ingestion and Preprocessing (P2) -- (depends on: Design System Architecture)
5. Train AI Diagnostic Model (P2) -- (depends on: Implement Data Ingestion and Preprocessing)
6. Develop User Interface (P2) -- (depends on: Design System Architecture)
7. Integrate System Components (P2) -- (depends on: Implement Data Ingestion and Preprocessing, Train AI Diagnostic Model, Develop User Interface)
8. Conduct System Testing (P2) -- (depends on: Integrate System Components)
9. Address Security Concerns (P2) -- (depends on: Integrate System Components)
10. Prepare Documentation (P2) -- (depends on: Integrate System Components)
11. Deploy and Monitor System (P1) -- (depends on: Conduct System Testing, Address Security Concerns, Prepare Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIVetAssistant can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that assists veterinarians in diagnosing pet ailments and recommending treatments..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
