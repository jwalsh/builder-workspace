# EndpointCentralizer

You are a coding agent working on EndpointCentralizer -- Centralize endpoint access and enable access from on-premises environments to cloud services.

## Foundational Axiom

Existing approaches to centralize endpoint access and enable access from on-premises environments fail because they optimize for the common case while ignoring structural constraints; EndpointCentralizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: gather and prioritize requirements for endpointcentralizer project

## Anti-Goals

- **General-purpose platform**: EndpointCentralizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather and Prioritize Requirements for EndpointCentralizer Project (P5)
2. Design System Architecture (Revised and Enhanced) (P5) -- (depends on: Gather Requirements, Analyze Existing Systems)
3. Implement Backend Services (P3) -- (depends on: Design System Architecture)
4. Develop Frontend Interface (P3) -- (depends on: Design System Architecture)
5. Set up Infrastructure (P3) -- (depends on: Design System Architecture)
6. Integrate with Existing Systems (P3) -- (depends on: Implement Backend Services)
7. Implement Security Measures (P2) -- (depends on: Design System Architecture)
8. Test and Quality Assurance (P2) -- (depends on: Implement Backend Services, Develop Frontend Interface, Implement Security Measures, Integrate with Existing Systems)
9. Documentation and Training (P3) -- (depends on: Test and Quality Assurance)
10. Deploy and Monitor (P2) -- (depends on: Test and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EndpointCentralizer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Centralize endpoint access and enable access from on-premises environments to cloud services..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
