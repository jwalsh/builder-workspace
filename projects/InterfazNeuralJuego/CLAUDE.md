# InterfazNeuralJuego

You are a coding agent working on InterfazNeuralJuego -- Un sistema de interfaz neural que permite a los jugadores controlar videojuegos con sus ondas cerebrales.

## Foundational Axiom

Existing tools treat un sistema de interfaz neural que permite a los jugadores co as a generic automation problem; InterfazNeuralJuego succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development - gaming system
- User interface: requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: InterfazNeuralJuego solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering (P1)
2. Design System Architecture (P2) -- (depends on: Requirements Gathering)
3. Frontend Development - Neural Interface (P3) -- (depends on: Design System Architecture)
4. Backend Development - Gaming System (P3) -- (depends on: Design System Architecture)
5. Database Design and Implementation (P4) -- (depends on: Design System Architecture)
6. Integration and Testing (P5) -- (depends on: Frontend Development - Neural Interface, Backend Development - Gaming System, Database Design and Implementation)
7. DevOps Configuration and Deployment (P5) -- (depends on: Integration and Testing)
8. Documentation and Technical Writing (P5) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InterfazNeuralJuego can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema de interfaz neural que permite a los jugadores controlar videojuegos con sus ondas cerebr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
