# RedSmartGrid

You are a coding agent working on RedSmartGrid -- Una red eléctrica inteligente que optimiza la distribución de energía para maximizar la eficiencia y sostenibilidad.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; RedSmartGrid maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Una red eléctrica inteligente que optimiza la distribución de energía para maximizar la eficiencia y
- User interface: create user interface for grid management

## Anti-Goals

- **General-purpose platform**: RedSmartGrid solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Architecture (P1)
2. Create Technical Documentation for RedSmartGrid System Design and Implementation (P5) -- (depends on: Define Project Architecture)
3. Create User Interface for Grid Management (P4) -- (depends on: Define Project Architecture)
4. Implement Energy Optimization Algorithms (P3) -- (depends on: Define Project Architecture)
5. Design Smart Meter Integration (P2) -- (depends on: Define Project Architecture)
6. Review Technical Documentation (RFC) (P1) -- (depends on: Write Technical Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RedSmartGrid can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una red eléctrica inteligente que optimiza la distribución de energía para maximizar la eficiencia y.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
