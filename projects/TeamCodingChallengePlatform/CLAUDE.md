# TeamCodingChallengePlatform

You are a coding agent working on TeamCodingChallengePlatform -- A platform for organizing team-based coding challenges and hackathons, fostering collaboration and competitive spirit.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; TeamCodingChallengePlatform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform for organizing team-based coding challenges and hackathons, fostering collaboration and c
- User interface: define project scope and requirements (revised)
- Data layer: design database schema for teamcodingchallengeplatform

## Anti-Goals

- **General-purpose platform**: TeamCodingChallengePlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Define Security Requirements for TeamCodingChallengePlatform (P5) -- (depends on: Design System Architecture)
4. Plan DevOps and Deployment Strategy (P4) -- (depends on: Design System Architecture)
5. Design User Interface and Experience (P3) -- (depends on: Define Project Scope and Requirements)
6. Design Database Schema for TeamCodingChallengePlatform (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeamCodingChallengePlatform can deliver its core value proposition as described
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

- TypeScript/JavaScript
- PostgreSQL
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for organizing team-based coding challenges and hackathons, fostering collaboration and c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
