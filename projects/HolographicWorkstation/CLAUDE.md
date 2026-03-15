# HolographicWorkstation

You are a coding agent working on HolographicWorkstation -- A fully holographic computer workstation that replaces traditional screens and input devices with 3D projections and gesture controls.

## Foundational Axiom

Existing approaches to fully holographic computer workstation fail because they optimize for the common case while ignoring structural constraints; HolographicWorkstation makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop projection system hardware and software
- User interface: define project scope and requirements - v2.0

## Anti-Goals

- **General-purpose platform**: HolographicWorkstation solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - v2.0 (P1)
2. Design Holographic User Interface (UI) (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Holographic UI Components (P3) -- (depends on: Design Holographic User Interface)
4. Design Holographic Projection System (P2) -- (depends on: Define Project Scope and Requirements)
5. Develop Projection System Hardware and Software (P3) -- (depends on: Design Holographic Projection System)
6. Design Gesture Control System (P2) -- (depends on: Define Project Scope and Requirements)
7. Develop Gesture Control Software (P3) -- (depends on: Design Gesture Control System)
8. Integrate UI Components with Projection and Gesture Systems (P4) -- (depends on: Develop Holographic UI Components, Develop Projection System Hardware and Software, Develop Gesture Control Software)
9. Perform Quality Assurance (QA) Testing (P5) -- (depends on: Integrate UI Components with Projection and Gesture Systems)
10. Resolve QA Issues (P5) -- (depends on: Perform Quality Assurance (QA) Testing)
11. Document HolographicWorkstation User Guide (P5) -- (depends on: Integrate UI Components with Projection and Gesture Systems)
12. Deploy HolographicWorkstation (P5) -- (depends on: Resolve QA Issues, Document HolographicWorkstation User Guide)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HolographicWorkstation can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A fully holographic computer workstation that replaces traditional screens and input devices with 3D.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
