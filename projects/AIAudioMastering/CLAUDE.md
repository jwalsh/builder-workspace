# AIAudioMastering

You are a coding agent working on AIAudioMastering -- An AI-powered audio mastering tool for professional-quality music production.

## Foundational Axiom

Existing approaches to ai-powered audio mastering tool fail because they optimize for the common case while ignoring structural constraints; AIAudioMastering makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement audio processing pipeline
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: AIAudioMastering solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop AI Model for Audio Mastering (P3) -- (depends on: Design System Architecture)
4. Implement Audio Processing Pipeline (P3) -- (depends on: Design System Architecture)
5. Design and Develop User Interface (P3) -- (depends on: Design System Architecture)
6. Set up Continuous Integration and Deployment (P2)
7. Implement Security Measures (P2)
8. Write Documentation and User Guides (P2) -- (depends on: Design and Develop User Interface)
9. Conduct Testing and Quality Assurance (P2) -- (depends on: Develop AI Model for Audio Mastering, Implement Audio Processing Pipeline, Design and Develop User Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIAudioMastering can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered audio mastering tool for professional-quality music production..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
