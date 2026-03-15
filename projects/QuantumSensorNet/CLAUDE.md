# QuantumSensorNet

You are a coding agent working on QuantumSensorNet -- Design a network of quantum sensors for ultra-precise measurements in applications ranging from navigation to medical imaging.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumSensorNet co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design data processing and analysis pipeline
- User interface: define project scope and requirements - updated
- Data layer: design data processing and analysis pipeline

## Anti-Goals

- **General-purpose platform**: QuantumSensorNet solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Updated (P5)
2. Implement Comprehensive Security Measures for QuantumSensorNet (P5) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
3. Design Quantum Sensor Architecture (P4) -- (depends on: Define Project Scope and Requirements)
4. Design Network Architecture and Communication Protocols (P4) -- (depends on: Define Project Scope and Requirements)
5. Design Data Processing and Analysis Pipeline (P4) -- (depends on: Define Project Scope and Requirements)
6. Develop Quantum Sensor Firmware and Software (P3) -- (depends on: Design Quantum Sensor Architecture)
7. Develop Network Infrastructure and Communication Software (P3) -- (depends on: Design Network Architecture and Communication Protocols)
8. Develop Data Processing and Analysis Software (P3) -- (depends on: Design Data Processing and Analysis Pipeline)
9. Design User Interfaces and Visualization Tools (P3) -- (depends on: Define Project Scope and Requirements)
10. Develop Testing and Validation Framework (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
11. Develop Deployment and Operations Strategies for QuantumSensorNet (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
12. Develop User Interfaces and Visualization Components (P2) -- (depends on: Design User Interfaces and Visualization Tools)
13. Integrate System Components (P2) -- (depends on: Develop Quantum Sensor Firmware and Software, Develop Network Infrastructure and Communication Software, Develop Data Processing and Analysis Software, Develop User Interfaces and Visualization Components)
14. Conduct System Testing and Validation (P2) -- (depends on: Integrate System Components, Develop Testing and Validation Framework)
15. Create Documentation and User Guides (P2) -- (depends on: Integrate System Components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumSensorNet can deliver its core value proposition as described
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

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Design a network of quantum sensors for ultra-precise measurements in applications ranging from navi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
