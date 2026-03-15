# NeuroplasticityOptimizer

You are a coding agent working on NeuroplasticityOptimizer -- A device that enhances brain plasticity, dramatically improving learning speed and cognitive flexibility.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroplasticityOptimizer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: create the software for the neuroplasticityoptimizer

## Anti-Goals

- **General-purpose platform**: NeuroplasticityOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design the NeuroplasticityOptimizer device architecture (P1)
2. Develop the device's hardware components (P2) -- (depends on: Design the NeuroplasticityOptimizer device architecture)
3. Create the software for the NeuroplasticityOptimizer (P3) -- (depends on: Design the NeuroplasticityOptimizer device architecture)
4. Integrate the hardware and software components (P4) -- (depends on: Develop the device's hardware components, Create the software for the NeuroplasticityOptimizer)
5. Test and validate the NeuroplasticityOptimizer device (P5) -- (depends on: Integrate the hardware and software components)
6. Document the NeuroplasticityOptimizer device specifications (P5) -- (depends on: Integrate the hardware and software components)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroplasticityOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that enhances brain plasticity, dramatically improving learning speed and cognitive flexibi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
