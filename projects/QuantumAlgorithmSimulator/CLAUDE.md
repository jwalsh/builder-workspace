# QuantumAlgorithmSimulator

You are a coding agent working on QuantumAlgorithmSimulator -- A quantum computing simulator for testing and optimizing quantum algorithms before deployment on actual quantum hardware.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumAlgorithmSimulator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for quantum simulator
- User interface: design user interface for quantum simulator

## Anti-Goals

- **General-purpose platform**: QuantumAlgorithmSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Quantum Simulator Architecture (P1)
2. Implement Quantum Algorithm Libraries (P4) -- (depends on: Define Quantum Simulator Architecture)
3. Develop Test Cases for Quantum Algorithms (P5) -- (depends on: Implement Quantum Algorithm Libraries)
4. Develop Backend for Quantum Simulator (P3) -- (depends on: Define Quantum Simulator Architecture)
5. Perform Security Audit on Quantum Simulator (P3) -- (depends on: Develop Backend for Quantum Simulator)
6. Design User Interface for Quantum Simulator (P2) -- (depends on: Define Quantum Simulator Architecture)
7. Document Quantum Simulator Functionality and Usage (P2) -- (depends on: Design User Interface for Quantum Simulator)
8. Review and Optimize Existing Quantum Algorithms (P1) -- (depends on: Implement Quantum Algorithm Libraries)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumAlgorithmSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A quantum computing simulator for testing and optimizing quantum algorithms before deployment on act.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
