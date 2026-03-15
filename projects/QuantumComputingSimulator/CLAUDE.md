# QuantumComputingSimulator

You are a coding agent working on QuantumComputingSimulator -- A simulation environment for learning quantum computing concepts through interactive coding exercises.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumComputingSimulator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: quantum computing simulation engine development
- User interface: project planning and requirements gathering
- Data layer: datastorageandpersistence

## Anti-Goals

- **General-purpose platform**: QuantumComputingSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design and System Planning (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Compliance (P4) -- (depends on: Architecture Design and System Planning)
4. User Interface Design and Development (P3) -- (depends on: Architecture Design and System Planning)
5. Quantum Computing Simulation Engine Development (P3) -- (depends on: Architecture Design and System Planning)
6. Testing and Quality Assurance (P3) -- (depends on: User Interface Design and Development, Quantum Computing Simulation Engine Development, Data Storage and Persistence)
7. Deployment and DevOps (P3) -- (depends on: User Interface Design and Development, Quantum Computing Simulation Engine Development, Data Storage and Persistence, Testing and Quality Assurance)
8. DataStorageandPersistence (P2) -- (depends on: ArchitectureDesignandSystemPlanning)
9. Documentation and User Guides (P2) -- (depends on: User Interface Design and Development, Quantum Computing Simulation Engine Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumComputingSimulator can deliver its core value proposition as described
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

- PostgreSQL
- MongoDB
- Redis
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A simulation environment for learning quantum computing concepts through interactive coding exercise.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
