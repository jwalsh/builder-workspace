# GlobalGlossaryGenerator

You are a coding agent working on GlobalGlossaryGenerator -- Ein System, das personalisierte Glossare für Unternehmen und Organisationen erstellt, die Inhalte in mehreren Sprachen übersetzen müssen.

## Foundational Axiom

Existing approaches to ein system, das personalisierte glossare für unternehmen und fail because they optimize for the common case while ignoring structural constraints; GlobalGlossaryGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements
- Data layer: set up database schema

## Anti-Goals

- **General-purpose platform**: GlobalGlossaryGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design GlobalGlossaryGenerator System Architecture (P2) -- (depends on: Define Project Requirements)
3. Configure DevOps Infrastructure (P5) -- (depends on: Design GlobalGlossaryGenerator System Architecture)
4. Develop Backend Services (P3) -- (depends on: Design GlobalGlossaryGenerator System Architecture)
5. Develop Frontend Interface (P3) -- (depends on: Design GlobalGlossaryGenerator System Architecture)
6. Write Technical Documentation (P5) -- (depends on: Develop Backend Services, Develop Frontend Interface)
7. Set Up Database Schema (P4) -- (depends on: Design GlobalGlossaryGenerator System Architecture)
8. Perform System Testing (P4) -- (depends on: Develop Backend Services, Develop Frontend Interface)
9. Implement Security Measures (P2) -- (depends on: Design GlobalGlossaryGenerator System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalGlossaryGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Ein System, das personalisierte Glossare für Unternehmen und Organisationen erstellt, die Inhalte in.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
