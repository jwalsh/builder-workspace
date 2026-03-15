# NeuralNetworkEnergyTrader

You are a coding agent working on NeuralNetworkEnergyTrader -- An AI system that optimizes energy trading in decentralized energy markets, balancing supply and demand.

## Foundational Axiom

Existing tools treat ai system as a generic automation problem; NeuralNetworkEnergyTrader succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data ingestion and processing pipeline
- User interface: revised project scope and requirements: define for neural network energy trading system
- Data layer: develop data ingestion and processing pipeline

## Anti-Goals

- **General-purpose platform**: NeuralNetworkEnergyTrader solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Revised Project Scope and Requirements: Define for Neural Network Energy Trading System (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Data Ingestion and Processing Pipeline (P3) -- (depends on: Design System Architecture)
4. Build Neural Network Model (P3) -- (depends on: Design System Architecture, Develop Data Ingestion and Processing Pipeline)
5. Implement Trading Strategies and Market Integration (P3) -- (depends on: Build Neural Network Model)
6. Implement Security Measures (P3) -- (depends on: Design System Architecture)
7. Develop User Interface and Monitoring (P2) -- (depends on: Design System Architecture)
8. Set up Infrastructure and Deployment (P2) -- (depends on: Design System Architecture)
9. Conduct Testing and Quality Assurance (P2) -- (depends on: Develop Data Ingestion and Processing Pipeline, Build Neural Network Model, Implement Trading Strategies and Market Integration, Develop User Interface and Monitoring)
10. Prepare Documentation and User Guides (P2) -- (depends on: Design System Architecture, Develop User Interface and Monitoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralNetworkEnergyTrader can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that optimizes energy trading in decentralized energy markets, balancing supply and dem.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
