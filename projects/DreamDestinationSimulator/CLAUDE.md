# DreamDestinationSimulator

You are a coding agent working on DreamDestinationSimulator -- A brain-computer interface that records and analyzes users' dreams to generate travel recommendations for destinations that match their subconscious desires.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; DreamDestinationSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: travel recommendation engine development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: DreamDestinationSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for DreamDestinationSimulator (P5) -- (depends on: Project Planning and Requirements Gathering, Ethical and Legal Considerations)
3. Security and Privacy Measures (P4) -- (depends on: System Architecture Design)
4. Brain-Computer Interface Development (P3) -- (depends on: System Architecture Design)
5. Dream Analysis Algorithm Development (P3) -- (depends on: System Architecture Design)
6. Travel Recommendation Engine Development (P3) -- (depends on: System Architecture Design, Dream Analysis Algorithm Development)
7. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
8. User Interface Design and Development (P2) -- (depends on: System Architecture Design)
9. Integration and Testing (P2) -- (depends on: Brain-Computer Interface Development, Dream Analysis Algorithm Development, Travel Recommendation Engine Development, User Interface Design and Development, Database Design and Implementation)
10. Deployment and DevOps (P2) -- (depends on: Integration and Testing)
11. Documentation and User Support (P2) -- (depends on: Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DreamDestinationSimulator can deliver its core value proposition as described
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
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A brain-computer interface that records and analyzes users' dreams to generate travel recommendation.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
