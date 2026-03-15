# PersonalCarbonSequestrator

You are a coding agent working on PersonalCarbonSequestrator -- A device that captures and converts an individual's CO2 emissions into useful materials, enabling a carbon-negative lifestyle.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; PersonalCarbonSequestrator captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design the software components
- User interface: develop the user interface

## Anti-Goals

- **General-purpose platform**: PersonalCarbonSequestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Design the Hardware Components (P2) -- (depends on: Define System Architecture)
3. Create the Device Enclosure (P4) -- (depends on: Design the Hardware Components)
4. Assemble the Device Prototype (P4) -- (depends on: Design the Hardware Components, Create the Device Enclosure)
5. Test the Prototype (P4) -- (depends on: Assemble the Device Prototype)
6. Iterate on the Design (if necessary) (P5) -- (depends on: Test the Prototype)
7. Document the Project (P5) -- (depends on: Define System Architecture)
8. Design the Software Components (P2) -- (depends on: Define System Architecture)
9. Develop the User Interface (P3) -- (depends on: Design the Software Components)
10. Implement the User Interface (P3) -- (depends on: Develop the User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalCarbonSequestrator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that captures and converts an individual's CO2 emissions into useful materials, enabling a .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
