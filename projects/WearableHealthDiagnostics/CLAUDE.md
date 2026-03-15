# WearableHealthDiagnostics

You are a coding agent working on WearableHealthDiagnostics -- A portable device that continuously monitors and diagnoses health conditions in real-time.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; WearableHealthDiagnostics embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design software architecture for the device
- User interface: define project scope and requirements (revised)
- Data layer: develop cloud infrastructure for data storage and analysis

## Anti-Goals

- **General-purpose platform**: WearableHealthDiagnostics solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design Software Architecture for the Device (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Cloud Infrastructure for Data Storage and Analysis (P4) -- (depends on: Design Software Architecture for the Device)
4. Implement Data Privacy and Security Measures (P5) -- (depends on: Develop Cloud Infrastructure for Data Storage and Analysis)
5. Design Hardware Architecture for the Device (P2) -- (depends on: Define Project Scope and Requirements)
6. Develop Firmware for the Device (P4) -- (depends on: Design Hardware Architecture for the Device)
7. Design User Interface for the Device (P3) -- (depends on: Design Hardware Architecture for the Device, Design Software Architecture for the Device)
8. Develop Mobile Application for Data Collection and Visualization (P3) -- (depends on: Design User Interface for the Device)
9. Test the Device Functionality and Performance (P2) -- (depends on: Develop Firmware for the Device, Develop Mobile Application for Data Collection and Visualization, Implement Data Privacy and Security Measures)
10. Document Project Implementation and User Guide (P5) -- (depends on: Test the Device Functionality and Performance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WearableHealthDiagnostics can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A portable device that continuously monitors and diagnoses health conditions in real-time..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
