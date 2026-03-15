# DreamRecorderAnalyzer

You are a coding agent working on DreamRecorderAnalyzer -- A device that records and analyzes brain activity during sleep, attempting to reconstruct visual elements of dreams.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; DreamRecorderAnalyzer captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A device that records and analyzes brain activity during sleep, attempting to reconstruct visual ele
- User interface: define project requirements and goals
- Data layer: design dreamdatamodel

## Anti-Goals

- **General-purpose platform**: DreamRecorderAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements and Goals (P1)
2. Design DreamDataModel (P2) -- (depends on: Define Project Requirements and Goals)
3. Develop SleepDataCollector Module (P2) -- (depends on: Define Project Requirements and Goals)
4. Implement DreamReconstructionAlgorithm (P3) -- (depends on: SleepDataCollector Module, Define Project Requirements and Goals)
5. Create User Interface Design (P2) -- (depends on: Define Project Requirements and Goals)
6. Integrate Components and Test Functionality (P4) -- (depends on: Design DreamDataModel, Develop SleepDataCollector Module, Implement DreamReconstructionAlgorithm, Create User Interface Design)
7. Address Security Concerns and Enhance Privacy Features (P4) -- (depends on: Integrate Components and Test Functionality)
8. Perform Functional Testing on DreamRecorderAnalyzer (P3) -- (depends on: Integrate Components and Test Functionality)
9. Document Project Features and Functionality (P2) -- (depends on: Define Project Requirements and Goals)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DreamRecorderAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that records and analyzes brain activity during sleep, attempting to reconstruct visual ele.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
