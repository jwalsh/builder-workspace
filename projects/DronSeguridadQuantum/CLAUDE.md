# DronSeguridadQuantum

You are a coding agent working on DronSeguridadQuantum -- Drones equipados con tecnología de comunicación cuántica para misiones militares seguras.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; DronSeguridadQuantum co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design drones hardware and software architecture
- User interface: define comprehensive project requirements for dronseguridadquantum

## Anti-Goals

- **General-purpose platform**: DronSeguridadQuantum solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Quantum Communication System Architecture (P2) -- (depends on: Define Project Requirements)
2. Design Drones Hardware and Software Architecture (P2) -- (depends on: Design Quantum Communication System Architecture)
3. Develop Drones Software (P3) -- (depends on: Design Drones Hardware and Software Architecture)
4. Test Drones Functionality and Integration (P4) -- (depends on: Develop Drones Software)
5. Deploy and Conduct Initial Test Flights (P5) -- (depends on: Test Drones Functionality and Integration)
6. Review and Address Feedback from Test Flights (P5) -- (depends on: Deploy and Conduct Initial Test Flights)
7. Develop Quantum Communication System Software (P3) -- (depends on: Design Quantum Communication System Architecture)
8. Test Quantum Communication System Integration (P4) -- (depends on: Develop Quantum Communication System Software)
9. Implement Quantum Key Distribution (QKD) Algorithm (P3) -- (depends on: Develop Quantum Communication System Software)
10. Define Comprehensive Project Requirements for DronSeguridadQuantum (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DronSeguridadQuantum can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Drones equipados con tecnología de comunicación cuántica para misiones militares seguras..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
