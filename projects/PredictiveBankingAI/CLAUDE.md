# PredictiveBankingAI

You are a coding agent working on PredictiveBankingAI -- An AI system for personal banking that predicts future financial needs, automates savings, and provides personalized financial advice based on spending patterns and life events.

## Foundational Axiom

Existing approaches to ai system for personal banking fail because they optimize for the common case while ignoring structural constraints; PredictiveBankingAI makes those constraints first-class.

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

- **General-purpose platform**: PredictiveBankingAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Compliance (P4) -- (depends on: System Architecture Design)
4. Data Collection and Preprocessing (P3) -- (depends on: System Architecture Design)
5. AI Model Development (P3) -- (depends on: Data Collection and Preprocessing)
6. Revised User Interface Design for PredictiveBankingAI (P3) -- (depends on: System Architecture Design, User Experience Research)
7. Frontend Development (P3) -- (depends on: User Interface Design, AI Model Development)
8. Backend Development (P3) -- (depends on: System Architecture Design, AI Model Development)
9. Database Design and Implementation (P3) -- (depends on: System Architecture Design, Data Modeling and Requirements Analysis)
10. Testing and Quality Assurance (P3) -- (depends on: Frontend Development, Backend Development)
11. Deployment and DevOps (P3) -- (depends on: Frontend Development, Backend Development, Database Design and Implementation)
12. Documentation and User Support (P2) -- (depends on: Frontend Development, Backend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PredictiveBankingAI can deliver its core value proposition as described
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

- MongoDB
- Docker
- Kubernetes
- AWS
- TensorFlow
- PyTorch

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system for personal banking that predicts future financial needs, automates savings, and provi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to financial analysts and portfolio managers.
