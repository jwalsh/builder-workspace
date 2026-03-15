# IoTBasedAnimalTracking

You are a coding agent working on IoTBasedAnimalTracking -- An IoT system for tracking the movement and health of wild or domestic animals.

## Foundational Axiom

Existing approaches to iot system fail because they optimize for the common case while ignoring structural constraints; IoTBasedAnimalTracking makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: develop frontend interface design
- Data layer: create database schema and models

## Anti-Goals

- **General-purpose platform**: IoTBasedAnimalTracking solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
2. Document System Functionality (P5) -- (depends on: Design System Architecture)
3. Implement Backend Services (P3) -- (depends on: Design System Architecture)
4. Set Up IoT Device Integration (P4) -- (depends on: Implement Backend Services)
5. Write Unit Tests for Core Functionality (P4) -- (depends on: Implement Backend Services)
6. Develop Frontend Interface Design (P3) -- (depends on: Design System Architecture)
7. Create Database Schema and Models (P3) -- (depends on: Implement Backend Services)
8. Conduct Code Review for Frontend Components (P3) -- (depends on: Develop Frontend Interface Design)
9. Conduct Code Review for Backend Services (P3) -- (depends on: Implement Backend Services)
10. Define Project Scope and Functional/Non-Functional Requirements for IoT-based Animal Tracking System (Revised) (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: IoTBasedAnimalTracking can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An IoT system for tracking the movement and health of wild or domestic animals..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
