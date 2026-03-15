# WearablePetHealthMonitor

You are a coding agent working on WearablePetHealthMonitor -- A wearable device that tracks a pet’s health and fitness in real-time.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; WearablePetHealthMonitor embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop mobile application backend
- User interface: develop mobile application ui/ux
- Data layer: establish data storage solution

## Anti-Goals

- **General-purpose platform**: WearablePetHealthMonitor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Pet Health and Fitness Metrics (P1)
2. Design Wearable Device Hardware (P2) -- (depends on: Define Pet Health and Fitness Metrics)
3. Develop Wearable Device Firmware (P3) -- (depends on: Design Wearable Device Hardware)
4. Develop Mobile Application UI/UX (P4) -- (depends on: Define Pet Health and Fitness Metrics)
5. Develop Mobile Application Backend (P5) -- (depends on: Develop Wearable Device Firmware, Develop Mobile Application UI/UX)
6. Write User Manual for the Wearable Pet Health Monitor (P5) -- (depends on: Develop Wearable Device Firmware, Develop Mobile Application UI/UX)
7. Establish Data Storage Solution (P3) -- (depends on: Develop Mobile Application Backend)
8. Integrate Wearable Device with Mobile Application (P2) -- (depends on: Design Wearable Device Hardware, Develop Wearable Device Firmware, Develop Mobile Application UI/UX, Develop Mobile Application Backend)
9. Test and Validate the System (P2) -- (depends on: Integrate Wearable Device with Mobile Application, Establish Data Storage Solution)
10. Perform Security Audit on the System (P1) -- (depends on: Develop Wearable Device Firmware, Develop Mobile Application UI/UX, Develop Mobile Application Backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WearablePetHealthMonitor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable device that tracks a pet’s health and fitness in real-time..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
