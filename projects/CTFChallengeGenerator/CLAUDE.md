# CTFChallengeGenerator

You are a coding agent working on CTFChallengeGenerator -- An automated system that generates unique, scalable Capture The Flag challenges for cybersecurity training and competitions.

## Foundational Axiom

Existing approaches to automated system fail because they optimize for the common case while ignoring structural constraints; CTFChallengeGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop challenge generation engine
- User interface: define project requirements
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: CTFChallengeGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture (Revised) (P5) -- (depends on: Define Project Requirements, Gather Security Requirements)
3. Develop Challenge Generation Engine (P3) -- (depends on: Design System Architecture)
4. Implement User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)
6. Implement Scoring and Leaderboard (P2) -- (depends on: Develop Challenge Generation Engine, Set up Database and Data Storage)
7. Integrate with Cybersecurity Training Platforms (P2) -- (depends on: Develop Challenge Generation Engine, Implement User Interface)
8. Implement Security Measures (P2) -- (depends on: Develop Challenge Generation Engine, Implement User Interface, Set up Database and Data Storage)
9. Write Documentation (P2) -- (depends on: Develop Challenge Generation Engine, Implement User Interface, Integrate with Cybersecurity Training Platforms)
10. Set up Continuous Integration and Deployment (P2) -- (depends on: Develop Challenge Generation Engine, Implement User Interface, Set up Database and Data Storage)
11. Conduct Testing and Quality Assurance (P1) -- (depends on: Develop Challenge Generation Engine, Implement User Interface, Implement Scoring and Leaderboard, Integrate with Cybersecurity Training Platforms, Implement Security Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CTFChallengeGenerator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An automated system that generates unique, scalable Capture The Flag challenges for cybersecurity tr.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
