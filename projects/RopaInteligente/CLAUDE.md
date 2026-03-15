# RopaInteligente

You are a coding agent working on RopaInteligente -- Prendas inteligentes capaces de monitorear la temperatura corporal y signos vitales en tiempo real.

## Foundational Axiom

Existing approaches to prendas inteligentes capaces de monitorear la temperatura co fail because they optimize for the common case while ignoring structural constraints; RopaInteligente makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop real-time data processing system
- User interface: develop mobile application for data visualization
- Data layer: develop real-time data processing system

## Anti-Goals

- **General-purpose platform**: RopaInteligente solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Smart Clothing Architecture (P1)
2. Develop Temperature Monitoring Sensor (P2) -- (depends on: Design Smart Clothing Architecture)
3. Develop Vital Signs Monitoring Sensor (P2) -- (depends on: Design Smart Clothing Architecture)
4. Develop Power Source for Smart Clothing (P3) -- (depends on: Design Smart Clothing Architecture)
5. Develop Real-time Data Processing System (P2) -- (depends on: Design Smart Clothing Architecture)
6. Develop Mobile Application for Data Visualization (P3) -- (depends on: Develop Real-time Data Processing System)
7. Test and Validate Smart Clothing Prototype (P4) -- (depends on: Develop Temperature Monitoring Sensor, Develop Vital Signs Monitoring Sensor, Develop Power Source for Smart Clothing, Develop Real-time Data Processing System, Develop Mobile Application for Data Visualization)
8. Revise and Approve Final Design Documentation (P5) -- (depends on: Design Smart Clothing Architecture, Test and Validate Smart Clothing Prototype)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RopaInteligente can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Prendas inteligentes capaces de monitorear la temperatura corporal y signos vitales en tiempo real..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
