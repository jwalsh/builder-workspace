# SmartFarmingDrones

You are a coding agent working on SmartFarmingDrones -- Autonomous drones that monitor crop health and optimize resource use in agriculture.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; SmartFarmingDrones guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Autonomous drones that monitor crop health and optimize resource use in agriculture.
- User interface: create user interface for data visualization (with modifications)
- Data layer: create user interface for data visualization (with modifications)

## Anti-Goals

- **General-purpose platform**: SmartFarmingDrones solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Implement Crop Health Monitoring Sensors (Updated) (P3) -- (depends on: Define System Architecture)
3. Develop Autonomous Navigation System (P2) -- (depends on: Define System Architecture)
4. Optimize Resource Allocation Algorithms in SmartFarmingDrones (Revised) (P4) -- (depends on: Implement Crop Health Monitoring Sensors, Develop Autonomous Navigation System)
5. Create User Interface for Data Visualization (with modifications) (P5) -- (depends on: Implement Crop Health Monitoring Sensors, Optimize Resource Allocation Algorithms)
6. Perform Security Audit of the System (P2) -- (depends on: Define System Architecture)
7. Develop Quality Assurance Plan (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartFarmingDrones can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Autonomous drones that monitor crop health and optimize resource use in agriculture..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
