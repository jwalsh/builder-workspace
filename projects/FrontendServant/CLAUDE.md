# FrontendServant

You are a coding agent working on FrontendServant -- Implement the Backend for Frontend (BFF) pattern to load UI-ready data projections and enable event-driven UI updates.

## Foundational Axiom

Existing approaches to implement the backend fail because they optimize for the common case while ignoring structural constraints; FrontendServant makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: gather requirements and define architecture for backend for frontend (bff) implementation
- User interface: gather requirements and define architecture for backend for frontend (bff) implementation
- Data layer: design data projections

## Anti-Goals

- **General-purpose platform**: FrontendServant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements and Define Architecture for Backend for Frontend (BFF) Implementation (P5)
2. Design Data Projections (P4) -- (depends on: Gather Requirements and Define Architecture)
3. Implement BFF Layer (P3) -- (depends on: Gather Requirements and Define Architecture, Design Data Projections)
4. Set up Event-Driven Architecture (P3) -- (depends on: Gather Requirements and Define Architecture, Implement BFF Layer)
5. Integrate with Backend Services (P2) -- (depends on: Implement BFF Layer)
6. Implement UI Components (P2) -- (depends on: Design Data Projections, Set up Event-Driven Architecture)
7. Set up Testing and Deployment Pipelines (P2) -- (depends on: Implement BFF Layer, Implement UI Components)
8. Conduct Security Audits (P2) -- (depends on: Implement BFF Layer, Set up Event-Driven Architecture)
9. Write Documentation (P1) -- (depends on: Implement BFF Layer, Implement UI Components, Set up Event-Driven Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FrontendServant can deliver its core value proposition as described
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

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Implement the Backend for Frontend (BFF) pattern to load UI-ready data projections and enable event-.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
