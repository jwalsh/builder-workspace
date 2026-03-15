# AugmentedRealityEducation

You are a coding agent working on AugmentedRealityEducation -- An AR platform that immerses students in interactive learning environments.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; AugmentedRealityEducation closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop ar rendering engine
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: AugmentedRealityEducation solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design AR Learning Platform Architecture - REVISED (P2) -- (depends on: Define Project Scope and Requirements, Determine User Roles and Permissions, Specify Data Privacy Considerations, Design Error Handling Mechanisms, Plan Performance Optimization Strategies)
3. Develop AR Rendering Engine (P3) -- (depends on: Design AR Learning Platform Architecture)
4. Build Content Management System (P3) -- (depends on: Design AR Learning Platform Architecture)
5. Design User Interface and Experience (Revised) (P3) -- (depends on: Design AR Learning Platform Architecture)
6. Conduct User Acceptance Testing (P5) -- (depends on: Develop AR Rendering Engine, Build Content Management System, Design User Interface and Experience)
7. Write Documentation and User Guides (P5) -- (depends on: Design User Interface and Experience)
8. Implement Security and Privacy Measures (P4) -- (depends on: Design AR Learning Platform Architecture)
9. Set up Continuous Integration and Deployment (P4) -- (depends on: Design AR Learning Platform Architecture)
10. Deploy and Launch AR Learning Platform (P5) -- (depends on: Develop AR Rendering Engine, Build Content Management System, Design User Interface and Experience, Implement Security and Privacy Measures, Set up Continuous Integration and Deployment, Conduct User Acceptance Testing, Write Documentation and User Guides)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AugmentedRealityEducation can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AR platform that immerses students in interactive learning environments..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
