# TranslateTechIa

You are a coding agent working on TranslateTechIa -- Un sistema di traduzione che utilizza le tecnologie di intelligenza artificiale e di apprendimento automatico per fornire traduzioni precise e efficaci per le imprese e le organizzazioni.

## Foundational Axiom

Existing approaches to un sistema di traduzione che utilizza le tecnologie di intel fail because they optimize for the common case while ignoring structural constraints; TranslateTechIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement the backend services for translatetechia
- User interface: develop the frontend interface for translatetechia
- Data layer: set up the database structure for translatetechia

## Anti-Goals

- **General-purpose platform**: TranslateTechIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and goals (P1)
2. Research and evaluate AI and machine learning technologies (P2)
3. Design the core architecture of TranslateTechIa (P3) -- (depends on: Research and evaluate AI and machine learning technologies)
4. Perform security audits on the system (P5) -- (depends on: Define project scope and goals, Design the core architecture of TranslateTechIa)
5. Develop the frontend interface for TranslateTechIa (P4) -- (depends on: Define project scope and goals, Design the core architecture of TranslateTechIa)
6. Implement the backend services for TranslateTechIa (P4) -- (depends on: Define project scope and goals, Design the core architecture of TranslateTechIa)
7. Perform functional testing on TranslateTechIa (P5) -- (depends on: Develop the frontend interface for TranslateTechIa, Implement the backend services for TranslateTechIa)
8. Review and refine project requirements and specifications (P5) -- (depends on: Perform functional testing on TranslateTechIa)
9. Set up the database structure for TranslateTechIa (P4) -- (depends on: Define project scope and goals, Design the core architecture of TranslateTechIa)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TranslateTechIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un sistema di traduzione che utilizza le tecnologie di intelligenza artificiale e di apprendimento a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
