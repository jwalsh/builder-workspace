# ClimateTwinEarth

You are a coding agent working on ClimateTwinEarth -- Develop a high-fidelity digital twin of Earth's climate system for accurate long-term climate change predictions and mitigation strategies.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; ClimateTwinEarth captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Develop a high-fidelity digital twin of Earth's climate system for accurate long-term climate change
- User interface: requirements gathering and analysis
- Data layer: data integration and management

## Anti-Goals

- **General-purpose platform**: ClimateTwinEarth solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design (P1) -- (depends on: Requirements Gathering and Analysis)
3. Climate Modeling and Simulation (P4) -- (depends on: System Architecture Design)
4. Data Integration and Management (P4) -- (depends on: System Architecture Design)
5. Visualization and User Interface (P4) -- (depends on: System Architecture Design)
6. Testing and Validation (P5) -- (depends on: Climate Modeling and Simulation, Data Integration and Management, Visualization and User Interface)
7. Deployment and Operations (P5) -- (depends on: Testing and Validation)
8. Security and Compliance (P4) -- (depends on: System Architecture Design)
9. Documentation and Training (P4) -- (depends on: Visualization and User Interface)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ClimateTwinEarth can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Develop a high-fidelity digital twin of Earth's climate system for accurate long-term climate change.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
