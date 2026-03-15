# PersonalizedAdMemorySupressor

You are a coding agent working on PersonalizedAdMemorySupressor -- A system that helps users selectively suppress memories of advertisements, reducing their psychological impact and influence on purchasing decisions.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; PersonalizedAdMemorySupressor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that helps users selectively suppress memories of advertisements, reducing their psychologi
- User interface: gather requirements (revised)
- Data layer: implement data storage and retrieval

## Anti-Goals

- **General-purpose platform**: PersonalizedAdMemorySupressor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements (Revised) (P5)
2. Design System Architecture (Updated and Clarified) (P5) -- (depends on: Gather Requirements (Update: Include specific details on user needs, system capabilities, and performance expectations), Conduct Risk Assessment (Update: Detailed analysis of potential risks associated with the system's functionality and user data protection), Ethics Considerations (Update: Address any ethical concerns, potential biases in memory suppression, and guidelines for handling sensitive information))
3. Implement Security and Privacy Measures (P4) -- (depends on: Design System Architecture)
4. Develop Ad Memory Suppression Algorithm (P3) -- (depends on: Design System Architecture)
5. Build User Interface (P3) -- (depends on: Design System Architecture)
6. Implement Data Storage and Retrieval (P3) -- (depends on: Design System Architecture)
7. Develop Testing Strategy (P3) -- (depends on: Design System Architecture)
8. Integrate with Advertising Networks (P2) -- (depends on: Design System Architecture)
9. Prepare Deployment and Monitoring (P2) -- (depends on: Design System Architecture)
10. Create Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalizedAdMemorySupressor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that helps users selectively suppress memories of advertisements, reducing their psychologi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
