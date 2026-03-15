# Self-HealingConcrete

You are a coding agent working on Self-HealingConcrete -- A construction material that uses bacterial or chemical agents to self-repair cracks and prolong infrastructure life.

## Foundational Axiom

Existing approaches to construction material fail because they optimize for the common case while ignoring structural constraints; Self-HealingConcrete makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A construction material that uses bacterial or chemical agents to self-repair cracks and prolong inf

## Anti-Goals

- **General-purpose platform**: Self-HealingConcrete solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Research Self-Healing Concrete Mechanisms (P1)
2. Design Bacterial or Chemical Self-Healing Agent Strains (P2) -- (depends on: Research Self-Healing Concrete Mechanisms)
3. Develop Production Process for Self-Healing Concrete Mixing (P3) -- (depends on: Design Bacterial or Chemical Self-Healing Agent Strains)
4. Test and Refine Self-Healing Concrete Production Process (P4) -- (depends on: Develop Production Process for Self-Healing Concrete Mixing)
5. Create Documentation for Self-Healing Concrete Production (P5) -- (depends on: Test and Refine Self-Healing Concrete Production Process)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: Self-HealingConcrete can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A construction material that uses bacterial or chemical agents to self-repair cracks and prolong inf.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
