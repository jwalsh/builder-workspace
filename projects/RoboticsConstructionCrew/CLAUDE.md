# RoboticsConstructionCrew

You are a coding agent working on RoboticsConstructionCrew -- A team of specialized construction robots capable of working collaboratively to perform various tasks on construction sites, improving efficiency and safety.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; RoboticsConstructionCrew guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: robot software development
- User interface: project planning and requirements gathering
- Data layer: data management and analytics

## Anti-Goals

- **General-purpose platform**: RoboticsConstructionCrew solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for RoboticsConstructionCrew (P1) -- (depends on: Project Planning and Requirements Gathering, System Requirements Specification, Hardware/Software Procurement, Design Review)
3. Robot Hardware Design and Prototyping (P3) -- (depends on: System Architecture Design)
4. Robot Software Development (P3) -- (depends on: System Architecture Design)
5. Central Management System Development (P3) -- (depends on: System Architecture Design)
6. Data Management and Analytics (P4) -- (depends on: System Architecture Design)
7. Security and Access Control for RoboticsConstructionCrew (P4) -- (depends on: System Architecture Design)
8. Integration and Testing (P4) -- (depends on: Robot Hardware Design and Prototyping, Robot Software Development, Central Management System Development, Data Management and Analytics, Security and Access Control)
9. Deployment and Maintenance (P5) -- (depends on: Integration and Testing)
10. Documentation and Training (P4) -- (depends on: System Architecture Design, Robot Hardware Design and Prototyping, Robot Software Development, Central Management System Development, Data Management and Analytics, Security and Access Control)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RoboticsConstructionCrew can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A team of specialized construction robots capable of working collaboratively to perform various task.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
