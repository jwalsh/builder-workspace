# PhilosophicalMemeGenerator

You are a coding agent working on PhilosophicalMemeGenerator -- An AI system that creates and disseminates philosophical memes, making complex ideas more accessible and engaging for a broader audience.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; PhilosophicalMemeGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that creates and disseminates philosophical memes, making complex ideas more accessible
- User interface: define project scope and requirements (revised)

## Anti-Goals

- **General-purpose platform**: PhilosophicalMemeGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Meme Generation Module (P3) -- (depends on: Design System Architecture)
4. Build Content Management System (P3) -- (depends on: Design System Architecture)
5. Implement Distribution Channels (P3) -- (depends on: Design System Architecture)
6. Develop User Interface (P2) -- (depends on: Build Content Management System)
7. Implement Security Measures (P2) -- (depends on: Design System Architecture)
8. Set up Testing and Quality Assurance (P2) -- (depends on: Develop Meme Generation Module, Build Content Management System, Implement Distribution Channels, Develop User Interface)
9. Write Documentation and User Guides (P2) -- (depends on: Develop User Interface)
10. Deploy and Monitor System (P1) -- (depends on: Set up Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PhilosophicalMemeGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that creates and disseminates philosophical memes, making complex ideas more accessible.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
