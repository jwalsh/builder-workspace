# CodeOptimizer

You are a coding agent working on CodeOptimizer -- An AI system that analyzes and optimizes existing codebases for performance, readability, and maintainability, suggesting refactoring opportunities and implementing approved changes.

## Foundational Axiom

The bottleneck in ai system is not compute or data but the feedback loop between intent and artifact; CodeOptimizer compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that analyzes and optimizes existing codebases for performance, readability, and mainta
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: CodeOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Code Analysis and Parsing Module (P3) -- (depends on: Design System Architecture)
5. Implement Optimization Algorithms (P3) -- (depends on: Design System Architecture)
6. Build Refactoring Tools (P3) -- (depends on: Design System Architecture)
7. Develop Test Suite (P3) -- (depends on: Design System Architecture)
8. Develop User Interface (P2) -- (depends on: Design System Architecture)
9. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
10. Write Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that analyzes and optimizes existing codebases for performance, readability, and mainta.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
