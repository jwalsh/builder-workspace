# assistantNeurofeedback

You are a coding agent working on assistantNeurofeedback -- Un dispositif qui offre une rétroaction neuro en temps réel pour améliorer les pratiques de méditation et pleine conscience.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; assistantNeurofeedback models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un dispositif qui offre une rétroaction neuro en temps réel pour améliorer les pratiques de méditati
- User interface: define project requirements and specifications

## Anti-Goals

- **General-purpose platform**: assistantNeurofeedback solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project requirements and specifications (P1)
2. Design the user interface and user experience (P2) -- (depends on: Define project requirements and specifications)
3. Develop the real-time neuro feedback system (P3) -- (depends on: Define project requirements and specifications)
4. Integrate the real-time neuro feedback system with the UI/UX design (P4) -- (depends on: Design the user interface and user experience, Develop the real-time neuro feedback system)
5. Test and validate the assistantNeurofeedback device (P5) -- (depends on: Integrate the real-time neuro feedback system with the UI/UX design)
6. Document the assistantNeurofeedback device design and functionality (P5) -- (depends on: Test and validate the assistantNeurofeedback device)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantNeurofeedback can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un dispositif qui offre une rétroaction neuro en temps réel pour améliorer les pratiques de méditati.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
