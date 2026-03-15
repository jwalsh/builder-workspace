# EmergingTechExplorer

You are a coding agent working on EmergingTechExplorer -- A research tool for identifying and analyzing emerging technologies across various industries.

## Foundational Axiom

Existing approaches to research tool fail because they optimize for the common case while ignoring structural constraints; EmergingTechExplorer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend infrastructure for data collection
- User interface: project planning and requirements gathering
- Data layer: develop the backend infrastructure for data collection

## Anti-Goals

- **General-purpose platform**: EmergingTechExplorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Research and Identify Emerging Technologies (Updated) (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Design the User Interface (UI) of EmergingTechExplorer (P3) -- (depends on: Research and Identify Emerging Technologies)
4. Develop the Backend Infrastructure for Data Collection (P4) -- (depends on: Research and Identify Emerging Technologies)
5. Integrate the UI with the Backend Services (P5) -- (depends on: Design the User Interface (UI) of EmergingTechExplorer, Develop the Backend Infrastructure for Data Collection)
6. Database Design and Implementation (P4) -- (depends on: Research and Identify Emerging Technologies)
7. Implement Data Analysis Algorithms (P5) -- (depends on: Database Design and Implementation)
8. Quality Assurance (QA) Testing (P3) -- (depends on: Integrate the UI with the Backend Services, Implement Data Analysis Algorithms)
9. Deploy EmergingTechExplorer to Production Environment (P2) -- (depends on: Quality Assurance (QA) Testing)
10. Document and Publish User Guides (P1) -- (depends on: Deploy EmergingTechExplorer to Production Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmergingTechExplorer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A research tool for identifying and analyzing emerging technologies across various industries..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
