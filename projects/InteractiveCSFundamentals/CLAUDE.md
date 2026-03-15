# InteractiveCSFundamentals

You are a coding agent working on InteractiveCSFundamentals -- A comprehensive, interactive course covering computer science fundamentals, with hands-on coding exercises and visualizations.

## Foundational Axiom

Existing approaches to comprehensive, interactive course covering computer science fail because they optimize for the common case while ignoring structural constraints; InteractiveCSFundamentals makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: set up backend infrastructure
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: InteractiveCSFundamentals solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Set up Backend Infrastructure (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop User Authentication and Authorization (P4) -- (depends on: Set up Backend Infrastructure)
4. Implement Progress Tracking and Reporting (P4) -- (depends on: Set up Backend Infrastructure)
5. Design and Develop User Interface (P4) -- (depends on: Define Project Scope and Requirements)
6. Integrate Frontend and Backend Components (P4) -- (depends on: Develop User Authentication and Authorization, Implement Progress Tracking and Reporting, Design and Develop User Interface)
7. Conduct Comprehensive Testing (P5) -- (depends on: Integrate Frontend and Backend Components)
8. Implement Security Measures (P5) -- (depends on: Integrate Frontend and Backend Components)
9. Deploy and Launch the Course Platform (P5) -- (depends on: Conduct Comprehensive Testing, Implement Security Measures)
10. Develop Maintenance and Support Plan (P5) -- (depends on: Deploy and Launch the Course Platform)
11. Design Course Structure and Curriculum (P2) -- (depends on: Define Project Scope and Requirements)
12. Develop Interactive Coding Exercises (P3) -- (depends on: Design Course Structure and Curriculum)
13. Implement Visualizations and Simulations (P3) -- (depends on: Design Course Structure and Curriculum)
14. Create Course Content (P3) -- (depends on: Design Course Structure and Curriculum)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InteractiveCSFundamentals can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A comprehensive, interactive course covering computer science fundamentals, with hands-on coding exe.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
