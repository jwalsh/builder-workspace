# DistributedQuantumComputingSimulator

You are a coding agent working on DistributedQuantumComputingSimulator -- A distributed system for simulating quantum circuits and algorithms across a classical computing cluster, enabling large-scale quantum research.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; DistributedQuantumComputingSimulator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: cluster management software development
- User interface: requirements gathering
- Data layer: database schema design and implementation

## Anti-Goals

- **General-purpose platform**: DistributedQuantumComputingSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering (P1)
2. System Architecture Design (P2) -- (depends on: Requirements Gathering)
3. DevOps Infrastructure Setup and Configuration (P5) -- (depends on: System Architecture Design)
4. Security Assessment and Implementation (P5) -- (depends on: System Architecture Design)
5. Cluster Management Software Development (P3) -- (depends on: System Architecture Design)
6. Quantum Circuit Simulation Algorithm Design (P3) -- (depends on: System Architecture Design)
7. Frontend Interface Design and Development (P4) -- (depends on: System Architecture Design)
8. Database Schema Design and Implementation (P4) -- (depends on: System Architecture Design)
9. Unit and Integration Testing (P2) -- (depends on: Cluster Management Software Development, Quantum Circuit Simulation Algorithm Design, Frontend Interface Design and Development, Database Schema Design and Implementation)
10. System Integration and Acceptance Testing (P1) -- (depends on: Unit and Integration Testing)
11. Deployment Planning (P5) -- (depends on: Unit and Integration Testing, System Integration and Acceptance Testing)
12. Deployment Execution (P1) -- (depends on: Deployment Planning)
13. Documentation Development (P5) -- (depends on: Deployment Execution)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedQuantumComputingSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed system for simulating quantum circuits and algorithms across a classical computing clu.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
