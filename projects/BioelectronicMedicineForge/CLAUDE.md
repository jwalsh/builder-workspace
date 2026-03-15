# BioelectronicMedicineForge

You are a coding agent working on BioelectronicMedicineForge -- Develop a platform for designing and testing bioelectronic medical devices that interface directly with the nervous system.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; BioelectronicMedicineForge embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend systems
- User interface: revise project scope and requirements - update
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: BioelectronicMedicineForge solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Revise Project Scope and Requirements - Update (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Backend Systems (P3) -- (depends on: Design System Architecture)
4. Develop Frontend User Interface (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
6. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
7. Develop Testing and Quality Assurance Strategies (P3) -- (depends on: Design System Architecture)
8. Establish Security and Compliance (P2) -- (depends on: Design System Architecture)
9. Create Documentation and User Guides (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BioelectronicMedicineForge can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Develop a platform for designing and testing bioelectronic medical devices that interface directly w.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
