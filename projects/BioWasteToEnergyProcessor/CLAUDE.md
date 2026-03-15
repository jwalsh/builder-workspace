# BioWasteToEnergyProcessor

You are a coding agent working on BioWasteToEnergyProcessor -- A system that efficiently converts various types of biological waste into usable energy and bio-products.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; BioWasteToEnergyProcessor maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: waste processing module
- User interface: project planning and requirements gathering
- Data layer: data management and analytics

## Anti-Goals

- **General-purpose platform**: BioWasteToEnergyProcessor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for BioWasteToEnergyProcessor (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Access Control (P5) -- (depends on: System Architecture Design, Data Handling and Storage)
4. Waste Processing Module (P3) -- (depends on: System Architecture Design)
5. Energy Conversion Module (P3) -- (depends on: System Architecture Design)
6. Bio-product Extraction Module (P3) -- (depends on: System Architecture Design)
7. Data Management and Analytics (P4) -- (depends on: System Architecture Design)
8. User Interface and Monitoring (P4) -- (depends on: System Architecture Design)
9. Integration and Testing (P5) -- (depends on: Waste Processing Module, Energy Conversion Module, Bio-product Extraction Module, Data Management and Analytics, User Interface and Monitoring, Security and Access Control)
10. Deployment and Maintenance (P5) -- (depends on: Integration and Testing)
11. Documentation and Training (P4) -- (depends on: System Architecture Design, Waste Processing Module, Energy Conversion Module, Bio-product Extraction Module, Data Management and Analytics, User Interface and Monitoring, Security and Access Control)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioWasteToEnergyProcessor can deliver its core value proposition as described
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

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that efficiently converts various types of biological waste into usable energy and bio-prod.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
