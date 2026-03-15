# CrossGenerationalMentorMatcher

You are a coding agent working on CrossGenerationalMentorMatcher -- A tool specifically designed to facilitate mentorship between different generational groups in the workplace.

## Foundational Axiom

Existing approaches to tool specifically designed fail because they optimize for the common case while ignoring structural constraints; CrossGenerationalMentorMatcher makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A tool specifically designed to facilitate mentorship between different generational groups in the w
- User interface: project planning and requirements gathering
- Data layer: security and data privacy

## Anti-Goals

- **General-purpose platform**: CrossGenerationalMentorMatcher solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Security and Data Privacy (P4) -- (depends on: Architecture Design)
4. Database Design and Implementation (P3) -- (depends on: Architecture Design)
5. User Authentication and Authorization (P3) -- (depends on: Architecture Design)
6. User Interface Design and Development (P3) -- (depends on: Architecture Design)
7. Communication and Collaboration Features (P3) -- (depends on: Architecture Design, Database Design and Implementation)
8. Mentorship Matching Algorithm (P2) -- (depends on: Architecture Design, Database Design and Implementation)
9. Progress Tracking and Reporting (P2) -- (depends on: Architecture Design, Database Design and Implementation)
10. Testing and Quality Assurance (P3) -- (depends on: User Interface Design and Development, Mentorship Matching Algorithm, Communication and Collaboration Features, Progress Tracking and Reporting)
11. Deployment and DevOps (P3) -- (depends on: Testing and Quality Assurance)
12. Documentation and User Support (P2) -- (depends on: User Interface Design and Development, Mentorship Matching Algorithm, Communication and Collaboration Features, Progress Tracking and Reporting)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossGenerationalMentorMatcher can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool specifically designed to facilitate mentorship between different generational groups in the w.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
