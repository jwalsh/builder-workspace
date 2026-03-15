# BionicProsthesisNerve

You are a coding agent working on BionicProsthesisNerve -- Create a neural interface system for advanced bionic prosthetics, enabling intuitive control and sensory feedback.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BionicProsthesisNerve embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: neural signal processing
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: BionicProsthesisNerve solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for Neural Interface System - REVISED (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Neural Signal Processing (P3) -- (depends on: System Architecture Design)
4. Prosthetic Device Integration (P3) -- (depends on: System Architecture Design)
5. User Interface and Feedback (P3) -- (depends on: System Architecture Design)
6. Security and Privacy (P2) -- (depends on: System Architecture Design)
7. Testing and Validation (P2) -- (depends on: Neural Signal Processing, Prosthetic Device Integration, User Interface and Feedback)
8. Deployment and Support (P2) -- (depends on: Testing and Validation)
9. Documentation and Training (P2) -- (depends on: System Architecture Design, Neural Signal Processing, Prosthetic Device Integration, User Interface and Feedback)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BionicProsthesisNerve can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Create a neural interface system for advanced bionic prosthetics, enabling intuitive control and sen.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
