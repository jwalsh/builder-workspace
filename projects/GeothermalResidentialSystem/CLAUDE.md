# GeothermalResidentialSystem

You are a coding agent working on GeothermalResidentialSystem -- A compact, efficient geothermal heating and cooling system designed for residential use.

## Foundational Axiom

The bottleneck in compact, efficient geothermal heating and cooling system designed is not compute or data but the feedback loop between intent and artifact; GeothermalResidentialSystem compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development for geothermalresidentialsystem
- User interface: requirements gathering for geothermalresidentialsystem
- Data layer: database design for geothermalresidentialsystem

## Anti-Goals

- **General-purpose platform**: GeothermalResidentialSystem solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering for GeothermalResidentialSystem (P1)
2. Design Architecture for GeothermalResidentialSystem (P2) -- (depends on: Requirements Gathering for GeothermalResidentialSystem)
3. Database Design for GeothermalResidentialSystem (P3) -- (depends on: Design Architecture for GeothermalResidentialSystem)
4. Frontend Design for GeothermalResidentialSystem (P4) -- (depends on: Design Architecture for GeothermalResidentialSystem)
5. Backend Development for GeothermalResidentialSystem (P4) -- (depends on: Database Design for GeothermalResidentialSystem, Frontend Design for GeothermalResidentialSystem)
6. Integration Testing for GeothermalResidentialSystem (P5) -- (depends on: Backend Development for GeothermalResidentialSystem, Frontend Design for GeothermalResidentialSystem)
7. Deployment Plan for GeothermalResidentialSystem (P5) -- (depends on: Integration Testing for GeothermalResidentialSystem)
8. Security Assessment for GeothermalResidentialSystem (P5) -- (depends on: Deployment Plan for GeothermalResidentialSystem)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GeothermalResidentialSystem can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A compact, efficient geothermal heating and cooling system designed for residential use..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
