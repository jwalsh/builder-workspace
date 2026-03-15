# BioInformaticsPipeline

You are a coding agent working on BioInformaticsPipeline -- Develop a scalable pipeline for processing and analyzing large-scale genomic data, supporting personalized medicine initiatives.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BioInformaticsPipeline embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data processing pipeline
- User interface: define project requirements
- Data layer: develop data ingestion module

## Anti-Goals

- **General-purpose platform**: BioInformaticsPipeline solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Develop Data Ingestion Module (P3) -- (depends on: Design System Architecture)
5. Implement Data Processing Pipeline (P3) -- (depends on: Design System Architecture)
6. Develop Analysis Algorithms (P3) -- (depends on: Design System Architecture)
7. Design and Implement Data Storage (P3) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
9. Develop Test Suite (P3) -- (depends on: Design System Architecture)
10. Develop User Interface (P2) -- (depends on: Design System Architecture)
11. Write Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioInformaticsPipeline can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Develop a scalable pipeline for processing and analyzing large-scale genomic data, supporting person.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
