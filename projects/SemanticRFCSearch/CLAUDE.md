# SemanticRFCSearch

You are a coding agent working on SemanticRFCSearch -- An advanced search engine that understands the context and content of RFCs, allowing for more intuitive and accurate searches.

## Foundational Axiom

Existing approaches to advanced search engine fail because they optimize for the common case while ignoring structural constraints; SemanticRFCSearch makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: natural language processing (nlp) module
- User interface: project planning and requirements gathering
- Data layer: data ingestion and management

## Anti-Goals

- **General-purpose platform**: SemanticRFCSearch solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (Revised) (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Natural Language Processing (NLP) Module (P3) -- (depends on: System Architecture Design)
4. Indexing and Search Engine (P3) -- (depends on: System Architecture Design)
5. User Interface and Experience (P3) -- (depends on: System Architecture Design)
6. Data Ingestion and Management (P2) -- (depends on: System Architecture Design)
7. Testing and Quality Assurance (P2) -- (depends on: Natural Language Processing (NLP) Module, Indexing and Search Engine, User Interface and Experience, Data Ingestion and Management)
8. Security and Compliance (P2) -- (depends on: System Architecture Design)
9. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance, Security and Compliance)
10. Documentation and User Support (P1) -- (depends on: User Interface and Experience, Deployment and DevOps)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SemanticRFCSearch can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced search engine that understands the context and content of RFCs, allowing for more intuit.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to technical writers and documentation teams.
