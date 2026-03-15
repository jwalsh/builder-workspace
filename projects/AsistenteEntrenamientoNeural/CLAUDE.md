# AsistenteEntrenamientoNeural

You are a coding agent working on AsistenteEntrenamientoNeural -- Un asistente que usa IA y estimulación neural para mejorar el rendimiento físico y mental.

## Foundational Axiom

Existing tools treat un asistente que usa ia y estimulación neural para mejorar e as a generic automation problem; AsistenteEntrenamientoNeural succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un asistente que usa IA y estimulación neural para mejorar el rendimiento físico y mental.
- User interface: define project scope and requirements (revised and expanded)
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: AsistenteEntrenamientoNeural solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised and Expanded) (P5)
2. Design System Architecture for AsistenteEntrenamientoNeural (Revised and Updated - Ready for Final Review) (P5) -- (depends on: Define Project Scope and Requirements, Conduct Risk Assessment and Regulatory Compliance Review)
3. Develop AI and Machine Learning Models (P3) -- (depends on: Design System Architecture)
4. Implement Neural Stimulation Interface (P3) -- (depends on: Design System Architecture)
5. Build User Interface and Experience (P3) -- (depends on: Design System Architecture)
6. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
7. Establish Security and Privacy Measures (P2) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
9. Develop Testing and Quality Assurance Plan (P2) -- (depends on: Design System Architecture)
10. Create Documentation and User Guides (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AsistenteEntrenamientoNeural can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Un asistente que usa IA y estimulación neural para mejorar el rendimiento físico y mental..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
