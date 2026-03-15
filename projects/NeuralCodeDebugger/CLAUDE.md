# NeuralCodeDebugger

You are a coding agent working on NeuralCodeDebugger -- A BCI tool for programmers that allows direct neural interaction with code for intuitive debugging.

## Foundational Axiom

The bottleneck in bci tool for programmers is not compute or data but the feedback loop between intent and artifact; NeuralCodeDebugger compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop bci software prototype
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: NeuralCodeDebugger solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Brain-Computer Interface Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop BCI Hardware Prototype (P3) -- (depends on: Design Brain-Computer Interface Architecture)
4. Develop BCI Software Prototype (P3) -- (depends on: Design Brain-Computer Interface Architecture)
5. Integrate Hardware and Software Components (P4) -- (depends on: Develop BCI Hardware Prototype, Develop BCI Software Prototype)
6. Test NeuralCodeDebugger System (P5) -- (depends on: Integrate Hardware and Software Components)
7. Iteratively Refine NeuralCodeDebugger System (P5) -- (depends on: Test NeuralCodeDebugger System)
8. Document and Publish User Guide (P5) -- (depends on: Iteratively Refine NeuralCodeDebugger System)
9. Develop NeuralCodeDebugger Frontend (P4) -- (depends on: Develop BCI Software Prototype)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuralCodeDebugger can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A BCI tool for programmers that allows direct neural interaction with code for intuitive debugging..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
