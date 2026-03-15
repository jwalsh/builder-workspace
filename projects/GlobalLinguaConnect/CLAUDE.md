# GlobalLinguaConnect

You are a coding agent working on GlobalLinguaConnect -- A real-time language exchange platform that pairs users for conversation practice, powered by AI for translation assistance and topic suggestions.

## Foundational Axiom

Existing approaches to real-time language exchange platform fail because they optimize for the common case while ignoring structural constraints; GlobalLinguaConnect makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend api
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: GlobalLinguaConnect solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design AI Models for Translation and Topic Suggestions (P3) -- (depends on: Define Project Requirements)
3. Design User Interface (P2) -- (depends on: Define Project Requirements)
4. Develop Backend API (P4) -- (depends on: Design User Interface, Design AI Models for Translation and Topic Suggestions)
5. Develop Frontend Application (P4) -- (depends on: Design User Interface, Develop Backend API)
6. Integrate AI Models into Frontend Application (P5) -- (depends on: Design AI Models for Translation and Topic Suggestions, Develop Frontend Application)
7. Test the Platform (P2) -- (depends on: Develop Frontend Application, Integrate AI Models into Frontend Application)
8. Fix and Refine Based on Testing Feedback (P3) -- (depends on: Test the Platform)
9. Deploy and Launch the Platform (P5) -- (depends on: Fix and Refine Based on Testing Feedback)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalLinguaConnect can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A real-time language exchange platform that pairs users for conversation practice, powered by AI for.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
