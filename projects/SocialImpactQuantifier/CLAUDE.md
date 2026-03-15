# SocialImpactQuantifier

You are a coding agent working on SocialImpactQuantifier -- An AI system that predicts and measures the potential social impact of policies, initiatives, and technological innovations across various societal metrics.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; SocialImpactQuantifier makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that predicts and measures the potential social impact of policies, initiatives, and te
- User interface: define project scope and requirements
- Data layer: develop data ingestion pipeline

## Anti-Goals

- **General-purpose platform**: SocialImpactQuantifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design System Architecture - Revised (Revision for Review) (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement User Interface (P4) -- (depends on: Design System Architecture)
4. Set up Infrastructure and Deployment (P4) -- (depends on: Design System Architecture)
5. Conduct Security Audits (P4) -- (depends on: Design System Architecture)
6. Write Technical Documentation (P4) -- (depends on: Design System Architecture)
7. Develop Data Ingestion Pipeline (P3) -- (depends on: Design System Architecture)
8. Build Impact Prediction Models (P3) -- (depends on: Design System Architecture, Develop Data Ingestion Pipeline)
9. Develop Comprehensive Testing Strategy for SocialImpactQuantifier System (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SocialImpactQuantifier can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that predicts and measures the potential social impact of policies, initiatives, and te.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
