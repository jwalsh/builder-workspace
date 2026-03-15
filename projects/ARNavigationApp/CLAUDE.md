# ARNavigationApp

You are a coding agent working on ARNavigationApp -- A mobile augmented reality app for intuitive navigation and location-based information display.

## Foundational Axiom

Existing approaches to mobile augmented reality app fail because they optimize for the common case while ignoring structural constraints; ARNavigationApp makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: data storage and management

## Anti-Goals

- **General-purpose platform**: ARNavigationApp solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Backend Development (P4) -- (depends on: Architecture Design)
4. User Interface and Experience Design (P3) -- (depends on: Project Planning and Requirements Gathering)
5. Frontend Development (P4) -- (depends on: Architecture Design, User Interface and Experience Design)
6. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development)
7. Security and Compliance (P4) -- (depends on: Architecture Design, Backend Development, Frontend Development)
8. Deployment and DevOps (P4) -- (depends on: Backend Development, Frontend Development, Testing and Quality Assurance)
9. Data Storage and Management (P3) -- (depends on: Architecture Design, Offline Functionality Consideration)
10. Documentation and User Support (P3) -- (depends on: User Interface and Experience Design, Backend Development, Frontend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ARNavigationApp can deliver its core value proposition as described
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
- TypeScript/JavaScript
- PostgreSQL
- MongoDB
- Redis
- Docker
- Kubernetes
- AWS
- GraphQL
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A mobile augmented reality app for intuitive navigation and location-based information display..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
