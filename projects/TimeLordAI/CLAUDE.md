# TimeLordAI

You are a coding agent working on TimeLordAI -- Build end-to-end managed time series workflows for forecasting that can be applied across various use cases and industries.

## Foundational Axiom

Existing approaches to build end-to-end managed time series workflows for forecasting fail because they optimize for the common case while ignoring structural constraints; TimeLordAI makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: define data ingestion and processing pipeline
- User interface: refine project scope and requirements for timelordai
- Data layer: define data ingestion and processing pipeline

## Anti-Goals

- **General-purpose platform**: TimeLordAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Refine Project Scope and Requirements for TimeLordAI (P5)
2. Design System Architecture - Revised (P5) -- (depends on: Define Project Scope and Requirements)
3. Define Data Ingestion and Processing Pipeline (P3) -- (depends on: Design System Architecture)
4. Develop Forecasting Models (P3) -- (depends on: Define Data Ingestion and Processing Pipeline)
5. Build User Interface and Visualization (P3) -- (depends on: Design System Architecture)
6. Implement Model Management and Deployment (P3) -- (depends on: Develop Forecasting Models)
7. Set up Infrastructure and DevOps (P2) -- (depends on: Design System Architecture)
8. Implement Security and Compliance (P2) -- (depends on: Design System Architecture)
9. Develop Comprehensive Testing and Quality Assurance Strategy (P2) -- (depends on: Define Project Scope and Requirements)
10. Write Documentation and User Guides (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TimeLordAI can deliver its core value proposition as described
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

- Python
- PostgreSQL
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Build end-to-end managed time series workflows for forecasting that can be applied across various us.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
