# ThoughtToTextTranslator

You are a coding agent working on ThoughtToTextTranslator -- A BCI system that translates thought patterns into written text, enabling communication for individuals with speech impairments.

## Foundational Axiom

Existing approaches to bci system fail because they optimize for the common case while ignoring structural constraints; ThoughtToTextTranslator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop brain signal processing algorithms
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: ThoughtToTextTranslator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design BCI System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Brain Signal Processing Algorithms (P3) -- (depends on: Design BCI System Architecture)
4. Design User Interface (P4) -- (depends on: Define Project Scope and Requirements)
5. Implement BCI System (P5) -- (depends on: Design BCI System Architecture, Develop Brain Signal Processing Algorithms, Design User Interface)
6. Test ThoughtToTextTranslator System (P5) -- (depends on: Implement BCI System)
7. Document ThoughtToTextTranslator System - Detailed Technical Documentation (P5) -- (depends on: Implement BCI System)
8. Develop Text Generation Module (P3) -- (depends on: Develop Brain Signal Processing Algorithms)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThoughtToTextTranslator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A BCI system that translates thought patterns into written text, enabling communication for individu.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
