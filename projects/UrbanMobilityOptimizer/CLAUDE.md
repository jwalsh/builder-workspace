# UrbanMobilityOptimizer

You are a coding agent working on UrbanMobilityOptimizer -- A system that integrates various transportation modes to optimize urban mobility and reduce congestion.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; UrbanMobilityOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that integrates various transportation modes to optimize urban mobility and reduce congesti
- User interface: design user interface
- Data layer: establish database schema

## Anti-Goals

- **General-purpose platform**: UrbanMobilityOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Establish Database Schema (P5) -- (depends on: Define System Architecture)
3. Design User Interface (P4) -- (depends on: Define System Architecture)
4. Develop Congestion Reduction Algorithms (P3) -- (depends on: Define System Architecture)
5. Implement DevOps Strategy (P1) -- (depends on: Define System Architecture)
6. Write Technical Documentation (P3) -- (depends on: Implement DevOps Strategy)
7. Integrate Multimodal Transportation Modes (P2) -- (depends on: Define System Architecture)
8. Perform Quality Assurance Testing (P2) -- (depends on: Implement DevOps Strategy)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: UrbanMobilityOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that integrates various transportation modes to optimize urban mobility and reduce congesti.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
