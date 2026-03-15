# FlexTimeOptimizer

You are a coding agent working on FlexTimeOptimizer -- A system that helps employees find their optimal work schedule based on their productivity patterns and personal commitments.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; FlexTimeOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that helps employees find their optimal work schedule based on their productivity patterns 
- User interface: project planning and requirements gathering
- Data layer: database design for flextimeoptimizer

## Anti-Goals

- **General-purpose platform**: FlexTimeOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design - FlexTimeOptimizer (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Access Control (P4) -- (depends on: System Architecture Design)
4. Deployment and DevOps Planning (Revised) (P4) -- (depends on: System Architecture Design)
5. Database Design for FlexTimeOptimizer (P3) -- (depends on: System Architecture Design)
6. User Interface Design (UI/UX) - Review and Update (P3) -- (depends on: System Architecture Design, User Research and Persona Development)
7. Documentation Planning - FlexTimeOptimizer (P3) -- (depends on: System Architecture Design, User Interface Design, Data Model Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FlexTimeOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes
- AWS
- GraphQL
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that helps employees find their optimal work schedule based on their productivity patterns .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
