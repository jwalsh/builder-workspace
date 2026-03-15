# QuantumRandomnessGenerator

You are a coding agent working on QuantumRandomnessGenerator -- A system that generates true random numbers using quantum processes for use in cryptography and security applications.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumRandomnessGenerator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement supporting services and infrastructure
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: QuantumRandomnessGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Research Quantum Random Number Generation Techniques (P3)
3. Design System Architecture for Quantum Randomness Generator (P3) -- (depends on: Define Project Scope and Requirements, Research Quantum Random Number Generation Techniques)
4. Implement Quantum Random Number Generation (P2) -- (depends on: Design System Architecture)
5. Develop Random Number Consumption Interface (P2) -- (depends on: Design System Architecture)
6. Implement Supporting Services and Infrastructure (P3) -- (depends on: Design System Architecture)
7. Write Documentation (P4) -- (depends on: Implement Quantum Random Number Generation, Develop Random Number Consumption Interface, Implement Supporting Services and Infrastructure)
8. Develop Test Suite (P3) -- (depends on: Implement Quantum Random Number Generation, Develop Random Number Consumption Interface, Implement Supporting Services and Infrastructure)
9. Conduct Security Audits (P2) -- (depends on: Implement Quantum Random Number Generation, Develop Random Number Consumption Interface, Implement Supporting Services and Infrastructure)
10. Deploy and Monitor (P1) -- (depends on: Conduct Security Audits, Develop Test Suite, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumRandomnessGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that generates true random numbers using quantum processes for use in cryptography and secu.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
