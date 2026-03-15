# SeismicDataInterpreter

You are a coding agent working on SeismicDataInterpreter -- Advanced machine learning algorithms for interpreting seismic data to improve accuracy in identifying potential oil and gas reserves.

## Foundational Axiom

Existing approaches to advanced machine learning algorithms fail because they optimize for the common case while ignoring structural constraints; SeismicDataInterpreter makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data acquisition and preprocessing
- User interface: data acquisition and preprocessing
- Data layer: data acquisition and preprocessing

## Anti-Goals

- **General-purpose platform**: SeismicDataInterpreter solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Data Acquisition and Preprocessing (P2)
2. Machine Learning Model Development (P3) -- (depends on: Data Acquisition and Preprocessing)
3. Model Training and Evaluation (P4) -- (depends on: Machine Learning Model Development)
4. User Interface and Visualization (P4) -- (depends on: Model Training and Evaluation)
5. Testing and Quality Assurance (P5) -- (depends on: User Interface and Visualization, Model Training and Evaluation)
6. Deployment and Monitoring (P5) -- (depends on: Testing and Quality Assurance)
7. Documentation and User Training (P4) -- (depends on: User Interface and Visualization)
8. Security and Compliance (P3)
9. Project Planning and Requirements Gathering (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SeismicDataInterpreter can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Advanced machine learning algorithms for interpreting seismic data to improve accuracy in identifyin.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
