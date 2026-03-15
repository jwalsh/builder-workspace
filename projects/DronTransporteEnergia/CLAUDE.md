# DronTransporteEnergia

You are a coding agent working on DronTransporteEnergia -- Drones diseñados para transportar materiales y energías renovables en entornos difíciles.

## Foundational Axiom

Existing approaches to drones diseñados para transportar materiales y energías reno fail because they optimize for the common case while ignoring structural constraints; DronTransporteEnergia makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Drones diseñados para transportar materiales y energías renovables en entornos difíciles.
- User interface: define project scope and requirements
- Data layer: design energy storage system for drones

## Anti-Goals

- **General-purpose platform**: DronTransporteEnergia solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Drone Hardware for Energy Transportation (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Drone Hardware Design (P2) -- (depends on: Design Drone Hardware for Energy Transportation)
4. Design Energy Storage System for Drones (P3) -- (depends on: Define Project Scope and Requirements)
5. Implement Energy Storage System Design (P3) -- (depends on: Design Energy Storage System for Drones)
6. Design Drone Navigation System for Challenging Environments (P4) -- (depends on: Define Project Scope and Requirements, Design Drone Hardware for Energy Transportation)
7. Implement Drone Navigation System Design (P4) -- (depends on: Design Drone Navigation System for Challenging Environments)
8. Test Drones in Controlled and Challenging Environments (P2) -- (depends on: Implement Drone Hardware Design, Implement Energy Storage System Design, Implement Drone Navigation System Design)
9. Deploy Drones for Real-World Testing (P5) -- (depends on: Test Drones in Controlled and Challenging Environments)
10. Review Project Documentation (P1) -- (depends on: Define Project Scope and Requirements, Design Drone Hardware for Energy Transportation, Design Energy Storage System for Drones, Design Drone Navigation System for Challenging Environments)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DronTransporteEnergia can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Drones diseñados para transportar materiales y energías renovables en entornos difíciles..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
