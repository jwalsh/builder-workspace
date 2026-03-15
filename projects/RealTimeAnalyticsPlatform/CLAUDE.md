# RealTimeAnalyticsPlatform

You are a coding agent working on RealTimeAnalyticsPlatform -- A platform for processing and analyzing high-volume, real-time data streams for instant insights.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; RealTimeAnalyticsPlatform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement real-time data processing algorithms
- User interface: design and develop user interface for real-time analytics
- Data layer: set up real-time data storage solution

## Anti-Goals

- **General-purpose platform**: RealTimeAnalyticsPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Set Up Real-Time Data Storage Solution (P5) -- (depends on: Define System Architecture)
3. Perform Integration Testing and Ensure Platform Stability (P5) -- (depends on: Complete all development tasks)
4. Design and Develop User Interface for Real-Time Analytics (P4) -- (depends on: Define System Architecture)
5. Document and Publish User Guide for RealTimeAnalyticsPlatform (P4) -- (depends on: Complete all development tasks)
6. Develop Real-Time Data Ingestion Module (P2) -- (depends on: Define System Architecture)
7. Implement Real-Time Data Processing Algorithms (P3) -- (depends on: Develop Real-Time Data Ingestion Module)
8. Implement Real-Time Data Analysis Capabilities (P2) -- (depends on: Implement Real-Time Data Processing Algorithms)
9. Perform Security Audit and Implement Measures (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeAnalyticsPlatform can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for processing and analyzing high-volume, real-time data streams for instant insights..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to marketing professionals and campaign managers.
