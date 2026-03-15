# DroneRefinery_Inspector

You are a coding agent working on DroneRefinery_Inspector -- An autonomous drone system for conducting safety inspections in oil refineries, detecting leaks and structural issues.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; DroneRefinery_Inspector guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data processing and analysis
- User interface: project planning and requirements gathering
- Data layer: data processing and analysis

## Anti-Goals

- **General-purpose platform**: DroneRefinery_Inspector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Drone Hardware and Sensor Integration (P3) -- (depends on: System Architecture Design)
4. Autonomous Navigation and Control System (P3) -- (depends on: System Architecture Design)
5. Data Processing and Analysis (P3) -- (depends on: System Architecture Design)
6. Security and Compliance (P3) -- (depends on: System Architecture Design)
7. User Interface and Reporting (P2) -- (depends on: System Architecture Design)
8. Integration with Refinery Systems (P2) -- (depends on: System Architecture Design)
9. Testing and Validation (P2) -- (depends on: Drone Hardware and Sensor Integration, Autonomous Navigation and Control System, Data Processing and Analysis, User Interface and Reporting, Integration with Refinery Systems)
10. Deployment and Maintenance (P2) -- (depends on: Testing and Validation, Security and Compliance)
11. Documentation and Training (P2) -- (depends on: User Interface and Reporting, Deployment and Maintenance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DroneRefinery_Inspector can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An autonomous drone system for conducting safety inspections in oil refineries, detecting leaks and .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
