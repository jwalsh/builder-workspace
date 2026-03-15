# VoiceUIOptimizer

You are a coding agent working on VoiceUIOptimizer -- A platform for designing, testing, and optimizing voice user interfaces for various applications.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; VoiceUIOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend for voiceuioptimizer
- User interface: design architecture for voiceuioptimizer
- Data layer: implement database for voiceuioptimizer

## Anti-Goals

- **General-purpose platform**: VoiceUIOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for VoiceUIOptimizer (P2) -- (depends on: Define Project Scope and Requirements)
2. Develop Frontend for VoiceUIOptimizer (P3) -- (depends on: Design Architecture for VoiceUIOptimizer)
3. Develop Backend for VoiceUIOptimizer (P3) -- (depends on: Design Architecture for VoiceUIOptimizer)
4. Test and Optimize VoiceUIOptimizer (P5) -- (depends on: Develop Frontend for VoiceUIOptimizer, Develop Backend for VoiceUIOptimizer)
5. Document VoiceUIOptimizer (P5) -- (depends on: Develop Frontend for VoiceUIOptimizer, Develop Backend for VoiceUIOptimizer)
6. Implement Database for VoiceUIOptimizer (P4) -- (depends on: Design Architecture for VoiceUIOptimizer)
7. Implement Continuous Integration and Deployment Pipeline (P4) -- (depends on: Design Architecture for VoiceUIOptimizer)
8. Refine Project Scope and Detailed Requirements for VoiceUIOptimizer (v2) (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VoiceUIOptimizer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform for designing, testing, and optimizing voice user interfaces for various applications..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
