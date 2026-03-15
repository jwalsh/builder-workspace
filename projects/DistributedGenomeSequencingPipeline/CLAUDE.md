# DistributedGenomeSequencingPipeline

You are a coding agent working on DistributedGenomeSequencingPipeline -- A distributed pipeline for large-scale genome sequencing and analysis, processing massive amounts of genetic data across a cluster.

## Foundational Axiom

Existing approaches to distributed pipeline fail because they optimize for the common case while ignoring structural constraints; DistributedGenomeSequencingPipeline makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend components for data processing
- User interface: define project requirements and goals
- Data layer: implement backend components for data processing

## Anti-Goals

- **General-purpose platform**: DistributedGenomeSequencingPipeline solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements and Goals (P1)
2. Design Architecture of the Pipeline (P2) -- (depends on: Define Project Requirements and Goals)
3. Implement Backend Components for Data Processing (P3) -- (depends on: Design Architecture of the Pipeline)
4. Develop Scalable Data Storage Solutions (P3) -- (depends on: Design Architecture of the Pipeline)
5. Implement Distributed Computing Solutions (P3) -- (depends on: Design Architecture of the Pipeline)
6. Implement Analysis and Visualization Tools (P3) -- (depends on: Design Architecture of the Pipeline)
7. Document System Architecture and Usage (P5) -- (depends on: Design Architecture of the Pipeline, Implement Frontend Interface for Data Submission, Implement Backend Components for Data Processing, Develop Scalable Data Storage Solutions, Implement Distributed Computing Solutions, Implement Analysis and Visualization Tools)
8. Develop Frontend Interface for Data Submission (P3) -- (depends on: Design Architecture of the Pipeline)
9. Define Project Requirements and Goals - RFC Review (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DistributedGenomeSequencingPipeline can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A distributed pipeline for large-scale genome sequencing and analysis, processing massive amounts of.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
