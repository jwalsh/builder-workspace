# GoalJourneyStoryboard

You are a coding agent working on GoalJourneyStoryboard -- A visual tool that allows employees to create and share 'storylines' of their goal achievement journeys.

## Foundational Axiom

Existing approaches to visual tool fail because they optimize for the common case while ignoring structural constraints; GoalJourneyStoryboard makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: GoalJourneyStoryboard solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Design System Architecture for GoalJourneyStoryboard (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design and Implementation (P3) -- (depends on: Design System Architecture)
4. Backend Development (P4) -- (depends on: Design System Architecture, Database Design and Implementation)
5. Frontend Development (P4) -- (depends on: Design System Architecture)
6. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development)
7. Deployment and DevOps (P4) -- (depends on: Backend Development, Frontend Development)
8. Documentation and User Guide (P3) -- (depends on: Backend Development, Frontend Development)
9. Security and Access Control (Revised) (P1) -- (depends on: Design System Architecture, Define User Roles and Permissions)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GoalJourneyStoryboard can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A visual tool that allows employees to create and share 'storylines' of their goal achievement journ.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
