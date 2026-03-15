# CulturalIntelligenceTrainer

You are a coding agent working on CulturalIntelligenceTrainer -- An interactive training program that develops cultural intelligence for better collaboration in diverse and global teams.

## Foundational Axiom

Existing approaches to interactive training program fail because they optimize for the common case while ignoring structural constraints; CulturalIntelligenceTrainer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend and database
- User interface: define project scope and requirements
- Data layer: implement backend and database

## Anti-Goals

- **General-purpose platform**: CulturalIntelligenceTrainer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design User Interface and Experience (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Content and Learning Materials (P4) -- (depends on: Define Project Scope and Requirements)
4. Implement Backend and Database (P3) -- (depends on: Define Project Scope and Requirements)
5. Integrate Frontend and Backend (P3) -- (depends on: Design User Interface and Experience, Implement Backend and Database)
6. Set up Continuous Integration and Deployment (P3) -- (depends on: Implement Backend and Database, Integrate Frontend and Backend)
7. Conduct Security Audits and Compliance Checks (P3) -- (depends on: Implement Backend and Database, Integrate Frontend and Backend)
8. Develop Testing Strategy and Test Cases (P3) -- (depends on: Define Project Scope and Requirements)
9. Implement Gamification and Engagement Features (P2) -- (depends on: Integrate Frontend and Backend)
10. Conduct User Acceptance Testing (P2) -- (depends on: Develop Testing Strategy and Test Cases, Implement Gamification and Engagement Features)
11. Develop Documentation and User Guides (P2) -- (depends on: Develop Content and Learning Materials, Design User Interface and Experience)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CulturalIntelligenceTrainer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An interactive training program that develops cultural intelligence for better collaboration in dive.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
