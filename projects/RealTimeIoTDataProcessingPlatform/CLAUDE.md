# RealTimeIoTDataProcessingPlatform

You are a coding agent working on RealTimeIoTDataProcessingPlatform -- A platform for ingesting and processing data from millions of IoT devices in real-time, with support for complex event processing and automated actions.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; RealTimeIoTDataProcessingPlatform makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design architecture for real-time data processing
- User interface: create web interface for monitoring and management
- Data layer: design architecture for real-time data processing

## Anti-Goals

- **General-purpose platform**: RealTimeIoTDataProcessingPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for Real-Time Data Processing (P1)
2. Implement Automated Action Support (P5) -- (depends on: Design Architecture for Real-Time Data Processing)
3. Write User Documentation (P5) -- (depends on: Design Architecture for Real-Time Data Processing)
4. Create Web Interface for Monitoring and Management (P4) -- (depends on: Design Architecture for Real-Time Data Processing)
5. Implement Complex Event Processing Layer (P3) -- (depends on: Design Architecture for Real-Time Data Processing)
6. Perform DevOps Configuration and Setup (P3) -- (depends on: Design Architecture for Real-Time Data Processing)
7. Define Interface for IoT Devices Ingestion (P2) -- (depends on: Design Architecture for Real-Time Data Processing)
8. Set Up Database Schema and Storage Strategy (P2) -- (depends on: Design Architecture for Real-Time Data Processing)
9. Perform Security Audit and Risk Assessment (P1) -- (depends on: Design Architecture for Real-Time Data Processing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeIoTDataProcessingPlatform can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for ingesting and processing data from millions of IoT devices in real-time, with support.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
