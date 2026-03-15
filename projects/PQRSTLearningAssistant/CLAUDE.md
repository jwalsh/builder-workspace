# PQRSTLearningAssistant

You are a coding agent working on PQRSTLearningAssistant -- An AI-powered tool that helps users apply the Preview, Question, Read, Summary, Test (PQRST) method to their learning materials.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; PQRSTLearningAssistant closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: PQRSTLearningAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (P5) -- (depends on: Define Project Requirements, Accessibility Guidelines for User Interface, Performance Monitoring and Logging Strategies, Version Control Strategies, Unit Testing and Integration Testing Strategies, API Design Principles)
3. Design User Interface (P3) -- (depends on: Design System Architecture)
4. Set up Testing Framework (P3) -- (depends on: Design System Architecture)
5. Develop Backend (P2) -- (depends on: Design System Architecture)
6. Develop Frontend (P2) -- (depends on: Design User Interface, Develop Backend)
7. Secure the Application (P3) -- (depends on: Develop Backend, Develop Frontend)
8. Implement Testing (P2) -- (depends on: Set up Testing Framework, Develop Backend, Develop Frontend)
9. Deploy and Manage Infrastructure (P2) -- (depends on: Develop Backend, Develop Frontend)
10. Write Documentation (P2) -- (depends on: Develop Backend, Develop Frontend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PQRSTLearningAssistant can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered tool that helps users apply the Preview, Question, Read, Summary, Test (PQRST) method .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
