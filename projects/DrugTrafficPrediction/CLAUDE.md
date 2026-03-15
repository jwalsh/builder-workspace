# DrugTrafficPrediction

You are a coding agent working on DrugTrafficPrediction -- An AI system that analyzes patterns in drug-related crimes and global trade data to predict potential drug trafficking routes.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; DrugTrafficPrediction embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data collection and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data collection and preprocessing

## Anti-Goals

- **General-purpose platform**: DrugTrafficPrediction solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Data Collection and Preprocessing (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Compliance (P4) -- (depends on: Project Planning and Requirements Gathering)
4. Model Architecture Design for Drug Traffic Prediction System (Revised) (P3) -- (depends on: Project Planning and Requirements Gathering)
5. Data Storage and Management (P3) -- (depends on: Data Collection and Preprocessing)
6. User Interface Design (UI/UX) - Review and Improvements Suggestions (P3) -- (depends on: Project Planning and Requirements Gathering)
7. Model Implementation (P2) -- (depends on: Model Architecture Design)
8. User Interface Implementation (P2) -- (depends on: User Interface Design, Model Implementation)
9. Testing and Evaluation (P2) -- (depends on: Model Implementation, User Interface Implementation)
10. Documentation and Training (P3) -- (depends on: User Interface Implementation, Testing and Evaluation)
11. Deployment and Monitoring (P2) -- (depends on: Testing and Evaluation, Security and Compliance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DrugTrafficPrediction can deliver its core value proposition as described
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

- TensorFlow
- PyTorch

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that analyzes patterns in drug-related crimes and global trade data to predict potentia.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
