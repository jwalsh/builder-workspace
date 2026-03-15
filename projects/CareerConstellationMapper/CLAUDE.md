# CareerConstellationMapper

You are a coding agent working on CareerConstellationMapper -- A tool that maps out possible career paths within the organization, showing interconnections between different roles and departments.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; CareerConstellationMapper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: gather requirements
- Data layer: define data model for careerconstellationmapper

## Anti-Goals

- **General-purpose platform**: CareerConstellationMapper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Define Data Model for CareerConstellationMapper (P4) -- (depends on: Gather Requirements)
3. Develop Backend (P3) -- (depends on: Define Data Model)
4. Develop Frontend (P3) -- (depends on: Define Data Model)
5. Testing and Quality Assurance (P2) -- (depends on: Develop Backend, Develop Frontend)
6. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)
7. Implement Security with Enhancements for Improved Data Privacy (P1) -- (depends on: Develop Backend, Develop Frontend)
8. Documentation (P1) -- (depends on: Develop Backend, Develop Frontend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CareerConstellationMapper can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A tool that maps out possible career paths within the organization, showing interconnections between.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
