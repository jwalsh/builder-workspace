# WellnessIntegrationScorer

You are a coding agent working on WellnessIntegrationScorer -- A tool that scores how well employees are integrating wellness activities into their work routine, offering personalized suggestions.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; WellnessIntegrationScorer embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements
- Data layer: implement data storage and retrieval

## Anti-Goals

- **General-purpose platform**: WellnessIntegrationScorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for WellnessIntegrationScorer (P5) -- (depends on: Define Project Scope and Requirements)
3. Implement Security Measures (P4) -- (depends on: Design System Architecture)
4. Set up Development Environment (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage and Retrieval (P3) -- (depends on: Design System Architecture, Set up Development Environment)
6. Develop Comprehensive Testing Strategy for WellnessIntegrationScorer (P3) -- (depends on: Design System Architecture)
7. Implement Backend Services (P2) -- (depends on: Design System Architecture, Set up Development Environment)
8. Develop User Interface (P2) -- (depends on: Design System Architecture, Set up Development Environment)
9. Create Documentation (P3) -- (depends on: Design System Architecture, Implement Backend Services, Develop User Interface, Implement Data Storage and Retrieval)
10. Conduct System Testing (P2) -- (depends on: Implement Backend Services, Develop User Interface, Implement Data Storage and Retrieval, Develop Testing Strategy)
11. Deploy to Production (P1) -- (depends on: Conduct System Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: WellnessIntegrationScorer can deliver its core value proposition as described
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

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool that scores how well employees are integrating wellness activities into their work routine, o.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
