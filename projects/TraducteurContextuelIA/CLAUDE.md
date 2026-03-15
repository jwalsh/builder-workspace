# TraducteurContextuelIA

You are a coding agent working on TraducteurContextuelIA -- Un service de traduction avancé qui utilise l'IA pour comprendre le contexte et produire des traductions plus naturelles et précises.

## Foundational Axiom

Existing approaches to un service de traduction avancé qui utilise l'ia pour compre fail because they optimize for the common case while ignoring structural constraints; TraducteurContextuelIA makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: define project scope and requirements for contextually aware ai translation service
- User interface: define project scope and requirements for contextually aware ai translation service

## Anti-Goals

- **General-purpose platform**: TraducteurContextuelIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements for Contextually Aware AI Translation Service (P1)
2. Design Context Understanding Algorithm (P2) -- (depends on: Define Project Scope and Requirements)
3. Integrate Translation API for Actual Text Translation (P4) -- (depends on: Design Context Understanding Algorithm)
4. Develop User Interface for Input and Output Text (P5) -- (depends on: Integrate Translation API for Actual Text Translation)
5. Develop AI Model for Natural Language Processing (P3) -- (depends on: Design Context Understanding Algorithm)
6. Implement Security Measures (P2) -- (depends on: Develop User Interface for Input and Output Text)
7. Test and Validate the System Performance (P1) -- (depends on: Develop User Interface for Input and Output Text)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TraducteurContextuelIA can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un service de traduction avancé qui utilise l'IA pour comprendre le contexte et produire des traduct.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
