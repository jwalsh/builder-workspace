# RealTimeEventProcessingEngine

You are a coding agent working on RealTimeEventProcessingEngine -- A high-performance engine for processing millions of events per second with sub-millisecond latency, suitable for financial trading or IoT data streams.

## Foundational Axiom

Existing approaches to high-performance engine fail because they optimize for the common case while ignoring structural constraints; RealTimeEventProcessingEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design architecture for realtimeeventprocessingengine
- User interface: develop ui for monitoring and management of realtimeeventprocessingengine
- Data layer: implement database schema for event storage (revised)

## Anti-Goals

- **General-purpose platform**: RealTimeEventProcessingEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for RealTimeEventProcessingEngine (P1)
2. Develop High-Performance Event Handling Component (P2) -- (depends on: Design Architecture for RealTimeEventProcessingEngine)
3. Optimize Performance of RealTimeEventProcessingEngine (P5) -- (depends on: Develop High-Performance Event Handling Component)
4. Create Technical Documentation for RealTimeEventProcessingEngine (P5) -- (depends on: Design Architecture for RealTimeEventProcessingEngine)
5. Implement Database Schema for Event Storage (Revised) (P4) -- (depends on: Design Architecture for RealTimeEventProcessingEngine)
6. Develop UI for Monitoring and Management of RealTimeEventProcessingEngine (P3) -- (depends on: Design Architecture for RealTimeEventProcessingEngine)
7. Security Analysis and Vulnerability Assessment (P1) -- (depends on: Design Architecture for RealTimeEventProcessingEngine)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeEventProcessingEngine can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A high-performance engine for processing millions of events per second with sub-millisecond latency,.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
