# NeuroGamingController

You are a coding agent working on NeuroGamingController -- A gaming controller that incorporates BCI technology for thought-based game interactions.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroGamingController models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop gaming application backend
- User interface: develop gaming application frontend

## Anti-Goals

- **General-purpose platform**: NeuroGamingController solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Develop BCI Firmware (P3) -- (depends on: Controller Hardware Design)
2. Develop Gaming Application Backend (P4) -- (depends on: BCI Firmware)
3. Develop Gaming Application Frontend (P5) -- (depends on: Gaming Application Backend)
4. Integrate BCI with Gaming Application (P3) -- (depends on: BCI Firmware, Gaming Application Backend)
5. Test BCI Integration (P4) -- (depends on: Integrate BCI with Gaming Application)
6. Define BCI Interface Specification (P1)
7. Design Controller Hardware (P2) -- (depends on: BCI Interface Specification)
8. Document Controller Assembly Process (P2) -- (depends on: Controller Hardware Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroGamingController can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A gaming controller that incorporates BCI technology for thought-based game interactions..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
