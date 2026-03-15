# QuantumRealitySimulator

You are a coding agent working on QuantumRealitySimulator -- A quantum computer-powered simulator capable of creating fully immersive, alternate reality experiences indistinguishable from actual reality.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumRealitySimulator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend for quantum computation
- User interface: define project scope and requirements
- Data layer: develop database for storing user profiles and settings

## Anti-Goals

- **General-purpose platform**: QuantumRealitySimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Develop Database for Storing User Profiles and Settings (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend for User Interaction (P3) -- (depends on: Define Project Scope and Requirements)
4. Design Quantum Algorithm for Simulating Reality (P2) -- (depends on: Define Project Scope and Requirements)
5. Implement Backend for Quantum Computation (P4) -- (depends on: Define Project Scope and Requirements, Design Quantum Algorithm for Simulating Reality)
6. Secure the QuantumRealitySimulator System (P5) -- (depends on: Develop Frontend for User Interaction, Implement Backend for Quantum Computation)
7. Test QuantumRealitySimulator for Functionality and Performance (P4) -- (depends on: Implement Frontend for User Interaction, Implement Backend for Quantum Computation)
8. Document the QuantumRealitySimulator (P3) -- (depends on: Implement Frontend for User Interaction, Implement Backend for Quantum Computation)
9. Perform DevOps Tasks for Deployment and Scaling (P2) -- (depends on: Define Project Scope and Requirements)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumRealitySimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A quantum computer-powered simulator capable of creating fully immersive, alternate reality experien.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
