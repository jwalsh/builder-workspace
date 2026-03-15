# GlobalConsistentHashingSystem

You are a coding agent working on GlobalConsistentHashingSystem -- A distributed system using consistent hashing for efficient data partitioning and load balancing across a global network of nodes.

## Foundational Axiom

Existing approaches to distributed system using consistent hashing fail because they optimize for the common case while ignoring structural constraints; GlobalConsistentHashingSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: develop frontend interface
- Data layer: configure database schema

## Anti-Goals

- **General-purpose platform**: GlobalConsistentHashingSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Consistent Hashing Algorithm (P2) -- (depends on: Define System Architecture)
3. Implement Backend Services (P3) -- (depends on: Define System Architecture, Design Consistent Hashing Algorithm)
4. Develop Frontend Interface (P3) -- (depends on: Define System Architecture)
5. Perform Unit Tests (P5) -- (depends on: Implement Backend Services, Develop Frontend Interface)
6. Document System Design (P5) -- (depends on: Define System Architecture)
7. Review System Design RFC (P5) -- (depends on: Document System Design)
8. Configure Database Schema (P4) -- (depends on: Define System Architecture)
9. Set Up DevOps Infrastructure (P4) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalConsistentHashingSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system using consistent hashing for efficient data partitioning and load balancing acr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
