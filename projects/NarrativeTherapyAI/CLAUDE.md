# NarrativeTherapyAI

You are a coding agent working on NarrativeTherapyAI -- An AI therapist that helps individuals reframe their personal narratives through storytelling techniques, promoting psychological healing and personal growth.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; NarrativeTherapyAI embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI therapist that helps individuals reframe their personal narratives through storytelling techni
- User interface: requirements gathering and analysis for narrative therapy ai
- Data layer: data storage and management

## Anti-Goals

- **General-purpose platform**: NarrativeTherapyAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis for Narrative Therapy AI (P2)
2. System Architecture Design (P3) -- (depends on: Requirements Gathering and Analysis)
3. AI Model Development (P4) -- (depends on: System Architecture Design)
4. User Interface Design and Development (P4) -- (depends on: System Architecture Design)
5. Data Storage and Management (P4) -- (depends on: System Architecture Design)
6. Integration and Testing (P5) -- (depends on: AI Model Development, User Interface Design and Development, Data Storage and Management)
7. Deployment and DevOps (P5) -- (depends on: Integration and Testing)
8. Documentation and User Support (P5) -- (depends on: Integration and Testing)
9. Security and Privacy Implementation (P4) -- (depends on: System Architecture Design)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NarrativeTherapyAI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI therapist that helps individuals reframe their personal narratives through storytelling techni.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
