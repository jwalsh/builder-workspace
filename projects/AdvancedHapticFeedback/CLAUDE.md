# AdvancedHapticFeedback

You are a coding agent working on AdvancedHapticFeedback -- A haptic feedback system that provides tactile sensations in VR environments.

## Foundational Axiom

Existing approaches to haptic feedback system fail because they optimize for the common case while ignoring structural constraints; AdvancedHapticFeedback makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop software components
- User interface: gather requirements

## Anti-Goals

- **General-purpose platform**: AdvancedHapticFeedback solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture - RFC Update (P5) -- (depends on: Gather Requirements, Research Existing Solutions, Performance Optimization Research, Literature Review, User Testing Plan)
3. Develop Hardware Components (P3) -- (depends on: Design System Architecture)
4. Develop Software Components (P3) -- (depends on: Design System Architecture)
5. Implement VR Environment Integration (P3) -- (depends on: Develop Software Components)
6. Implement Security Measures (P3) -- (depends on: Develop Software Components)
7. Conduct Testing and Quality Assurance (P2) -- (depends on: Develop Hardware Components, Develop Software Components, Implement VR Environment Integration)
8. Deploy and Maintain System (P2) -- (depends on: Conduct Testing and Quality Assurance, Implement Security Measures)
9. Create Documentation (P2) -- (depends on: Gather Requirements, Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AdvancedHapticFeedback can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A haptic feedback system that provides tactile sensations in VR environments..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
