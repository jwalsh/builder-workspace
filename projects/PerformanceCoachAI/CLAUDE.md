# PerformanceCoachAI

You are a coding agent working on PerformanceCoachAI -- An AI-driven coaching assistant that provides personalized advice on improving work performance based on individual goals and challenges.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; PerformanceCoachAI captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI-driven coaching assistant that provides personalized advice on improving work performance base
- User interface: project planning and requirements gathering
- Data layer: data pipeline implementation

## Anti-Goals

- **General-purpose platform**: PerformanceCoachAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for PerformanceCoachAI (P5) -- (depends on: Project Planning and Requirements Gathering, Data Collection and Preparation)
3. AI Model Development (P3) -- (depends on: System Architecture Design)
4. Data Pipeline Implementation (P3) -- (depends on: System Architecture Design)
5. User Interface Design and Development (P3) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design, Data Modeling)
7. Security and Privacy Considerations (P2) -- (depends on: System Architecture Design)
8. Integration and System Testing (P2) -- (depends on: AI Model Development, Data Pipeline Implementation, User Interface Design and Development, Database Design and Implementation)
9. Deployment and DevOps (P2) -- (depends on: Integration and System Testing)
10. Documentation and User Guides (P1) -- (depends on: User Interface Design and Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PerformanceCoachAI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- MongoDB
- Redis
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-driven coaching assistant that provides personalized advice on improving work performance base.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
