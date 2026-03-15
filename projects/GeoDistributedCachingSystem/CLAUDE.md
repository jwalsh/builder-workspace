# GeoDistributedCachingSystem

You are a coding agent working on GeoDistributedCachingSystem -- A globally distributed caching system that minimizes latency for users worldwide while maintaining data consistency.

## Foundational Axiom

Existing approaches to globally distributed caching system fail because they optimize for the common case while ignoring structural constraints; GeoDistributedCachingSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for system management
- User interface: develop frontend interface for system management
- Data layer: design data consistency strategy

## Anti-Goals

- **General-purpose platform**: GeoDistributedCachingSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture Design (P1)
2. Design Data Consistency Strategy (P2) -- (depends on: Define System Architecture Design)
3. Implement Data Consistency Mechanisms (P4) -- (depends on: Design Data Consistency Strategy)
4. Design Scalability Strategy (P3) -- (depends on: Define System Architecture Design)
5. Implement Scalability Mechanisms (P5) -- (depends on: Design Scalability Strategy)
6. Design Performance Optimization Strategy (P4) -- (depends on: Define System Architecture Design)
7. Implement Performance Optimization Mechanisms (P6) -- (depends on: Design Performance Optimization Strategy)
8. Perform System Integration Testing (P7) -- (depends on: Implement Data Consistency Mechanisms, Implement Scalability Mechanisms, Implement Performance Optimization Mechanisms)
9. Create Technical Documentation for the Design (P5) -- (depends on: Define System Architecture Design)
10. Set Up Database Schema and Models (P3) -- (depends on: Define System Architecture Design)
11. Develop Backend Services for System Management (P2) -- (depends on: Define System Architecture Design)
12. Develop Frontend Interface for System Management (P1) -- (depends on: Define System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeoDistributedCachingSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A globally distributed caching system that minimizes latency for users worldwide while maintaining d.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
