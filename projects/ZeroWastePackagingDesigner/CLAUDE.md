# ZeroWastePackagingDesigner

You are a coding agent working on ZeroWastePackagingDesigner -- An AI tool that designs packaging solutions with zero waste, using biodegradable or infinitely recyclable materials.

## Foundational Axiom

Existing approaches to ai tool fail because they optimize for the common case while ignoring structural constraints; ZeroWastePackagingDesigner makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI tool that designs packaging solutions with zero waste, using biodegradable or infinitely recyc
- User interface: design the user interface for ai model input
- Data layer: develop biodegradable and recyclable materials database

## Anti-Goals

- **General-purpose platform**: ZeroWastePackagingDesigner solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define the AI model architecture (P1)
2. Design the user interface for AI model input (P3) -- (depends on: Define the AI model architecture)
3. Develop biodegradable and recyclable materials database (P2)
4. Develop an algorithm for zero waste packaging design (P1) -- (depends on: Define the AI model architecture, Develop biodegradable and recyclable materials database)
5. Implement AI model for packaging design (P2) -- (depends on: Design the user interface for AI model input, Develop an algorithm for zero waste packaging design)
6. Test and refine AI model performance (P3) -- (depends on: Implement AI model for packaging design)
7. Document the project and AI model functionality (P5) -- (depends on: Test and refine AI model performance)
8. Review the project requirements and plan (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ZeroWastePackagingDesigner can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI tool that designs packaging solutions with zero waste, using biodegradable or infinitely recyc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
