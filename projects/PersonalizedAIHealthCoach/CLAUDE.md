# PersonalizedAIHealthCoach

You are a coding agent working on PersonalizedAIHealthCoach -- An AI health coach that provides personalized wellness advice based on health metrics.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; PersonalizedAIHealthCoach embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: define project scope and requirements for personalizedaihealthcoach
- Data layer: set up database and storage

## Anti-Goals

- **General-purpose platform**: PersonalizedAIHealthCoach solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements for PersonalizedAIHealthCoach (P1)
2. Design AI Health Coach Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop User Interface (Frontend) (P3) -- (depends on: Design AI Health Coach Architecture)
4. Implement Backend Services (P3) -- (depends on: Design AI Health Coach Architecture)
5. Set Up Database and Storage (P3) -- (depends on: Design AI Health Coach Architecture)
6. Develop AI Model for Personalized Advice (P4) -- (depends on: Design AI Health Coach Architecture)
7. Integrate API Services and Authentication (P3) -- (depends on: Implement Backend Services, Design AI Health Coach Architecture)
8. Document System Architecture, Design Decisions, and API Usage (P5) -- (depends on: Develop User Interface (Frontend), Implement Backend Services, Set Up Database and Storage, Develop AI Model for Personalized Advice, Integrate API Services and Authentication)
9. Test and Validate Functionality (P4) -- (depends on: Develop User Interface (Frontend), Implement Backend Services, Set Up Database and Storage, Develop AI Model for Personalized Advice, Integrate API Services and Authentication)
10. Review Code Quality and Security (P4) -- (depends on: Develop User Interface (Frontend), Implement Backend Services, Set Up Database and Storage, Develop AI Model for Personalized Advice, Integrate API Services and Authentication)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalizedAIHealthCoach can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI health coach that provides personalized wellness advice based on health metrics..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
