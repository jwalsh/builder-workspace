# BionicLimbEnhancer

You are a coding agent working on BionicLimbEnhancer -- An advanced prosthetic system that integrates with the nervous system to provide enhanced strength and dexterity.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BionicLimbEnhancer embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: software development
- User interface: requirements gathering and analysis
- Data layer: secure data management for bioniclimbenhancer (updated)

## Anti-Goals

- **General-purpose platform**: BionicLimbEnhancer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P2)
2. System Architecture Design for BionicLimbEnhancer (P5) -- (depends on: Requirements Gathering and Analysis)
3. Hardware Development (P4) -- (depends on: System Architecture Design)
4. Software Development (P4) -- (depends on: System Architecture Design)
5. Neural Interface Integration (P4) -- (depends on: System Architecture Design)
6. Testing and Validation (P4) -- (depends on: Hardware Development, Software Development, Neural Interface Integration)
7. Regulatory Compliance and Certification (P4) -- (depends on: Testing and Validation)
8. Deployment and Support (P5) -- (depends on: Regulatory Compliance and Certification)
9. Secure Data Management for BionicLimbEnhancer (Updated) (P3) -- (depends on: System Architecture Design)
10. Documentation and User Guides (P3) -- (depends on: Software Development, Hardware Development, Neural Interface Integration)
11. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BionicLimbEnhancer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An advanced prosthetic system that integrates with the nervous system to provide enhanced strength a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
