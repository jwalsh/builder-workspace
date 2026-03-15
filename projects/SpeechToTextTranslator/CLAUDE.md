# SpeechToTextTranslator

You are a coding agent working on SpeechToTextTranslator -- Un sistema di traduzione vocale che utilizza l'intelligenza artificiale e l'apprendimento automatico per fornire traduzioni precise e efficaci in tempo reale.

## Foundational Axiom

Existing approaches to un sistema di traduzione vocale che utilizza l'intelligenza fail because they optimize for the common case while ignoring structural constraints; SpeechToTextTranslator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop real-time processing component
- User interface: design user interface

## Anti-Goals

- **General-purpose platform**: SpeechToTextTranslator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop Speech Recognition Module (P2) -- (depends on: Define System Architecture)
3. Develop Text Translation Module (P2) -- (depends on: Define System Architecture)
4. Develop Real-Time Processing Component (P3) -- (depends on: Develop Speech Recognition Module, Develop Text Translation Module)
5. Design User Interface (P4) -- (depends on: Define System Architecture)
6. Test SpeechToTextTranslator (P5) -- (depends on: Develop Speech Recognition Module, Develop Text Translation Module, Develop Real-Time Processing Component, Design User Interface)
7. Review System Design (P1) -- (depends on: Define System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SpeechToTextTranslator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un sistema di traduzione vocale che utilizza l'intelligenza artificiale e l'apprendimento automatico.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
