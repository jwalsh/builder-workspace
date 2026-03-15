# plateformeSoinPersonnalisé

You are a coding agent working on plateformeSoinPersonnalisé -- Une plateforme qui utilise l'IA pour fournir des soins de santé personnalisés basés sur des données génétiques.

## Foundational Axiom

Existing approaches to une plateforme qui utilise l'ia pour fournir des soins de sa fail because they optimize for the common case while ignoring structural constraints; plateformeSoinPersonnalisé makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Une plateforme qui utilise l'IA pour fournir des soins de santé personnalisés basés sur des données 
- User interface: design user interface for data input and output
- Data layer: create database schema and set up data storage

## Anti-Goals

- **General-purpose platform**: plateformeSoinPersonnalisé solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Overall Architecture (P1)
2. Create Database Schema and Set Up Data Storage (P5) -- (depends on: Define Overall Architecture)
3. Design User Interface for Data Input and Output (P4) -- (depends on: Define Overall Architecture)
4. Develop Genetic Data Handling Module (P2) -- (depends on: Define Overall Architecture)
5. Implement AI Model for Personalized Healthcare (P3) -- (depends on: Develop Genetic Data Handling Module)
6. Implement DevOps Pipeline (P2) -- (depends on: Define Overall Architecture)
7. Conduct Security Audit and Implement Measures (P1) -- (depends on: Define Overall Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: plateformeSoinPersonnalisé can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Une plateforme qui utilise l'IA pour fournir des soins de santé personnalisés basés sur des données .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
