# MindMeldSocialNetwork

You are a coding agent working on MindMeldSocialNetwork -- A social network that allows for direct mind-to-mind communication and emotion sharing among connected individuals.

## Foundational Axiom

Existing approaches to social network fail because they optimize for the common case while ignoring structural constraints; MindMeldSocialNetwork makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: requirements gathering and analysis
- Data layer: set up database schema

## Anti-Goals

- **General-purpose platform**: MindMeldSocialNetwork solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design MindMeldSocialNetwork Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
3. Develop Frontend Components (P3) -- (depends on: Design MindMeldSocialNetwork Architecture)
4. Develop Backend Services (P3) -- (depends on: Design MindMeldSocialNetwork Architecture)
5. Implement Emotion Detection and Sharing Features (P5) -- (depends on: Develop Frontend Components, Develop Backend Services)
6. Perform Security Audit and Implement Measures (P5) -- (depends on: Design MindMeldSocialNetwork Architecture)
7. Integration Testing and Quality Assurance (P5) -- (depends on: Implement Emotion Detection and Sharing Features)
8. Deploy MindMeldSocialNetwork Application (P5) -- (depends on: Perform Security Audit and Implement Measures, Integration Testing and Quality Assurance)
9. Set Up Database Schema (P4) -- (depends on: Design MindMeldSocialNetwork Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MindMeldSocialNetwork can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A social network that allows for direct mind-to-mind communication and emotion sharing among connect.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
