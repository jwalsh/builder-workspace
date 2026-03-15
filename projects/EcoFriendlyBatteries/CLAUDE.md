# EcoFriendlyBatteries

You are a coding agent working on EcoFriendlyBatteries -- Advanced batteries made from environmentally friendly materials for longer energy storage.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; EcoFriendlyBatteries captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Advanced batteries made from environmentally friendly materials for longer energy storage.

## Anti-Goals

- **General-purpose platform**: EcoFriendlyBatteries solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Develop a prototype design for the EcoFriendlyBatteries (P2) -- (depends on: Research and compile a list of eco-friendly materials for battery production)
2. Create 3D models for the prototype design (P2) -- (depends on: Develop a prototype design for the EcoFriendlyBatteries)
3. Source eco-friendly materials for prototype production (P3) -- (depends on: Research and compile a list of eco-friendly materials for battery production)
4. Manufacture the prototype EcoFriendlyBattery (P4) -- (depends on: Create 3D models for the prototype design, Source eco-friendly materials for prototype production)
5. Perform initial testing on the EcoFriendlyBattery prototype (P4) -- (depends on: Manufacture the prototype EcoFriendlyBattery)
6. Document test results and provide feedback for design improvements (P4) -- (depends on: Perform initial testing on the EcoFriendlyBattery prototype)
7. Iterate and refine the design based on test results (P5) -- (depends on: Document test results and provide feedback for design improvements)
8. Research and Compile a List of Eco-friendly Materials for Advanced Battery Production - RFC Draft (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EcoFriendlyBatteries can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Advanced batteries made from environmentally friendly materials for longer energy storage..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
