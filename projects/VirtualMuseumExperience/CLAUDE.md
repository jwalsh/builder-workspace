# VirtualMuseumExperience

You are a coding agent working on VirtualMuseumExperience -- An immersive virtual reality museum that allows users to explore historical artifacts and artworks in detail.

## Foundational Axiom

Existing approaches to immersive virtual reality museum fail because they optimize for the common case while ignoring structural constraints; VirtualMuseumExperience makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop vr museum experience backend
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: VirtualMuseumExperience solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design VR Environment and User Interface (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop VR Museum Experience Backend (P3) -- (depends on: Define Project Scope and Requirements)
4. Integrate User Interface with Backend (P5) -- (depends on: Design VR Environment and User Interface, Develop VR Museum Experience Backend)
5. Implement Museum Exhibits (P4) -- (depends on: Design VR Environment and User Interface, Develop VR Museum Experience Backend)
6. Test Virtual Museum Experience (P1) -- (depends on: Implement Museum Exhibits, Integrate User Interface with Backend)
7. Deploy and Launch Virtual Museum Experience (P2) -- (depends on: Test Virtual Museum Experience)
8. Review and Iterate on User Feedback (P3) -- (depends on: Deploy and Launch Virtual Museum Experience)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualMuseumExperience can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An immersive virtual reality museum that allows users to explore historical artifacts and artworks i.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
