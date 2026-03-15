# LanguageLeverage

You are a coding agent working on LanguageLeverage -- Ein System, das Übersetzungen für Unternehmen und Organisationen bereitstellt, die Inhalte in mehreren Sprachen übersetzen müssen, um die Kommunikation mit Kunden und Partnern weltweit zu verbessern.

## Foundational Axiom

Existing approaches to ein system, das übersetzungen für unternehmen und organisati fail because they optimize for the common case while ignoring structural constraints; LanguageLeverage makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: build backend services
- User interface: define project requirements
- Data layer: set up database schema

## Anti-Goals

- **General-purpose platform**: LanguageLeverage solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Frontend Interface (P3) -- (depends on: Define Project Requirements, Design Architecture)
4. Build Backend Services (P3) -- (depends on: Define Project Requirements, Design Architecture)
5. Implement Translation Engine (P4) -- (depends on: Define Project Requirements, Design Architecture)
6. Set Up Database Schema (P4) -- (depends on: Define Project Requirements, Design Architecture)
7. Deploy Test Environment (P5) -- (depends on: Define Project Requirements, Design Architecture, Develop Frontend Interface, Build Backend Services, Implement Translation Engine, Set Up Database Schema)
8. Test Translation System (P5) -- (depends on: Deploy Test Environment)
9. Revise and Refactor Code (P5) -- (depends on: Test Translation System)
10. Prepare Documentation (P5) -- (depends on: Test Translation System)
11. Deploy Production Environment (P5) -- (depends on: Revise and Refactor Code)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LanguageLeverage can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Ein System, das Übersetzungen für Unternehmen und Organisationen bereitstellt, die Inhalte in mehrer.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
