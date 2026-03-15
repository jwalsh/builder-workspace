# PureFunctionalGameEngine

You are a coding agent working on PureFunctionalGameEngine -- A game engine designed with pure functions and immutable state, exploring new approaches to game logic and rendering.

## Foundational Axiom

Existing approaches to game engine designed with pure functions and immutable state fail because they optimize for the common case while ignoring structural constraints; PureFunctionalGameEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A game engine designed with pure functions and immutable state, exploring new approaches to game log

## Anti-Goals

- **General-purpose platform**: PureFunctionalGameEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Architectural Design (P1)
2. Implement Core Functional Game Logic (P2) -- (depends on: Define Architectural Design)
3. Design Game Rendering using Functional Approach (P3) -- (depends on: Define Architectural Design)
4. Write Technical Documentation (P4) -- (depends on: Implement Core Functional Game Logic, Design Game Rendering using Functional Approach)
5. Review Technical Documentation Draft (P5) -- (depends on: Write Technical Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PureFunctionalGameEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A game engine designed with pure functions and immutable state, exploring new approaches to game log.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to game developers and interactive media designers.
