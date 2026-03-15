# LowLatencyMessagingProtocol

You are a coding agent working on LowLatencyMessagingProtocol -- A new network protocol designed for ultra-low latency messaging in distributed systems, optimized for high-frequency trading and online gaming.

## Foundational Axiom

Existing approaches to new network protocol designed fail because they optimize for the common case while ignoring structural constraints; LowLatencyMessagingProtocol makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A new network protocol designed for ultra-low latency messaging in distributed systems, optimized fo
- User interface: define protocol requirements for lowlatencymessagingprotocol

## Anti-Goals

- **General-purpose platform**: LowLatencyMessagingProtocol solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Protocol Requirements for LowLatencyMessagingProtocol (P5)
2. Design Protocol Architecture (Revised and Clarified) (P4) -- (depends on: Define Protocol Requirements)
3. Implement Protocol Core (P3) -- (depends on: Design Protocol Architecture)
4. Implement Protocol Extensions (P3) -- (depends on: Implement Protocol Core)
5. Develop Testing Framework (P2) -- (depends on: Implement Protocol Core)
6. Conduct Security Audit (P2) -- (depends on: Implement Protocol Extensions)
7. Write Documentation (P2) -- (depends on: Implement Protocol Extensions)
8. Deploy and Monitor (P1) -- (depends on: Conduct Security Audit, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LowLatencyMessagingProtocol can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A new network protocol designed for ultra-low latency messaging in distributed systems, optimized fo.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
