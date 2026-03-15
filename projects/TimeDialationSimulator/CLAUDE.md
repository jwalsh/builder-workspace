# TimeDialationSimulator

You are a coding agent working on TimeDialationSimulator -- A device that manipulates the perception of time, allowing users to subjectively slow down or speed up time for productivity or leisure.

## Foundational Axiom

Existing approaches to device fail because they optimize for the common case while ignoring structural constraints; TimeDialationSimulator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend functionality for time manipulation
- User interface: develop frontend interface for user interaction
- Data layer: integrate database for user data storage

## Anti-Goals

- **General-purpose platform**: TimeDialationSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design TimeDialationSimulator Concept (P1)
2. Research and Define TimeManipulation Algorithms (P2) -- (depends on: Design TimeDialationSimulator Concept)
3. Implement Backend Functionality for Time Manipulation (P4) -- (depends on: Research and Define TimeManipulation Algorithms)
4. Integrate Database for User Data Storage (P5) -- (depends on: Implement Backend Functionality for Time Manipulation)
5. Develop Frontend Interface for User Interaction (P3) -- (depends on: Design TimeDialationSimulator Concept)
6. Write Technical Documentation for TimeDialationSimulator (P4) -- (depends on: Implement Backend Functionality for Time Manipulation, Develop Frontend Interface for User Interaction)
7. Perform DevOps to Deploy and Test the System (P1) -- (depends on: Develop Frontend Interface for User Interaction, Implement Backend Functionality for Time Manipulation, Integrate Database for User Data Storage)
8. Address Security Concerns in TimeDialationSimulator (P3) -- (depends on: Perform DevOps to Deploy and Test the System)
9. Conduct Quality Assurance Testing (P2) -- (depends on: Perform DevOps to Deploy and Test the System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TimeDialationSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that manipulates the perception of time, allowing users to subjectively slow down or speed .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and media producers.
