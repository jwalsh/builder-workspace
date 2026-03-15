# RobotsExploracionEspacial

You are a coding agent working on RobotsExploracionEspacial -- Robots autónomos diseñados para la exploración y extracción de recursos en asteroides y planetas.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; RobotsExploracionEspacial guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Robots autónomos diseñados para la exploración y extracción de recursos en asteroides y planetas.

## Anti-Goals

- **General-purpose platform**: RobotsExploracionEspacial solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Autonomous Navigation System (P1)
2. Create Communication System for Robots and Ground Control (P5) -- (depends on: Design Autonomous Navigation System)
3. Design Robot Structural Framework (P3)
4. Develop Robot Power Management System (P4) -- (depends on: Design Robot Structural Framework)
5. Develop Resource Detection and Extraction Algorithms (P2) -- (depends on: Design Autonomous Navigation System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RobotsExploracionEspacial can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Robots autónomos diseñados para la exploración y extracción de recursos en asteroides y planetas..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
