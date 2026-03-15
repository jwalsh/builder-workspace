# AirPollutionCaptureTree

You are a coding agent working on AirPollutionCaptureTree -- An artificial tree-like structure that efficiently captures air pollutants and CO2 from urban environments.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; AirPollutionCaptureTree captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An artificial tree-like structure that efficiently captures air pollutants and CO2 from urban enviro
- User interface: project planning and requirements gathering for airpollutioncapturetree

## Anti-Goals

- **General-purpose platform**: AirPollutionCaptureTree solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering for AirPollutionCaptureTree (P5)
2. System Architecture Design - Revised (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Air Filtration Mechanism Development (P3) -- (depends on: System Architecture Design)
4. Tree Structure Design and Implementation (P3) -- (depends on: System Architecture Design)
5. Security and Compliance (P3) -- (depends on: System Architecture Design)
6. Urban Integration and Deployment (P2) -- (depends on: Air Filtration Mechanism Development, Tree Structure Design and Implementation)
7. Testing and Quality Assurance (P2) -- (depends on: Air Filtration Mechanism Development, Tree Structure Design and Implementation, Urban Integration and Deployment)
8. Documentation and User Guides (P2) -- (depends on: Air Filtration Mechanism Development, Tree Structure Design and Implementation, Urban Integration and Deployment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AirPollutionCaptureTree can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- TypeScript/JavaScript

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An artificial tree-like structure that efficiently captures air pollutants and CO2 from urban enviro.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
