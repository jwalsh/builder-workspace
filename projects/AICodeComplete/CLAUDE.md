# AICodeComplete

You are a coding agent working on AICodeComplete -- An advanced code completion system that uses deep learning to provide context-aware suggestions, including entire function implementations and design patterns.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; AICodeComplete captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data collection and preprocessing
- User interface: project planning and requirements gathering
- Data layer: data collection and preprocessing

## Anti-Goals

- **General-purpose platform**: AICodeComplete solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design for AICodeComplete (P2) -- (depends on: Project Planning and Requirements Gathering)
3. Deep Learning Model Development (P3) -- (depends on: System Architecture Design)
4. Code Editor Integration (P3) -- (depends on: System Architecture Design)
5. Testing and Quality Assurance (P4) -- (depends on: Deep Learning Model Development, Code Editor Integration)
6. Deployment and Continuous Integration/Delivery (P5) -- (depends on: Deep Learning Model Development, Code Editor Integration, Testing and Quality Assurance)
7. Documentation and User Support (P5) -- (depends on: Deep Learning Model Development, Code Editor Integration)
8. Data Collection and Preprocessing (P4) -- (depends on: Deep Learning Model Development)
9. Security and Privacy Considerations in AICodeComplete: Review and Update (P4) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AICodeComplete can deliver its core value proposition as described
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

- Python
- TypeScript/JavaScript
- Java
- PostgreSQL
- MongoDB
- Docker
- Kubernetes
- AWS
- TensorFlow
- PyTorch
- GraphQL

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced code completion system that uses deep learning to provide context-aware suggestions, inc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
