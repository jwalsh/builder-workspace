# MoralCompassApp

You are a coding agent working on MoralCompassApp -- A mobile application that helps users make ethical decisions by analyzing situations and providing guidance based on ethical theories.

## Foundational Axiom

Existing approaches to mobile application fail because they optimize for the common case while ignoring structural constraints; MoralCompassApp makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A mobile application that helps users make ethical decisions by analyzing situations and providing g
- User interface: requirement gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: MoralCompassApp solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirement Gathering and Analysis (P1)
2. Develop Ethical Decision Algorithm (P3) -- (depends on: Requirement Gathering and Analysis)
3. Design the User Interface (UI) (P2) -- (depends on: Requirement Gathering and Analysis)
4. Create Unit and Integration Tests (P5) -- (depends on: Develop Ethical Decision Algorithm, Design the User Interface)
5. Deploy and Test in Staging Environment (P2) -- (depends on: Develop Ethical Decision Algorithm, Design the User Interface, Create Unit and Integration Tests)
6. Write Documentation for Developers and Users (P5) -- (depends on: Deploy and Test in Staging Environment)
7. Database Design and Implementation (P4) -- (depends on: Develop Ethical Decision Algorithm)
8. Review Code for Quality and Security (P4) -- (depends on: Deploy and Test in Staging Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MoralCompassApp can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A mobile application that helps users make ethical decisions by analyzing situations and providing g.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
