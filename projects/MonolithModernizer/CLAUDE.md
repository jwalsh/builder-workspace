# MonolithModernizer

You are a coding agent working on MonolithModernizer -- Expand on-premises monoliths to the cloud, reducing latency for global users while maintaining transactional isolation using CQRS and read-local write-global patterns.

## Foundational Axiom

Existing approaches to expand on-premises monoliths to the cloud, reducing latency fail because they optimize for the common case while ignoring structural constraints; MonolithModernizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Expand on-premises monoliths to the cloud, reducing latency for global users while maintaining trans
- User interface: design user interface and experience for distributed application
- Data layer: design data storage and replication strategy for monolithmodernizer

## Anti-Goals

- **General-purpose platform**: MonolithModernizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Architecture Design (P1)
2. Design CQRS and Event-Driven Architecture for Distributed System - RFC (P3) -- (depends on: Project Planning and Architecture Design)
3. Design Data Storage and Replication Strategy for MonolithModernizer (P3) -- (depends on: Project Planning and Architecture Design)
4. Conduct Security and Compliance Review (P4) -- (depends on: Project Planning and Architecture Design)
5. Plan Cloud Infrastructure and Deployment for MonolithModernizer Project (Updated) (P4) -- (depends on: Project Planning and Architecture Design, Security and Compliance Review)
6. Design User Interface and Experience for Distributed Application (P4) -- (depends on: Project Planning and Architecture Design, Distributed Application Backend Design, Performance Optimization Strategies)
7. Document Architecture and Implementation (P5) -- (depends on: Project Planning and Architecture Design, Design CQRS and Event-Driven Architecture, Design Data Storage and Replication Strategy, Plan Cloud Infrastructure and Deployment, Design User Interface and Experience)
8. Revised Testing and Quality Assurance Strategy (Planning Complete) (P4) -- (depends on: Project Planning and Architecture Design)
9. Analyze Existing Monolithic Application (P2)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MonolithModernizer can deliver its core value proposition as described
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
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Expand on-premises monoliths to the cloud, reducing latency for global users while maintaining trans.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
