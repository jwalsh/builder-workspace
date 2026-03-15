# MicrobialFuelCell

You are a coding agent working on MicrobialFuelCell -- A scaled-up microbial fuel cell system that generates electricity from organic matter in wastewater.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; MicrobialFuelCell embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development for data collection and processing
- User interface: requirements gathering for microbial fuel cell system
- Data layer: backend development for data collection and processing

## Anti-Goals

- **General-purpose platform**: MicrobialFuelCell solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for Microbial Fuel Cell System (P1)
2. Design Concept for Microbial Fuel Cell System (P2) -- (depends on: Requirements Gathering for Microbial Fuel Cell System)
3. Backend Development for Data Collection and Processing (P3) -- (depends on: Design Concept for Microbial Fuel Cell System)
4. Frontend Development for User Interface and Visualization (P3) -- (depends on: Design Concept for Microbial Fuel Cell System)
5. Deploy Microbial Fuel Cell System on Test Environment (P5) -- (depends on: Backend Development for Data Collection and Processing, Frontend Development for User Interface and Visualization)
6. Security Audit for Microbial Fuel Cell System (P5) -- (depends on: Deploy Microbial Fuel Cell System on Test Environment)
7. Test Microbial Fuel Cell System Components (P2) -- (depends on: Deploy Microbial Fuel Cell System on Test Environment)
8. Iterative Refinement and Integration (P1) -- (depends on: Test Microbial Fuel Cell System Components)
9. Prepare Microbial Fuel Cell System for Deployment (P3) -- (depends on: Iterative Refinement and Integration)
10. Deploy Microbial Fuel Cell System in Production Environment (P5) -- (depends on: Prepare Microbial Fuel Cell System for Deployment)
11. Database Design and Integration (P4) -- (depends on: Backend Development for Data Collection and Processing)
12. Detailed Documentation for Microbial Fuel Cell System (P4) -- (depends on: Deploy Microbial Fuel Cell System on Test Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MicrobialFuelCell can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A scaled-up microbial fuel cell system that generates electricity from organic matter in wastewater..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
