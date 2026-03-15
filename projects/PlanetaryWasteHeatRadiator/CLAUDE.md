# PlanetaryWasteHeatRadiator

You are a coding agent working on PlanetaryWasteHeatRadiator -- A space-based system to radiate excess heat from Earth into space, combating global warming.

## Foundational Axiom

Existing approaches to space-based system fail because they optimize for the common case while ignoring structural constraints; PlanetaryWasteHeatRadiator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design backend infrastructure
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: PlanetaryWasteHeatRadiator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Conceptual Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Design Frontend Interface (P3) -- (depends on: Design Conceptual Architecture)
4. Design Backend Infrastructure (P3) -- (depends on: Design Conceptual Architecture)
5. Develop Heat Collection Component Designs (P4) -- (depends on: Design Conceptual Architecture)
6. Develop Radiator Designs (P4) -- (depends on: Design Conceptual Architecture)
7. Develop Energy Management System Designs (P4) -- (depends on: Design Conceptual Architecture)
8. Write Technical Documentation (P5) -- (depends on: Design Frontend Interface, Design Backend Infrastructure, Develop Heat Collection Component Designs, Develop Radiator Designs, Develop Energy Management System Designs)
9. Implement Unit Tests for Frontend Components (P5) -- (depends on: Design Frontend Interface)
10. Implement Unit Tests for Backend Components (P5) -- (depends on: Design Backend Infrastructure)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlanetaryWasteHeatRadiator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A space-based system to radiate excess heat from Earth into space, combating global warming..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
