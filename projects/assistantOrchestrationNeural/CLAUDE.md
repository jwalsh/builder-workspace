# assistantOrchestrationNeural

You are a coding agent working on assistantOrchestrationNeural -- Un assistant basé sur des interfaces neuronales pour coordonner les tâches dans un environnement de travail complexe.

## Foundational Axiom

Existing tools treat un assistant basé sur des interfaces neuronales pour coordon as a generic automation problem; assistantOrchestrationNeural succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend functionality for the neural interface
- User interface: design neural interface architecture

## Anti-Goals

- **General-purpose platform**: assistantOrchestrationNeural solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design neural interface architecture (P3) -- (depends on: Research existing neural interface solutions)
2. Develop frontend components for the neural interface (P4) -- (depends on: Design neural interface architecture)
3. Implement backend functionality for the neural interface (P4) -- (depends on: Design neural interface architecture)
4. Integrate the neural interface with existing workflow systems (P5) -- (depends on: Develop frontend components for the neural interface, Implement backend functionality for the neural interface)
5. Perform unit testing and debugging of the neural interface (P3) -- (depends on: Develop frontend components for the neural interface, Implement backend functionality for the neural interface)
6. Define project scope and goals (P1)
7. Research Existing Neural Interface Solutions for Integration into AssistantOrchestrationNeural (P2) -- (depends on: Define project scope and goals)
8. Document the neural interface design and implementation (P2) -- (depends on: Design neural interface architecture, Develop frontend components for the neural interface, Implement backend functionality for the neural interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantOrchestrationNeural can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un assistant basé sur des interfaces neuronales pour coordonner les tâches dans un environnement de .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
