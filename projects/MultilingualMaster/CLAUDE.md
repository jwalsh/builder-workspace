# MultilingualMaster

You are a coding agent working on MultilingualMaster -- Ein System, das Übersetzungen in mehreren Sprachen für Unternehmen und Organisationen bereitstellt, die Inhalte in mehreren Sprachen übersetzen müssen.

## Foundational Axiom

Existing approaches to ein system, das übersetzungen in mehreren sprachen für unter fail because they optimize for the common case while ignoring structural constraints; MultilingualMaster makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements
- Data layer: configure database schema

## Anti-Goals

- **General-purpose platform**: MultilingualMaster solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Requirements)
3. Configure Database Schema (P5) -- (depends on: Design System Architecture)
4. Set Up Continuous Integration/Continuous Deployment (CI/CD) (P5) -- (depends on: Design System Architecture)
5. Develop Frontend Interface (P3) -- (depends on: Design System Architecture)
6. Develop Backend Services (P3) -- (depends on: Design System Architecture)
7. Perform Unit Tests (P2) -- (depends on: Develop Frontend Interface, Develop Backend Services)
8. Create Translation Workflow (P4) -- (depends on: Define Project Requirements, Design System Architecture)
9. Implement Translation Management UI (P4) -- (depends on: Create Translation Workflow)
10. Perform Integration Tests (P3) -- (depends on: Develop Frontend Interface, Develop Backend Services, Implement Translation Management UI)
11. Conduct System Testing (P4) -- (depends on: Develop Frontend Interface, Develop Backend Services, Implement Translation Management UI, Configure Database Schema, Set Up CI/CD)
12. Fix Identified Issues (P5) -- (depends on: Perform Unit Tests, Perform Integration Tests, Conduct System Testing)
13. Document the Application (P5) -- (depends on: Develop Frontend Interface, Develop Backend Services)
14. Deploy the MultilingualMaster System (P5) -- (depends on: Fix Identified Issues, Configure Database Schema, Set Up CI/CD)
15. Secure the Application (P1) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MultilingualMaster can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Ein System, das Übersetzungen in mehreren Sprachen für Unternehmen und Organisationen bereitstellt, .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
