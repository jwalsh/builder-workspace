# NeuralSearchEngine

You are a coding agent working on NeuralSearchEngine -- A search engine interface that uses BCI to interpret and refine search queries based on user's thoughts.

## Foundational Axiom

Existing tools treat search engine interface as a generic automation problem; NeuralSearchEngine succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A search engine interface that uses BCI to interpret and refine search queries based on user's thoug
- User interface: requirements gathering and analysis
- Data layer: database design

## Anti-Goals

- **General-purpose platform**: NeuralSearchEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. BCI Interface Design (P2) -- (depends on: Requirements Gathering and Analysis)
3. BCI System Architecture Design (P3) -- (depends on: Requirements Gathering and Analysis)
4. BCI Algorithm Development (P4) -- (depends on: BCI System Architecture Design)
5. Database Design (P2) -- (depends on: BCI System Architecture Design)
6. Integration and Testing (P5) -- (depends on: BCI Interface Design, BCI Algorithm Development, Database Design)
7. User Acceptance Testing (UAT) (P4) -- (depends on: Integration and Testing)
8. Deployment and Launch (P5) -- (depends on: Integration and Testing, User Acceptance Testing (UAT))

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralSearchEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A search engine interface that uses BCI to interpret and refine search queries based on user's thoug.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
