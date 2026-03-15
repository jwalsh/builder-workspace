# BiocomputerArchitect

You are a coding agent working on BiocomputerArchitect -- Design and simulate biocomputers using engineered cellular components for parallel processing and low-energy computation.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BiocomputerArchitect embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Design and simulate biocomputers using engineered cellular components for parallel processing and lo
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: BiocomputerArchitect solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Research Biocomputer Architecture (P2)
2. Design Biocomputer Architecture (RFC Approved) (P3) -- (depends on: Research Biocomputer Architecture)
3. Develop Simulation Framework (P4) -- (depends on: Design Biocomputer Architecture)
4. Implement Biocomputer Simulation (P4) -- (depends on: Design Biocomputer Architecture, Develop Simulation Framework)
5. Validate and Test Simulation (P5) -- (depends on: Implement Biocomputer Simulation)
6. Optimize Biocomputer Architecture (P4) -- (depends on: Validate and Test Simulation)
7. Document and Report Findings (P5) -- (depends on: Validate and Test Simulation, Optimize Biocomputer Architecture)
8. Define Project Scope and Requirements (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BiocomputerArchitect can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Design and simulate biocomputers using engineered cellular components for parallel processing and lo.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
