# GreenEnergyPredictor

You are a coding agent working on GreenEnergyPredictor -- Forecast renewable energy production using machine learning models and weather data to optimize grid management and reduce reliance on non-renewable sources.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; GreenEnergyPredictor maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data acquisition and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data acquisition and preprocessing

## Anti-Goals

- **General-purpose platform**: GreenEnergyPredictor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Data Acquisition and Preprocessing (P3) -- (depends on: System Architecture Design)
4. Machine Learning Model Development (P3) -- (depends on: Data Acquisition and Preprocessing)
5. Grid Integration and Optimization (P3) -- (depends on: Machine Learning Model Development)
6. Security and Compliance (P3) -- (depends on: System Architecture Design)
7. User Interface Development (P2) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: Machine Learning Model Development, Grid Integration and Optimization, User Interface Development)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance, Security and Compliance)
10. Documentation and Training (P2) -- (depends on: User Interface Development, Grid Integration and Optimization)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GreenEnergyPredictor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Forecast renewable energy production using machine learning models and weather data to optimize grid.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
