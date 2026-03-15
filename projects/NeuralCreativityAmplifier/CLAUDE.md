# NeuralCreativityAmplifier

You are a coding agent working on NeuralCreativityAmplifier -- A system designed to enhance creative thinking by stimulating specific brain regions.

## Foundational Axiom

Existing tools treat system designed as a generic automation problem; NeuralCreativityAmplifier succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement the backend logic - rfc update
- User interface: requirements gathering
- Data layer: integrate database functionality - neuralcreativityamplifier

## Anti-Goals

- **General-purpose platform**: NeuralCreativityAmplifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering (P1)
2. Design the NeuralCreativityAmplifier System (P2) -- (depends on: Requirements Gathering)
3. Develop the Frontend Interface for NeuralCreativityAmplifier System (P3) -- (depends on: Design the NeuralCreativityAmplifier System)
4. Implement the Backend Logic - RFC Update (P3) -- (depends on: Design the NeuralCreativityAmplifier System)
5. Integrate Database Functionality - NeuralCreativityAmplifier (P4) -- (depends on: Design the NeuralCreativityAmplifier System)
6. Test the NeuralCreativityAmplifier System (P4) -- (depends on: Develop the Frontend Interface, Implement the Backend Logic, Integrate Database Functionality)
7. Deploy the NeuralCreativityAmplifier System (P5) -- (depends on: Test the NeuralCreativityAmplifier System)
8. Review and Approve Design Documents (P2) -- (depends on: Design the NeuralCreativityAmplifier System)
9. Review and Approve Requirements Document (P1) -- (depends on: Requirements Gathering)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralCreativityAmplifier can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system designed to enhance creative thinking by stimulating specific brain regions..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
