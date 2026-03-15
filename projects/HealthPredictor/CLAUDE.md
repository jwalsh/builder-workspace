# HealthPredictor

You are a coding agent working on HealthPredictor -- Use machine learning on patient health data to predict medical outcomes such as disease progression and hospital readmission probability.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; HealthPredictor embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data acquisition and preprocessing (update)
- User interface: project planning and requirements gathering
- Data layer: data acquisition and preprocessing (update)

## Anti-Goals

- **General-purpose platform**: HealthPredictor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Data Acquisition and Preprocessing (Update) (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Data Modeling and Feature Engineering for Predictive Analysis in HealthPredictor (P3) -- (depends on: Data Acquisition and Preprocessing)
4. Model Training and Evaluation (P3) -- (depends on: Data Modeling and Feature Engineering)
5. Backend Development for HealthPredictor (P2) -- (depends on: Model Training and Evaluation, Data Ingestion and Preprocessing)
6. Frontend Development for HealthPredictor (P2) -- (depends on: Backend Development)
7. Security and Compliance (P3) -- (depends on: Backend Development, Frontend Development)
8. System Integration and Testing (P2) -- (depends on: Backend Development, Frontend Development)
9. Deployment and Monitoring (P2) -- (depends on: System Integration and Testing, Security and Compliance)
10. Documentation and Training (P2) -- (depends on: Frontend Development, Backend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HealthPredictor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Use machine learning on patient health data to predict medical outcomes such as disease progression .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
