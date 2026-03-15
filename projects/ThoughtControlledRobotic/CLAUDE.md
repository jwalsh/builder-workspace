# ThoughtControlledRobotic

You are a coding agent working on ThoughtControlledRobotic -- A BCI system for controlling robotic systems with thought, useful in various industries including space exploration.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; ThoughtControlledRobotic guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop bci system software
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: ThoughtControlledRobotic solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design BCI System Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop BCI System Software (P3) -- (depends on: Design BCI System Architecture)
4. Develop Robotic System Architecture (P2) -- (depends on: Define Project Requirements)
5. Develop Robotic System Software (P3) -- (depends on: Develop Robotic System Architecture)
6. Test BCI System Integration (P4) -- (depends on: Develop BCI System Software, Develop Robotic System Software)
7. Integrate BCI and Robotic Systems for Space Exploration (P5) -- (depends on: Test BCI System Integration)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThoughtControlledRobotic can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A BCI system for controlling robotic systems with thought, useful in various industries including sp.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
