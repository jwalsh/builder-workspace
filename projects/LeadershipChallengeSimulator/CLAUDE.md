# LeadershipChallengeSimulator

You are a coding agent working on LeadershipChallengeSimulator -- A gamified platform that presents leaders with real-world business challenges to hone their decision-making skills.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; LeadershipChallengeSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: LeadershipChallengeSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for LeadershipChallengeSimulator (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
4. Backend Development (P4) -- (depends on: System Architecture Design, Database Design and Implementation)
5. Frontend Development (P4) -- (depends on: System Architecture Design)
6. Challenge Scenario Design and Development (P3) -- (depends on: Project Planning and Requirements Gathering)
7. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development, Challenge Scenario Design and Development)
8. Security and Compliance (P4) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation)
9. Deployment and DevOps (P5) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation, Testing and Quality Assurance, Security and Compliance)
10. Documentation and User Support (P3) -- (depends on: Project Planning and Requirements Gathering, Challenge Scenario Design and Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LeadershipChallengeSimulator can deliver its core value proposition as described
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
- GraphQL
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A gamified platform that presents leaders with real-world business challenges to hone their decision.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
