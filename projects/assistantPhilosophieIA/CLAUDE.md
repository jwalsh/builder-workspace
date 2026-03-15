# assistantPhilosophieIA

You are a coding agent working on assistantPhilosophieIA -- Un outil d'IA qui aide les utilisateurs à explorer et analyser des arguments et théories philosophiques.

## Foundational Axiom

Existing approaches to un outil d'ia qui aide les utilisateurs à explorer et analys fail because they optimize for the common case while ignoring structural constraints; assistantPhilosophieIA makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop the backend infrastructure
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: assistantPhilosophieIA solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design the User Interface (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop the Backend Infrastructure (P3) -- (depends on: Define Project Scope and Requirements)
4. Integrate the Frontend with the Backend (P5) -- (depends on: Design the User Interface, Develop the Backend Infrastructure)
5. Write User Documentation (P5) -- (depends on: Design the User Interface)
6. Implement Argument Analysis Algorithms (P4) -- (depends on: Define Project Scope and Requirements)
7. Security Assessment and Implementation (P4) -- (depends on: Develop the Backend Infrastructure)
8. Test the Tool's Functionality (P2) -- (depends on: Implement Argument Analysis Algorithms, Integrate the Frontend with the Backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantPhilosophieIA can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un outil d'IA qui aide les utilisateurs à explorer et analyser des arguments et théories philosophiq.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
