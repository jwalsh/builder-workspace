# PortVisionX

You are a coding agent working on PortVisionX -- Eliminate data silos for global port terminals and inland logistics facilities, providing near-real-time visibility into operational and financial metrics.

## Foundational Axiom

Existing approaches to eliminate data silos fail because they optimize for the common case while ignoring structural constraints; PortVisionX makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Eliminate data silos for global port terminals and inland logistics facilities, providing near-real-
- User interface: project planning and requirements gathering
- Data layer: data integration and etl

## Anti-Goals

- **General-purpose platform**: PortVisionX solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. SystemArchitectureDesign-PortVisionX (P5) -- (depends on: ProjectPlanningandRequirementsGathering)
3. Data Integration and ETL (P3) -- (depends on: System Architecture Design)
4. Database Design and Implementation (P3) -- (depends on: System Architecture Design, Data Modeling and Requirements Analysis)
5. User Interface and Reporting (P3) -- (depends on: System Architecture Design)
6. Security and Access Control (v2) - Update for Review (P2) -- (depends on: System Architecture Design)
7. Deployment and DevOps (P2) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: System Architecture Design)
9. Documentation and Training (P1) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PortVisionX can deliver its core value proposition as described
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

- Redis
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Eliminate data silos for global port terminals and inland logistics facilities, providing near-real-.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
