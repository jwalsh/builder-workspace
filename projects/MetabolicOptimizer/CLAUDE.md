# MetabolicOptimizer

You are a coding agent working on MetabolicOptimizer -- A system that analyzes individual metabolic profiles and provides personalized nutrition and exercise recommendations.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; MetabolicOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that analyzes individual metabolic profiles and provides personalized nutrition and exercis
- User interface: create user profile and data collection interface
- Data layer: create user profile and data collection interface

## Anti-Goals

- **General-purpose platform**: MetabolicOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Integrate Metabolic Profile Analysis Module (P4) -- (depends on: Define System Architecture)
3. Develop Recommendation Algorithm (P5) -- (depends on: Integrate Metabolic Profile Analysis Module)
4. Develop User Registration and Authentication (P2) -- (depends on: Define System Architecture)
5. Create User Profile and Data Collection Interface (P3) -- (depends on: Develop User Registration and Authentication)
6. Implement User Interface for Recommendations (P3) -- (depends on: Develop Recommendation Algorithm)
7. Perform Unit Tests for each Module (P4) -- (depends on: Develop User Registration and Authentication, Create User Profile and Data Collection Interface, Integrate Metabolic Profile Analysis Module, Develop Recommendation Algorithm, Implement User Interface for Recommendations)
8. Perform System Integration Tests (P5) -- (depends on: Perform Unit Tests for each Module)
9. Design and Implement Database Structure (P2) -- (depends on: Define System Architecture)
10. Document System Design and Implementation (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MetabolicOptimizer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that analyzes individual metabolic profiles and provides personalized nutrition and exercis.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
