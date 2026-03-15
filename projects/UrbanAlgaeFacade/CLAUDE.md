# UrbanAlgaeFacade

You are a coding agent working on UrbanAlgaeFacade -- Building facades integrated with algae bioreactors, producing oxygen, absorbing CO2, and generating biomass.

## Foundational Axiom

Existing approaches to building facades integrated with algae bioreactors, producin fail because they optimize for the common case while ignoring structural constraints; UrbanAlgaeFacade makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Building facades integrated with algae bioreactors, producing oxygen, absorbing CO2, and generating 

## Anti-Goals

- **General-purpose platform**: UrbanAlgaeFacade solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Concept Development (P1)
2. Algae Bioreactor Design (P3) -- (depends on: Design Concept Development)
3. Facade Structural Analysis (P4) -- (depends on: Design Concept Development)
4. System Integration Design (P5) -- (depends on: Algae Bioreactor Design, Facade Structural Analysis)
5. Material Selection (P2) -- (depends on: Design Concept Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: UrbanAlgaeFacade can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Building facades integrated with algae bioreactors, producing oxygen, absorbing CO2, and generating .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
