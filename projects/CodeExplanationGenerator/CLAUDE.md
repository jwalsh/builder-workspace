# CodeExplanationGenerator

You are a coding agent working on CodeExplanationGenerator -- An AI tool that generates clear, line-by-line explanations of submitted code, helping users understand complex solutions.

## Foundational Axiom

The bottleneck in ai tool is not compute or data but the feedback loop between intent and artifact; CodeExplanationGenerator compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI tool that generates clear, line-by-line explanations of submitted code, helping users understa
- User interface: define project scope and requirements - updated

## Anti-Goals

- **General-purpose platform**: CodeExplanationGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Updated (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Scope and Requirements)
3. Ensure Security and Compliance (P4) -- (depends on: Design System Architecture)
4. Develop Code Parsing Module (P3) -- (depends on: Design System Architecture)
5. Develop Explanation Generation Module (P3) -- (depends on: Design System Architecture)
6. Design and Develop User Interface (P3) -- (depends on: Design System Architecture)
7. Implement Testing and Quality Assurance (P3) -- (depends on: Develop Code Parsing Module, Develop Explanation Generation Module, Design and Develop User Interface)
8. Set up Development Environment (P2)
9. Write Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
10. Deploy and Release (P1) -- (depends on: Develop Code Parsing Module, Develop Explanation Generation Module, Design and Develop User Interface, Implement Testing and Quality Assurance, Ensure Security and Compliance, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeExplanationGenerator can deliver its core value proposition as described
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

- Python
- TypeScript/JavaScript
- Java
- Docker
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI tool that generates clear, line-by-line explanations of submitted code, helping users understa.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
