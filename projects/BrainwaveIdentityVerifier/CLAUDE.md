# BrainwaveIdentityVerifier

You are a coding agent working on BrainwaveIdentityVerifier -- A secure identity verification system using unique brainwave signatures.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; BrainwaveIdentityVerifier models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop brainwave processing pipeline
- User interface: define project scope and requirements
- Data layer: implement brainwave data acquisition

## Anti-Goals

- **General-purpose platform**: BrainwaveIdentityVerifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Brainwave Data Acquisition (P3) -- (depends on: Design System Architecture)
4. Develop Brainwave Processing Pipeline (P3) -- (depends on: Design System Architecture)
5. Design and Implement Database (P3) -- (depends on: Design System Architecture)
6. Build User Interface (P3) -- (depends on: Design System Architecture)
7. Create Documentation and User Guides (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
8. Develop Identity Verification Module (P2) -- (depends on: Develop Brainwave Processing Pipeline, Design and Implement Database)
9. Implement Security Measures (P2) -- (depends on: Design System Architecture, Design and Implement Database)
10. Conduct System Integration and Testing (P2) -- (depends on: Implement Brainwave Data Acquisition, Develop Brainwave Processing Pipeline, Develop Identity Verification Module, Build User Interface, Implement Security Measures)
11. Deploy and Monitor System (P2) -- (depends on: Conduct System Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BrainwaveIdentityVerifier can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A secure identity verification system using unique brainwave signatures..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
