# BioremediationNanobot

You are a coding agent working on BioremediationNanobot -- Engineered nanobots that use biological processes to clean up environmental contaminants in soil and water.

## Foundational Axiom

Existing approaches to engineered nanobots fail because they optimize for the common case while ignoring structural constraints; BioremediationNanobot makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement nanobot software
- User interface: define project requirements
- Data layer: establish data management and analysis

## Anti-Goals

- **General-purpose platform**: BioremediationNanobot solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design Nanobot Architecture (P4) -- (depends on: Define Project Requirements)
3. Implement Nanobot Software (P3) -- (depends on: Design Nanobot Architecture)
4. Develop Monitoring and Control System (P3) -- (depends on: Design Nanobot Architecture)
5. Establish Data Management and Analysis (P3) -- (depends on: Design Nanobot Architecture)
6. Conduct Simulations and Testing (P2) -- (depends on: Implement Nanobot Software, Develop Monitoring and Control System, Establish Data Management and Analysis)
7. Develop Deployment and Maintenance Procedures (P2) -- (depends on: Conduct Simulations and Testing)
8. Implement Security Measures (P2) -- (depends on: Implement Nanobot Software, Develop Monitoring and Control System)
9. Create Documentation and Training Materials (P1) -- (depends on: Develop Deployment and Maintenance Procedures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioremediationNanobot can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Engineered nanobots that use biological processes to clean up environmental contaminants in soil and.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and media producers.
