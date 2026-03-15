# SocietalHealthDashboard

You are a coding agent working on SocietalHealthDashboard -- A real-time analytics platform that measures and visualizes various indicators of societal health, from economic factors to social cohesion and collective well-being.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; SocietalHealthDashboard embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: real-time analytics engine
- User interface: project planning and requirements gathering
- Data layer: data modeling and database design

## Anti-Goals

- **General-purpose platform**: SocietalHealthDashboard solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Modeling and Database Design (P4) -- (depends on: System Architecture Design)
4. Security and Access Control (Updated) (P4) -- (depends on: System Architecture Design)
5. Data Ingestion and ETL Pipeline (P3) -- (depends on: System Architecture Design, Data Modeling and Database Design)
6. Real-time Analytics Engine (P3) -- (depends on: System Architecture Design, Data Modeling and Database Design)
7. Visualization and Reporting (P3) -- (depends on: System Architecture Design, Real-time Analytics Engine)
8. Continuous Integration and Deployment (CI/CD) (P3) -- (depends on: System Architecture Design, Code Quality Standards, Testing Strategy)
9. Testing and Quality Assurance (P3) -- (depends on: Data Ingestion and ETL Pipeline, Real-time Analytics Engine, Visualization and Reporting)
10. Documentation and User Guides (P2) -- (depends on: System Architecture Design, Data Ingestion and ETL Pipeline, Real-time Analytics Engine, Visualization and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SocietalHealthDashboard can deliver its core value proposition as described
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

- PostgreSQL
- MongoDB

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A real-time analytics platform that measures and visualizes various indicators of societal health, f.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
