# CorporateSkillQuest

You are a coding agent working on CorporateSkillQuest -- A gamified corporate training platform that turns skill development into an engaging, competitive adventure.

## Foundational Axiom

Existing approaches to gamified corporate training platform fail because they optimize for the common case while ignoring structural constraints; CorporateSkillQuest makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements - revised
- Data layer: set up database

## Anti-Goals

- **General-purpose platform**: CorporateSkillQuest solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P1)
2. Design System Architecture for CorporateSkillQuest (P1) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P3) -- (depends on: Design System Architecture)
5. Set up Database (P3) -- (depends on: Design System Architecture)
6. Create Documentation (P5) -- (depends on: Develop Frontend, Develop Backend, Set up Database)
7. Implement Security Measures (P4) -- (depends on: Develop Frontend, Develop Backend, Set up Database)
8. Set up Continuous Integration and Deployment (P4) -- (depends on: Develop Frontend, Develop Backend)
9. Conduct Testing and Quality Assurance (P4) -- (depends on: Develop Frontend, Develop Backend, Set up Database)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CorporateSkillQuest can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript
- PostgreSQL
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A gamified corporate training platform that turns skill development into an engaging, competitive ad.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to game developers and interactive media designers.
