# WearableAirQualityMonitor

You are a coding agent working on WearableAirQualityMonitor -- A wearable device that continuously monitors air quality and alerts users to dangerous levels.

## Foundational Axiom

Existing approaches to wearable device fail because they optimize for the common case while ignoring structural constraints; WearableAirQualityMonitor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement air quality data processing algorithm
- User interface: develop sensors interface for device
- Data layer: implement air quality data processing algorithm

## Anti-Goals

- **General-purpose platform**: WearableAirQualityMonitor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Air Quality Metrics (P1)
2. Design Wearable Device Architecture (P2) -- (depends on: Define Air Quality Metrics)
3. Develop Sensors Interface for Device (P3) -- (depends on: Design Wearable Device Architecture)
4. Integrate Air Quality Sensor Modules (P4) -- (depends on: Develop Sensors Interface for Device)
5. Implement Air Quality Data Processing Algorithm (P4) -- (depends on: Integrate Air Quality Sensor Modules)
6. Implement Alert System for Dangerous Levels (P5) -- (depends on: Implement Air Quality Data Processing Algorithm)
7. Develop User Interface for Device (P3) -- (depends on: Design Wearable Device Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WearableAirQualityMonitor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable device that continuously monitors air quality and alerts users to dangerous levels..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to iot engineers and embedded systems developers.
