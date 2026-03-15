# CodingConceptMindMapper

You are a coding agent working on CodingConceptMindMapper -- A tool that helps users create and explore mind maps of coding concepts, reinforcing understanding of relationships between ideas.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; CodingConceptMindMapper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements
- Data layer: set up database and data models

## Anti-Goals

- **General-purpose platform**: CodingConceptMindMapper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and requirements (P5)
2. Design system architecture (P5) -- (depends on: Define project scope and requirements)
3. Develop backend services (P2) -- (depends on: Design system architecture)
4. Design user interface and experience for CodingConceptMindMapper (P3) -- (depends on: Define project scope and requirements)
5. Develop frontend application (P2) -- (depends on: Design user interface and experience, Develop backend services)
6. Implement security measures (P4) -- (depends on: Develop backend services, Develop frontend application)
7. Set up database and data models (P3) -- (depends on: Design system architecture)
8. Set up continuous integration and deployment (P3) -- (depends on: Develop backend services, Develop frontend application)
9. Write documentation and user guides (P2) -- (depends on: Develop frontend application)
10. Conduct testing and quality assurance (P2) -- (depends on: Develop backend services, Develop frontend application)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodingConceptMindMapper can deliver its core value proposition as described
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

- Python
- TypeScript/JavaScript
- PostgreSQL
- MongoDB
- Redis
- Docker
- AWS
- GraphQL
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that helps users create and explore mind maps of coding concepts, reinforcing understanding o.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
