# DatabaseQueryOptimizer

You are a coding agent working on DatabaseQueryOptimizer -- A tool that challenges users to optimize database queries, teaching best practices in database management and performance tuning.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; DatabaseQueryOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project requirements
- Data layer: implement database

## Anti-Goals

- **General-purpose platform**: DatabaseQueryOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Develop Backend (P3) -- (depends on: Design System Architecture)
4. Develop Frontend (P3) -- (depends on: Design System Architecture)
5. Implement Database (P3) -- (depends on: Design System Architecture)
6. Write Documentation (P2) -- (depends on: Develop Backend, Develop Frontend)
7. Implement Testing (P2) -- (depends on: Develop Backend, Develop Frontend)
8. Secure the Application (P2) -- (depends on: Develop Backend, Develop Frontend)
9. Deploy to Production (P1) -- (depends on: Develop Backend, Develop Frontend, Implement Database, Write Documentation, Implement Testing, Secure the Application)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DatabaseQueryOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- MongoDB
- Docker
- Kubernetes
- GraphQL

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that challenges users to optimize database queries, teaching best practices in database manag.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
