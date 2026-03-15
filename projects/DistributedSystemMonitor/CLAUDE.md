# DistributedSystemMonitor

You are a coding agent working on DistributedSystemMonitor -- A comprehensive monitoring system for large-scale distributed applications, providing real-time insights into system health, performance, and potential issues.

## Foundational Axiom

Existing approaches to comprehensive monitoring system fail because they optimize for the common case while ignoring structural constraints; DistributedSystemMonitor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services for distributedsystemmonitor
- User interface: requirements gathering for distributedsystemmonitor
- Data layer: database design and implementation for distributedsystemmonitor

## Anti-Goals

- **General-purpose platform**: DistributedSystemMonitor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for DistributedSystemMonitor (P1)
2. Design Architecture for DistributedSystemMonitor (P2) -- (depends on: Requirements Gathering for DistributedSystemMonitor)
3. Develop Frontend Interface for DistributedSystemMonitor (P3) -- (depends on: Design Architecture for DistributedSystemMonitor)
4. Implement Backend Services for DistributedSystemMonitor (P3) -- (depends on: Design Architecture for DistributedSystemMonitor)
5. Database Design and Implementation for DistributedSystemMonitor (P3) -- (depends on: Design Architecture for DistributedSystemMonitor)
6. Integration Testing of DistributedSystemMonitor Components (P4) -- (depends on: Develop Frontend Interface for DistributedSystemMonitor, Implement Backend Services for DistributedSystemMonitor, Database Design and Implementation for DistributedSystemMonitor)
7. Deployment of DistributedSystemMonitor System (P5) -- (depends on: Integration Testing of DistributedSystemMonitor Components)
8. Security Review for DistributedSystemMonitor System (P5) -- (depends on: Deployment of DistributedSystemMonitor System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedSystemMonitor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive monitoring system for large-scale distributed applications, providing real-time insi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
