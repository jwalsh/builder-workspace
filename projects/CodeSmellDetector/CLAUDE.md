# CodeSmellDetector

You are a coding agent working on CodeSmellDetector -- A tool that teaches users to identify and refactor code smells, improving code quality and maintainability.

## Foundational Axiom

The bottleneck in tool is not compute or data but the feedback loop between intent and artifact; CodeSmellDetector compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop code smell detection engine
- User interface: define project scope and requirements - revised

## Anti-Goals

- **General-purpose platform**: CodeSmellDetector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Code Smell Detection Engine (P3) -- (depends on: Design System Architecture)
4. Build User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Continuous Integration and Deployment (P3)
6. Perform Security Audits and Testing (P3) -- (depends on: Develop Code Smell Detection Engine, Build User Interface)
7. Implement Learning and Teaching Features (P2) -- (depends on: Develop Code Smell Detection Engine, Build User Interface)
8. Implement Quality Assurance and Testing (P3) -- (depends on: Develop Code Smell Detection Engine, Build User Interface, Implement Learning and Teaching Features)
9. Write Documentation and User Guides (P2) -- (depends on: Implement Learning and Teaching Features)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeSmellDetector can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that teaches users to identify and refactor code smells, improving code quality and maintaina.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
