# AdaptiveGoalAdjuster

You are a coding agent working on AdaptiveGoalAdjuster -- An AI system that helps employees and managers dynamically adjust goals based on changing circumstances and progress.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AdaptiveGoalAdjuster makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements - revised
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: AdaptiveGoalAdjuster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend User Interface (P3) -- (depends on: Design System Architecture)
4. Write User Documentation (P5) -- (depends on: Develop Frontend User Interface)
5. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
6. Develop Backend Services (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P4) -- (depends on: Develop Backend Services, Develop Frontend User Interface)
8. Conduct System Testing (P4) -- (depends on: Develop Backend Services, Develop Frontend User Interface)
9. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AdaptiveGoalAdjuster can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that helps employees and managers dynamically adjust goals based on changing circumstan.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
