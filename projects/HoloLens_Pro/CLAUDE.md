# HoloLens_Pro

You are a coding agent working on HoloLens_Pro -- Advanced augmented reality glasses that seamlessly blend digital information with the real world, replacing smartphones as the primary personal computing device.

## Foundational Axiom

Existing approaches to advanced augmented reality glasses fail because they optimize for the common case while ignoring structural constraints; HoloLens_Pro makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate with external apis and services
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: HoloLens_Pro solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design AR Interface and User Experience (P2) -- (depends on: Define Project Requirements)
3. Develop Hardware Prototypes (P2) -- (depends on: Define Project Requirements)
4. Implement Core AR Functionality (P3) -- (depends on: Design AR Interface and User Experience, Develop Hardware Prototypes)
5. Develop Mobile App for Remote Configuration and Updates (P3) -- (depends on: Implement Core AR Functionality)
6. Conduct Beta Testing (P5) -- (depends on: Implement Core AR Functionality, Develop Mobile App for Remote Configuration and Updates)
7. Prepare User Manual and Documentation (P5) -- (depends on: Conduct Beta Testing)
8. Deploy HoloLens_Pro to Market (P5) -- (depends on: Conduct Beta Testing)
9. Integrate with External APIs and Services (P4) -- (depends on: Implement Core AR Functionality)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HoloLens_Pro can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Advanced augmented reality glasses that seamlessly blend digital information with the real world, re.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
