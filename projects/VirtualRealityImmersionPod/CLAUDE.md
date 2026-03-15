# VirtualRealityImmersionPod

You are a coding agent working on VirtualRealityImmersionPod -- A full-body VR pod that provides complete sensory immersion for entertainment, education, and remote work.

## Foundational Axiom

Existing approaches to full-body vr pod fail because they optimize for the common case while ignoring structural constraints; VirtualRealityImmersionPod makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: create software architecture for immersive experience
- User interface: develop frontend interface for user interaction

## Anti-Goals

- **General-purpose platform**: VirtualRealityImmersionPod solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Conceptualization for Full-Body VR Pod (P1)
2. Create Software Architecture for Immersive Experience (P3) -- (depends on: Design Conceptualization for Full-Body VR Pod)
3. Implement Backend Services for VR Pod Functionality (P5) -- (depends on: Create Software Architecture for Immersive Experience)
4. Develop Frontend Interface for User Interaction (P4) -- (depends on: Create Software Architecture for Immersive Experience)
5. Test and Validate Immersive Experience in the VR Pod (P2) -- (depends on: Implement Haptic Feedback and Sensory Systems)
6. Write User Manual for VR Pod Operations - DRAFT -> REVIEW (P4) -- (depends on: Test and Validate Immersive Experience in the VR Pod)
7. Develop Hardware Requirements for VR Pod (P2) -- (depends on: Design Conceptualization for Full-Body VR Pod)
8. Integrate Haptic Feedback and Sensory Systems (P1) -- (depends on: Develop Hardware Requirements for VR Pod)
9. Review Integration of Hardware and Software Components (P3) -- (depends on: Integrate Haptic Feedback and Sensory Systems)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualRealityImmersionPod can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A full-body VR pod that provides complete sensory immersion for entertainment, education, and remote.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
