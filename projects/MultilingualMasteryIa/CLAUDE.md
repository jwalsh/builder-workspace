# MultilingualMasteryIa

You are a coding agent working on MultilingualMasteryIa -- Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para proporcionar traducciones precisas y eficientes en varias lenguas.

## Foundational Axiom

Existing approaches to un sistema de traducción que utiliza la inteligencia artific fail because they optimize for the common case while ignoring structural constraints; MultilingualMasteryIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development (1 of n)
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: MultilingualMasteryIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. System Design (P2) -- (depends on: Requirements Gathering and Analysis)
3. Backend Development (1 of N) (P3) -- (depends on: System Design)
4. Frontend Development (1 of N) (P3) -- (depends on: System Design)
5. Integration Testing (P5) -- (depends on: Backend Development (1 of N), Frontend Development (1 of N))
6. Security Audit (P5) -- (depends on: Integration Testing)
7. Documentation (P5) -- (depends on: Integration Testing)
8. Database Design and Implementation (P4) -- (depends on: System Design)
9. DevOps and Infrastructure Setup (P4) -- (depends on: System Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MultilingualMasteryIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un sistema de traducción que utiliza la inteligencia artificial y el aprendizaje automático para pro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
