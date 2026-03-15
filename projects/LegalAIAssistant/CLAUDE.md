# LegalAIAssistant

You are a coding agent working on LegalAIAssistant -- An AI-powered legal assistant that helps lawyers analyze case law, draft documents, and provide initial legal advice to clients.

## Foundational Axiom

Existing approaches to ai-powered legal assistant fail because they optimize for the common case while ignoring structural constraints; LegalAIAssistant makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project scope and requirements for legalaiassistant
- Data layer: establish database schema and integrations

## Anti-Goals

- **General-purpose platform**: LegalAIAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements for LegalAIAssistant (P1)
2. Design LegalAIAssistant Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend Interface (P3) -- (depends on: Design LegalAIAssistant Architecture)
4. Develop Backend Services (P3) -- (depends on: Design LegalAIAssistant Architecture)
5. Establish Database Schema and Integrations (P4) -- (depends on: Design LegalAIAssistant Architecture)
6. Perform Quality Assurance Tests (P5) -- (depends on: Develop Frontend Interface, Develop Backend Services, Establish Database Schema and Integrations)
7. Deploy LegalAIAssistant to Production Environment (P5) -- (depends on: Perform Quality Assurance Tests)
8. Conduct Security Audit and Remediation (P5) -- (depends on: Deploy LegalAIAssistant to Production Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: LegalAIAssistant can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-powered legal assistant that helps lawyers analyze case law, draft documents, and provide init.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
