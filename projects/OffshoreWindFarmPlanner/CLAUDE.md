# OffshoreWindFarmPlanner

You are a coding agent working on OffshoreWindFarmPlanner -- AI-powered software for optimal planning and layout of offshore wind farms, considering environmental factors and energy production efficiency.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; OffshoreWindFarmPlanner maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: AI-powered software for optimal planning and layout of offshore wind farms, considering environmenta
- User interface: project planning and requirements gathering
- Data layer: environmental data integration

## Anti-Goals

- **General-purpose platform**: OffshoreWindFarmPlanner solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering, Environmental Data Analysis, Wind Energy Modeling)
3. Environmental Data Integration (P3) -- (depends on: System Architecture Design)
4. Wind Farm Layout Optimization Algorithm (P3) -- (depends on: System Architecture Design)
5. User Interface Design - Refined (P3) -- (depends on: System Architecture Design)
6. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
7. Security and Access Control (P3) -- (depends on: System Architecture Design)
8. Testing and Quality Assurance (P2) -- (depends on: Environmental Data Integration, Wind Farm Layout Optimization Algorithm, User Interface Design, Database Design and Implementation, Security and Access Control)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)
10. Documentation and User Guides (P2) -- (depends on: User Interface Design, Wind Farm Layout Optimization Algorithm)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: OffshoreWindFarmPlanner can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: AI-powered software for optimal planning and layout of offshore wind farms, considering environmenta.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
