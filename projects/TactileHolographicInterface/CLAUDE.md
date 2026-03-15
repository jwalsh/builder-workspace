# TactileHolographicInterface

You are a coding agent working on TactileHolographicInterface -- An interface that allows users to feel and manipulate holographic objects as if they were physical.

## Foundational Axiom

Existing approaches to interface fail because they optimize for the common case while ignoring structural constraints; TactileHolographicInterface makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An interface that allows users to feel and manipulate holographic objects as if they were physical.
- User interface: develop user interface for holographic object manipulation

## Anti-Goals

- **General-purpose platform**: TactileHolographicInterface solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Haptic Feedback System Design (P1)
2. Create Haptic Feedback System Prototype (P5) -- (depends on: Define Haptic Feedback System Design)
3. Document Final Design and Development Process (P5) -- (depends on: Perform Final User Testing)
4. Develop Holographic Object Generation Algorithm (P2) -- (depends on: Define Haptic Feedback System Design)
5. Implement Tactile Sensor Integration (P3) -- (depends on: Define Haptic Feedback System Design)
6. Develop User Interface for Holographic Object Manipulation (P4) -- (depends on: Develop Holographic Object Generation Algorithm, Implement Tactile Sensor Integration)
7. Perform User Testing and Gather Feedback (P1) -- (depends on: Create Haptic Feedback System Prototype)
8. Iterate on Design Based on User Feedback (P2) -- (depends on: Perform User Testing and Gather Feedback)
9. Implement Revised Haptic Feedback System (P3) -- (depends on: Iterate on Design Based on User Feedback)
10. Repeat User Testing and Gather Additional Feedback (P4) -- (depends on: Implement Revised Haptic Feedback System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TactileHolographicInterface can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An interface that allows users to feel and manipulate holographic objects as if they were physical..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
