# FoodSynthesizer

You are a coding agent working on FoodSynthesizer -- A device that can synthesize meals from base molecules, allowing for instant creation of any dish with perfect nutritional balance.

## Foundational Axiom

Existing approaches to device fail because they optimize for the common case while ignoring structural constraints; FoodSynthesizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: document user manual and api reference for foodsynthesizer
- User interface: develop user interface for selection and ordering
- Data layer: implement base molecule storage system

## Anti-Goals

- **General-purpose platform**: FoodSynthesizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Base Molecule Libraries (P1)
2. Design Meal Synthesis Algorithms (P2) -- (depends on: Define Base Molecule Libraries)
3. Implement Base Molecule Storage System (P3) -- (depends on: Define Base Molecule Libraries)
4. Implement Meal Synthesis System (P5) -- (depends on: Design Meal Synthesis Algorithms, Implement Base Molecule Storage System)
5. Perform Unit Tests for Synthesis System (P4) -- (depends on: Implement Meal Synthesis System)
6. Integration Tests for Complete System (P5) -- (depends on: Perform Unit Tests for Synthesis System)
7. Develop User Interface for Selection and Ordering (P4) -- (depends on: Design Meal Synthesis Algorithms)
8. Create Recipe Database (P3) -- (depends on: Design Meal Synthesis Algorithms)
9. Document User Manual and API Reference for FoodSynthesizer (P3)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FoodSynthesizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that can synthesize meals from base molecules, allowing for instant creation of any dish wi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
