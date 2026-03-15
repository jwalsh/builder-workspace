# NeuralDataCompressor

You are a coding agent working on NeuralDataCompressor -- A system that compresses and stores large amounts of information in neural patterns for later retrieval.

## Foundational Axiom

Existing tools treat system as a generic automation problem; NeuralDataCompressor succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements (revised)
- Data layer: implement data storage and retrieval solutions

## Anti-Goals

- **General-purpose platform**: NeuralDataCompressor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design Overall System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Write Documentation for the Project (P5) -- (depends on: Design Overall System Architecture)
4. Implement Backend Services (P3) -- (depends on: Design Overall System Architecture)
5. Develop Compression Algorithms (P4) -- (depends on: Design Overall System Architecture)
6. Integrate Compression Algorithms into the System (P4) -- (depends on: Develop Compression Algorithms)
7. Perform Initial Testing and Integration Checks (P5) -- (depends on: Implement Frontend Interface, Implement Backend Services, Integrate Compression Algorithms into the System)
8. Implement Data Storage and Retrieval Solutions (P4) -- (depends on: Design Overall System Architecture)
9. Develop Frontend Interface (P3) -- (depends on: Design Overall System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralDataCompressor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TensorFlow
- PyTorch

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that compresses and stores large amounts of information in neural patterns for later retrie.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
