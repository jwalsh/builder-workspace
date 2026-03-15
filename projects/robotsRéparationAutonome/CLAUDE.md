# robotsRéparationAutonome

You are a coding agent working on robotsRéparationAutonome -- Des robots capables de détecter et réparer automatiquement les infrastructures endommagées.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; robotsRéparationAutonome guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Des robots capables de détecter et réparer automatiquement les infrastructures endommagées.

## Anti-Goals

- **General-purpose platform**: robotsRéparationAutonome solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Autonomous Robot Architecture (P1)
2. Write User Manual for robotsRéparationAutonome - REFACTORED (P5) -- (depends on: Design Autonomous Robot Architecture)
3. Create Infrastructure Damage Detection Algorithm (P4) -- (depends on: Design Autonomous Robot Architecture)
4. Develop Repair Mechanisms for the Robot (P3) -- (depends on: Design Autonomous Robot Architecture)
5. Review and Approve Design of robotsRéparationAutonome (P3) -- (depends on: Design Autonomous Robot Architecture)
6. Develop Autonomous Robot Detection System (P2) -- (depends on: Design Autonomous Robot Architecture)
7. Test and Validate the Functionality of robotsRéparationAutonome (P2) -- (depends on: Develop Autonomous Robot Detection System, Develop Repair Mechanisms for the Robot)
8. Perform Security Audit on robotsRéparationAutonome (P1) -- (depends on: Design Autonomous Robot Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: robotsRéparationAutonome can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des robots capables de détecter et réparer automatiquement les infrastructures endommagées..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
