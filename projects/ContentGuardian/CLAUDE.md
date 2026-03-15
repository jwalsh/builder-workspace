# ContentGuardian

You are a coding agent working on ContentGuardian -- Efficiently moderate user-contributed content and sensitive information across various industries using a serverless architecture.

## Foundational Axiom

Existing approaches to efficiently moderate user-contributed content and sensitive fail because they optimize for the common case while ignoring structural constraints; ContentGuardian makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Efficiently moderate user-contributed content and sensitive information across various industries us
- User interface: define project scope and requirements - revised
- Data layer: define data models and storage

## Anti-Goals

- **General-purpose platform**: ContentGuardian solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture for ContentGuardian (Revised) (P5) -- (depends on: Define Project Scope and Requirements)
3. Write Documentation (P4) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
4. Define Data Models and Storage (P3) -- (depends on: Design System Architecture)
5. Implement Content Moderation Pipeline (P2) -- (depends on: Design System Architecture, Define Data Models and Storage)
6. Build User Interfaces (P2) -- (depends on: Design System Architecture, Define Data Models and Storage)
7. Set up CI/CD and Deployment (P3) -- (depends on: Implement Content Moderation Pipeline, Build User Interfaces)
8. Develop Testing Strategy (P3) -- (depends on: Implement Content Moderation Pipeline, Build User Interfaces)
9. Implement Security and Compliance (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ContentGuardian can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Efficiently moderate user-contributed content and sensitive information across various industries us.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and media producers.
