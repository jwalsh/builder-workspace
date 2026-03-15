# AlgaeBiofuelFarm

You are a coding agent working on AlgaeBiofuelFarm -- An optimized system for cultivating algae and efficiently converting it into biofuel.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; AlgaeBiofuelFarm embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An optimized system for cultivating algae and efficiently converting it into biofuel.
- User interface: revised requirements gathering and analysis
- Data layer: data management and analytics

## Anti-Goals

- **General-purpose platform**: AlgaeBiofuelFarm solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Revised Requirements Gathering and Analysis (P5)
2. System Architecture Design (P4) -- (depends on: Requirements Gathering and Analysis)
3. Cultivation Subsystem (P3) -- (depends on: System Architecture Design)
4. Conversion Subsystem (P3) -- (depends on: System Architecture Design)
5. Optimization Subsystem (P3) -- (depends on: System Architecture Design)
6. Data Management and Analytics (P3) -- (depends on: System Architecture Design)
7. User Interface and Monitoring (P2) -- (depends on: System Architecture Design)
8. System Integration and Testing (P2) -- (depends on: Cultivation Subsystem, Conversion Subsystem, Optimization Subsystem, Data Management and Analytics, User Interface and Monitoring)
9. Security and Compliance (P2) -- (depends on: System Architecture Design)
10. Deployment and Maintenance (P2) -- (depends on: System Integration and Testing, Security and Compliance)
11. Documentation and Training (P2) -- (depends on: System Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AlgaeBiofuelFarm can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An optimized system for cultivating algae and efficiently converting it into biofuel..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
