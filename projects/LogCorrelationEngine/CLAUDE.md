# LogCorrelationEngine

You are a coding agent working on LogCorrelationEngine -- A system that correlates logs from multiple sources to identify complex patterns and potential security incidents.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; LogCorrelationEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data ingestion and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data ingestion and preprocessing

## Anti-Goals

- **General-purpose platform**: LogCorrelationEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Data Ingestion and Preprocessing (P3) -- (depends on: System Architecture Design)
4. Log Correlation Engine (P3) -- (depends on: System Architecture Design)
5. Data Storage and Management (P3) -- (depends on: System Architecture Design)
6. User Interface and Reporting (P4) -- (depends on: System Architecture Design)
7. Security and Access Control (P4) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P4) -- (depends on: Data Ingestion and Preprocessing, Log Correlation Engine, Data Storage and Management, User Interface and Reporting, Security and Access Control)
9. Deployment and Monitoring (P5) -- (depends on: Testing and Quality Assurance)
10. Documentation and User Training (P5) -- (depends on: User Interface and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LogCorrelationEngine can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that correlates logs from multiple sources to identify complex patterns and potential secur.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
