# SupplyChainOptimizationSimulator

You are a coding agent working on SupplyChainOptimizationSimulator -- A simulation tool for optimizing global supply chain operations under various scenarios.

## Foundational Axiom

Existing approaches to simulation tool fail because they optimize for the common case while ignoring structural constraints; SupplyChainOptimizationSimulator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services and algorithms
- User interface: develop frontend interface
- Data layer: integrate database and data management system

## Anti-Goals

- **General-purpose platform**: SupplyChainOptimizationSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals (P1)
2. Design Architecture for Simulation Tool (P2) -- (depends on: Define Project Scope and Goals)
3. Develop Backend Services and Algorithms (P4) -- (depends on: Design Architecture for Simulation Tool)
4. Integrate Database and Data Management System (P5) -- (depends on: Develop Backend Services and Algorithms)
5. Develop Frontend Interface (P3) -- (depends on: Design Architecture for Simulation Tool)
6. Implement DevOps and CI/CD Pipeline (P2) -- (depends on: Develop Frontend Interface, Develop Backend Services and Algorithms, Integrate Database and Data Management System)
7. Conduct Quality Assurance Tests (P5) -- (depends on: Implement DevOps and CI/CD Pipeline)
8. Write Technical Documentation (P1) -- (depends on: Define Project Scope and Goals, Design Architecture for Simulation Tool)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SupplyChainOptimizationSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A simulation tool for optimizing global supply chain operations under various scenarios..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to supply chain managers and logistics operators.
