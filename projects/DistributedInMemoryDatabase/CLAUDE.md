# DistributedInMemoryDatabase

You are a coding agent working on DistributedInMemoryDatabase -- An in-memory database system distributed across multiple nodes, providing high-speed data access with strong consistency guarantees.

## Foundational Axiom

Existing approaches to in-memory database system distributed across multiple nodes, fail because they optimize for the common case while ignoring structural constraints; DistributedInMemoryDatabase makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An in-memory database system distributed across multiple nodes, providing high-speed data access wit
- User interface: define project requirements and goals (revised)
- Data layer: define system architecture for distributed in-memory database

## Anti-Goals

- **General-purpose platform**: DistributedInMemoryDatabase solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture for Distributed In-Memory Database (P1)
2. Develop Communication Protocol for Node Coordination (P4) -- (depends on: Define System Architecture for Distributed In-Memory Database)
3. Implement Communication Protocol for Node Coordination (P5) -- (depends on: Develop Communication Protocol for Node Coordination)
4. Write Unit Tests for Communication Protocol (P4) -- (depends on: Implement Communication Protocol for Node Coordination)
5. Implement Key-Value Storage System Prototype (P3) -- (depends on: Design Key-Value Storage System for In-Memory Database)
6. Write Unit Tests for Key-Value Storage System (P3) -- (depends on: Implement Key-Value Storage System Prototype)
7. Write User Documentation for Distributed In-Memory Database (P2) -- (depends on: Define System Architecture for Distributed In-Memory Database)
8. Define Project Requirements and Goals (Revised) (P1)
9. Perform Security Review of Distributed In-Memory Database Design (P1) -- (depends on: Define System Architecture for Distributed In-Memory Database)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedInMemoryDatabase can deliver its core value proposition as described
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

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An in-memory database system distributed across multiple nodes, providing high-speed data access wit.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
