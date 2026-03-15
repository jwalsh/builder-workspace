# FraudBuster

You are a coding agent working on FraudBuster -- Implement real-time fraud detection using both rule-based and machine learning approaches with a high-performance database solution.

## Foundational Axiom

Security in implement real-time fraud detection using both rule-based an fails when it is bolted on after the fact; FraudBuster makes security a structural property of the system rather than an additional layer.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Implement real-time fraud detection using both rule-based and machine learning approaches with a hig
- User interface: define project scope and requirements - v2.0
- Data layer: implement data ingestion pipeline

## Anti-Goals

- **General-purpose platform**: FraudBuster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - v2.0 (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Data Ingestion Pipeline (P3) -- (depends on: Design System Architecture)
4. Develop Rule-based Fraud Detection Module (P3) -- (depends on: Design System Architecture)
5. Implement Machine Learning Fraud Detection (P3) -- (depends on: Design System Architecture)
6. Design and Implement High-Performance Database Solution (P3) -- (depends on: Design System Architecture)
7. Implement Security and Access Controls (P3) -- (depends on: Design System Architecture)
8. Develop User Interface and Reporting (P2) -- (depends on: Implement Data Ingestion Pipeline, Develop Rule-based Fraud Detection Module, Implement Machine Learning Fraud Detection, Design and Implement High-Performance Database Solution)
9. Set up Continuous Integration and Deployment (P2) -- (depends on: Implement Data Ingestion Pipeline, Develop Rule-based Fraud Detection Module, Implement Machine Learning Fraud Detection, Design and Implement High-Performance Database Solution, Develop User Interface and Reporting)
10. Conduct System Testing and Quality Assurance (P2) -- (depends on: Implement Data Ingestion Pipeline, Develop Rule-based Fraud Detection Module, Implement Machine Learning Fraud Detection, Design and Implement High-Performance Database Solution, Develop User Interface and Reporting)
11. Prepare Documentation and User Guides (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Implement Data Ingestion Pipeline, Develop Rule-based Fraud Detection Module, Implement Machine Learning Fraud Detection, Design and Implement High-Performance Database Solution, Develop User Interface and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FraudBuster can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Implement real-time fraud detection using both rule-based and machine learning approaches with a hig.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to security engineers and soc analysts responsible for system protection.
