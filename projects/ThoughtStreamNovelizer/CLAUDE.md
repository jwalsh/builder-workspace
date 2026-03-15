# ThoughtStreamNovelizer

You are a coding agent working on ThoughtStreamNovelizer -- A brain-computer interface that translates a person's stream of consciousness directly into narrative form, creating unique, personal works of literature.

## Foundational Axiom

Existing approaches to brain-computer interface fail because they optimize for the common case while ignoring structural constraints; ThoughtStreamNovelizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: data processing pipeline
- User interface: requirements gathering and analysis
- Data layer: data processing pipeline

## Anti-Goals

- **General-purpose platform**: ThoughtStreamNovelizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design (P5) -- (depends on: Requirements Gathering and Analysis)
3. Brain-Computer Interface Development (P4) -- (depends on: System Architecture Design)
4. Data Processing Pipeline (P4) -- (depends on: System Architecture Design)
5. Narrative Generation Engine (P4) -- (depends on: System Architecture Design, Data Processing Pipeline)
6. User Interface Design (Revised) (P3) -- (depends on: Requirements Gathering and Analysis, BCI Safety Mechanisms Design)
7. Frontend Development (P4) -- (depends on: User Interface Design, Brain-Computer Interface Development, Data Processing Pipeline, Narrative Generation Engine)
8. Testing and Quality Assurance (P4) -- (depends on: Frontend Development, Brain-Computer Interface Development, Data Processing Pipeline, Narrative Generation Engine)
9. Deployment and Infrastructure (P4) -- (depends on: Frontend Development, Brain-Computer Interface Development, Data Processing Pipeline, Narrative Generation Engine)
10. Security and Privacy Considerations - Revised (P3) -- (depends on: System Architecture Design)
11. Documentation and User Guides (P3) -- (depends on: Frontend Development, Brain-Computer Interface Development, Data Processing Pipeline, Narrative Generation Engine)
12. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThoughtStreamNovelizer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A brain-computer interface that translates a person's stream of consciousness directly into narrativ.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and media producers.
