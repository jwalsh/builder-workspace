# OilTradeAIAnalyst

You are a coding agent working on OilTradeAIAnalyst -- An AI system for analyzing global oil markets, predicting price trends, and optimizing trading strategies.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; OilTradeAIAnalyst makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system for analyzing global oil markets, predicting price trends, and optimizing trading strat
- User interface: requirements gathering and analysis
- Data layer: system architecture design for oiltradeaianalyst - optimized for data-driven decisions and efficient trading strategies

## Anti-Goals

- **General-purpose platform**: OilTradeAIAnalyst solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for OilTradeAIAnalyst - Optimized for Data-Driven Decisions and Efficient Trading Strategies (P5) -- (depends on: Requirements Gathering and Analysis, Data Sources Identification)
3. Data Pipeline and Storage (P4) -- (depends on: System Architecture Design)
4. Predictive Modeling and Analysis (P4) -- (depends on: System Architecture Design, Data Pipeline and Storage)
5. Trading Strategy Optimization (P4) -- (depends on: Predictive Modeling and Analysis)
6. User Interface and Visualization (P4) -- (depends on: System Architecture Design)
7. Testing and Quality Assurance (P4) -- (depends on: Data Pipeline and Storage, Predictive Modeling and Analysis, Trading Strategy Optimization, User Interface and Visualization)
8. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
9. Documentation and Training (P5) -- (depends on: User Interface and Visualization)
10. Security and Compliance (P4) -- (depends on: System Architecture Design)
11. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OilTradeAIAnalyst can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system for analyzing global oil markets, predicting price trends, and optimizing trading strat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
