# AutonomousDroneHive

You are a coding agent working on AutonomousDroneHive -- Design a system for managing autonomous drone swarms for applications in agriculture, search and rescue, and urban planning.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; AutonomousDroneHive guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: build data processing and analytics
- User interface: define system requirements for autonomousdronehive: revised
- Data layer: build data processing and analytics

## Anti-Goals

- **General-purpose platform**: AutonomousDroneHive solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements for AutonomousDroneHive: Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define System Requirements)
3. Implement Security and Access Control (P4) -- (depends on: Design System Architecture)
4. Develop Drone Control and Communication (P3) -- (depends on: Design System Architecture)
5. Implement Mission Planning and Optimization (P3) -- (depends on: Design System Architecture)
6. Build Data Processing and Analytics (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
8. Develop User Interfaces (P2) -- (depends on: Design System Architecture)
9. Conduct System Testing and Validation (P2) -- (depends on: Develop Drone Control and Communication, Implement Mission Planning and Optimization, Build Data Processing and Analytics, Develop User Interfaces, Implement Security and Access Control)
10. Prepare Documentation and Training Materials (P2) -- (depends on: Develop User Interfaces)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AutonomousDroneHive can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Design a system for managing autonomous drone swarms for applications in agriculture, search and res.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
