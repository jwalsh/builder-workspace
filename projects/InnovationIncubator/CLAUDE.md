# InnovationIncubator

You are a coding agent working on InnovationIncubator -- A platform that encourages and manages employee-driven innovation initiatives, from ideation to implementation.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; InnovationIncubator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements
- Data layer: design scalable, secure and performant database schema for innovationincubator

## Anti-Goals

- **General-purpose platform**: InnovationIncubator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture - RFC Review and Revisions (P5) -- (depends on: Define Project Scope and Requirements, Gather Non-Functional Requirements)
3. Set up Development Environment (P4) -- (depends on: Design System Architecture)
4. Design Scalable, Secure and Performant Database Schema for InnovationIncubator (P4) -- (depends on: Define Project Scope and Requirements, Define User Roles and Permissions)
5. Design User Interface and Experience (UI/UX) - Refactored (P3) -- (depends on: Define Project Scope and Requirements, Conduct User Research and Persona Analysis)
6. Implement Comprehensive Security Measures (Revised) (P3) -- (depends on: Design System Architecture)
7. Implement Backend Services (P2) -- (depends on: Design System Architecture, Design Database Schema)
8. Implement Frontend Components (P2) -- (depends on: Design User Interface and Experience)
9. Write Documentation (P3) -- (depends on: Implement Backend Services, Implement Frontend Components)
10. Conduct Testing and Quality Assurance (P2) -- (depends on: Implement Backend Services, Implement Frontend Components)
11. Deploy and Monitor Platform (P1) -- (depends on: Implement Backend Services, Implement Frontend Components, Conduct Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InnovationIncubator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that encourages and manages employee-driven innovation initiatives, from ideation to impl.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
