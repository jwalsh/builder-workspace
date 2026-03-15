# EnergyHarvestingWearables

You are a coding agent working on EnergyHarvestingWearables -- Wearable devices that generate energy from body movements to power electronics.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; EnergyHarvestingWearables maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Wearable devices that generate energy from body movements to power electronics.
- User interface: requirements gathering and analysis

## Anti-Goals

- **General-purpose platform**: EnergyHarvestingWearables solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design the Wearable Hardware (P2) -- (depends on: Requirements Gathering and Analysis)
3. Design the Energy Harvesting Electronics (P2) -- (depends on: Design the Wearable Hardware)
4. Develop the Electronics Prototype (P3) -- (depends on: Design the Wearable Hardware, Design the Energy Harvesting Electronics)
5. Develop the Mobile App Interface (P3) -- (depends on: Develop the Electronics Prototype)
6. Integrate Energy Harvesting Wearable with Mobile App (P3) -- (depends on: Develop the Electronics Prototype, Develop the Mobile App Interface)
7. User Acceptance Testing (UAT) (P4) -- (depends on: Develop the Electronics Prototype, Develop the Mobile App Interface, Integrate Energy Harvesting Wearable with Mobile App)
8. Deployment and Release Management (P5) -- (depends on: User Acceptance Testing (UAT))
9. Documentation and User Manual (P5) -- (depends on: User Acceptance Testing (UAT))

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EnergyHarvestingWearables can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Wearable devices that generate energy from body movements to power electronics..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
