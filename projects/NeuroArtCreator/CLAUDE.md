# NeuroArtCreator

You are a coding agent working on NeuroArtCreator -- A BCI-powered system that translates brain activity into visual or auditory art.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroArtCreator models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A BCI-powered system that translates brain activity into visual or auditory art.
- User interface: define project scope and requirements - rfc for code-architect review
- Data layer: implement brain activity data acquisition module

## Anti-Goals

- **General-purpose platform**: NeuroArtCreator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC for Code-Architect Review (P1)
2. Design BCI System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Brain Activity Data Acquisition Module (P3) -- (depends on: Design BCI System Architecture)
4. Design and Develop Art Generation Algorithm (P3) -- (depends on: Implement Brain Activity Data Acquisition Module)
5. Create User Interface for Art Preview and Controls (P4) -- (depends on: Design BCI System Architecture)
6. Document System Design and Implementation Details (P5) -- (depends on: Design BCI System Architecture, Implement Brain Activity Data Acquisition Module, Design and Develop Art Generation Algorithm, Create User Interface for Art Preview and Controls)
7. Test Art Generation Algorithm and User Interface (P4) -- (depends on: Design and Develop Art Generation Algorithm, Create User Interface for Art Preview and Controls)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroArtCreator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A BCI-powered system that translates brain activity into visual or auditory art..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
