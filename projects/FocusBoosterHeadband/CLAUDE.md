# FocusBoosterHeadband

You are a coding agent working on FocusBoosterHeadband -- A wearable headband that uses EEG to monitor attention levels and provides subtle alerts to maintain focus.

## Foundational Axiom

Existing approaches to wearable headband fail because they optimize for the common case while ignoring structural constraints; FocusBoosterHeadband makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A wearable headband that uses EEG to monitor attention levels and provides subtle alerts to maintain
- User interface: enhanced requirements gathering and analysis
- Data layer: create a database schema for storing and analyzing data

## Anti-Goals

- **General-purpose platform**: FocusBoosterHeadband solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Enhanced Requirements Gathering and Analysis (P1)
2. Design the User Interface for the Headband (P2) -- (depends on: Requirements Gathering and Analysis)
3. Design the Electronics for EEG Monitoring (P2) -- (depends on: Requirements Gathering and Analysis)
4. Develop the Mobile Application for FocusBoosterHeadband (P3) -- (depends on: Design the User Interface for the Headband, Design the Electronics for EEG Monitoring)
5. Implement the FocusBoosterHeadband's Electronics (P4) -- (depends on: Design the Electronics for EEG Monitoring)
6. Perform Functional and Security Testing (P5) -- (depends on: Develop the Mobile Application for FocusBoosterHeadband, Implement the FocusBoosterHeadband's Electronics)
7. Prepare User Manual and Documentation (P5) -- (depends on: Develop the Mobile Application for FocusBoosterHeadband, Implement the FocusBoosterHeadband's Electronics)
8. Integration of Mobile Application and FocusBoosterHeadband (P4) -- (depends on: Develop the Mobile Application for FocusBoosterHeadband, Implement the FocusBoosterHeadband's Electronics)
9. Create a Database Schema for Storing and Analyzing Data (P3) -- (depends on: Requirements Gathering and Analysis)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FocusBoosterHeadband can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A wearable headband that uses EEG to monitor attention levels and provides subtle alerts to maintain.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
