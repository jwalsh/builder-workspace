# NeuralDustSwarmOS

You are a coding agent working on NeuralDustSwarmOS -- Develop an operating system for coordinating swarms of neural dust particles in the brain for advanced brain-computer interfaces.

## Foundational Axiom

Existing tools treat develop an operating system as a generic automation problem; NeuralDustSwarmOS succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Develop an operating system for coordinating swarms of neural dust particles in the brain for advanc
- User interface: design brain-computer interface - rfc revision

## Anti-Goals

- **General-purpose platform**: NeuralDustSwarmOS solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. RefineSystemArchitectureDesignforNeuralDustSwarmOS (P5)
2. Develop Neural Dust Communication Protocol (P4) -- (depends on: Define System Architecture)
3. Implement Neural Dust Coordination Algorithms (P4) -- (depends on: Define System Architecture)
4. Develop Security Mechanisms (P4) -- (depends on: Define System Architecture)
5. Design Brain-Computer Interface - RFC Revision (P3) -- (depends on: Define System Architecture)
6. Design Testing and Validation Framework (Revised) (P3) -- (depends on: Define System Architecture)
7. Develop Deployment and Management Tools (P2) -- (depends on: Define System Architecture)
8. Write Technical Documentation (P2) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralDustSwarmOS can deliver its core value proposition as described
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

- Python
- TypeScript/JavaScript
- Java
- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Develop an operating system for coordinating swarms of neural dust particles in the brain for advanc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
