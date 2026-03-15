# GeneticHeritageJourney

You are a coding agent working on GeneticHeritageJourney -- A travel service that creates personalized itineraries based on an individual's genetic heritage, allowing people to explore their ancestral roots.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; GeneticHeritageJourney embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: GeneticHeritageJourney solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for GeneticHeritageJourney (Revised) (P3) -- (depends on: Requirements Gathering and Analysis)
3. Database Design and Implementation (P4) -- (depends on: System Architecture Design)
4. Backend Development (P4) -- (depends on: System Architecture Design, Database Design and Implementation)
5. Frontend Development (P4) -- (depends on: System Architecture Design)
6. Integration and Testing (P5) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation)
7. Deployment and DevOps (P5) -- (depends on: Integration and Testing)
8. Security and Compliance (Revised) (P4) -- (depends on: System Architecture Design)
9. Documentation and User Support (P4) -- (depends on: Frontend Development, Backend Development)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeneticHeritageJourney can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A travel service that creates personalized itineraries based on an individual's genetic heritage, al.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
