# GravityEnergyStorage

You are a coding agent working on GravityEnergyStorage -- An energy storage system that uses gravity, lifting heavy weights when energy is abundant and lowering them to generate electricity when needed.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; GravityEnergyStorage maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop software components
- User interface: define project requirements for gravity energy storage system
- Data layer: define project requirements for gravity energy storage system

## Anti-Goals

- **General-purpose platform**: GravityEnergyStorage solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements for Gravity Energy Storage System (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Develop Mechanical Components (P3) -- (depends on: Design System Architecture)
4. Develop Electrical Components (P3) -- (depends on: Design System Architecture)
5. Develop Software Components (P3) -- (depends on: Design System Architecture)
6. Integrate System Components (P2) -- (depends on: Develop Mechanical Components, Develop Electrical Components, Develop Software Components)
7. Test and Validate System (P2) -- (depends on: Integrate System Components)
8. Deploy and Maintain System (P1) -- (depends on: Test and Validate System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GravityEnergyStorage can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An energy storage system that uses gravity, lifting heavy weights when energy is abundant and loweri.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
