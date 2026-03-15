# RobotsReparacionAutonoma

You are a coding agent working on RobotsReparacionAutonoma -- Robots capaces de detectar y reparar infraestructuras dañadas de manera autónoma.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; RobotsReparacionAutonoma guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Robots capaces de detectar y reparar infraestructuras dañadas de manera autónoma.
- User interface: create user interface for monitoring and control

## Anti-Goals

- **General-purpose platform**: RobotsReparacionAutonoma solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design the Autonomous Repair Robot Architecture (P1)
2. Design and Develop the Repair Mechanism (P5) -- (depends on: Design the Autonomous Repair Robot Architecture)
3. Perform Security Audit of the System (P5) -- (depends on: Design the Autonomous Repair Robot Architecture)
4. Create a Robust Damage Assessment Algorithm (P4) -- (depends on: Design the Autonomous Repair Robot Architecture)
5. Implement Autonomous Navigation for the Robot (P3) -- (depends on: Design the Autonomous Repair Robot Architecture)
6. Develop the Detection System (P2) -- (depends on: Design the Autonomous Repair Robot Architecture)
7. Create User Interface for Monitoring and Control (P2) -- (depends on: Design the Autonomous Repair Robot Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RobotsReparacionAutonoma can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Robots capaces de detectar y reparar infraestructuras dañadas de manera autónoma..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
