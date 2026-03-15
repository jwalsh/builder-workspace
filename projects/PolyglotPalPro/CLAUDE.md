# PolyglotPalPro

You are a coding agent working on PolyglotPalPro -- Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per fornire traduzioni personalizzate e migliorare la comunicazione globale per professionisti e imprese.

## Foundational Axiom

Existing approaches to un assistente di traduzione che utilizza l'intelligenza arti fail because they optimize for the common case while ignoring structural constraints; PolyglotPalPro makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop translation engine
- User interface: design user interface for professional users
- Data layer: implement database structure and integration

## Anti-Goals

- **General-purpose platform**: PolyglotPalPro solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals (P1)
2. Research and Select AI and Machine Learning Technologies (P2) -- (depends on: Define Project Scope and Goals)
3. Design AI/ML Model Architecture (P4) -- (depends on: Research and Select AI and Machine Learning Technologies)
4. Develop Translation Engine (P5) -- (depends on: Design AI/ML Model Architecture)
5. Develop User Authentication and Authorization System (P4) -- (depends on: Define Project Scope and Goals)
6. Implement Database Structure and Integration (P3) -- (depends on: Define Project Scope and Goals)
7. Set Up Continuous Integration/Continuous Deployment Pipeline (P2) -- (depends on: Develop Translation Engine, Develop User Authentication and Authorization System, Implement Database Structure and Integration)
8. Perform Initial Quality Assurance Testing (P5) -- (depends on: Develop Translation Engine, Develop User Authentication and Authorization System, Implement Database Structure and Integration, Set Up Continuous Integration/Continuous Deployment Pipeline)
9. Review and Address Feedback from QA Testers (P4) -- (depends on: Perform Initial Quality Assurance Testing)
10. Design User Interface for Professional Users (P3) -- (depends on: Define Project Scope and Goals)
11. Design User Interface for Corporate Users (P3) -- (depends on: Define Project Scope and Goals)
12. Create Documentation for Users and Developers (P2) -- (depends on: Develop Translation Engine, Develop User Authentication and Authorization System, Implement Database Structure and Integration, Set Up Continuous Integration/Continuous Deployment Pipeline)
13. Review Documentation for Clarity and Completeness (P1) -- (depends on: Create Documentation for Users and Developers)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PolyglotPalPro can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un assistente di traduzione che utilizza l'intelligenza artificiale e l'apprendimento automatico per.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
