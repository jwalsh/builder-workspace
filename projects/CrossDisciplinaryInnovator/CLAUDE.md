# CrossDisciplinaryInnovator

You are a coding agent working on CrossDisciplinaryInnovator -- An AI system that generates innovative ideas by combining concepts from different scientific disciplines.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; CrossDisciplinaryInnovator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement ai processing algorithms
- User interface: define project scope and requirements
- Data layer: develop data collection module

## Anti-Goals

- **General-purpose platform**: CrossDisciplinaryInnovator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design AI System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Data Collection Module (P3) -- (depends on: Design AI System Architecture)
4. Implement AI Processing Algorithms (P4) -- (depends on: Develop Data Collection Module, Design AI System Architecture)
5. Create User Interface for Idea Generation (P5) -- (depends on: Implement AI Processing Algorithms)
6. Perform System Audit (P5) -- (depends on: Implement AI Processing Algorithms)
7. Test AI System Functionality (P2) -- (depends on: Implement AI Processing Algorithms)
8. Deploy AI System for User Testing (P3) -- (depends on: Test AI System Functionality)
9. Gather User Feedback and Iterate (P4) -- (depends on: Deploy AI System for User Testing)
10. Iterate on AI System and Improve Performance (P5) -- (depends on: Gather User Feedback and Iterate)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossDisciplinaryInnovator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that generates innovative ideas by combining concepts from different scientific discipl.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
