# SpaceMiningRobots

You are a coding agent working on SpaceMiningRobots -- Robots designed for autonomous resource extraction from asteroids and planets.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; SpaceMiningRobots guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Robots designed for autonomous resource extraction from asteroids and planets.

## Anti-Goals

- **General-purpose platform**: SpaceMiningRobots solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Robot Architecture (P1)
2. Design and Develop Power Systems for Robots (P5) -- (depends on: Design Robot Architecture)
3. Develop Navigation System (P2) -- (depends on: Design Robot Architecture)
4. Create Communication Systems for Robots and Earth Control Centers (P4) -- (depends on: Design Robot Architecture, Develop Navigation System)
5. Implement Resource Detection and Extraction Mechanisms (P3) -- (depends on: Design Robot Architecture, Develop Navigation System)
6. Establish Safety and Security Protocols for Robots (P2)
7. Formulate Mission Control Strategy (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SpaceMiningRobots can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Robots designed for autonomous resource extraction from asteroids and planets..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
