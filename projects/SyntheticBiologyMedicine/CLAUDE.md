# SyntheticBiologyMedicine

You are a coding agent working on SyntheticBiologyMedicine -- Using synthetic biology to create custom medicines tailored to individual patients.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; SyntheticBiologyMedicine embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Using synthetic biology to create custom medicines tailored to individual patients.

## Anti-Goals

- **General-purpose platform**: SyntheticBiologyMedicine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Synthetic Biology Strategy for Custom Medicine Production (P1)
2. Identify Key Components for Custom Medicine Design (P2) -- (depends on: Define Synthetic Biology Strategy for Custom Medicine Production)
3. Design Custom Synthetic Biological Modules (P4) -- (depends on: Define Synthetic Biology Strategy for Custom Medicine Production, Identify Key Components for Custom Medicine Design)
4. Develop Automated Manufacturing Processes (P5) -- (depends on: Design Custom Synthetic Biological Modules)
5. Develop Personalized Sequencing Techniques (P3) -- (depends on: Identify Key Components for Custom Medicine Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SyntheticBiologyMedicine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Using synthetic biology to create custom medicines tailored to individual patients..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
