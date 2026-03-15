# FunctionalProgrammingDojo

You are a coding agent working on FunctionalProgrammingDojo -- An interactive learning environment focused on teaching functional programming concepts through hands-on exercises and challenges.

## Foundational Axiom

The bottleneck in interactive learning environment focused on teaching functio is not compute or data but the feedback loop between intent and artifact; FunctionalProgrammingDojo compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements (revised)
- Data layer: set up data storage

## Anti-Goals

- **General-purpose platform**: FunctionalProgrammingDojo solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture for FunctionalProgrammingDojo: Revised (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P3) -- (depends on: Design System Architecture)
5. Set up Data Storage (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P4) -- (depends on: Develop Frontend, Develop Backend, Set up Data Storage)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Develop Frontend, Develop Backend, Set up Data Storage)
8. Implement Exercise Content (P2) -- (depends on: Define Project Scope and Requirements)
9. Conduct Quality Assurance Testing (P3) -- (depends on: Develop Frontend, Develop Backend, Set up Data Storage, Implement Exercise Content)
10. Launch and Promote (P2) -- (depends on: Conduct Quality Assurance Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalProgrammingDojo can deliver its core value proposition as described
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

- MongoDB
- Redis
- Docker
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An interactive learning environment focused on teaching functional programming concepts through hand.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
