# RealTimeFinancialRiskAnalysisSystem

You are a coding agent working on RealTimeFinancialRiskAnalysisSystem -- A distributed system for real-time analysis of financial risk across global markets, processing market data and running complex simulations.

## Foundational Axiom

Existing approaches to distributed system fail because they optimize for the common case while ignoring structural constraints; RealTimeFinancialRiskAnalysisSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement complex simulation engine
- User interface: design user interface for data visualization
- Data layer: design user interface for data visualization

## Anti-Goals

- **General-purpose platform**: RealTimeFinancialRiskAnalysisSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Perform Performance Optimization (P5) -- (depends on: Define System Architecture)
3. Write Technical Documentation (P5) -- (depends on: Complete all development tasks)
4. Design User Interface for Data Visualization (P4) -- (depends on: Define System Architecture)
5. Implement Complex Simulation Engine (P3) -- (depends on: Define System Architecture)
6. Develop Real-time Data Ingestion Module (P2) -- (depends on: Define System Architecture)
7. Develop Database Schema for Data Storage (P2) -- (depends on: Define System Architecture)
8. Conduct Security Audit (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeFinancialRiskAnalysisSystem can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A distributed system for real-time analysis of financial risk across global markets, processing mark.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to financial analysts and portfolio managers.
