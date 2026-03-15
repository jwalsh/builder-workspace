# GlobalGlossaryPro

You are a coding agent working on GlobalGlossaryPro -- Ein System, das personalisierte Glossare für Unternehmen und Organisationen erstellt, die Inhalte in mehreren Sprachen übersetzen müssen.

## Foundational Axiom

Existing approaches to ein system, das personalisierte glossare für unternehmen und fail because they optimize for the common case while ignoring structural constraints; GlobalGlossaryPro makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services and api
- User interface: develop glossary management interface

## Anti-Goals

- **General-purpose platform**: GlobalGlossaryPro solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Update Technical Documentation Task (P5) -- (depends on: Develop Backend Services, Develop Frontend Interface)
2. Implement Backend Services and API (P4) -- (depends on: Design System Architecture)
3. Integrate with Translation Services (P5) -- (depends on: Implement Backend Services and API)
4. Develop Glossary Management Interface (P4) -- (depends on: Design System Architecture)
5. Create Unit Tests for Core Functionality (P3) -- (depends on: Develop Glossary Management Interface, Implement Backend Services and API)
6. Perform Security Audit (P2) -- (depends on: Develop Glossary Management Interface, Implement Backend Services and API)
7. Deploy System for Initial Testing (P4) -- (depends on: Create Unit Tests for Core Functionality, Perform Security Audit)
8. Iterate Based on Test Results and Feedback (P5) -- (depends on: Deploy System for Initial Testing)
9. Requirements Gathering and Analysis (P1)
10. Define Project Scope and Goals (P2) -- (depends on: Requirements Gathering and Analysis)
11. Prepare Documentation and Training Materials (P2) -- (depends on: Iterate Based on Test Results and Feedback)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: GlobalGlossaryPro can deliver its core value proposition as described
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
