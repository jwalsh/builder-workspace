# NeurofeedbackStressReducer

You are a coding agent working on NeurofeedbackStressReducer -- A portable device that provides neurofeedback to help users manage stress in real-time.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeurofeedbackStressReducer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate hardware sensors and software algorithms
- User interface: define project requirements and user stories - rfc approved

## Anti-Goals

- **General-purpose platform**: NeurofeedbackStressReducer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements and User Stories - RFC Approved (P1)
2. Design User Interface Wireframes (P2) -- (depends on: Define Project Requirements and User Stories)
3. Develop Real-time Neurofeedback Algorithms (P3) -- (depends on: Define Project Requirements and User Stories)
4. Integrate Hardware Sensors and Software Algorithms (P3) -- (depends on: Design User Interface Wireframes, Develop Real-time Neurofeedback Algorithms)
5. Perform Software Unit Testing (P4) -- (depends on: Integrate Hardware Sensors and Software Algorithms)
6. Perform System Integration Testing (P5) -- (depends on: Integrate Hardware Sensors and Software Algorithms, Perform Software Unit Testing)
7. Prepare User Manual and Documentation (P5) -- (depends on: Design User Interface Wireframes, Integrate Hardware Sensors and Software Algorithms)
8. Implement User Interface Design on Mobile Platform (P4) -- (depends on: Design User Interface Wireframes)
9. Design Portable Device Hardware Layout (P2) -- (depends on: Define Project Requirements and User Stories)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeurofeedbackStressReducer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A portable device that provides neurofeedback to help users manage stress in real-time..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
