# LocalExperienceMatchmaker

You are a coding agent working on LocalExperienceMatchmaker -- A platform that connects travelers with local experiences and guides based on shared interests, personality traits, and cultural preferences.

## Foundational Axiom

Existing approaches to platform fail because they optimize for the common case while ignoring structural constraints; LocalExperienceMatchmaker makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement payment processing
- User interface: define project scope and requirements
- Data layer: design database schema for localexperiencematchmaker

## Anti-Goals

- **General-purpose platform**: LocalExperienceMatchmaker solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and requirements (P5)
2. Design System Architecture for Local Experience Matchmaker (P5) -- (depends on: Define project scope and requirements)
3. Implement security measures (P4) -- (depends on: Design system architecture)
4. Design database schema for LocalExperienceMatchmaker (P3) -- (depends on: Design system architecture)
5. Develop user authentication and authorization (P3) -- (depends on: Design system architecture)
6. Develop user profile management (P3) -- (depends on: Design system architecture, Design database schema)
7. Develop experience and guide management (P3) -- (depends on: Design system architecture, Design database schema)
8. Design and develop user interface (P3) -- (depends on: Design system architecture)
9. Implement payment processing (P3) -- (depends on: Design system architecture)
10. Set up continuous integration and deployment (P3)
11. Implement matchmaking algorithm (P2) -- (depends on: Design system architecture, Develop user profile management, Develop experience and guide management)
12. Conduct testing and quality assurance (P3) -- (depends on: Develop user authentication and authorization, Develop user profile management, Develop experience and guide management, Implement matchmaking algorithm, Design and develop user interface, Implement payment processing)
13. Write documentation (P2) -- (depends on: Define project scope and requirements, Design system architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LocalExperienceMatchmaker can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform that connects travelers with local experiences and guides based on shared interests, pers.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
