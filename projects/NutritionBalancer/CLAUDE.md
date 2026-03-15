# NutritionBalancer

You are a coding agent working on NutritionBalancer -- An AI nutritionist that creates personalized meal plans based on individual health goals and preferences.

## Foundational Axiom

Existing approaches to ai nutritionist fail because they optimize for the common case while ignoring structural constraints; NutritionBalancer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for ai model integration
- User interface: define project requirements and scope (revised)
- Data layer: establish database schema and connect to backend services

## Anti-Goals

- **General-purpose platform**: NutritionBalancer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements and Scope (REVISED) (P1)
2. Design the NutritionBalancer Architecture (P2) -- (depends on: Define Project Requirements and Scope)
3. Create Frontend Components for User Interface (P3) -- (depends on: Design the NutritionBalancer Architecture)
4. Implement Backend Services for AI Model Integration (P3) -- (depends on: Design the NutritionBalancer Architecture)
5. Conduct Code Reviews and Provide Feedback (P5) -- (depends on: Create Frontend Components for User Interface, Implement Backend Services for AI Model Integration)
6. Prepare Documentation and Technical Writings (P5) -- (depends on: Define Project Requirements and Scope, Design the NutritionBalancer Architecture)
7. Implement Test Cases and Write Unit Tests for Backend Services (P4) -- (depends on: Implement Backend Services for AI Model Integration)
8. Establish Database Schema and Connect to Backend Services (P3) -- (depends on: Design the NutritionBalancer Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NutritionBalancer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI nutritionist that creates personalized meal plans based on individual health goals and prefere.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
