# ServiceDependencyMapper

You are a coding agent working on ServiceDependencyMapper -- A tool that automatically maps and visualizes service dependencies in microservices architectures.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; ServiceDependencyMapper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement service discovery and mapping
- User interface: defineprojectscopeandrequirements-revised
- Data layer: implement data storage and persistence

## Anti-Goals

- **General-purpose platform**: ServiceDependencyMapper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. DefineProjectScopeandRequirements-REVISED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Service Discovery and Mapping (P3) -- (depends on: Design System Architecture)
4. Develop Visualization Components (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage and Persistence (P3) -- (depends on: Design System Architecture)
6. Integrate with Target Microservices Architecture (P2) -- (depends on: Implement Service Discovery and Mapping)
7. Implement Security and Access Controls (P2) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P2) -- (depends on: Implement Service Discovery and Mapping, Develop Visualization Components, Implement Data Storage and Persistence, Integrate with Target Microservices Architecture, Implement Security and Access Controls)
9. Conduct Testing and Quality Assurance (P2) -- (depends on: Set up Continuous Integration and Deployment)
10. Write User Documentation and Guides (P2) -- (depends on: Conduct Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ServiceDependencyMapper can deliver its core value proposition as described
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

- Kubernetes
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that automatically maps and visualizes service dependencies in microservices architectures..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
