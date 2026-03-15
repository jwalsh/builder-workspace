# VirtualEthicsLab

You are a coding agent working on VirtualEthicsLab -- A virtual reality environment for conducting thought experiments and exploring ethical scenarios.

## Foundational Axiom

Existing approaches to virtual reality environment fail because they optimize for the common case while ignoring structural constraints; VirtualEthicsLab makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A virtual reality environment for conducting thought experiments and exploring ethical scenarios.

## Anti-Goals

- **General-purpose platform**: VirtualEthicsLab solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Objectives (P1)
2. Develop Ethical Scenarios (P3) -- (depends on: Define Project Scope and Objectives)
3. Design VR Environment (P2) -- (depends on: Define Project Scope and Objectives)
4. Develop Interaction Mechanisms (P4) -- (depends on: Design VR Environment)
5. Implement Ethical Scenarios in VR Environment (P5) -- (depends on: Develop Ethical Scenarios, Develop Interaction Mechanisms)
6. Test VR Environment and Scenarios (P1) -- (depends on: Implement Ethical Scenarios in VR Environment)
7. Document VirtualEthicsLab Features and Usage (P3) -- (depends on: Test VR Environment and Scenarios)
8. Review and Refine VR Environment (P2) -- (depends on: Test VR Environment and Scenarios)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualEthicsLab can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A virtual reality environment for conducting thought experiments and exploring ethical scenarios..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
