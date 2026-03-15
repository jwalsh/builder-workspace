# PredictiveCreditScoring

You are a coding agent working on PredictiveCreditScoring -- An AI-driven credit scoring system that uses alternative data sources and predictive analytics to provide more accurate and inclusive credit assessments.

## Foundational Axiom

Existing approaches to ai-driven credit scoring system fail because they optimize for the common case while ignoring structural constraints; PredictiveCreditScoring makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data acquisition and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data acquisition and preprocessing

## Anti-Goals

- **General-purpose platform**: PredictiveCreditScoring solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for Predictive Credit Scoring (Revised) (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Data Acquisition and Preprocessing (P3) -- (depends on: System Architecture Design)
4. Machine Learning Model Development (P3) -- (depends on: Data Acquisition and Preprocessing)
5. User Interface Design and Development (P4) -- (depends on: System Architecture Design)
6. Data Security and Privacy (Revised) (P2) -- (depends on: System Architecture Design)
7. Integration and Testing (P4) -- (depends on: Machine Learning Model Development, User Interface Design and Development, Data Security and Privacy)
8. Deployment and Monitoring (P5) -- (depends on: Integration and Testing)
9. Documentation and Training (P4) -- (depends on: Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PredictiveCreditScoring can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-driven credit scoring system that uses alternative data sources and predictive analytics to pr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
