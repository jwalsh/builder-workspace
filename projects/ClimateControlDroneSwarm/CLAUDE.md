# ClimateControlDroneSwarm

You are a coding agent working on ClimateControlDroneSwarm -- Drones working in unison to monitor and manage climate in agricultural settings.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; ClimateControlDroneSwarm captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Drones working in unison to monitor and manage climate in agricultural settings.
- User interface: define drone hardware requirements
- Data layer: integrate sensor data with climate modeling algorithms

## Anti-Goals

- **General-purpose platform**: ClimateControlDroneSwarm solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Drone Hardware Requirements (P3)
2. Develop Climate Modeling Algorithms (P5) -- (depends on: Define Drone Hardware Requirements)
3. Design Drone Firmware Architecture (P4) -- (depends on: Define Drone Hardware Requirements)
4. Implement Communication Protocol for Drones (P4) -- (depends on: Define Drone Hardware Requirements)
5. Integrate Sensor Data with Climate Modeling Algorithms (P4) -- (depends on: Design Drone Firmware Architecture, Develop Climate Modeling Algorithms)
6. Design User Interface for Climate Control Drones (P2)
7. Write Unit Tests for Drones and Algorithms (P2) -- (depends on: Design Drone Firmware Architecture, Develop Climate Modeling Algorithms)
8. Document Climate Control Drone System (P1) -- (depends on: Define Drone Hardware Requirements, Design Drone Firmware Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ClimateControlDroneSwarm can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Drones working in unison to monitor and manage climate in agricultural settings..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
