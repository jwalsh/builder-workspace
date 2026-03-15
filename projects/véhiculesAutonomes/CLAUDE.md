# véhiculesAutonomes

You are a coding agent working on véhiculesAutonomes -- Une flotte de véhicules entièrement autonomes conçus pour les environnements urbains.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; véhiculesAutonomes guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Une flotte de véhicules entièrement autonomes conçus pour les environnements urbains.
- User interface: create user interface for vehicle controls

## Anti-Goals

- **General-purpose platform**: véhiculesAutonomes solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture for Autonomous Vehicles (P1)
2. Create User Interface for Vehicle Controls (P5) -- (depends on: Define System Architecture for Autonomous Vehicles)
3. Design Urban Navigation System (P2) -- (depends on: Define System Architecture for Autonomous Vehicles)
4. Develop Sensor and Perception System (P3) -- (depends on: Define System Architecture for Autonomous Vehicles)
5. Implement Machine Learning Models for Decision Making (P4) -- (depends on: Design Urban Navigation System, Develop Sensor and Perception System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: véhiculesAutonomes can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une flotte de véhicules entièrement autonomes conçus pour les environnements urbains..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
