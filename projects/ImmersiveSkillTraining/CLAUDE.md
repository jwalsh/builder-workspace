# ImmersiveSkillTraining

You are a coding agent working on ImmersiveSkillTraining -- A platform for immersive skill training simulations across various industries, from surgery to space exploration.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; ImmersiveSkillTraining closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend
- User interface: requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: ImmersiveSkillTraining solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning (P1)
2. Requirements Gathering (P2) -- (depends on: Project Planning)
3. Design the Architecture (P3) -- (depends on: Requirements Gathering)
4. Develop the Simulation Models (P5) -- (depends on: Design the Architecture)
5. Develop the Backend (P4) -- (depends on: Design the Architecture)
6. Documentation (P5) -- (depends on: Develop the Frontend, Develop the Backend)
7. Database Design and Implementation (P4) -- (depends on: Design the Architecture)
8. Testing and Quality Assurance (P4) -- (depends on: Develop the Frontend, Develop the Backend)
9. DevOps Configuration (P3) -- (depends on: Design the Architecture)
10. Refined Requirements Gathering for Immersive Skill Training Platform - Revised (P2) -- (depends on: Project Planning)
11. Security Audit (P2) -- (depends on: Design the Architecture)
12. Deployment and Launch (P1) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ImmersiveSkillTraining can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for immersive skill training simulations across various industries, from surgery to space.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
