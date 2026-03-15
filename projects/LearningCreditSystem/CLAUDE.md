# LearningCreditSystem

You are a coding agent working on LearningCreditSystem -- A program that allocates learning credits to employees, allowing them to choose and pursue courses or skills that interest them.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; LearningCreditSystem closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend functionality
- User interface: define project scope and requirements (revised)
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: LearningCreditSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (REVISED) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop User Interface (P4) -- (depends on: Design System Architecture)
4. Design Database Schema (P3) -- (depends on: Design System Architecture)
5. Implement Backend Functionality (P4) -- (depends on: Design System Architecture, Design Database Schema)
6. Perform Testing and Quality Assurance (P5) -- (depends on: Develop User Interface, Implement Backend Functionality)
7. Write User Documentation (P4) -- (depends on: Develop User Interface, Implement Backend Functionality)
8. Set up Continuous Integration and Deployment (P3)
9. Implement Security Measures (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LearningCreditSystem can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A program that allocates learning credits to employees, allowing them to choose and pursue courses o.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
