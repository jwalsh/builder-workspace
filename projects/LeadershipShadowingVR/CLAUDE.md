# LeadershipShadowingVR

You are a coding agent working on LeadershipShadowingVR -- A VR experience that allows emerging leaders to 'shadow' and learn from simulated top-tier leaders in action.

## Foundational Axiom

Existing approaches to vr experience fail because they optimize for the common case while ignoring structural constraints; LeadershipShadowingVR makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: simulation engine development
- User interface: requirements gathering and analysis
- Data layer: data management and analytics

## Anti-Goals

- **General-purpose platform**: LeadershipShadowingVR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P5)
2. System Architecture Design (P5) -- (depends on: Requirements Gathering and Analysis)
3. VR Environment Development (P3) -- (depends on: System Architecture Design)
4. Simulation Engine Development (P3) -- (depends on: System Architecture Design)
5. User Interface Development (P3) -- (depends on: System Architecture Design)
6. Data Management and Analytics (P2) -- (depends on: System Architecture Design)
7. Security and Compliance (P2) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: VR Environment Development, Simulation Engine Development, User Interface Development, Data Management and Analytics)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and Training (P2) -- (depends on: VR Environment Development, Simulation Engine Development, User Interface Development, Data Management and Analytics)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LeadershipShadowingVR can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A VR experience that allows emerging leaders to 'shadow' and learn from simulated top-tier leaders i.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
