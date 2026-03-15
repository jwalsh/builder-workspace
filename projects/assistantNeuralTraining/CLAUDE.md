# assistantNeuralTraining

You are a coding agent working on assistantNeuralTraining -- Un assistant qui utilise l'IA et la stimulation neurale pour améliorer les performances physiques et mentales.

## Foundational Axiom

Existing tools treat un assistant qui utilise l'ia et la stimulation neurale pour as a generic automation problem; assistantNeuralTraining succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend infrastructure for assistant
- User interface: define project scope and requirements - rfc

## Anti-Goals

- **General-purpose platform**: assistantNeuralTraining solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC (P1)
2. Develop Backend Infrastructure for Assistant (P5) -- (depends on: Define Project Scope and Requirements)
3. Research and Select AI Technologies (P2) -- (depends on: Define Project Scope and Requirements)
4. Develop Neural Stimulation Methodology (P3) -- (depends on: Research and Select AI Technologies)
5. Integrate AI and Neural Stimulation Modules (P2) -- (depends on: Research and Select AI Technologies, Develop Neural Stimulation Methodology)
6. Test Assistant Functionality and Performance (P4) -- (depends on: Integrate AI and Neural Stimulation Modules)
7. Refine Assistant Based on Test Results (P3) -- (depends on: Test Assistant Functionality and Performance)
8. Document Assistant Functionality and Usage (P5) -- (depends on: Refine Assistant Based on Test Results)
9. Design User Interface for Assistant (P4) -- (depends on: Define Project Scope and Requirements)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantNeuralTraining can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un assistant qui utilise l'IA et la stimulation neurale pour améliorer les performances physiques et.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
