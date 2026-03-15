# StranglerFig

You are a coding agent working on StranglerFig -- Break monoliths confidently using a parallel run strategy. Compare responses between legacy systems and new microservices to ensure smooth transitions.

## Foundational Axiom

Existing approaches to break monoliths confidently using a parallel run strategy. c fail because they optimize for the common case while ignoring structural constraints; StranglerFig makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: parallel run strategy for microservices integration
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: StranglerFig solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Architecture Design for StranglerFig Project (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Parallel Run Strategy for Microservices Integration (P3) -- (depends on: Architecture Design)
4. Microservice Development (P4) -- (depends on: Architecture Design, Parallel Run Strategy)
5. Testing and Validation (P4) -- (depends on: Microservice Development, Parallel Run Strategy)
6. Security and Compliance (P4) -- (depends on: Microservice Development)
7. Deployment and Monitoring (P5) -- (depends on: Microservice Development, Testing and Validation, Security and Compliance)
8. Documentation and Training (P5) -- (depends on: Microservice Development, Deployment and Monitoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: StranglerFig can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Break monoliths confidently using a parallel run strategy. Compare responses between legacy systems .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
