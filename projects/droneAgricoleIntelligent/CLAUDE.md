# droneAgricoleIntelligent

You are a coding agent working on droneAgricoleIntelligent -- Des drones autonomes capables de surveiller les cultures et d'optimiser l'utilisation des ressources agricoles.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; droneAgricoleIntelligent guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Des drones autonomes capables de surveiller les cultures et d'optimiser l'utilisation des ressources

## Anti-Goals

- **General-purpose platform**: droneAgricoleIntelligent solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Drone Hardware for Agricultural Surveillance (P3)
2. Create Computer Vision Algorithms for Crop Monitoring (P2) -- (depends on: Design Drone Hardware for Agricultural Surveillance)
3. Develop Resource Optimization Algorithm (P5) -- (depends on: Create Computer Vision Algorithms for Crop Monitoring)
4. Develop Autonomous Navigation System (P4) -- (depends on: Design Drone Hardware for Agricultural Surveillance)
5. Write Technical Documentation for the Project (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: droneAgricoleIntelligent can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des drones autonomes capables de surveiller les cultures et d'optimiser l'utilisation des ressources.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
