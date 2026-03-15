# MachineLearningCodeLab

You are a coding agent working on MachineLearningCodeLab -- An interactive environment for learning machine learning concepts through coding exercises and real-world data sets.

## Foundational Axiom

Existing tools treat interactive environment as a generic automation problem; MachineLearningCodeLab succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements
- Data layer: set up data storage

## Anti-Goals

- **General-purpose platform**: MachineLearningCodeLab solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P3) -- (depends on: Design System Architecture)
5. Set up Data Storage (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P4) -- (depends on: Develop Frontend, Develop Backend, Set up Data Storage)
7. Implement Testing and Continuous Integration (P3) -- (depends on: Develop Frontend, Develop Backend)
8. Develop Machine Learning Exercises (P2) -- (depends on: Define Project Scope and Requirements)
9. Deploy and Monitor System (P2) -- (depends on: Develop Frontend, Develop Backend, Set up Data Storage, Implement Testing and Continuous Integration, Implement Security Measures)
10. Conduct User Testing and Feedback (P2) -- (depends on: Deploy and Monitor System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MachineLearningCodeLab can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An interactive environment for learning machine learning concepts through coding exercises and real-.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
