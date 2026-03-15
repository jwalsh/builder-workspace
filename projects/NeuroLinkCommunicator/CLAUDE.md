# NeuroLinkCommunicator

You are a coding agent working on NeuroLinkCommunicator -- A brain-computer interface device for direct thought-to-text and thought-to-speech communication, revolutionizing how people interact with devices and each other.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroLinkCommunicator models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A brain-computer interface device for direct thought-to-text and thought-to-speech communication, re
- User interface: define project scope and requirements: neurolinkcommunicator

## Anti-Goals

- **General-purpose platform**: NeuroLinkCommunicator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements: NeuroLinkCommunicator (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Brain-Computer Interface (P3) -- (depends on: Design System Architecture)
4. Implement Thought-to-Text and Thought-to-Speech Algorithms (P3) -- (depends on: Design System Architecture)
5. Design User Interface (P3) -- (depends on: Define Project Scope and Requirements)
6. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
7. Implement Security and Privacy Measures (P2) -- (depends on: Design System Architecture)
8. Conduct Extensive Testing (P2) -- (depends on: Develop Brain-Computer Interface, Implement Thought-to-Text and Thought-to-Speech Algorithms, Design User Interface)
9. Prepare Documentation and User Guides (P2) -- (depends on: Define Project Scope and Requirements, Design User Interface)
10. Plan Product Launch and Marketing Strategy (P2) -- (depends on: Conduct Extensive Testing, Prepare Documentation and User Guides)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroLinkCommunicator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A brain-computer interface device for direct thought-to-text and thought-to-speech communication, re.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
