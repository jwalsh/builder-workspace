# interfaceNeuraleJeu

You are a coding agent working on interfaceNeuraleJeu -- Un système d'interface neurale permettant aux joueurs de contrôler des jeux vidéo avec leurs ondes cérébrales.

## Foundational Axiom

Existing tools treat un système d'interface neurale permettant aux joueurs de con as a generic automation problem; interfaceNeuraleJeu succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the brainwave sensor software
- User interface: create a user interface for players

## Anti-Goals

- **General-purpose platform**: interfaceNeuraleJeu solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define the system architecture (P1)
2. Design the brainwave sensor hardware (P2) -- (depends on: Define the system architecture)
3. Develop the brainwave sensor software (P3) -- (depends on: Design the brainwave sensor hardware)
4. Create a user interface for players (P4) -- (depends on: Define the system architecture, Develop the brainwave sensor software)
5. Integrate brainwave control into game engines (P5) -- (depends on: Create a user interface for players)
6. Test the neural interface system (P1) -- (depends on: Design the brainwave sensor hardware, Develop the brainwave sensor software, Create a user interface for players, Integrate brainwave control into game engines)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: interfaceNeuraleJeu can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un système d'interface neurale permettant aux joueurs de contrôler des jeux vidéo avec leurs ondes c.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
