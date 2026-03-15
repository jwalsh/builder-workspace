# LegalExpertSystem

You are a coding agent working on LegalExpertSystem -- An expert system that provides preliminary legal advice and case assessments based on user inputs and legal databases.

## Foundational Axiom

Existing approaches to expert system fail because they optimize for the common case while ignoring structural constraints; LegalExpertSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design the backend architecture
- User interface: define system requirements and functionalities
- Data layer: establish database schema

## Anti-Goals

- **General-purpose platform**: LegalExpertSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements and Functionalities (P1)
2. Design the Backend Architecture (P2) -- (depends on: Define System Requirements and Functionalities)
3. Establish Database Schema (P3) -- (depends on: Design the Backend Architecture)
4. Implement Data Models and Queries (P3) -- (depends on: Establish Database Schema)
5. Develop the Reasoning Engine Algorithm (P4) -- (depends on: Design the Backend Architecture)
6. Design the User Interface (UI) (P2) -- (depends on: Define System Requirements and Functionalities)
7. Integrate User Interface with Backend (P4) -- (depends on: Design the User Interface, Implement Data Models and Queries, Develop the Reasoning Engine Algorithm)
8. Perform Unit Tests and Code Reviews (P5) -- (depends on: Implement Data Models and Queries, Develop the Reasoning Engine Algorithm, Integrate User Interface with Backend)
9. Write System Documentation (P5) -- (depends on: Define System Requirements and Functionalities, Integrate User Interface with Backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LegalExpertSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An expert system that provides preliminary legal advice and case assessments based on user inputs an.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
