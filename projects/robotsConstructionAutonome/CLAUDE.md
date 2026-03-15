# robotsConstructionAutonome

You are a coding agent working on robotsConstructionAutonome -- Des robots automatisés pour réaliser des tâches de construction comme la pose de briques et le coulage de béton.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; robotsConstructionAutonome guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop robotic arm control software

## Anti-Goals

- **General-purpose platform**: robotsConstructionAutonome solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design and prototype robotic arm for brick placement (P3)
2. Create a system for brick selection and delivery (P5) -- (depends on: Design and prototype robotic arm for brick placement)
3. Develop robotic arm control software (P4) -- (depends on: Design and prototype robotic arm for brick placement)
4. Research and implement concrete pouring automation (P1)
5. Test and Refine Robots' Construction Capabilities (P4) -- (depends on: Design and prototype robotic arm for brick placement, Create a system for brick selection and delivery, Research and implement concrete pouring automation)
6. Develop robotic arm gripper design (P2) -- (depends on: Design and prototype robotic arm for brick placement)
7. Design and develop safety mechanisms for the robots (P2)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: robotsConstructionAutonome can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Des robots automatisés pour réaliser des tâches de construction comme la pose de briques et le coula.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
