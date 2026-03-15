# FunctionalMacroSystem

You are a coding agent working on FunctionalMacroSystem -- A powerful macro system designed for functional languages, allowing for elegant metaprogramming and domain-specific language creation.

## Foundational Axiom

Existing approaches to powerful macro system designed fail because they optimize for the common case while ignoring structural constraints; FunctionalMacroSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A powerful macro system designed for functional languages, allowing for elegant metaprogramming and 
- User interface: requirements gathering for functionalmacrosystem

## Anti-Goals

- **General-purpose platform**: FunctionalMacroSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for FunctionalMacroSystem (P1)
2. Design Phase Initiation (P2) -- (depends on: Requirements Gathering)
3. Library Research and Selection (P3) -- (depends on: Design Phase Initiation)
4. Domain-Specific Language (DSL) Design (P4) -- (depends on: Design Phase Initiation)
5. Macro System Implementation (P5) -- (depends on: Library Research and Selection, Domain-Specific Language (DSL) Design)
6. Unit Testing (P2) -- (depends on: Macro System Implementation)
7. Integration Testing (P3) -- (depends on: Unit Testing)
8. Code Review and Refactoring (P4) -- (depends on: Macro System Implementation, Integration Testing)
9. Documentation Creation for FunctionalMacroSystem (P5) -- (depends on: Code Review and Refactoring)
10. Deployment Planning (P1) -- (depends on: Code Review and Refactoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalMacroSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A powerful macro system designed for functional languages, allowing for elegant metaprogramming and .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
