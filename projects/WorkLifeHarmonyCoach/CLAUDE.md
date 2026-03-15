# WorkLifeHarmonyCoach

You are a coding agent working on WorkLifeHarmonyCoach -- An AI coach that helps users achieve better work-life balance through personalized scheduling and habit formation.

## Foundational Axiom

Existing approaches to ai coach fail because they optimize for the common case while ignoring structural constraints; WorkLifeHarmonyCoach makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI coach that helps users achieve better work-life balance through personalized scheduling and ha
- User interface: define user interface requirements

## Anti-Goals

- **General-purpose platform**: WorkLifeHarmonyCoach solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Develop AI Scheduling Algorithm (P5)
2. Develop Habit Formation Module (P4)
3. Define User Interface Requirements (P3)
4. Design the User Interface (P2) -- (depends on: Define User Interface Requirements)
5. Integrate User Interface with AI Modules (P1) -- (depends on: Design the User Interface, Develop AI Scheduling Algorithm, Develop Habit Formation Module)
6. Perform Unit Testing (P2) -- (depends on: Develop AI Scheduling Algorithm, Develop Habit Formation Module, Integrate User Interface with AI Modules)
7. Perform System Integration Testing (P1) -- (depends on: Perform Unit Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WorkLifeHarmonyCoach can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI coach that helps users achieve better work-life balance through personalized scheduling and ha.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
