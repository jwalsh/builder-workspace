# TeamMoodAnalyzer

You are a coding agent working on TeamMoodAnalyzer -- An opt-in tool that gauges team morale and suggests activities or interventions to improve team spirit.

## Foundational Axiom

Existing approaches to opt-in tool fail because they optimize for the common case while ignoring structural constraints; TeamMoodAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements - v2.0
- Data layer: design database schema for teammoodanalyzer

## Anti-Goals

- **General-purpose platform**: TeamMoodAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - v2.0 (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Design User Interface for TeamMoodAnalyzer - Revised (P3) -- (depends on: Design System Architecture)
4. Implement Frontend Application (P4) -- (depends on: Design User Interface)
5. Write User Documentation (P5) -- (depends on: Implement Frontend Application)
6. Design Database Schema for TeamMoodAnalyzer (P3) -- (depends on: Design System Architecture)
7. Implement Backend Services (P4) -- (depends on: Design System Architecture, Design Database Schema)
8. Perform Security Audit (P5) -- (depends on: Implement Backend Services, Implement Frontend Application)
9. Conduct User Acceptance Testing (P5) -- (depends on: Implement Backend Services, Implement Frontend Application, Write User Documentation)
10. Set up Continuous Integration and Deployment (P4)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TeamMoodAnalyzer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An opt-in tool that gauges team morale and suggests activities or interventions to improve team spir.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
