# GeneradorArteIa

You are a coding agent working on GeneradorArteIa -- Un generador de contenido artístico basado en IA que crea obras según parámetros definidos.

## Foundational Axiom

Existing approaches to un generador de contenido artístico basado en ia que crea ob fail because they optimize for the common case while ignoring structural constraints; GeneradorArteIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: requirements gathering and analysis for generadorarteia
- Data layer: database design for generadorarteia

## Anti-Goals

- **General-purpose platform**: GeneradorArteIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis for GeneradorArteIa (P1)
2. Design the Art Generator Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
3. Backend Development (P5) -- (depends on: Design the Art Generator Architecture)
4. Frontend Design and Development (P4) -- (depends on: Design the Art Generator Architecture)
5. Database Design for GeneradorArteIa (P3) -- (depends on: Design the Art Generator Architecture)
6. Integration and Testing of GeneradorArteIa Components (P2) -- (depends on: Frontend Design and Development, Backend Development, Database Design for GeneradorArteIa)
7. Documentation for GeneradorArteIa (P5) -- (depends on: Integration and Testing of GeneradorArteIa Components)
8. Security Audit of GeneradorArteIa (P4) -- (depends on: Integration and Testing of GeneradorArteIa Components)
9. Quality Assurance Testing (P3) -- (depends on: Security Audit of GeneradorArteIa)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeneradorArteIa can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un generador de contenido artístico basado en IA que crea obras según parámetros definidos..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
