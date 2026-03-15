# LegalDocumentGenerator

You are a coding agent working on LegalDocumentGenerator -- An AI system that generates customized legal documents based on user inputs and jurisdictional requirements.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; LegalDocumentGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: create backend services for document generation
- User interface: define project scope and requirements (v2)
- Data layer: integrate database for storing user and document data

## Anti-Goals

- **General-purpose platform**: LegalDocumentGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (v2) (P1)
2. Design Architecture for LegalDocumentGenerator (P2) -- (depends on: Define Project Scope and Requirements)
3. Create Backend Services for Document Generation (P4) -- (depends on: Design Architecture for LegalDocumentGenerator)
4. Develop User Interface for Input Collection (P3) -- (depends on: Design Architecture for LegalDocumentGenerator)
5. Integrate Database for Storing User and Document Data (P3) -- (depends on: Design Architecture for LegalDocumentGenerator)
6. Document System Design and Implementation (P3) -- (depends on: Design Architecture for LegalDocumentGenerator)
7. Write Unit Tests for Individual Components (P2) -- (depends on: Develop User Interface for Input Collection, Create Backend Services for Document Generation, Integrate Database for Storing User and Document Data)
8. Perform Code Review on Individual Components (P2) -- (depends on: Develop User Interface for Input Collection, Create Backend Services for Document Generation, Integrate Database for Storing User and Document Data)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LegalDocumentGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Rust

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that generates customized legal documents based on user inputs and jurisdictional requi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
