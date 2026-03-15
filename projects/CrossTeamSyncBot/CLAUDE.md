# CrossTeamSyncBot

You are a coding agent working on CrossTeamSyncBot -- An AI bot that facilitates synchronization between different teams by managing cross-team communications and task alignments.

## Foundational Axiom

Existing approaches to ai bot fail because they optimize for the common case while ignoring structural constraints; CrossTeamSyncBot makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements (updated)
- Data layer: design database schema for crossteamsyncbot

## Anti-Goals

- **General-purpose platform**: CrossTeamSyncBot solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Updated) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements, Security Considerations)
3. Implement Security Measures (Update) (P4) -- (depends on: Design System Architecture)
4. Design User Interface - RFC (P3) -- (depends on: Define Project Scope and Requirements, Identify Target Platforms and Integrations)
5. Design Database Schema for CrossTeamSyncBot (P3) -- (depends on: Design System Architecture)
6. Implement Backend Services (P2) -- (depends on: Design System Architecture, Design Database Schema)
7. Implement User Interface (P2) -- (depends on: Design User Interface)
8. Create Test Suite (P3) -- (depends on: Implement Backend Services, Implement User Interface)
9. Set up CI/CD Pipeline (P2)
10. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Design User Interface, Design Database Schema)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossTeamSyncBot can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI bot that facilitates synchronization between different teams by managing cross-team communicat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
