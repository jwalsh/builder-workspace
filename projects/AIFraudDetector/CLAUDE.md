# AIFraudDetector

You are a coding agent working on AIFraudDetector -- An advanced AI system that detects and prevents fraudulent activities in real-time across various banking channels, adapting to new fraud patterns autonomously.

## Foundational Axiom

Security in advanced ai system fails when it is bolted on after the fact; AIFraudDetector makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: feature engineering and model training
- User interface: project planning and requirements gathering
- Data layer: data pipeline and storage

## Anti-Goals

- **General-purpose platform**: AIFraudDetector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Pipeline and Storage (P3) -- (depends on: System Architecture Design)
4. Feature Engineering and Model Training (P3) -- (depends on: Data Pipeline and Storage)
5. Real-time Fraud Detection and Alerting (P2) -- (depends on: Feature Engineering and Model Training)
6. User Interface and Reporting (P3) -- (depends on: Real-time Fraud Detection and Alerting)
7. Documentation and Training (P3) -- (depends on: User Interface and Reporting, Real-time Fraud Detection and Alerting)
8. Security and Compliance (P2) -- (depends on: System Architecture Design)
9. Testing and Quality Assurance (P2) -- (depends on: Real-time Fraud Detection and Alerting, User Interface and Reporting)
10. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIFraudDetector can deliver its core value proposition as described
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

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced AI system that detects and prevents fraudulent activities in real-time across various ba.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
