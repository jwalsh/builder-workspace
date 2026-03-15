# AdaptiveLearningPathCreator

You are a coding agent working on AdaptiveLearningPathCreator -- An AI-driven system that creates personalized learning paths for users based on their goals, current skills, and performance on coding challenges.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; AdaptiveLearningPathCreator closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-driven system that creates personalized learning paths for users based on their goals, current
- User interface: define project requirements
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: AdaptiveLearningPathCreator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Requirements)
3. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
4. Develop User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
6. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
7. Create Test Suite and Test Plan (P3) -- (depends on: Design System Architecture)
8. Write Technical Documentation (P3) -- (depends on: Design System Architecture)
9. Implement Adaptive Learning Algorithm (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AdaptiveLearningPathCreator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-driven system that creates personalized learning paths for users based on their goals, current.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
