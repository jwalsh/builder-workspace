# réseauSmartGrid

You are a coding agent working on réseauSmartGrid -- Un réseau électrique intelligent qui optimise la distribution d'énergie pour maximiser l'efficacité et la durabilité.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; réseauSmartGrid maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un réseau électrique intelligent qui optimise la distribution d'énergie pour maximiser l'efficacité 
- User interface: create user interface for grid management
- Data layer: design database structure for smart grid data

## Anti-Goals

- **General-purpose platform**: réseauSmartGrid solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Smart Grid Architecture (P1)
2. Design Database Structure for Smart Grid Data (P5) -- (depends on: Define Smart Grid Architecture)
3. Develop Intelligent Energy Distribution Algorithm (P2) -- (depends on: Define Smart Grid Architecture)
4. Implement Real-time Monitoring System (P3) -- (depends on: Define Smart Grid Architecture)
5. Create User Interface for Grid Management (P4) -- (depends on: Develop Intelligent Energy Distribution Algorithm, Implement Real-time Monitoring System)
6. Implement Data Security Measures (P1) -- (depends on: Create User Interface for Grid Management, Design Database Structure for Smart Grid Data)
7. Perform System Integration and Testing (P2) -- (depends on: Define Smart Grid Architecture, Develop Intelligent Energy Distribution Algorithm, Implement Real-time Monitoring System, Create User Interface for Grid Management, Design Database Structure for Smart Grid Data, Implement Data Security Measures)
8. Prepare Technical Documentation (P3) -- (depends on: Perform System Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: réseauSmartGrid can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un réseau électrique intelligent qui optimise la distribution d'énergie pour maximiser l'efficacité .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
