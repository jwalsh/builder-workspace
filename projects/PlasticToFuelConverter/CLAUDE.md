# PlasticToFuelConverter

You are a coding agent working on PlasticToFuelConverter -- A system that converts plastic waste into usable fuel, addressing both energy needs and plastic pollution.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; PlasticToFuelConverter makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that converts plastic waste into usable fuel, addressing both energy needs and plastic poll
- User interface: design conversion process hardware interface
- Data layer: set up data collection and storage system

## Anti-Goals

- **General-purpose platform**: PlasticToFuelConverter solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop Plastic Waste Sorting Algorithm (P2) -- (depends on: Define System Architecture)
3. Design Conversion Process Hardware Interface (P3) -- (depends on: Define System Architecture)
4. Implement Conversion Process Control Logic (P4) -- (depends on: Develop Plastic Waste Sorting Algorithm, Design Conversion Process Hardware Interface)
5. Set Up Data Collection and Storage System (P2) -- (depends on: Define System Architecture)
6. Test PlasticToFuelConverter System (P5) -- (depends on: Implement Conversion Process Control Logic, Set Up Data Collection and Storage System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PlasticToFuelConverter can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that converts plastic waste into usable fuel, addressing both energy needs and plastic poll.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
