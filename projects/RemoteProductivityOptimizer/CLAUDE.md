# RemoteProductivityOptimizer

You are a coding agent working on RemoteProductivityOptimizer -- A platform that helps remote workers optimize their home office setup and daily routines for maximum productivity and well-being.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; RemoteProductivityOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: requirements gathering and analysis for remoteproductivityoptimizer
- Data layer: database design for remoteproductivityoptimizer

## Anti-Goals

- **General-purpose platform**: RemoteProductivityOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. SystemArchitectureDesign (P5) -- (depends on: RequirementsGatheringandAnalysis)
2. Requirements Gathering and Analysis for RemoteProductivityOptimizer (P2)
3. Database Design for RemoteProductivityOptimizer (P3) -- (depends on: Requirements Gathering and Analysis)
4. Frontend Development (P4) -- (depends on: System Architecture Design, Database Design)
5. Backend Development (P4) -- (depends on: System Architecture Design, Database Design)
6. Documentation and User Support (P5) -- (depends on: Frontend Development, Backend Development)
7. DevOps and Deployment (P4) -- (depends on: Frontend Development, Backend Development)
8. Testing and Quality Assurance (P4) -- (depends on: Frontend Development, Backend Development)
9. Security Auditing and Compliance (P4) -- (depends on: Frontend Development, Backend Development)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RemoteProductivityOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- PostgreSQL
- MongoDB
- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that helps remote workers optimize their home office setup and daily routines for maximum.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
