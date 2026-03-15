# DistributedVirtualRealityEnvironment

You are a coding agent working on DistributedVirtualRealityEnvironment -- A platform for creating and maintaining large-scale distributed virtual reality environments, synchronizing state across thousands of users.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; DistributedVirtualRealityEnvironment captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for environment management
- User interface: define project scope and requirements (revised)
- Data layer: implement database structure and queries

## Anti-Goals

- **General-purpose platform**: DistributedVirtualRealityEnvironment solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Architecture Design for Distributed Virtual Reality Environment (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface for User Interaction (P3) -- (depends on: Architecture Design for Distributed Virtual Reality Environment)
4. Develop Backend Services for Environment Management (P3) -- (depends on: Architecture Design for Distributed Virtual Reality Environment)
5. Implement Database Structure and Queries (P4) -- (depends on: Architecture Design for Distributed Virtual Reality Environment)
6. Set Up Continuous Integration/Continuous Deployment Pipeline (P4) -- (depends on: Architecture Design for Distributed Virtual Reality Environment)
7. Perform Unit and Integration Testing (P5) -- (depends on: Develop Frontend Interface for User Interaction, Develop Backend Services for Environment Management, Implement Database Structure and Queries, Set Up Continuous Integration/Continuous Deployment Pipeline)
8. Document Project Architecture, Design Decisions, and Best Practices (P5) -- (depends on: Architecture Design for Distributed Virtual Reality Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedVirtualRealityEnvironment can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for creating and maintaining large-scale distributed virtual reality environments, synchr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
