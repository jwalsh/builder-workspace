# BioNanoAssembler

You are a coding agent working on BioNanoAssembler -- Develop a platform for designing and manufacturing bio-inspired nanomachines for medical and environmental applications.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BioNanoAssembler embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Develop a platform for designing and manufacturing bio-inspired nanomachines for medical and environ
- User interface: define project scope and requirements
- Data layer: establish data management and storage - update (v2)

## Anti-Goals

- **General-purpose platform**: BioNanoAssembler solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture - Revised (Updated) (P5) -- (depends on: Define Project Scope and Requirements, Design Database Schema)
3. Establish Data Management and Storage - Update (v2) (P4) -- (depends on: Design System Architecture, Define Data Formats and Standards)
4. Develop Molecular Modeling and Simulation Tools (P3) -- (depends on: Design System Architecture)
5. Build User Interface and Visualization Components (P3) -- (depends on: Design System Architecture)
6. Implement Manufacturing and Assembly Algorithms (P3) -- (depends on: Design System Architecture)
7. Develop Comprehensive Security and Access Control Mechanisms for BioNanoAssembler Platform (Revised) (P2) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
9. Develop Comprehensive Testing and Validation Strategies (Revised) (P2) -- (depends on: Design System Architecture)
10. Create Documentation and User Guides (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioNanoAssembler can deliver its core value proposition as described
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

- TensorFlow

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Develop a platform for designing and manufacturing bio-inspired nanomachines for medical and environ.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
