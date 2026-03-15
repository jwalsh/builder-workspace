# InterfazHCIAvanzada

You are a coding agent working on InterfazHCIAvanzada -- Una interfaz hombre-máquina avanzada que ofrece experiencias interactivas inmersivas y responsivas.

## Foundational Axiom

Existing approaches to una interfaz hombre-máquina avanzada que ofrece experiencias fail because they optimize for the common case while ignoring structural constraints; InterfazHCIAvanzada makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend integration
- User interface: frontend development (layout & components)
- Data layer: database schema design

## Anti-Goals

- **General-purpose platform**: InterfazHCIAvanzada solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Frontend Development (Layout & Components) (P5) -- (depends on: User Interface Design)
2. Frontend Development (Interactivity & Responsiveness) (P5) -- (depends on: Frontend Development (Layout & Components))
3. Backend Integration (P2) -- (depends on: Frontend Development (Interactivity & Responsiveness))
4. Testing and Quality Assurance (P5) -- (depends on: Frontend Development (Interactivity & Responsiveness), Backend Integration)
5. Requirements Gathering for Advanced HCI Interface - Updated (P1)
6. Design Concept Development (P2) -- (depends on: Requirements Gathering)
7. User Experience (UX) Design (P4) -- (depends on: Design Concept Development)
8. Database Schema Design (P3) -- (depends on: Backend Integration)
9. Database Implementation (P4) -- (depends on: Database Schema Design)
10. Documentation (P4) -- (depends on: Frontend Development (Interactivity & Responsiveness), Backend Integration)
11. User Interface (UI) Design (P3) -- (depends on: Design Concept Development)
12. Deployment and Release of Advanced HCI Interface (P1) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InterfazHCIAvanzada can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una interfaz hombre-máquina avanzada que ofrece experiencias interactivas inmersivas y responsivas..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
