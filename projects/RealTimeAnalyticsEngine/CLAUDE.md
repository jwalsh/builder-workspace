# RealTimeAnalyticsEngine

You are a coding agent working on RealTimeAnalyticsEngine -- An analytics engine capable of processing and visualizing data in real-time from thousands of sources, suitable for live dashboards and monitoring systems.

## Foundational Axiom

Existing approaches to analytics engine capable of processing and visualizing data fail because they optimize for the common case while ignoring structural constraints; RealTimeAnalyticsEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design architecture for realtimeanalyticsengine
- User interface: define project scope and requirements
- Data layer: implement backend services for data processing

## Anti-Goals

- **General-purpose platform**: RealTimeAnalyticsEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Architecture for RealTimeAnalyticsEngine (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Backend Services for Data Processing (P4) -- (depends on: Design Architecture for RealTimeAnalyticsEngine)
4. Develop Real-time Data Streaming Mechanism (P5) -- (depends on: Implement Backend Services for Data Processing)
5. Implement CI/CD Pipeline for RealTimeAnalyticsEngine (P3) -- (depends on: Implement Backend Services for Data Processing)
6. Implement Security Measures for RealTimeAnalyticsEngine (P5) -- (depends on: Implement CI/CD Pipeline for RealTimeAnalyticsEngine)
7. Develop Frontend Interface for RealTimeAnalyticsEngine (P3) -- (depends on: Design Architecture for RealTimeAnalyticsEngine)
8. Perform Unit Testing and Quality Assurance for RealTimeAnalyticsEngine (P4) -- (depends on: Develop Frontend Interface for RealTimeAnalyticsEngine)
9. Set Up and Configure RealTimeAnalyticsEngine Database (P2) -- (depends on: Design Architecture for RealTimeAnalyticsEngine)
10. Document RealTimeAnalyticsEngine Functionality and Usage (P2) -- (depends on: Develop Frontend Interface for RealTimeAnalyticsEngine)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeAnalyticsEngine can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An analytics engine capable of processing and visualizing data in real-time from thousands of source.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to marketing professionals and campaign managers.
