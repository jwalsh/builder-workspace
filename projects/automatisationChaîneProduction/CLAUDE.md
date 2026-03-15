# automatisationChaîneProduction

You are a coding agent working on automatisationChaîneProduction -- Une chaîne de production automatisée intégrant des robots pour optimiser l'efficacité et réduire les coûts.

## Foundational Axiom

Existing approaches to une chaîne de production automatisée intégrant des robots po fail because they optimize for the common case while ignoring structural constraints; automatisationChaîneProduction makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for data processing
- User interface: develop frontend interface for user interaction
- Data layer: develop backend services for data processing

## Anti-Goals

- **General-purpose platform**: automatisationChaîneProduction solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Overall Project Scope and Objectives (P1)
2. Design Architecture for the Automated Production Chain (P3) -- (depends on: Research and Gather Existing Solutions in Automated Production Chains)
3. Integrate Robot Systems into the Automated Production Chain (P5) -- (depends on: Define Overall Project Scope and Objectives, Design Architecture for the Automated Production Chain)
4. Develop Frontend Interface for User Interaction (P4) -- (depends on: Define Overall Project Scope and Objectives, Design Architecture for the Automated Production Chain)
5. Develop Backend Services for Data Processing (P4) -- (depends on: Define Overall Project Scope and Objectives, Design Architecture for the Automated Production Chain)
6. Test and Validate the Automated Production Chain (P5) -- (depends on: Develop Frontend Interface for User Interaction, Develop Backend Services for Data Processing, Integrate Robot Systems into the Automated Production Chain)
7. Implement DevOps Practices for Continuous Integration and Deployment (P5) -- (depends on: Develop Frontend Interface for User Interaction, Develop Backend Services for Data Processing, Integrate Robot Systems into the Automated Production Chain)
8. Research Existing Solutions in Automated Production Chains (P2) -- (depends on: Define Overall Project Scope and Objectives)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: automatisationChaîneProduction can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une chaîne de production automatisée intégrant des robots pour optimiser l'efficacité et réduire les.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
