# droneGestionClimat

You are a coding agent working on droneGestionClimat -- Des drones autonomes pour la gestion du climat en milieu agricole, optimisant l'humidité et la température.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; droneGestionClimat guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: define the software architecture for drone control and data processing
- User interface: create a user-friendly interface for the drone system
- Data layer: define the software architecture for drone control and data processing

## Anti-Goals

- **General-purpose platform**: droneGestionClimat solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design the drone hardware (P3)
2. Define the software architecture for drone control and data processing (P4) -- (depends on: Design the drone hardware)
3. Implement the drone's autonomous navigation system (P5) -- (depends on: Design the drone hardware, Define the software architecture for drone control and data processing)
4. Create a user-friendly interface for the drone system (P1) -- (depends on: Implement the drone's autonomous navigation system)
5. Setup continuous integration and deployment pipeline (P4) -- (depends on: Implement the drone's autonomous navigation system, Create a user-friendly interface for the drone system)
6. Develop a database structure for storing climate and drone data (P3) -- (depends on: Define the software architecture for drone control and data processing)
7. Develop the climate data processing algorithms (P2) -- (depends on: Define the software architecture for drone control and data processing)
8. Perform initial testing on drones and software (P2) -- (depends on: Implement the drone's autonomous navigation system, Create a user-friendly interface for the drone system)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: droneGestionClimat can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des drones autonomes pour la gestion du climat en milieu agricole, optimisant l'humidité et la tempé.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
