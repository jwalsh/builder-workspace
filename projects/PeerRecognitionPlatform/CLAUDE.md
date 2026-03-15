# PeerRecognitionPlatform

You are a coding agent working on PeerRecognitionPlatform -- A social platform for employees to publicly recognize and appreciate their colleagues' contributions.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; PeerRecognitionPlatform captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design for peerrecognitionplatform

## Anti-Goals

- **General-purpose platform**: PeerRecognitionPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Access Control (P5) -- (depends on: System Architecture Design, User Management and Authentication)
4. Frontend Development (P4) -- (depends on: System Architecture Design)
5. Database Design for PeerRecognitionPlatform (P2) -- (depends on: System Architecture Design, User Authentication and Authorization)
6. Backend Development (P4) -- (depends on: System Architecture Design, Database Design)
7. Testing and Quality Assurance (P5) -- (depends on: Frontend Development, Backend Development)
8. Deployment and DevOps (P5) -- (depends on: Frontend Developer, Backend Developer, Task-Decomposer, Project Manager, Code-Architect, Database Specialist, QA Tester, Security Specialist)
9. Documentation and User Guides (P4) -- (depends on: System Architecture Design, Frontend Development, Backend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PeerRecognitionPlatform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript
- Java
- PostgreSQL
- MongoDB
- Redis
- Docker
- Kubernetes
- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A social platform for employees to publicly recognize and appreciate their colleagues' contributions.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
