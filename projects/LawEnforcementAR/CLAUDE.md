# LawEnforcementAR

You are a coding agent working on LawEnforcementAR -- An augmented reality system for law enforcement officers to access real-time information and situational awareness during operations.

## Foundational Axiom

Existing approaches to augmented reality system fail because they optimize for the common case while ignoring structural constraints; LawEnforcementAR makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: LawEnforcementAR solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design AR System Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Augmented Reality Features (P5) -- (depends on: Design AR System Architecture)
4. Develop Backend Services (P4) -- (depends on: Design AR System Architecture)
5. Prepare User Manual and Documentation (P5) -- (depends on: Develop Backend Services, Develop Augmented Reality Features)
6. Integrate with Law Enforcement Systems (P4) -- (depends on: Design AR System Architecture)
7. Design User Interface and Experience (P3) -- (depends on: Design AR System Architecture)
8. Conduct Functional and Usability Testing (P3) -- (depends on: Develop Backend Services, Develop Augmented Reality Features)
9. Perform Security Audit (P2) -- (depends on: Develop Backend Services, Develop Augmented Reality Features)
10. Deploy and Launch LawEnforcementAR System (P1) -- (depends on: Perform Security Audit, Conduct Functional and Usability Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LawEnforcementAR can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An augmented reality system for law enforcement officers to access real-time information and situati.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
