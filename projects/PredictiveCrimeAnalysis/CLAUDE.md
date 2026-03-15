# PredictiveCrimeAnalysis

You are a coding agent working on PredictiveCrimeAnalysis -- An AI system that analyzes crime data and social factors to predict potential crime hotspots and optimize police resource allocation.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; PredictiveCrimeAnalysis makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that analyzes crime data and social factors to predict potential crime hotspots and opt
- User interface: requirements gathering and analysis
- Data layer: data pipeline and etl

## Anti-Goals

- **General-purpose platform**: PredictiveCrimeAnalysis solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design (P5) -- (depends on: Requirements Gathering and Analysis)
3. Data Pipeline and ETL (P4) -- (depends on: System Architecture Design)
4. Machine Learning Model Development (P4) -- (depends on: System Architecture Design, Data Pipeline and ETL)
5. User Interface and Visualization (P4) -- (depends on: System Architecture Design)
6. Testing and Quality Assurance (P5) -- (depends on: Data Pipeline and ETL, Machine Learning Model Development, User Interface and Visualization)
7. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
8. Documentation and Training (P5) -- (depends on: User Interface and Visualization, Deployment and DevOps)
9. Security and Privacy Considerations (P4) -- (depends on: System Architecture Design)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PredictiveCrimeAnalysis can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that analyzes crime data and social factors to predict potential crime hotspots and opt.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
