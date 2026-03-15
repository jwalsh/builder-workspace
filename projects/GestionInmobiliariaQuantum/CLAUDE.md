# GestionInmobiliariaQuantum

You are a coding agent working on GestionInmobiliariaQuantum -- Una herramienta basada en tecnología cuántica para predecir tendencias inmobiliarias con alta precisión.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; GestionInmobiliariaQuantum co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend implementation
- User interface: requirements gathering
- Data layer: database setup

## Anti-Goals

- **General-purpose platform**: GestionInmobiliariaQuantum solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering (P1)
2. Technology Stack Selection (P2) -- (depends on: Requirements Gathering)
3. Quantum Algorithm Design (P3) -- (depends on: Technology Stack Selection)
4. Database Setup (P5) -- (depends on: Quantum Algorithm Design, Technology Stack Selection)
5. Backend Implementation (P4) -- (depends on: Quantum Algorithm Design, Technology Stack Selection)
6. Frontend Design (P4) -- (depends on: Technology Stack Selection)
7. DevOps and Infrastructure Management (P5) -- (depends on: Backend Implementation, Frontend Design)
8. Documentation and Knowledge Sharing (P4) -- (depends on: Backend Implementation, Frontend Design)
9. Integration of Quantum Libraries (P3) -- (depends on: Quantum Algorithm Design)
10. Testing and Quality Assurance (P2) -- (depends on: Backend Implementation, Frontend Design)
11. Security Assessment and Hardening (P1) -- (depends on: Backend Implementation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GestionInmobiliariaQuantum can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una herramienta basada en tecnología cuántica para predecir tendencias inmobiliarias con alta precis.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
