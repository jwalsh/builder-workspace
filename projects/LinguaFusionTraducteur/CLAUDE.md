# LinguaFusionTraducteur

You are a coding agent working on LinguaFusionTraducteur -- Un système de traduction automatique qui combine les technologies d'intelligence artificielle et d'apprentissage automatique pour fournir des traductions précises et efficaces.

## Foundational Axiom

Existing approaches to un système de traduction automatique qui combine les technol fail because they optimize for the common case while ignoring structural constraints; LinguaFusionTraducteur makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development (api design & implementation)
- User interface: requirements gathering and analysis
- Data layer: database design & implementation

## Anti-Goals

- **General-purpose platform**: LinguaFusionTraducteur solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Security Review and Audit (P5) -- (depends on: All other tasks)
2. Deployment and Launch (P5) -- (depends on: All other tasks)
3. Requirements Gathering and Analysis (P1)
4. System Design and Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
5. AI/ML Model Development (P4) -- (depends on: System Design and Architecture)
6. Backend Development (API Design & Implementation) (P3) -- (depends on: System Design and Architecture)
7. Frontend Development (UI/UX Design & Implementation) (P3) -- (depends on: System Design and Architecture)
8. Integration Testing (P4) -- (depends on: Backend Development, Frontend Development, AI/ML Model Development)
9. Database Design & Implementation (P3) -- (depends on: System Design and Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LinguaFusionTraducteur can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un système de traduction automatique qui combine les technologies d'intelligence artificielle et d'a.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
