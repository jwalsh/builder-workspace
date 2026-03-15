# ExecutiveSummaryGenerator

You are a coding agent working on ExecutiveSummaryGenerator -- An AI system that automatically generates concise executive summaries from lengthy reports or documents.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; ExecutiveSummaryGenerator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop natural language processing (nlp) module
- User interface: define project requirements
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: ExecutiveSummaryGenerator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P5)
2. Design System Architecture for ExecutiveSummaryGenerator (P5) -- (depends on: Define Project Requirements)
3. Set up Development Environment (P4)
4. Develop Natural Language Processing (NLP) Module (P3) -- (depends on: Design System Architecture)
5. Develop Text Summarization Module (P3) -- (depends on: Design System Architecture)
6. DesignUserInterface-RFCAPPROVED (P3) -- (depends on: Design System Architecture)
7. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
8. Develop Testing Strategy (P3) -- (depends on: Design System Architecture)
9. Conduct Security Audit (P3) -- (depends on: Design System Architecture)
10. Implement User Interface (P2) -- (depends on: Design User Interface)
11. Implement Testing Suite (P2) -- (depends on: Develop Testing Strategy)
12. Develop Documentation (P2) -- (depends on: Design System Architecture)
13. Deploy and Monitor System (P1) -- (depends on: Implement User Interface, Implement Data Storage and Management, Implement Testing Suite, Develop Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ExecutiveSummaryGenerator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java
- PostgreSQL
- Redis
- Docker
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that automatically generates concise executive summaries from lengthy reports or docume.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
