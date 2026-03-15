# DataVault

You are a coding agent working on DataVault -- Provide a secure environment for advertisers to store, share, and access data using predefined permission models for cross-platform insights.

## Foundational Axiom

Existing approaches to provide a secure environment fail because they optimize for the common case while ignoring structural constraints; DataVault makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Provide a secure environment for advertisers to store, share, and access data using predefined permi
- User interface: gather requirements
- Data layer: define data models

## Anti-Goals

- **General-purpose platform**: DataVault solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Gather Requirements)
3. Define Data Models (P4) -- (depends on: Gather Requirements)
4. Implement Security Mechanisms (P5) -- (depends on: Design System Architecture, Define Data Models)
5. Build Data Storage and Management Components (P4) -- (depends on: Define Data Models)
6. Develop User Interface (P3) -- (depends on: Design System Architecture)
7. Implement Cross-Platform Integration (P3) -- (depends on: Build Data Storage and Management Components)
8. Test and Quality Assurance (P4) -- (depends on: Implement Security Mechanisms, Build Data Storage and Management Components, Develop User Interface, Implement Cross-Platform Integration)
9. Set Up Deployment and Monitoring (P3)
10. Write Documentation (P2) -- (depends on: Gather Requirements, Design System Architecture, Define Data Models)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DataVault can deliver its core value proposition as described
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

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Provide a secure environment for advertisers to store, share, and access data using predefined permi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
