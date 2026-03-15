# gestionImmobilierQuantum

You are a coding agent working on gestionImmobilierQuantum -- Un outil basé sur les technologies quantiques pour prédire les tendances de l'immobilier avec une grande précision.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; gestionImmobilierQuantum co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for data processing and quantum computation
- User interface: develop frontend interface for user interaction
- Data layer: develop backend services for data processing and quantum computation

## Anti-Goals

- **General-purpose platform**: gestionImmobilierQuantum solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Create Project Architecture (P4) -- (depends on: Define Project Scope and Requirements)
2. Develop Frontend Interface for User Interaction (P5) -- (depends on: Create Project Architecture)
3. Develop Backend Services for Data Processing and Quantum Computation (P5) -- (depends on: Create Project Architecture)
4. Establish Database Structure and Integration (P4) -- (depends on: Create Project Architecture)
5. Research Quantum Computing Techniques for Real Estate Prediction (P2) -- (depends on: Define Project Scope and Requirements)
6. Design Quantum Algorithm for Real Estate Prediction (P3) -- (depends on: Research Quantum Computing Techniques for Real Estate Prediction)
7. Implement DevOps and Deployment Strategies (P3) -- (depends on: Create Project Architecture)
8. Perform Unit and Integration Tests (P2) -- (depends on: Develop Frontend Interface for User Interaction, Develop Backend Services for Data Processing and Quantum Computation)
9. Define Quantum Real Estate Prediction Tool Scope and Requirements - RFC DRAFT (P1)
10. Secure the Application (P1) -- (depends on: Create Project Architecture)
11. Document and Maintain Technical Documentation (P1) -- (depends on: Define Project Scope and Requirements)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: gestionImmobilierQuantum can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un outil basé sur les technologies quantiques pour prédire les tendances de l'immobilier avec une gr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
