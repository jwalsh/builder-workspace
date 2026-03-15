# NeuroPhobiaTreatment

You are a coding agent working on NeuroPhobiaTreatment -- A VR-based system combined with BCI for treating phobias through controlled exposure and neural feedback.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroPhobiaTreatment models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A VR-based system combined with BCI for treating phobias through controlled exposure and neural feed
- User interface: implement bci interface
- Data layer: develop data collection module

## Anti-Goals

- **General-purpose platform**: NeuroPhobiaTreatment solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop VR Environment (P2) -- (depends on: Define System Architecture)
3. Implement BCI Interface (P2) -- (depends on: Define System Architecture)
4. Integrate VR and BCI Components (P3) -- (depends on: Develop VR Environment, Implement BCI Interface)
5. Perform System Testing (P5) -- (depends on: Integrate VR and BCI Components)
6. Write User Documentation (P4) -- (depends on: Develop VR Environment, Implement BCI Interface)
7. Address Dependency Issues (P4)
8. Develop Data Collection Module (P3) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroPhobiaTreatment can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A VR-based system combined with BCI for treating phobias through controlled exposure and neural feed.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
