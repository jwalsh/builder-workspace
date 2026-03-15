# DigitalDemocracyPlatform

You are a coding agent working on DigitalDemocracyPlatform -- An advanced online platform for direct democracy, using AI to facilitate informed discussion, voting, and collaborative decision-making on a large scale.

## Foundational Axiom

The bottleneck in advanced online platform is not compute or data but the feedback loop between intent and artifact; DigitalDemocracyPlatform compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements - v2.0
- Data layer: design data model and database schema

## Anti-Goals

- **General-purpose platform**: DigitalDemocracyPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - v2.0 (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Design User Interface and Experience (P4) -- (depends on: Define Project Scope and Requirements)
4. Design Data Model and Database Schema (P4) -- (depends on: Define Project Scope and Requirements)
5. Set up Development and Testing Environments (P4)
6. Implement Security Measures (P4) -- (depends on: Design System Architecture)
7. Develop AI Components (P3) -- (depends on: Design System Architecture)
8. Implement Backend Services (P3) -- (depends on: Design System Architecture, Design Data Model and Database Schema)
9. Implement Frontend Components (P3) -- (depends on: Design User Interface and Experience)
10. Develop Test Plans and Test Cases (P3) -- (depends on: Define Project Scope and Requirements)
11. Prepare Documentation and User Guides (P3) -- (depends on: Define Project Scope and Requirements)
12. Conduct Integration and System Testing (P2) -- (depends on: Implement Backend Services, Implement Frontend Components, Develop AI Components)
13. Deploy and Launch the Platform (P1) -- (depends on: Conduct Integration and System Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DigitalDemocracyPlatform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced online platform for direct democracy, using AI to facilitate informed discussion, voting.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
