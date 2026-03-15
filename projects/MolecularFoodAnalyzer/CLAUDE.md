# MolecularFoodAnalyzer

You are a coding agent working on MolecularFoodAnalyzer -- A handheld device that instantly analyzes the molecular composition of food, detecting contaminants and nutritional content.

## Foundational Axiom

Existing approaches to handheld device fail because they optimize for the common case while ignoring structural constraints; MolecularFoodAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate ui with backend
- User interface: requirements gathering and analysis
- Data layer: database design

## Anti-Goals

- **General-purpose platform**: MolecularFoodAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design the User Interface (UI) (P2) -- (depends on: Requirements Gathering and Analysis)
3. Implement the UI (P4) -- (depends on: Design the User Interface (UI))
4. Design the Algorithm for Molecular Analysis (P3) -- (depends on: Requirements Gathering and Analysis)
5. Implement the Algorithm for Molecular Analysis (P4) -- (depends on: Design the Algorithm for Molecular Analysis)
6. Integrate UI with Backend (P5) -- (depends on: Implement the UI, Implement the Algorithm for Molecular Analysis)
7. Test the Functionality of Molecular Food Analyzer (P5) -- (depends on: Integrate UI with Backend)
8. Security Review (P5) -- (depends on: Integrate UI with Backend)
9. Deploy the MolecularFoodAnalyzer Device (P5) -- (depends on: Test the Functionality)
10. Database Design (P3) -- (depends on: Requirements Gathering and Analysis)
11. Design the Hardware Architecture (P2) -- (depends on: Requirements Gathering and Analysis)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MolecularFoodAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A handheld device that instantly analyzes the molecular composition of food, detecting contaminants .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
