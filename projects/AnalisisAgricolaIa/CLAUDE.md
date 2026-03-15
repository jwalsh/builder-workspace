# AnalisisAgricolaIa

You are a coding agent working on AnalisisAgricolaIa -- Un sistema de IA que analiza datos agrícolas para maximizar el rendimiento y minimizar pérdidas.

## Foundational Axiom

Existing approaches to un sistema de ia que analiza datos agrícolas para maximizar fail because they optimize for the common case while ignoring structural constraints; AnalisisAgricolaIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un sistema de IA que analiza datos agrícolas para maximizar el rendimiento y minimizar pérdidas.
- User interface: gather requirements
- Data layer: set up data pipeline

## Anti-Goals

- **General-purpose platform**: AnalisisAgricolaIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture for AnalisisAgricolaIa (P5) -- (depends on: Gather Requirements, Data Collection Strategy, UI/UX Design)
3. Set up Data Pipeline (P3) -- (depends on: Design System Architecture)
4. Develop Machine Learning Models (P3) -- (depends on: Design System Architecture, Set up Data Pipeline)
5. Set up Comprehensive Testing Framework (P3) -- (depends on: Design System Architecture)
6. Build User Interface (P2) -- (depends on: Design System Architecture)
7. Deploy and Monitor System (P2) -- (depends on: Build User Interface, Develop Machine Learning Models, Set up Data Pipeline, Implement Security Measures - Security Measures Implementation, Set up Testing Framework)
8. Write Documentation (P2) -- (depends on: Gather Requirements, Design System Architecture)
9. Implement Comprehensive Security Measures (Revised) (P1) -- (depends on: Design System Architecture, Security Best Practices Research)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AnalisisAgricolaIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema de IA que analiza datos agrícolas para maximizar el rendimiento y minimizar pérdidas..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to agricultural scientists and farm operators.
