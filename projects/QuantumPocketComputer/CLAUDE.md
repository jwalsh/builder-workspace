# QuantumPocketComputer

You are a coding agent working on QuantumPocketComputer -- A pocket-sized quantum computer capable of solving complex problems instantaneously, used for everything from financial modeling to scientific research.

## Foundational Axiom

Quantum computing tools fail when they abstract away hardware constraints; QuantumPocketComputer co-designs algorithms with the physical substrate.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop quantum circuit simulator software
- User interface: develop user interface design for quantumpocketcomputer

## Anti-Goals

- **General-purpose platform**: QuantumPocketComputer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Quantum Algorithms for Problem Solving (P1)
2. Design Quantum Hardware Architecture (P2) -- (depends on: Define Quantum Algorithms for Problem Solving)
3. Manufacture Quantum Hardware Components (P5) -- (depends on: Design Quantum Hardware Architecture)
4. Assemble and Integrate Quantum Hardware Components (P5) -- (depends on: Manufacture Quantum Hardware Components)
5. Develop User Interface Design for QuantumPocketComputer (P4) -- (depends on: Design Quantum Hardware Architecture)
6. Document QuantumPocketComputer Development Process (P4)
7. Develop Quantum Circuit Simulator Software (P3) -- (depends on: Define Quantum Algorithms for Problem Solving)
8. Test and Optimize Quantum Algorithms (P3) -- (depends on: Develop Quantum Circuit Simulator Software, Define Quantum Algorithms for Problem Solving)
9. Implement Quantum Error Correction Techniques (P2) -- (depends on: Design Quantum Hardware Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: QuantumPocketComputer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A pocket-sized quantum computer capable of solving complex problems instantaneously, used for everyt.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to quantum computing researchers and algorithm developers.
