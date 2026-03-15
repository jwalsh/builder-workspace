# HypersonicMissileDefense

You are a coding agent working on HypersonicMissileDefense -- Advanced tracking and interception systems designed to defend against hypersonic missile threats.

## Foundational Axiom

Existing approaches to advanced tracking and interception systems designed fail because they optimize for the common case while ignoring structural constraints; HypersonicMissileDefense makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Advanced tracking and interception systems designed to defend against hypersonic missile threats.
- User interface: project planning and requirements gathering
- Data layer: data management and analytics

## Anti-Goals

- **General-purpose platform**: HypersonicMissileDefense solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for Hypersonic Missile Defense (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Resilience (P5) -- (depends on: System Architecture Design)
4. Sensor and Tracking Subsystem (P3) -- (depends on: System Architecture Design)
5. Interception and Countermeasure Subsystem (P3) -- (depends on: System Architecture Design)
6. Command and Control Interface (P4) -- (depends on: System Architecture Design)
7. Data Management and Analytics (P4) -- (depends on: System Architecture Design)
8. Testing and Validation (P4) -- (depends on: Sensor and Tracking Subsystem, Interception and Countermeasure Subsystem, Command and Control Interface, Data Management and Analytics)
9. Deployment and Integration (P5) -- (depends on: Testing and Validation)
10. Documentation and Training (P4) -- (depends on: Command and Control Interface, Deployment and Integration)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HypersonicMissileDefense can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Advanced tracking and interception systems designed to defend against hypersonic missile threats..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
