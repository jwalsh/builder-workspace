# RealTimeBiddingPlatform

You are a coding agent working on RealTimeBiddingPlatform -- A distributed platform for real-time bidding in online advertising, capable of handling millions of bid requests per second with sub-10ms latency.

## Foundational Axiom

Existing approaches to distributed platform fail because they optimize for the common case while ignoring structural constraints; RealTimeBiddingPlatform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design real-time data processing system
- User interface: create frontend interface design
- Data layer: establish database design and schema

## Anti-Goals

- **General-purpose platform**: RealTimeBiddingPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Establish Database Design and Schema (P5) -- (depends on: Define System Architecture)
3. Write Comprehensive Technical Documentation for RealTimeBiddingPlatform (P5) -- (depends on: Complete all high-level tasks)
4. Develop Bidder Implementations (P4) -- (depends on: Define System Architecture)
5. Create Frontend Interface Design (P3) -- (depends on: Define System Architecture)
6. Design Real-Time Data Processing System (P2) -- (depends on: Define System Architecture)
7. Set Up DevOps and Continuous Integration/Deployment (P2) -- (depends on: Define System Architecture)
8. Perform Security Audit and Vulnerability Testing (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeBiddingPlatform can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A distributed platform for real-time bidding in online advertising, capable of handling millions of .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
