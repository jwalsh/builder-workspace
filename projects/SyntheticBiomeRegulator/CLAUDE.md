# SyntheticBiomeRegulator

You are a coding agent working on SyntheticBiomeRegulator -- An implant that manages the body's microbiome, optimizing health by regulating bacterial populations.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; SyntheticBiomeRegulator embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend logic for bacterial population regulation
- User interface: develop the frontend interface for user interaction
- Data layer: develop a database for storing microbiome data and user profiles

## Anti-Goals

- **General-purpose platform**: SyntheticBiomeRegulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals (P1)
2. Design the SyntheticBiomeRegulator Implant (P2) -- (depends on: Define Project Scope and Goals)
3. Develop a Database for Storing Microbiome Data and User Profiles (P5) -- (depends on: Design the SyntheticBiomeRegulator Implant)
4. Implement Backend Logic for Bacterial Population Regulation (P4) -- (depends on: Design the SyntheticBiomeRegulator Implant)
5. Develop the Frontend Interface for User Interaction (P3) -- (depends on: Design the SyntheticBiomeRegulator Implant)
6. Conduct Quality Assurance Testing on the SyntheticBiomeRegulator (P5) -- (depends on: Implement Backend Logic for Bacterial Population Regulation, Develop a Database for Storing Microbiome Data and User Profiles, Develop the Frontend Interface for User Interaction)
7. Write Technical Documentation for the SyntheticBiomeRegulator (P3) -- (depends on: Define Project Scope and Goals)
8. Implement DevOps for Deployment and Maintenance (P2) -- (depends on: Design the SyntheticBiomeRegulator Implant, Develop a Database for Storing Microbiome Data and User Profiles)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SyntheticBiomeRegulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An implant that manages the body's microbiome, optimizing health by regulating bacterial populations.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
