# MilitaryIoTNetwork

You are a coding agent working on MilitaryIoTNetwork -- A secure Internet of Things (IoT) network for military applications, connecting various sensors and devices for enhanced situational awareness.

## Foundational Axiom

Existing approaches to secure internet of things (iot) network fail because they optimize for the common case while ignoring structural constraints; MilitaryIoTNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A secure Internet of Things (IoT) network for military applications, connecting various sensors and 
- User interface: define project scope and requirements - rfc
- Data layer: design and implement data management system

## Anti-Goals

- **General-purpose platform**: MilitaryIoTNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Security Protocols and Mechanisms (P5) -- (depends on: Design System Architecture)
4. Design and Implement Network Infrastructure (P4) -- (depends on: Design System Architecture)
5. Develop IoT Device Integration (P4) -- (depends on: Design System Architecture)
6. Design and Implement Data Management System (P4) -- (depends on: Design System Architecture)
7. Develop User Interfaces and Visualization Tools (P3) -- (depends on: Design System Architecture, Design and Implement Data Management System)
8. Develop Test Plans and Conduct Testing (P4) -- (depends on: Develop Security Protocols and Mechanisms, Design and Implement Network Infrastructure, Develop IoT Device Integration, Design and Implement Data Management System, Develop User Interfaces and Visualization Tools)
9. Implement Continuous Integration and Deployment (CI/CD) (P3)
10. Create Documentation and User Guides (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MilitaryIoTNetwork can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A secure Internet of Things (IoT) network for military applications, connecting various sensors and .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
