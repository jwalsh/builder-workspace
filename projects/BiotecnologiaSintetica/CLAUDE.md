# BiotecnologiaSintetica

You are a coding agent working on BiotecnologiaSintetica -- Uso de la biotecnología sintética para crear medicamentos personalizados adaptados a las necesidades de los pacientes.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BiotecnologiaSintetica embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop drug customization engine
- User interface: gather requirements
- Data layer: develop patient data management

## Anti-Goals

- **General-purpose platform**: BiotecnologiaSintetica solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design Architecture for Personalized Medicine System - REVISED (P5) -- (depends on: Gather Requirements)
3. Develop Patient Data Management (P3) -- (depends on: Design System Architecture)
4. Develop Drug Customization Engine (P3) -- (depends on: Design System Architecture)
5. Build User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Security and Compliance (P2) -- (depends on: Design System Architecture)
7. Set up Testing and Deployment (P2) -- (depends on: Design System Architecture)
8. Conduct User Acceptance Testing (P2) -- (depends on: Develop Patient Data Management, Develop Drug Customization Engine, Build User Interface)
9. Document System and Processes (P2) -- (depends on: Develop Patient Data Management, Develop Drug Customization Engine, Build User Interface)
10. Deploy and Monitor System (P1) -- (depends on: Set up Testing and Deployment, Conduct User Acceptance Testing, Document System and Processes)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BiotecnologiaSintetica can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Uso de la biotecnología sintética para crear medicamentos personalizados adaptados a las necesidades.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
