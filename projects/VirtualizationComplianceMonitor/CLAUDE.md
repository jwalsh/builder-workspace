# VirtualizationComplianceMonitor

You are a coding agent working on VirtualizationComplianceMonitor -- A system for ensuring compliance with industry regulations and standards in virtualized environments.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; VirtualizationComplianceMonitor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define system requirements
- Data layer: implement database structure

## Anti-Goals

- **General-purpose platform**: VirtualizationComplianceMonitor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements (P1)
2. Write Security Guidelines (P5) -- (depends on: Define System Requirements)
3. Design System Architecture (P2) -- (depends on: Define System Requirements)
4. Develop Frontend Interface (P3) -- (depends on: Define System Requirements, Design System Architecture)
5. Develop Backend Services (P3) -- (depends on: Define System Requirements, Design System Architecture)
6. Request Code Review (RFC) (P5) -- (depends on: Design System Architecture, Develop Frontend Interface, Develop Backend Services)
7. Write Functional Specifications (P2) -- (depends on: Define System Requirements)
8. Request Functional Specifications Review (RFC) (P5) -- (depends on: Write Functional Specifications)
9. Implement Database Structure (P4) -- (depends on: Define System Requirements, Design System Architecture)
10. Configure DevOps Pipeline (P4) -- (depends on: Define System Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualizationComplianceMonitor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for ensuring compliance with industry regulations and standards in virtualized environments.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
