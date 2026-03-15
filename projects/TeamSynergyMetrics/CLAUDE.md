# TeamSynergyMetrics

You are a coding agent working on TeamSynergyMetrics -- A dashboard that visualizes team collaboration patterns, communication effectiveness, and collective productivity.

## Foundational Axiom

Existing approaches to dashboard fail because they optimize for the common case while ignoring structural constraints; TeamSynergyMetrics makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: data modeling and database design

## Anti-Goals

- **General-purpose platform**: TeamSynergyMetrics solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Modeling and Database Design (P3) -- (depends on: Architecture Design)
4. Backend Development (P3) -- (depends on: Architecture Design, Data Modeling and Database Design)
5. Frontend Development (P3) -- (depends on: Architecture Design)
6. Security and Access Control (P3) -- (depends on: Architecture Design, Backend Development)
7. Data Integration and ETL (P2) -- (depends on: Data Modeling and Database Design, Backend Development)
8. Continuous Integration and Deployment (P2) -- (depends on: Backend Development, Frontend Development)
9. Testing and Quality Assurance (P2) -- (depends on: Backend Development, Frontend Development, Data Integration and ETL)
10. Documentation and User Guides (P2) -- (depends on: Backend Development, Frontend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeamSynergyMetrics can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A dashboard that visualizes team collaboration patterns, communication effectiveness, and collective.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
