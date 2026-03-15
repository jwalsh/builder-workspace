# PhilosophicalArgumentMapper

You are a coding agent working on PhilosophicalArgumentMapper -- An AI-powered tool that visually maps the structure of philosophical arguments, showing premises, conclusions, and logical relationships.

## Foundational Axiom

Existing approaches to ai-powered tool fail because they optimize for the common case while ignoring structural constraints; PhilosophicalArgumentMapper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement logical inference engine
- User interface: gather requirements

## Anti-Goals

- **General-purpose platform**: PhilosophicalArgumentMapper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (P5)
2. Design System Architecture (Revised) (P4) -- (depends on: Gather Requirements)
3. Develop Argument Parser (P3) -- (depends on: Design System Architecture)
4. Implement Logical Inference Engine (P3) -- (depends on: Design System Architecture)
5. Set up Testing Framework (P3) -- (depends on: Design System Architecture)
6. Implement Security Measures (P3) -- (depends on: Design System Architecture)
7. Design User Interface for PhilosophicalArgumentMapper - Update and Clarification (P2) -- (depends on: Design System Architecture)
8. Implement User Interface (P2) -- (depends on: Design User Interface)
9. Write Documentation (P2) -- (depends on: Design System Architecture, Design User Interface)
10. Set up Deployment Environment (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PhilosophicalArgumentMapper can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-powered tool that visually maps the structure of philosophical arguments, showing premises, co.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to researchers and educators in philosophy and ethics.
