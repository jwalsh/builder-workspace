# QuantumSystemSimulator

You are a coding agent working on QuantumSystemSimulator -- A high-performance simulation tool for modeling complex quantum systems and their behaviors.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumSystemSimulator co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for quantumsystemsimulator
- User interface: design frontend interface for quantumsystemsimulator
- Data layer: implement database design for quantumsystemsimulator

## Anti-Goals

- **General-purpose platform**: QuantumSystemSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Architecture for QuantumSystemSimulator (P1)
2. Develop Backend Services for QuantumSystemSimulator (P3) -- (depends on: Define Architecture for QuantumSystemSimulator)
3. Develop Test Cases for QuantumSystemSimulator (P5) -- (depends on: Define Architecture for QuantumSystemSimulator, Develop Backend Services for QuantumSystemSimulator)
4. Implement Database Design for QuantumSystemSimulator (P4) -- (depends on: Define Architecture for QuantumSystemSimulator)
5. Design Frontend Interface for QuantumSystemSimulator (P2) -- (depends on: Define Architecture for QuantumSystemSimulator)
6. Review and Provide Feedback on QuantumSystemSimulator RFC (P2) -- (depends on: Define Architecture for QuantumSystemSimulator)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumSystemSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A high-performance simulation tool for modeling complex quantum systems and their behaviors..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
