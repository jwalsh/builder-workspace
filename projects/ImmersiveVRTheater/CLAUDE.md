# ImmersiveVRTheater

You are a coding agent working on ImmersiveVRTheater -- A VR platform that creates immersive live theater experiences for remote audiences.

## Foundational Axiom

Existing approaches to vr platform fail because they optimize for the common case while ignoring structural constraints; ImmersiveVRTheater makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A VR platform that creates immersive live theater experiences for remote audiences.
- User interface: requirements gathering for immersive vr theater platform

## Anti-Goals

- **General-purpose platform**: ImmersiveVRTheater solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for Immersive VR Theater Platform (P1)
2. Design Architecture (P2) -- (depends on: Requirements Gathering)
3. User Interface Design (P3) -- (depends on: Design Architecture)
4. Server Implementation (P3) -- (depends on: Design Architecture)
5. Networking Implementation (P3) -- (depends on: Design Architecture)
6. Integration and Testing (P4) -- (depends on: User Interface Design, Server Implementation, Networking Implementation)
7. Deployment Strategy Development (P5) -- (depends on: Integration and Testing)
8. Deploy to Staging Environment (P5) -- (depends on: Deployment Strategy Development, Integration and Testing)
9. Prepare Launch Announcement (P5) -- (depends on: Deploy to Staging Environment)
10. Hardware Selection (P4) -- (depends on: Design Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ImmersiveVRTheater can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A VR platform that creates immersive live theater experiences for remote audiences..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
