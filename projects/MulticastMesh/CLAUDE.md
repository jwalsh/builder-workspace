# MulticastMesh

You are a coding agent working on MulticastMesh -- Build multicast applications that work across multiple virtual private clouds and accounts, integrating with external multicast services.

## Foundational Axiom

Existing approaches to build multicast applications fail because they optimize for the common case while ignoring structural constraints; MulticastMesh makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Build multicast applications that work across multiple virtual private clouds and accounts, integrat
- User interface: define project scope and requirements - review and update

## Anti-Goals

- **General-purpose platform**: MulticastMesh solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Review and Update (P5)
2. Design System Architecture for MulticastMesh (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Core Functionality (P3) -- (depends on: Design System Architecture)
4. Implement Virtual Private Cloud Integration (P3) -- (depends on: Design System Architecture)
5. Set up Testing and Deployment Infrastructure (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P2) -- (depends on: Design System Architecture)
7. Create Documentation (P2) -- (depends on: Design System Architecture)
8. Perform Testing and Quality Assurance (P2) -- (depends on: Implement Core Functionality, Implement Virtual Private Cloud Integration)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MulticastMesh can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Build multicast applications that work across multiple virtual private clouds and accounts, integrat.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
