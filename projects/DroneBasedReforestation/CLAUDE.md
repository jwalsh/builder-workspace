# DroneBasedReforestation

You are a coding agent working on DroneBasedReforestation -- An automated drone system for large-scale reforestation, planting seeds in hard-to-reach or disaster-affected areas.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; DroneBasedReforestation guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop flight controller software
- User interface: design user interface for web dashboard
- Data layer: implement seed storage and loading module

## Anti-Goals

- **General-purpose platform**: DroneBasedReforestation solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Revised Technical Documentation - READY FOR APPROVAL (P5) -- (depends on: Define System Architecture)
3. Develop Flight Controller Software (P2) -- (depends on: Define System Architecture)
4. Implement Seed Dispensing Mechanism (P2) -- (depends on: Define System Architecture)
5. Integrate Sensor Systems for Navigation and Terrain Mapping (P3) -- (depends on: Define System Architecture)
6. Create Mobile Application for Operator Control (P3) -- (depends on: Define System Architecture)
7. Design User Interface for Web Dashboard (P3) -- (depends on: Define System Architecture)
8. Implement Seed Storage and Loading Module (P3) -- (depends on: Define System Architecture)
9. Develop Communication Protocol for Drone and Ground Station (P3) -- (depends on: Define System Architecture)
10. Perform Unit Testing for Major Components (P4) -- (depends on: Develop Flight Controller Software, Implement Seed Dispensing Mechanism, Integrate Sensor Systems for Navigation and Terrain Mapping, Create Mobile Application for Operator Control, Design User Interface for Web Dashboard, Implement Seed Storage and Loading Module, Develop Communication Protocol for Drone and Ground Station)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DroneBasedReforestation can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An automated drone system for large-scale reforestation, planting seeds in hard-to-reach or disaster.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
