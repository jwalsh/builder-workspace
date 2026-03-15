# CrossPlatformAppFramework

You are a coding agent working on CrossPlatformAppFramework -- A framework for developing high-performance, cross-platform mobile applications with native capabilities.

## Foundational Axiom

Existing approaches to framework fail because they optimize for the common case while ignoring structural constraints; CrossPlatformAppFramework makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A framework for developing high-performance, cross-platform mobile applications with native capabili
- User interface: design and implement ui components

## Anti-Goals

- **General-purpose platform**: CrossPlatformAppFramework solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope (P1)
2. Design Cross-platform Architecture (P2) -- (depends on: Define Project Scope)
3. Draft Cross-platform Design Document (P3) -- (depends on: Design Cross-platform Architecture)
4. Create Core Libraries for Each Platform (P4) -- (depends on: Draft Cross-platform Design Document)
5. Implement Native Capabilities for Each Platform (P4) -- (depends on: Create Core Libraries for Each Platform)
6. Perform Unit Testing on Core Libraries (P5) -- (depends on: Implement Native Capabilities for Each Platform)
7. Design and Implement UI Components (P3) -- (depends on: Design Cross-platform Architecture)
8. Test UI Components Across Platforms (P5) -- (depends on: Design and Implement UI Components)
9. Refactor and Optimize Core Libraries (P4) -- (depends on: Perform Unit Testing on Core Libraries)
10. Integrate Core Libraries and UI Components (P2) -- (depends on: Refactor and Optimize Core Libraries, Test UI Components Across Platforms)
11. Prepare Documentation for CrossPlatformAppFramework (P2) -- (depends on: Integrate Core Libraries and UI Components)
12. Review Framework Design and Implementation (P1) -- (depends on: Integrate Core Libraries and UI Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossPlatformAppFramework can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A framework for developing high-performance, cross-platform mobile applications with native capabili.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
