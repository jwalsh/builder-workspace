# LearningAchievementSystem

You are a coding agent working on LearningAchievementSystem -- A gamified learning platform that rewards progress and achievement across various educational domains.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; LearningAchievementSystem closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development tasks
- User interface: requirements gathering and analysis
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: LearningAchievementSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Initiation and Planning (P1)
2. Requirements Gathering and Analysis (P2) -- (depends on: Project Initiation and Planning)
3. Design the LearningAchievementSystem Architecture (P3) -- (depends on: Requirements Gathering and Analysis)
4. Implement Security Measures (P5) -- (depends on: Design the LearningAchievementSystem Architecture)
5. Frontend Development Tasks (P4) -- (depends on: Design the LearningAchievementSystem Architecture)
6. Backend Development Tasks (P4) -- (depends on: Design the LearningAchievementSystem Architecture)
7. Testing and Quality Assurance (P5) -- (depends on: Frontend Development Tasks, Backend Development Tasks)
8. Perform Code Reviews (P4) -- (depends on: Frontend Development Tasks, Backend Development Tasks)
9. Deploy the LearningAchievementSystem (P5) -- (depends on: Code Reviews, Testing and Quality Assurance)
10. Post-Deployment Monitoring and Maintenance (P5) -- (depends on: Deploy the LearningAchievementSystem)
11. Database Design and Implementation (P4) -- (depends on: Design the LearningAchievementSystem Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LearningAchievementSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A gamified learning platform that rewards progress and achievement across various educational domain.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
