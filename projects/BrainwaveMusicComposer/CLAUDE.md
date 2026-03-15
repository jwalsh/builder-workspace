# BrainwaveMusicComposer

You are a coding agent working on BrainwaveMusicComposer -- A BCI system that translates brainwaves into musical compositions.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; BrainwaveMusicComposer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement signal processing module
- User interface: define project requirements (updated)
- Data layer: develop brainwave data acquisition module

## Anti-Goals

- **General-purpose platform**: BrainwaveMusicComposer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (Updated) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Set up Development Environment (P4)
4. Develop Brainwave Data Acquisition Module (P3) -- (depends on: Design System Architecture)
5. Implement Signal Processing Module (P3) -- (depends on: Design System Architecture)
6. Create Music Composition Module (P3) -- (depends on: Design System Architecture, Implement Signal Processing Module)
7. Implement Testing Strategy (P3) -- (depends on: Design System Architecture)
8. Build User Interface (P2) -- (depends on: Design System Architecture)
9. Conduct Security Audit (P3) -- (depends on: Develop Brainwave Data Acquisition Module, Implement Signal Processing Module, Create Music Composition Module, Build User Interface)
10. Write Documentation (P2) -- (depends on: Define Project Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainwaveMusicComposer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A BCI system that translates brainwaves into musical compositions..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
