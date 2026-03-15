# WaveEnergyConverter

You are a coding agent working on WaveEnergyConverter -- An advanced system for harnessing ocean wave energy, converting it into electricity with minimal environmental impact.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; WaveEnergyConverter maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An advanced system for harnessing ocean wave energy, converting it into electricity with minimal env
- User interface: design user interface and control system
- Data layer: develop power conditioning and storage solution

## Anti-Goals

- **General-purpose platform**: WaveEnergyConverter solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Create Detailed Technical Specifications (P5) -- (depends on: Define System Architecture)
3. Design User Interface and Control System (P4) -- (depends on: Define System Architecture)
4. Develop Power Conditioning and Storage Solution (P3) -- (depends on: Define System Architecture)
5. Design Wave Energy Harvesting Mechanism (P2) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WaveEnergyConverter can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced system for harnessing ocean wave energy, converting it into electricity with minimal env.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
