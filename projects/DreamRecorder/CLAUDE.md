# DreamRecorder

You are a coding agent working on DreamRecorder -- A device that records dreams in high definition, allowing for playback, analysis, and sharing of subconscious experiences.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; DreamRecorder captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A device that records dreams in high definition, allowing for playback, analysis, and sharing of sub
- User interface: define project scope and requirements
- Data layer: design dream data recording algorithm

## Anti-Goals

- **General-purpose platform**: DreamRecorder solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design User Interface (UI) and Experience (UX) (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Mobile App for Dream Recorder Control and Playback (P3) -- (depends on: Design User Interface (UI) and Experience (UX), Define Project Scope and Requirements)
4. Conduct User Acceptance Testing (UAT) (P5) -- (depends on: Develop Mobile App for Dream Recorder Control and Playback)
5. Develop Device Hardware Specifications (P2) -- (depends on: Define Project Scope and Requirements)
6. Implement Device Prototypes (P4) -- (depends on: Develop Device Hardware Specifications)
7. Prepare Device Documentation (P5) -- (depends on: Implement Device Prototypes)
8. Prepare Marketing Materials and Launch Campaign (P5) -- (depends on: Complete Development)
9. Perform Unit and Integration Tests (P4) -- (depends on: Implement Device Prototypes)
10. Design Dream Data Recording Algorithm (P3) -- (depends on: Define Project Scope and Requirements)
11. Develop Dream Data Analysis Tool (P3) -- (depends on: Design Dream Data Recording Algorithm)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DreamRecorder can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that records dreams in high definition, allowing for playback, analysis, and sharing of sub.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
