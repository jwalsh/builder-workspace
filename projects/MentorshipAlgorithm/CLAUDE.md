# MentorshipAlgorithm

You are a coding agent working on MentorshipAlgorithm -- An AI-driven system that matches mentors and mentees based on skills, goals, personality traits, and availability.

## Foundational Axiom

Existing approaches to ai-driven system fail because they optimize for the common case while ignoring structural constraints; MentorshipAlgorithm makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-driven system that matches mentors and mentees based on skills, goals, personality traits, and
- User interface: define project requirements (revised)
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: MentorshipAlgorithm solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Document System (P4) -- (depends on: Define Project Requirements, Design System Architecture)
4. Design Database Schema (P3) -- (depends on: Design System Architecture)
5. Implement Authentication and Authorization (P3) -- (depends on: Design System Architecture)
6. Set up CI/CD Pipeline (P3)
7. Write Test Cases (P3) -- (depends on: Define Project Requirements)
8. Develop Matching Algorithm (P2) -- (depends on: Design System Architecture, Design Database Schema)
9. Build User Interface (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MentorshipAlgorithm can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-driven system that matches mentors and mentees based on skills, goals, personality traits, and.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
