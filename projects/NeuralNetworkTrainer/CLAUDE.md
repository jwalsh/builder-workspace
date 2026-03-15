# NeuralNetworkTrainer

You are a coding agent working on NeuralNetworkTrainer -- A BCI system that allows direct interaction with artificial neural networks for more intuitive AI training.

## Foundational Axiom

Existing tools treat bci system as a generic automation problem; NeuralNetworkTrainer succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A BCI system that allows direct interaction with artificial neural networks for more intuitive AI tr
- User interface: requirements gathering and analysis
- Data layer: implement database integration

## Anti-Goals

- **General-purpose platform**: NeuralNetworkTrainer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design Architecture and User Interface (P2) -- (depends on: Requirements Gathering and Analysis)
3. Develop BCI System Core Functionality (P3) -- (depends on: Design Architecture and User Interface)
4. Perform Unit Testing and Debugging (P5) -- (depends on: Develop BCI System Core Functionality)
5. Deploy and Conduct Initial Testing (P5) -- (depends on: Perform Unit Testing and Debugging)
6. Iterate and Improve Based on Feedback (P5) -- (depends on: Deploy and Conduct Initial Testing)
7. Implement Database Integration (P4) -- (depends on: Develop BCI System Core Functionality)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralNetworkTrainer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A BCI system that allows direct interaction with artificial neural networks for more intuitive AI tr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
