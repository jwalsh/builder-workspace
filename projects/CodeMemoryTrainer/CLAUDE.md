# CodeMemoryTrainer

You are a coding agent working on CodeMemoryTrainer -- A spaced repetition system designed to help users memorize and internalize important coding patterns and concepts.

## Foundational Axiom

The bottleneck in spaced repetition system designed is not compute or data but the feedback loop between intent and artifact; CodeMemoryTrainer compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements
- Data layer: design database schema

## Anti-Goals

- **General-purpose platform**: CodeMemoryTrainer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Design Database Schema (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P2) -- (depends on: Design System Architecture, Design Database Schema)
5. Develop Frontend (P2) -- (depends on: Design System Architecture)
6. Conduct Security Audits (P4) -- (depends on: Develop Backend, Develop Frontend)
7. Implement Spaced Repetition Algorithm (P3) -- (depends on: Develop Backend)
8. Set up Continuous Integration and Deployment (P3) -- (depends on: Develop Backend, Develop Frontend)
9. Write Documentation (P2) -- (depends on: Develop Backend, Develop Frontend)
10. Perform Testing and Quality Assurance (P2) -- (depends on: Develop Backend, Develop Frontend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeMemoryTrainer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A spaced repetition system designed to help users memorize and internalize important coding patterns.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
