# PetBehaviorAnalyzer

You are a coding agent working on PetBehaviorAnalyzer -- A machine learning system that analyzes pet behavior patterns to identify and address potential issues.

## Foundational Axiom

Existing approaches to machine learning system fail because they optimize for the common case while ignoring structural constraints; PetBehaviorAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for data processing and analysis
- User interface: define project requirements and scope - refined
- Data layer: develop pet behavior data collection strategy

## Anti-Goals

- **General-purpose platform**: PetBehaviorAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements and Scope - Refined (P1)
2. Develop Pet Behavior Data Collection Strategy (P2) -- (depends on: Define Project Requirements and Scope)
3. Create Frontend Interface for User Input and Analysis Results (P4) -- (depends on: Define Project Requirements and Scope, Develop Pet Behavior Data Collection Strategy)
4. Design Machine Learning Models for Behavior Analysis (P3) -- (depends on: Develop Pet Behavior Data Collection Strategy)
5. Implement Backend Services for Data Processing and Analysis (P4) -- (depends on: Define Project Requirements and Scope, Develop Pet Behavior Data Collection Strategy, Design Machine Learning Models for Behavior Analysis)
6. Document System Architecture and Workflow (P5) -- (depends on: Create Frontend Interface for User Input and Analysis Results, Implement Backend Services for Data Processing and Analysis)
7. Integrate Frontend with Backend Services (P4) -- (depends on: Create Frontend Interface for User Input and Analysis Results, Implement Backend Services for Data Processing and Analysis)
8. Develop Unit Tests for Each Functionality (P4) -- (depends on: Create Frontend Interface for User Input and Analysis Results, Implement Backend Services for Data Processing and Analysis)
9. Conduct Security Audit (P4) -- (depends on: Define Project Requirements and Scope)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PetBehaviorAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A machine learning system that analyzes pet behavior patterns to identify and address potential issu.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
