# MemoryEnhancementStimulator

You are a coding agent working on MemoryEnhancementStimulator -- A non-invasive brain stimulation device designed to enhance memory formation and recall.

## Foundational Axiom

Existing approaches to non-invasive brain stimulation device designed fail because they optimize for the common case while ignoring structural constraints; MemoryEnhancementStimulator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop software components
- User interface: requirements gathering and analysis

## Anti-Goals

- **General-purpose platform**: MemoryEnhancementStimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design MemoryEnhancementStimulator Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
3. Develop Hardware Components (P3) -- (depends on: Design MemoryEnhancementStimulator Architecture)
4. Develop Software Components (P3) -- (depends on: Design MemoryEnhancementStimulator Architecture)
5. Integration of Hardware and Software Components (P4) -- (depends on: Develop Hardware Components, Develop Software Components)
6. Perform Unit Tests (P5) -- (depends on: Integration of Hardware and Software Components)
7. Perform System Tests (P5) -- (depends on: Perform Unit Tests)
8. Security Audit and Vulnerability Testing (P5) -- (depends on: Integration of Hardware and Software Components)
9. Documentation and Knowledge Transfer (P5) -- (depends on: Integration of Hardware and Software Components)
10. User Acceptance Testing (UAT) (P5) -- (depends on: Perform System Tests)
11. Product Deployment and Launch (P5) -- (depends on: User Acceptance Testing (UAT))

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MemoryEnhancementStimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A non-invasive brain stimulation device designed to enhance memory formation and recall..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
