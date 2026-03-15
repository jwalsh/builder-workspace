# FunctionalReactiveUIFramework

You are a coding agent working on FunctionalReactiveUIFramework -- A reactive UI framework built on functional programming principles, emphasizing declarative UI descriptions and unidirectional data flow.

## Foundational Axiom

Existing approaches to reactive ui framework built on functional programming princi fail because they optimize for the common case while ignoring structural constraints; FunctionalReactiveUIFramework makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A reactive UI framework built on functional programming principles, emphasizing declarative UI descr
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: FunctionalReactiveUIFramework solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design the Architecture (P2) -- (depends on: Define Project Requirements)
3. Implement Core Functionalities (P3) -- (depends on: Design the Architecture)
4. Perform Code Review (P5) -- (depends on: Implement Core Functionalities)
5. Address Security Concerns (P5) -- (depends on: Implement Core Functionalities)
6. Create Test Cases (P4) -- (depends on: Implement Core Functionalities)
7. Deploy the Framework (P5) -- (depends on: Create Test Cases, Address Security Concerns)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalReactiveUIFramework can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A reactive UI framework built on functional programming principles, emphasizing declarative UI descr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
