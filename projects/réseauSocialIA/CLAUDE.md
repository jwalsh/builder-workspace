# réseauSocialIA

You are a coding agent working on réseauSocialIA -- Un réseau social intelligent qui propose des connexions et contenus basés sur les centres d'intérêts et le comportement utilisateur.

## Foundational Axiom

Existing approaches to un réseau social intelligent qui propose des connexions et c fail because they optimize for the common case while ignoring structural constraints; réseauSocialIA makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate frontend and backend components
- User interface: define user interface requirements
- Data layer: develop user data collection mechanisms

## Anti-Goals

- **General-purpose platform**: réseauSocialIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define User Interface Requirements (P3)
2. Design Machine Learning Model Architecture (P4) -- (depends on: Define User Interface Requirements)
3. Develop Machine Learning Algorithms (P5) -- (depends on: Design Machine Learning Model Architecture)
4. Integrate Frontend and Backend Components (P3) -- (depends on: Define User Interface Requirements, Develop Machine Learning Algorithms)
5. Develop User Data Collection Mechanisms (P2) -- (depends on: Design Machine Learning Model Architecture)
6. Perform Quality Assurance Testing (P2) -- (depends on: Integrate Frontend and Backend Components)
7. Develop User Authentication and Authorization Mechanisms (P1) -- (depends on: Define User Interface Requirements)
8. Write Technical Documentation (P1) -- (depends on: Integrate Frontend and Backend Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: réseauSocialIA can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un réseau social intelligent qui propose des connexions et contenus basés sur les centres d'intérêts.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
