# PredictivePolicing

You are a coding agent working on PredictivePolicing -- An AI-driven system that analyzes crime data, social factors, and environmental conditions to predict potential criminal activities and optimize police patrols.

## Foundational Axiom

Existing approaches to ai-driven system fail because they optimize for the common case while ignoring structural constraints; PredictivePolicing makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data ingestion and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data ingestion and preprocessing

## Anti-Goals

- **General-purpose platform**: PredictivePolicing solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for Predictive Policing System - Revised (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Data Ingestion and Preprocessing (P3) -- (depends on: System Architecture Design)
4. Predictive Modeling (P3) -- (depends on: Data Ingestion and Preprocessing)
5. Patrol Optimization (P3) -- (depends on: Predictive Modeling)
6. User Interface Development (P4) -- (depends on: System Architecture Design)
7. Testing and Quality Assurance (P4) -- (depends on: Data Ingestion and Preprocessing, Predictive Modeling, Patrol Optimization, User Interface Development)
8. Deployment and Monitoring (P5) -- (depends on: Testing and Quality Assurance)
9. Documentation and Training (P4) -- (depends on: User Interface Development)
10. Security and Privacy Measures for Predictive Policing System - RFC Review and Update (P1) -- (depends on: System Architecture Design, Data Collection and Processing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PredictivePolicing can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-driven system that analyzes crime data, social factors, and environmental conditions to predic.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
