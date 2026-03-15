# PlasmaFusionController

You are a coding agent working on PlasmaFusionController -- Create an advanced control system for plasma confinement in fusion reactors using real-time simulation and predictive modeling.

## Foundational Axiom

Existing approaches to create an advanced control system fail because they optimize for the common case while ignoring structural constraints; PlasmaFusionController makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Create an advanced control system for plasma confinement in fusion reactors using real-time simulati
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: PlasmaFusionController solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P5)
2. System Architecture Design for PlasmaFusionController (P4) -- (depends on: Requirements Gathering and Analysis)
3. Real-time Simulation Module Development (P3) -- (depends on: System Architecture Design)
4. Predictive Modeling Module Development (P3) -- (depends on: System Architecture Design)
5. User Interface Development (P3) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
7. Control System Development (P2) -- (depends on: Real-time Simulation Module Development, Predictive Modeling Module Development)
8. System Integration and Testing (P2) -- (depends on: Real-time Simulation Module Development, Predictive Modeling Module Development, Control System Development, User Interface Development, Database Design and Implementation)
9. Security Audit and Hardening (P2) -- (depends on: System Integration and Testing)
10. Deployment and Maintenance Planning (P2) -- (depends on: System Integration and Testing, Security Audit and Hardening)
11. Documentation and Training (P2) -- (depends on: System Integration and Testing, Deployment and Maintenance Planning)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlasmaFusionController can deliver its core value proposition as described
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
- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Create an advanced control system for plasma confinement in fusion reactors using real-time simulati.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
