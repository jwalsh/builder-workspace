# EmployeeVoiceAmplifier

You are a coding agent working on EmployeeVoiceAmplifier -- A platform that ensures every employee's ideas and concerns are heard and addressed by the right decision-makers.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; EmployeeVoiceAmplifier makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform that ensures every employee's ideas and concerns are heard and addressed by the right dec
- User interface: define project scope and requirements
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: EmployeeVoiceAmplifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security and Compliance Measures (P4) -- (depends on: Design System Architecture)
4. Set up Testing and Quality Assurance (P3) -- (depends on: Design System Architecture)
5. Plan and Execute Deployment and Rollout (P5) -- (depends on: Implement Security and Compliance Measures, Set up Testing and Quality Assurance)
6. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)
7. Implement Reporting and Analytics (P4) -- (depends on: Set up Database and Data Storage)
8. Design and Develop User Interfaces (P2) -- (depends on: Design System Architecture)
9. Develop User Documentation and Training Materials (P4) -- (depends on: Design and Develop User Interfaces)
10. Set up Development Environment (P3) -- (depends on: Design System Architecture)
11. Implement User Authentication and Authorization (P2) -- (depends on: Design System Architecture)
12. Implement Idea Submission and Tracking (P2) -- (depends on: Implement User Authentication and Authorization)
13. Implement Concern Reporting and Resolution (P2) -- (depends on: Implement User Authentication and Authorization)
14. Implement Notifications and Alerts (P3) -- (depends on: Implement Idea Submission and Tracking, Implement Concern Reporting and Resolution)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmployeeVoiceAmplifier can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that ensures every employee's ideas and concerns are heard and addressed by the right dec.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to hr professionals and talent acquisition teams.
