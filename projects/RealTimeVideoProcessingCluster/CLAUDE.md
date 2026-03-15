# RealTimeVideoProcessingCluster

You are a coding agent working on RealTimeVideoProcessingCluster -- A distributed system for real-time video processing, capable of handling thousands of video streams simultaneously for applications like surveillance or live streaming.

## Foundational Axiom

The bottleneck in distributed system is not compute or data but the feedback loop between intent and artifact; RealTimeVideoProcessingCluster compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop real-time video processing algorithms
- Data layer: integrate with external storage systems

## Anti-Goals

- **General-purpose platform**: RealTimeVideoProcessingCluster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design Clustering Strategy (P2) -- (depends on: Define System Architecture)
3. Develop Real-time Video Processing Algorithms (P3) -- (depends on: Define System Architecture)
4. Implement Video Processing Node (P5) -- (depends on: Design Clustering Strategy, Develop Real-time Video Processing Algorithms)
5. Create Video Streaming API (P4) -- (depends on: Define System Architecture)
6. Implement Security Measures (P3) -- (depends on: Define System Architecture)
7. Integrate with External Storage Systems (P2) -- (depends on: Define System Architecture)
8. Test and Optimize Performance (P1) -- (depends on: Implement Video Processing Node)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeVideoProcessingCluster can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system for real-time video processing, capable of handling thousands of video streams .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
