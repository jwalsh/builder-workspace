# CollaborationNetworkMapper

You are a coding agent working on CollaborationNetworkMapper -- A system that maps out collaboration networks within the organization, identifying key connectors and potential silos.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; CollaborationNetworkMapper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that maps out collaboration networks within the organization, identifying key connectors an
- User interface: define project scope and requirements - revised
- Data layer: implement data ingestion pipeline

## Anti-Goals

- **General-purpose platform**: CollaborationNetworkMapper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Data Ingestion Pipeline (P3) -- (depends on: Design System Architecture)
4. Design and Implement Data Storage (P3) -- (depends on: Design System Architecture)
5. Develop Network Analysis Algorithms (P4) -- (depends on: Implement Data Ingestion Pipeline, Design and Implement Data Storage)
6. Build User Interface (P4) -- (depends on: Develop Network Analysis Algorithms)
7. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P4) -- (depends on: Implement Data Ingestion Pipeline, Design and Implement Data Storage, Develop Network Analysis Algorithms, Build User Interface, Implement Security and Access Controls)
9. Conduct System Testing (P5) -- (depends on: Set up Continuous Integration and Deployment)
10. Write Documentation (P5) -- (depends on: Conduct System Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CollaborationNetworkMapper can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that maps out collaboration networks within the organization, identifying key connectors an.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
