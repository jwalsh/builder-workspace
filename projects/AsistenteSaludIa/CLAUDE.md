# AsistenteSaludIa

You are a coding agent working on AsistenteSaludIa -- Un asistente personal que ofrece consejos de salud personalizados basados en métricas en tiempo real.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; AsistenteSaludIa embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design health recommendation engine (revised)
- User interface: define project scope and requirements
- Data layer: design data storage and management for asistentesaludia

## Anti-Goals

- **General-purpose platform**: AsistenteSaludIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design the system architecture for AsistenteSaludIa (P5) -- (depends on: Define the scope and requirements of the project)
3. Design Data Storage and Management for AsistenteSaludIa (P3) -- (depends on: Design System Architecture)
4. Design Health Recommendation Engine (Revised) (P5) -- (depends on: Design System Architecture, Design Data Storage and Management, Define User Profiles and Preferences)
5. Design Security and Privacy Measures for Handling Sensitive Health Data and Ensuring User Privacy (P4) -- (depends on: Design System Architecture)
6. Design User Interface - Updated (P3) -- (depends on: Design System Architecture)
7. Define Testing Strategy (P3) -- (depends on: Design System Architecture)
8. Plan Deployment and DevOps (P3) -- (depends on: Design System Architecture)
9. Develop Documentation and User Guides (P2) -- (depends on: Design System Architecture, Design User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AsistenteSaludIa can deliver its core value proposition as described
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

- TypeScript/JavaScript
- MongoDB
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un asistente personal que ofrece consejos de salud personalizados basados en métricas en tiempo real.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
