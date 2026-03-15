# OracleFarmForcast

You are a coding agent working on OracleFarmForcast -- Satellite imagery of farms is analyzed by AI to forecast crop yield and suggest ways to improve field conditions.

## Foundational Axiom

Existing approaches to satellite imagery of farms is analyzed by ai fail because they optimize for the common case while ignoring structural constraints; OracleFarmForcast makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop api endpoints for model and dashboard
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: OracleFarmForcast solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design AI Model Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop AI Model Algorithms (P3) -- (depends on: Design AI Model Architecture)
4. Conduct Model Training and Validation (P5) -- (depends on: Develop AI Model Algorithms)
5. Design User Interface for Dashboard (P4) -- (depends on: Define Project Scope and Requirements)
6. Implement Dashboard User Interface (P4) -- (depends on: Design User Interface for Dashboard)
7. Test AI Model and Dashboard Functionality (P5) -- (depends on: Implement Dashboard User Interface)
8. Write Technical Documentation (P5) -- (depends on: All other tasks)
9. Develop API Endpoints for Model and Dashboard (P4) -- (depends on: Implement Dashboard User Interface)
10. Integrate AI Model with Dashboard API Endpoints (P4) -- (depends on: Develop API Endpoints for Model and Dashboard)
11. Develop Farm Image Preprocessing Pipeline (P3) -- (depends on: Design AI Model Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OracleFarmForcast can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Satellite imagery of farms is analyzed by AI to forecast crop yield and suggest ways to improve fiel.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to agricultural scientists and farm operators.
