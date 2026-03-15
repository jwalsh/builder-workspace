# SmartShelfSystem

You are a coding agent working on SmartShelfSystem -- An IoT-based shelf system that tracks inventory in real-time and optimizes product placement.

## Foundational Axiom

Existing approaches to iot-based shelf system fail because they optimize for the common case while ignoring structural constraints; SmartShelfSystem makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop cloud infrastructure and apis
- User interface: design user interface for web and mobile apps
- Data layer: implement database structure

## Anti-Goals

- **General-purpose platform**: SmartShelfSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop Cloud Infrastructure and APIs (P3) -- (depends on: Define System Architecture)
3. Implement Database Structure (P5) -- (depends on: Develop Cloud Infrastructure and APIs)
4. Design User Interface for Web and Mobile Apps (P4) -- (depends on: Develop Cloud Infrastructure and APIs)
5. Document System Functionality (P3) -- (depends on: Define System Architecture)
6. Develop IoT Hardware Components (P2) -- (depends on: Define System Architecture)
7. Perform Security Audit (P2) -- (depends on: Develop Cloud Infrastructure and APIs)
8. Conduct System Integration Testing (P1) -- (depends on: Develop Cloud Infrastructure and APIs, Design User Interface for Web and Mobile Apps)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartShelfSystem can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An IoT-based shelf system that tracks inventory in real-time and optimizes product placement..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
