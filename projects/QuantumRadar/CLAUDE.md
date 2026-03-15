# QuantumRadar

You are a coding agent working on QuantumRadar -- Design a quantum radar system using entangled photons for ultra-sensitive detection of stealth objects and improved imaging.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumRadar co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: photon detection and processing
- User interface: project planning and requirements gathering for quantumradar
- Data layer: data analysis and visualization

## Anti-Goals

- **General-purpose platform**: QuantumRadar solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering for QuantumRadar (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Quantum Entanglement Module (P3) -- (depends on: System Architecture Design)
4. Photon Detection and Processing (P3) -- (depends on: System Architecture Design)
5. Data Analysis and Visualization (P3) -- (depends on: System Architecture Design)
6. Security and Compliance (P2) -- (depends on: System Architecture Design)
7. Testing and Validation (P2) -- (depends on: Quantum Entanglement Module, Photon Detection and Processing, Data Analysis and Visualization)
8. Deployment and Integration (P2) -- (depends on: Testing and Validation)
9. Documentation and User Guides (P2) -- (depends on: System Architecture Design, Testing and Validation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumRadar can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Design a quantum radar system using entangled photons for ultra-sensitive detection of stealth objec.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
