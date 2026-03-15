# ThoughtToSpeechSynthesizer

You are a coding agent working on ThoughtToSpeechSynthesizer -- A device that synthesizes speech directly from thought patterns, bypassing the need for physical speech.

## Foundational Axiom

Existing approaches to device fail because they optimize for the common case while ignoring structural constraints; ThoughtToSpeechSynthesizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate speech synthesis engine
- User interface: define project scope and requirements - rfc approved
- Data layer: ensure data privacy and security compliance

## Anti-Goals

- **General-purpose platform**: ThoughtToSpeechSynthesizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC Approved (P1)
2. Develop Thought Pattern Recognition Algorithm (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Thought Pattern Recognition System (P2) -- (depends on: Develop Thought Pattern Recognition Algorithm)
4. Integrate Speech Synthesis Engine (P3) -- (depends on: Implement Thought Pattern Recognition System)
5. Ensure Data Privacy and Security Compliance (P5) -- (depends on: Integrate Speech Synthesis Engine)
6. Test and Optimize Performance of Synthesizer (P4) -- (depends on: Integrate Speech Synthesis Engine)
7. Document System Functionality and Capabilities (P5) -- (depends on: Test and Optimize Performance of Synthesizer)
8. Design User Interface for Thought Input (P3) -- (depends on: Develop Thought Pattern Recognition Algorithm)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ThoughtToSpeechSynthesizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that synthesizes speech directly from thought patterns, bypassing the need for physical spe.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
