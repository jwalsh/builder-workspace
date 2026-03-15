# SwarmDroneTechnology

You are a coding agent working on SwarmDroneTechnology -- A system for controlling and coordinating large swarms of drones for reconnaissance and tactical operations.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; SwarmDroneTechnology guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system for controlling and coordinating large swarms of drones for reconnaissance and tactical ope
- User interface: define system requirements

## Anti-Goals

- **General-purpose platform**: SwarmDroneTechnology solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define System Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Drone Control Module (P3) -- (depends on: Design System Architecture)
5. Develop Swarm Coordination Module (P3) -- (depends on: Design System Architecture)
6. Develop Communication Module (P3) -- (depends on: Design System Architecture)
7. Set up Development and Testing Environment (P3)
8. Develop Test Suite (P3) -- (depends on: Design System Architecture)
9. Develop User Interfaces (P2) -- (depends on: Design System Architecture)
10. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SwarmDroneTechnology can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for controlling and coordinating large swarms of drones for reconnaissance and tactical ope.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
