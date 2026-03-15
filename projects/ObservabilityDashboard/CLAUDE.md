# ObservabilityDashboard

You are a coding agent working on ObservabilityDashboard -- A comprehensive dashboard that provides real-time insights into system performance, health, and security across an organization's IT infrastructure.

## Foundational Axiom

Existing approaches to comprehensive dashboard fail because they optimize for the common case while ignoring structural constraints; ObservabilityDashboard makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data collection and processing
- User interface: define project scope and requirements - rfc review
- Data layer: implement data collection and processing

## Anti-Goals

- **General-purpose platform**: ObservabilityDashboard solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - RFC Review (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Implement Security Measures (P3) -- (depends on: Design System Architecture)
5. Set up Continuous Integration and Deployment (P3) -- (depends on: Set up Development Environment)
6. Prepare Documentation (P3) -- (depends on: Define Project Scope and Requirements, Design System Architecture)
7. Implement Data Collection and Processing (P2) -- (depends on: Design System Architecture, Set up Development Environment)
8. Design and Implement Data Storage (P2) -- (depends on: Design System Architecture, Set up Development Environment)
9. Develop User Interface (P2) -- (depends on: Design System Architecture, Set up Development Environment)
10. Conduct Testing and Quality Assurance (P2) -- (depends on: Implement Data Collection and Processing, Design and Implement Data Storage, Develop User Interface)
11. Deploy and Monitor (P1) -- (depends on: Implement Data Collection and Processing, Design and Implement Data Storage, Develop User Interface, Implement Security Measures, Conduct Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ObservabilityDashboard can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A comprehensive dashboard that provides real-time insights into system performance, health, and secu.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
