# TidalEnergyFence

You are a coding agent working on TidalEnergyFence -- A modular tidal energy system that can be installed along coastlines, harnessing tidal flows with minimal ecological impact.

## Foundational Axiom

Energy systems fail when they optimize for peak efficiency at the cost of resilience; TidalEnergyFence maintains correctness across the full operating envelope.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A modular tidal energy system that can be installed along coastlines, harnessing tidal flows with mi

## Anti-Goals

- **General-purpose platform**: TidalEnergyFence solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Conduct Preliminary Research and Analysis (P1)
2. Design Modular Tidal Energy Units (P2) -- (depends on: Conduct Preliminary Research and Analysis)
3. Design the Installation Structure (P2) -- (depends on: Conduct Preliminary Research and Analysis)
4. Prepare RFC: Performance and Safety Standards (P5) -- (depends on: Design Modular Tidal Energy Units, Design the Installation Structure)
5. Review Performance and Safety Standards RFC (P5) -- (depends on: Prepare RFC: Performance and Safety Standards)
6. Prepare RFC: Ecological Impact Assessment (P4) -- (depends on: Design Modular Tidal Energy Units, Design the Installation Structure)
7. Review Ecological Impact Assessment RFC (P4) -- (depends on: Prepare RFC: Ecological Impact Assessment)
8. Develop a Monitoring System for Performance and Ecological Impact (P3) -- (depends on: Design Modular Tidal Energy Units, Design the Installation Structure)
9. Create a Maintenance and Replacement Plan (P3) -- (depends on: Design Modular Tidal Energy Units)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TidalEnergyFence can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A modular tidal energy system that can be installed along coastlines, harnessing tidal flows with mi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to energy system operators and grid engineers.
