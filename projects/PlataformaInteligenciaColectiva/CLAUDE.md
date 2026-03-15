# PlataformaInteligenciaColectiva

You are a coding agent working on PlataformaInteligenciaColectiva -- Un sistema que aprovecha la inteligencia colectiva y los algoritmos de consenso para la toma de decisiones a gran escala.

## Foundational Axiom

Existing approaches to un sistema que aprovecha la inteligencia colectiva y los alg fail because they optimize for the common case while ignoring structural constraints; PlataformaInteligenciaColectiva makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: implement frontend design
- Data layer: develop database schema

## Anti-Goals

- **General-purpose platform**: PlataformaInteligenciaColectiva solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Implement Frontend Design (P2) -- (depends on: Define System Architecture)
3. Develop Backend Services (P2) -- (depends on: Define System Architecture)
4. Perform System Testing (P5) -- (depends on: Implement Frontend Design, Develop Backend Services)
5. Deploy and Monitor the Platform (P5) -- (depends on: Implement Frontend Design, Develop Backend Services)
6. Create Comprehensive User Documentation (P4) -- (depends on: Implement Frontend Design, Develop Backend Services)
7. Design Decision Algorithms (P3) -- (depends on: Define System Architecture)
8. Develop Database Schema (P3) -- (depends on: Define System Architecture)
9. Implement Security Measures (P3) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlataformaInteligenciaColectiva can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema que aprovecha la inteligencia colectiva y los algoritmos de consenso para la toma de deci.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
