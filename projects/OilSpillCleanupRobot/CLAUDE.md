# OilSpillCleanupRobot

You are a coding agent working on OilSpillCleanupRobot -- An autonomous robot designed for rapid deployment in oil spill situations, capable of efficiently cleaning up oil from water surfaces.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; OilSpillCleanupRobot guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop control software
- User interface: define project scope and requirements - revised
- Data layer: implement data storage and analytics

## Anti-Goals

- **General-purpose platform**: OilSpillCleanupRobot solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P5)
2. Design System Architecture for OilSpillCleanupRobot (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop Robot Hardware (P3) -- (depends on: Design System Architecture)
4. Develop Control Software (P3) -- (depends on: Design System Architecture)
5. Develop User Interface (P2) -- (depends on: Design System Architecture)
6. Implement Data Storage and Analytics (P2) -- (depends on: Design System Architecture)
7. Establish Testing and Quality Assurance (P3) -- (depends on: Develop Robot Hardware, Develop Control Software, Develop User Interface, Implement Data Storage and Analytics)
8. Implement Security and Compliance (P3) -- (depends on: Design System Architecture)
9. Comprehensive Deployment and Maintenance Plan for OilSpillCleanupRobot (P2) -- (depends on: Develop Robot Hardware, Develop Control Software, Develop User Interface, Implement Data Storage and Analytics)
10. Create Documentation and Training Materials (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Establish Testing and Quality Assurance, Plan Deployment and Maintenance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OilSpillCleanupRobot can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An autonomous robot designed for rapid deployment in oil spill situations, capable of efficiently cl.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
