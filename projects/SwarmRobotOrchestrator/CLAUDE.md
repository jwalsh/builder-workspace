# SwarmRobotOrchestrator

You are a coding agent working on SwarmRobotOrchestrator -- Build a control system for coordinating large swarms of robots for tasks such as disaster response or environmental monitoring.

## Foundational Axiom

Autonomous systems fail when they optimize for nominal conditions; SwarmRobotOrchestrator guarantees safe behavior across the full distribution of operating conditions.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Build a control system for coordinating large swarms of robots for tasks such as disaster response o
- User interface: define system requirements
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: SwarmRobotOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements (P5)
2. Design System Architecture for Swarm Robot Orchestrator (Revised) (P5) -- (depends on: Define System Requirements)
3. Implement Security and Access Control (Revised) (P5) -- (depends on: Design System Architecture, Define Communication Protocols)
4. Develop Communication Protocol (P3) -- (depends on: Design System Architecture)
5. Implement Robot Control System (P3) -- (depends on: Design System Architecture, Develop Communication Protocol)
6. Build Swarm Coordination Algorithm (P3) -- (depends on: Design System Architecture, Develop Communication Protocol)
7. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P3)
9. Develop Test Suite (P3) -- (depends on: Design System Architecture)
10. Create User Interface (P2) -- (depends on: Design System Architecture)
11. Write Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SwarmRobotOrchestrator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Build a control system for coordinating large swarms of robots for tasks such as disaster response o.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to robotics engineers and autonomous systems operators.
