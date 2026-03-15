# UrbanPlanningAI

You are a coding agent working on UrbanPlanningAI -- An AI system that optimizes city planning by considering factors such as traffic flow, energy efficiency, and quality of life.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; UrbanPlanningAI makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that optimizes city planning by considering factors such as traffic flow, energy effici

## Anti-Goals

- **General-purpose platform**: UrbanPlanningAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define AI System Architecture (P1)
2. Create AI Traffic Flow Model (Revised) (P2) -- (depends on: Define AI System Architecture)
3. Develop Energy Efficiency Model (P3) -- (depends on: Define AI System Architecture)
4. Improve Quality of Life Model (P4) -- (depends on: Define AI System Architecture)
5. Integrate Models into AI System (P5) -- (depends on: Create AI Traffic Flow Model, Develop Energy Efficiency Model, Improve Quality of Life Model)
6. Document the System Design and Implementation (P5) -- (depends on: Integrate Models into AI System)
7. Test and Validate the System (P1) -- (depends on: Integrate Models into AI System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: UrbanPlanningAI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that optimizes city planning by considering factors such as traffic flow, energy effici.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to urban planners and city administrators.
