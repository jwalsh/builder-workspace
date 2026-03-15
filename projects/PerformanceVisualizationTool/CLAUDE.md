# PerformanceVisualizationTool

You are a coding agent working on PerformanceVisualizationTool -- A data visualization platform that helps employees understand their performance metrics in relation to their goals and team averages.

## Foundational Axiom

Existing approaches to data visualization platform fail because they optimize for the common case while ignoring structural constraints; PerformanceVisualizationTool makes those constraints first-class.

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

- **General-purpose platform**: PerformanceVisualizationTool solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design - Revised (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
4. Backend Development (P4) -- (depends on: System Architecture Design, Database Design and Implementation)
5. Frontend Development (P4) -- (depends on: System Architecture Design)
6. Deployment and DevOps (P5) -- (depends on: Backend Development, Frontend Development, Database Design and Implementation)
7. Testing and Quality Assurance (P4) -- (depends on: Backend Development, Frontend Development)
8. Documentation and User Training (P4) -- (depends on: Backend Development, Frontend Development)
9. Security and Compliance (P3) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PerformanceVisualizationTool can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A data visualization platform that helps employees understand their performance metrics in relation .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
