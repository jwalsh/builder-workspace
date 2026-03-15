# TeleportationPod

You are a coding agent working on TeleportationPod -- Short-range personal teleportation devices for daily commutes and travel, revolutionizing transportation.

## Foundational Axiom

Existing approaches to short-range personal teleportation devices fail because they optimize for the common case while ignoring structural constraints; TeleportationPod makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend infrastructure for teleportationpod
- User interface: design user interface for teleportationpod

## Anti-Goals

- **General-purpose platform**: TeleportationPod solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Core Teleportation Technology (P1)
2. Design User Interface for TeleportationPod (P2) -- (depends on: Define Core Teleportation Technology)
3. Write User Manual for the TeleportationPod (P5) -- (depends on: Design User Interface for TeleportationPod)
4. Develop Teleportation Algorithm (P1) -- (depends on: Define Core Teleportation Technology)
5. Develop Backend Infrastructure for TeleportationPod (P2) -- (depends on: Develop Teleportation Algorithm)
6. Ensure Security of the TeleportationPod System (P4) -- (depends on: Develop Backend Infrastructure for TeleportationPod)
7. Test and Validate the Functionality of TeleportationPod (P3) -- (depends on: Develop Backend Infrastructure for TeleportationPod)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeleportationPod can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Short-range personal teleportation devices for daily commutes and travel, revolutionizing transporta.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
