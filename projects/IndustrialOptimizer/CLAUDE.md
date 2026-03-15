# IndustrialOptimizer

You are a coding agent working on IndustrialOptimizer -- Enable enterprises to scale faster, optimize their industrial operations in real time, and accelerate their digital transformation initiatives.

## Foundational Axiom

Existing approaches to enable enterprises fail because they optimize for the common case while ignoring structural constraints; IndustrialOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data ingestion and processing pipeline
- User interface: define project scope and requirements (revised)
- Data layer: develop data ingestion and processing pipeline

## Anti-Goals

- **General-purpose platform**: IndustrialOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P4)
2. Revised Design System Architecture for IndustrialOptimizer (P5) -- (depends on: Define Project Scope and Requirements, Identify Existing Systems and Integration Points)
3. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
4. Develop Data Ingestion and Processing Pipeline (P3) -- (depends on: Design System Architecture)
5. Implement Optimization Algorithms (P3) -- (depends on: Design System Architecture)
6. Build User Interface and Visualization Components (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
8. Conduct System Testing and Optimization (P2) -- (depends on: Develop Data Ingestion and Processing Pipeline, Implement Optimization Algorithms, Build User Interface and Visualization Components)
9. Prepare Documentation and Training Materials (P2) -- (depends on: Conduct System Testing and Optimization)
10. Deploy and Monitor the System (P1) -- (depends on: Conduct System Testing and Optimization, Prepare Documentation and Training Materials)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: IndustrialOptimizer can deliver its core value proposition as described
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

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Enable enterprises to scale faster, optimize their industrial operations in real time, and accelerat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to manufacturing engineers and production managers.
