# SystemHealthScorer

You are a coding agent working on SystemHealthScorer -- A machine learning model that assigns health scores to different components of a system based on various metrics.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; SystemHealthScorer embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: set up data collection and processing
- User interface: define project scope and requirements (revised)
- Data layer: set up data collection and processing

## Anti-Goals

- **General-purpose platform**: SystemHealthScorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design system architecture (Revised) (P4) -- (depends on: Define project scope and requirements)
3. Set up data collection and processing (P3) -- (depends on: Design system architecture)
4. Develop machine learning model (P3) -- (depends on: Design system architecture, Set up data collection and processing)
5. Implement user interface (P2) -- (depends on: Design system architecture, Develop machine learning model)
6. Conduct security review (P3) -- (depends on: Design system architecture, Set up data collection and processing, Develop machine learning model, Implement user interface)
7. Set up deployment and monitoring (P2) -- (depends on: Design system architecture, Set up data collection and processing, Develop machine learning model, Implement user interface)
8. Write documentation (P2) -- (depends on: Design system architecture, Set up data collection and processing, Develop machine learning model, Implement user interface, Set up deployment and monitoring)
9. Perform testing and quality assurance (P2) -- (depends on: Design system architecture, Set up data collection and processing, Develop machine learning model, Implement user interface, Set up deployment and monitoring)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SystemHealthScorer can deliver its core value proposition as described
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

- TypeScript/JavaScript
- Redis
- Docker
- Kubernetes
- AWS
- TensorFlow
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A machine learning model that assigns health scores to different components of a system based on var.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
