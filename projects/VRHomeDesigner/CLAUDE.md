# VRHomeDesigner

You are a coding agent working on VRHomeDesigner -- A virtual reality platform for home design and visualization, allowing potential buyers to customize and experience their future homes before construction.

## Foundational Axiom

Existing approaches to virtual reality platform fail because they optimize for the common case while ignoring structural constraints; VRHomeDesigner makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop virtual reality engine
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: VRHomeDesigner solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture for VRHomeDesigner - RFC Review and Update (P5) -- (depends on: Define Project Requirements)
3. Develop Virtual Reality Engine (P3) -- (depends on: Design System Architecture)
4. Implement 3D Modeling and Customization (P3) -- (depends on: Design System Architecture)
5. Design User Interface and Experience (P3) -- (depends on: Define Project Requirements)
6. Develop Backend Services (P3) -- (depends on: Design System Architecture)
7. Implement Security Measures (P3) -- (depends on: Design System Architecture)
8. Create Test Suite (P3) -- (depends on: Define Project Requirements)
9. Integrate Virtual Reality Engine and Backend (P2) -- (depends on: Develop Virtual Reality Engine, Develop Backend Services)
10. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
11. Write Documentation (P2) -- (depends on: Define Project Requirements)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VRHomeDesigner can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A virtual reality platform for home design and visualization, allowing potential buyers to customize.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
