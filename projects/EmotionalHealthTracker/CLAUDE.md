# EmotionalHealthTracker

You are a coding agent working on EmotionalHealthTracker -- A mobile app that tracks emotional states and provides coping strategies for mental health management.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; EmotionalHealthTracker embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design for emotional health tracker app

## Anti-Goals

- **General-purpose platform**: EmotionalHealthTracker solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for Emotional Health Tracker App (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design for Emotional Health Tracker App (P3) -- (depends on: System Architecture Design)
4. Security and Data Privacy (P3) -- (depends on: System Architecture Design, Database Design)
5. Mobile App Development (P2) -- (depends on: System Architecture Design, Database Design)
6. Backend Development (P2) -- (depends on: System Architecture Design, Database Design)
7. Documentation and User Support (P3) -- (depends on: Mobile App Development, Backend Development)
8. Testing and Quality Assurance (P2) -- (depends on: Mobile App Development, Backend Development)
9. Deployment and DevOps (P2) -- (depends on: Mobile App Development, Backend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmotionalHealthTracker can deliver its core value proposition as described
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
- MongoDB
- Redis
- AWS
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A mobile app that tracks emotional states and provides coping strategies for mental health managemen.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
