# AIInterrogationAssistant

You are a coding agent working on AIInterrogationAssistant -- An AI system that analyzes speech patterns, micro-expressions, and physiological data to assist in interrogation processes.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AIInterrogationAssistant makes those constraints first-class.

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

- **General-purpose platform**: AIInterrogationAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for AIInterrogationAssistant (Revised) (P5) -- (depends on: Project Planning and Requirements Gathering, Legal and Ethical Review, Data Privacy and Security Assessment)
3. Security and Privacy Considerations (P4) -- (depends on: System Architecture Design)
4. Data Collection and Preprocessing (P3) -- (depends on: System Architecture Design)
5. AI Model Development (P3) -- (depends on: Data Collection and Preprocessing)
6. User Interface Design - AI Interrogation Assistant (Revised) (P2) -- (depends on: System Architecture Design, Ethical Guidelines and Legal Compliance Review, User Research and Requirements Gathering, UI/UX Design Principles and Best Practices, AI Ethics)
7. Backend Development (P2) -- (depends on: AI Model Development, System Architecture Design)
8. Frontend Development (P2) -- (depends on: User Interface Design, Backend Development)
9. Testing and Evaluation (P2) -- (depends on: Backend Development, Frontend Development)
10. Deployment and Maintenance (P2) -- (depends on: Testing and Evaluation)
11. Documentation and Training (P2) -- (depends on: Backend Development, Frontend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIInterrogationAssistant can deliver its core value proposition as described
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

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that analyzes speech patterns, micro-expressions, and physiological data to assist in i.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
