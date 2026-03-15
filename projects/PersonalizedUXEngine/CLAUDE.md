# PersonalizedUXEngine

You are a coding agent working on PersonalizedUXEngine -- An engine that dynamically adjusts user interfaces based on individual user preferences and behavior patterns.

## Foundational Axiom

Existing approaches to engine fail because they optimize for the common case while ignoring structural constraints; PersonalizedUXEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design architecture of personalizeduxengine
- User interface: define project scope and requirements (revised)
- Data layer: establish database scheme for user data storage

## Anti-Goals

- **General-purpose platform**: PersonalizedUXEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design Architecture of PersonalizedUXEngine (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface for User Preferences Input (P3) -- (depends on: Design Architecture of PersonalizedUXEngine)
4. Implement Backend Logic for User Behavior Pattern Analysis (P3) -- (depends on: Design Architecture of PersonalizedUXEngine)
5. Establish Database Scheme for User Data Storage (P3) -- (depends on: Design Architecture of PersonalizedUXEngine)
6. Integrate Frontend with Backend and Database (P3) -- (depends on: Develop Frontend Interface for User Preferences Input, Implement Backend Logic for User Behavior Pattern Analysis, Establish Database Scheme for User Data Storage)
7. Write Test Cases for PersonalizedUXEngine Functionality (P4) -- (depends on: Integrate Frontend with Backend and Database)
8. Conduct Functional Testing of PersonalizedUXEngine (P4) -- (depends on: Write Test Cases for PersonalizedUXEngine Functionality)
9. Refactor and Optimize PersonalizedUXEngine as Needed (P5) -- (depends on: Conduct Functional Testing of PersonalizedUXEngine)
10. Document PersonalizedUXEngine Design and Implementation (P5) -- (depends on: Integrate Frontend with Backend and Database)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalizedUXEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An engine that dynamically adjusts user interfaces based on individual user preferences and behavior.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
