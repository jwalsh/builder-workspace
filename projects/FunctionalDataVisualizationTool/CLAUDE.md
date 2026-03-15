# FunctionalDataVisualizationTool

You are a coding agent working on FunctionalDataVisualizationTool -- A data visualization library that uses a functional approach to create composable, declarative data visualizations.

## Foundational Axiom

Existing approaches to data visualization library fail because they optimize for the common case while ignoring structural constraints; FunctionalDataVisualizationTool makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development tasks
- User interface: project initiation and requirements gathering
- Data layer: functional data visualization library design

## Anti-Goals

- **General-purpose platform**: FunctionalDataVisualizationTool solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation and Requirements Gathering (P1)
2. Design Phase (P2) -- (depends on: Project Initiation and Requirements Gathering)
3. Functional Data Visualization Library Design (P2) -- (depends on: Design Phase)
4. Frontend Development Tasks (P3) -- (depends on: Functional Data Visualization Library Design)
5. Backend Development Tasks (P3) -- (depends on: Functional Data Visualization Library Design)
6. Testing Phase (P4) -- (depends on: Frontend Development Tasks, Backend Development Tasks)
7. Code Review and Refinement (P4) -- (depends on: Testing Phase)
8. Documentation and Knowledge Base Creation (Revised) (P5) -- (depends on: Code Review and Refinement)
9. Deployment Planning (P5) -- (depends on: Code Review and Refinement)
10. Security Assessment and Vulnerability Fixing (P5) -- (depends on: Code Review and Refinement)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FunctionalDataVisualizationTool can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A data visualization library that uses a functional approach to create composable, declarative data .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
