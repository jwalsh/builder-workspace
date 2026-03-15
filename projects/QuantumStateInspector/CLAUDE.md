# QuantumStateInspector

You are a coding agent working on QuantumStateInspector -- A system for observing and analyzing the state of quantum computers, providing insights into quantum decoherence and error correction processes.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumStateInspector co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system for observing and analyzing the state of quantum computers, providing insights into quantum
- User interface: define project requirements - updated
- Data layer: implement data analysis and visualization

## Anti-Goals

- **General-purpose platform**: QuantumStateInspector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements - Updated (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Develop Quantum Computer Interface (P3) -- (depends on: Design System Architecture)
4. Implement Data Analysis and Visualization (P3) -- (depends on: Design System Architecture)
5. Build User Interface and Reporting (P3) -- (depends on: Design System Architecture)
6. Implement Security and Access Control (P2) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
8. Conduct System Testing (P2) -- (depends on: Develop Quantum Computer Interface, Implement Data Analysis and Visualization, Build User Interface and Reporting, Implement Security and Access Control)
9. Document System and User Guides (P2) -- (depends on: Design System Architecture, Develop Quantum Computer Interface, Implement Data Analysis and Visualization, Build User Interface and Reporting)
10. Deploy and Maintain Production System (P1) -- (depends on: Conduct System Testing, Document System and User Guides)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumStateInspector can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for observing and analyzing the state of quantum computers, providing insights into quantum.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
