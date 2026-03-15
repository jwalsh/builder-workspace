# BioLuminousBodyArt

You are a coding agent working on BioLuminousBodyArt -- Genetically engineered bioluminescent tattoos and body modifications that can change color and pattern at will.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BioLuminousBodyArt embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: genetic engineering research and development
- User interface: requirements gathering and analysis
- Data layer: database and data management

## Anti-Goals

- **General-purpose platform**: BioLuminousBodyArt solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for BioLuminousBodyArt Project - RFC Review and Update (P5) -- (depends on: Requirements Gathering and Analysis)
3. Genetic Engineering Research and Development (P4) -- (depends on: System Architecture Design)
4. User Interface and Control System Development (P4) -- (depends on: System Architecture Design)
5. Database and Data Management (P3) -- (depends on: System Architecture Design, Security Requirements)
6. Testing and Quality Assurance (P4) -- (depends on: Genetic Engineering Research and Development, User Interface and Control System Development, Database and Data Management)
7. Deployment and Operations (P5) -- (depends on: Testing and Quality Assurance)
8. Security and Regulatory Compliance (P4) -- (depends on: System Architecture Design)
9. Documentation and User Training (P4) -- (depends on: User Interface and Control System Development, Genetic Engineering Research and Development)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioLuminousBodyArt can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Genetically engineered bioluminescent tattoos and body modifications that can change color and patte.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
