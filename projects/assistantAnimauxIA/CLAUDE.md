# assistantAnimauxIA

You are a coding agent working on assistantAnimauxIA -- an AI-powered assistant that monitors domestic animal behavior and health in real time.

## Foundational Axiom

Existing approaches to real-time animal behavior monitoring fail because they optimize for the common case while ignoring structural constraints; assistantAnimauxIA makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and its dependency graph.
3. You will stop on any failing acceptance test and surface it as a CPRR refutation candidate.

## What You Are Building

- A Python-based backend for real-time ingestion and ML inference on animal sensor data.
- A frontend for data input and visualization of animal health insights.
- A scalable database layer for storing and querying animal behavior records.

## Anti-Goals

- **General-purpose platform**: This solves a specific monitoring problem, not a platform for all pet-tech.
- **Manual-first workflow**: If a human must babysit routine operations, the automation has failed.
- **Demo-ware**: Never optimize for impressive demos at the cost of production reliability.

## Build Order

1. Define project scope and requirements (P1, project-manager)
2. Design the AI model architecture (P2, code-architect; depends on 1)
3. Develop the frontend for data input and visualization (P3, frontend-developer; depends on 1)
4. Develop the backend for real-time data processing (P3, backend-developer; depends on 2)
5. Establish a database structure for animal data and insights (P4, database-specialist; depends on 4)
6. Implement necessary security measures (P5, security-specialist; depends on 3)
7. Conduct system testing and integration (P2, qa-tester; depends on 3, 4)

### Failure Handler

If an acceptance test fails, **stop**. Document what failed, what you tried, and what the blocker is. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

| ID    | Claim                                                        | Falsification                                                        |
|-------|--------------------------------------------------------------|----------------------------------------------------------------------|
| C-001 | Core value proposition can be delivered as described          | End-to-end integration test fails to produce expected output         |
| C-002 | AI/ML components achieve sufficient accuracy for production  | Model accuracy on held-out test set falls below domain threshold     |
| C-003 | System meets real-time latency requirements under load       | P95 latency exceeds target under simulated production load           |
| C-004 | Architecture scales horizontally to meet projected demand    | Load test shows non-linear degradation before target throughput      |

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: real-time animal behavior and health monitoring.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to primary users (UX researchers and interaction designers).

## Stack

- Python (default)
