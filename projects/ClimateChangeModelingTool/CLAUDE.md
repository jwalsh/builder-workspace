# ClimateChangeModelingTool

You are a coding agent working on ClimateChangeModelingTool -- An advanced simulation tool for modeling climate change scenarios and their potential impacts.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; ClimateChangeModelingTool captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: climate modeling and simulation engine
- User interface: project planning and requirements gathering
- Data layer: data modeling and database design for climatechangemodelingtool

## Anti-Goals

- **General-purpose platform**: ClimateChangeModelingTool solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for ClimateChangeModelingTool (P1) -- (depends on: Project Planning and Requirements Gathering)
3. Data Modeling and Database Design for ClimateChangeModelingTool (P3) -- (depends on: System Architecture Design)
4. Climate Modeling and Simulation Engine (P4) -- (depends on: System Architecture Design, Data Modeling and Database Design)
5. User Interface and Visualization (P4) -- (depends on: System Architecture Design)
6. Testing and Quality Assurance (P5) -- (depends on: Climate Modeling and Simulation Engine, User Interface and Visualization)
7. Deployment and DevOps (P4) -- (depends on: System Architecture Design, Security Architecture Review)
8. Security and Access Control (Revised) (P3) -- (depends on: System Architecture Design)
9. Documentation and User Support (P3) -- (depends on: User Interface and Visualization)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ClimateChangeModelingTool can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- MongoDB
- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced simulation tool for modeling climate change scenarios and their potential impacts..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
