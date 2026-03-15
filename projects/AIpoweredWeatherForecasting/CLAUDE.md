# AIpoweredWeatherForecasting

You are a coding agent working on AIpoweredWeatherForecasting -- An AI system that improves the accuracy of weather forecasting, optimizing renewable energy production and distribution.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; AIpoweredWeatherForecasting maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data collection and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data collection and preprocessing

## Anti-Goals

- **General-purpose platform**: AIpoweredWeatherForecasting solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Data Collection and Preprocessing (P3) -- (depends on: Project Planning and Requirements Gathering)
4. AI Model Development (P3) -- (depends on: Data Collection and Preprocessing)
5. User Interface Design (P3) -- (depends on: Project Planning and Requirements Gathering)
6. Integration with Renewable Energy Systems (P3) -- (depends on: AI Model Development)
7. Testing and Validation (P2) -- (depends on: AI Model Development, User Interface Design, Integration with Renewable Energy Systems)
8. Security and Compliance (P2) -- (depends on: System Architecture Design)
9. Deployment and Monitoring (P2) -- (depends on: Testing and Validation, Security and Compliance)
10. Documentation and Training (P2) -- (depends on: User Interface Design, Integration with Renewable Energy Systems)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIpoweredWeatherForecasting can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that improves the accuracy of weather forecasting, optimizing renewable energy producti.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
