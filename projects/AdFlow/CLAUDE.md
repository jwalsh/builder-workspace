# AdFlow

You are a coding agent working on AdFlow -- A comprehensive advertising flow management platform. The system will handle campaign management, content item approval, user management, and campaign auditing.

## Foundational Axiom

Existing approaches to comprehensive advertising flow management platform. the syst fail because they optimize for the common case while ignoring structural constraints; AdFlow makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A comprehensive advertising flow management platform. The system will handle campaign management, co
- User interface: project planning and requirements gathering
- Data layer: database design for adflow

## Anti-Goals

- **General-purpose platform**: AdFlow solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for AdFlow Platform (Updated) (P1) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Compliance (P5) -- (depends on: System Architecture Design)
4. Database Design for AdFlow (P3) -- (depends on: System Architecture Design)
5. User Management Module (P4) -- (depends on: System Architecture Design, Database Design)
6. Campaign Management Module (P4) -- (depends on: System Architecture Design, Database Design)
7. Content Approval Module (P4) -- (depends on: System Architecture Design, Database Design)
8. Campaign Auditing Module (P4) -- (depends on: System Architecture Design, Database Design)
9. Integration and Testing (P5) -- (depends on: User Management Module, Campaign Management Module, Content Approval Module, Campaign Auditing Module)
10. Deployment and DevOps (P5) -- (depends on: Integration and Testing)
11. Documentation and User Training (P5) -- (depends on: Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AdFlow can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- MongoDB
- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive advertising flow management platform. The system will handle campaign management, co.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
