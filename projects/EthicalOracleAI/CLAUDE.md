# EthicalOracleAI

You are a coding agent working on EthicalOracleAI -- An advanced AI system designed to provide impartial ethical guidance on complex moral dilemmas, considering multiple philosophical frameworks.

## Foundational Axiom

Existing approaches to advanced ai system designed fail because they optimize for the common case while ignoring structural constraints; EthicalOracleAI makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data processing pipeline
- User interface: defineprojectscopeandrequirements
- Data layer: implement data processing pipeline

## Anti-Goals

- **General-purpose platform**: EthicalOracleAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. DefineProjectScopeandRequirements (P5)
2. Design System Architecture for EthicalOracleAI (P5) -- (depends on: Define Project Scope and Requirements)
3. Develop AI Model (P3) -- (depends on: Design System Architecture)
4. Implement Data Processing Pipeline (P3) -- (depends on: Design System Architecture)
5. Develop User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures for EthicalOracleAI (P2) -- (depends on: Design System Architecture)
7. Develop Testing Strategy (P2) -- (depends on: Design System Architecture)
8. Prepare Deployment and DevOps (P2) -- (depends on: Design System Architecture, Implement Security Measures)
9. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EthicalOracleAI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced AI system designed to provide impartial ethical guidance on complex moral dilemmas, cons.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
