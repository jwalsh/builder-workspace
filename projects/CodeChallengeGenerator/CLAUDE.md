# CodeChallengeGenerator

You are a coding agent working on CodeChallengeGenerator -- An AI system that generates unique coding challenges based on specified difficulty levels, topics, and learning objectives.

## Foundational Axiom

The bottleneck in ai system is not compute or data but the feedback loop between intent and artifact; CodeChallengeGenerator compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that generates unique coding challenges based on specified difficulty levels, topics, a
- User interface: define project scope and requirements
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: CodeChallengeGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Set up Development Environment (P3) -- (depends on: Design System Architecture)
5. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)
6. Write Documentation (P3) -- (depends on: Design System Architecture)
7. Set up Testing Framework (P3) -- (depends on: Design System Architecture)
8. Implement Challenge Generation Logic (P2) -- (depends on: Design System Architecture)
9. Design and Implement User Interface (P2) -- (depends on: Design System Architecture)
10. Deploy and Monitor System (P2) -- (depends on: Implement Challenge Generation Logic, Design and Implement User Interface, Set up Database and Data Storage, Implement Security Measures, Write Documentation, Set up Testing Framework)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeChallengeGenerator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that generates unique coding challenges based on specified difficulty levels, topics, a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
