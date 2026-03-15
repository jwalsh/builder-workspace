# NeuroFeedbackMeditationAssistant

You are a coding agent working on NeuroFeedbackMeditationAssistant -- A device that provides real-time neurofeedback to assist in meditation and mindfulness practices.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroFeedbackMeditationAssistant models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate user interface with backend system
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: NeuroFeedbackMeditationAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P1)
2. Design User Interface Wireframes (P2) -- (depends on: Define Project Scope and Requirements)
3. Select Suitable Hardware Components (P3) -- (depends on: Define Project Scope and Requirements)
4. Develop Neurofeedback Algorithm (P4) -- (depends on: Select Suitable Hardware Components)
5. Integrate User Interface with Backend System (P2) -- (depends on: Design User Interface Wireframes, Develop Neurofeedback Algorithm)
6. Conduct Device Testing (P5) -- (depends on: Integrate User Interface with Backend System)
7. Document Project Design and Implementation (P5) -- (depends on: Define Project Scope and Requirements, Integrate User Interface with Backend System)
8. Implement Security Measures (P4) -- (depends on: Integrate User Interface with Backend System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroFeedbackMeditationAssistant can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A device that provides real-time neurofeedback to assist in meditation and mindfulness practices..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
