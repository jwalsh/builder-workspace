# AILegalResearchAssistant

You are a coding agent working on AILegalResearchAssistant -- An AI system that conducts comprehensive legal research, analyzes case law, and provides relevant citations for legal briefs.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; AILegalResearchAssistant makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop data acquisition and processing pipeline
- User interface: define project scope and requirements
- Data layer: develop data acquisition and processing pipeline

## Anti-Goals

- **General-purpose platform**: AILegalResearchAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for AI Legal Research Assistant (P5) -- (depends on: Define Project Scope and Requirements, Identify Legal Data Sources and APIs)
3. Develop Data Acquisition and Processing Pipeline (P3) -- (depends on: Design System Architecture)
4. Build Natural Language Processing (NLP) Module (P3) -- (depends on: Design System Architecture)
5. Develop User Interface and Interaction (P3) -- (depends on: Design System Architecture)
6. Implement Security and Compliance Measures (P3) -- (depends on: Design System Architecture)
7. Implement Legal Reasoning and Citation Engine (P2) -- (depends on: Build Natural Language Processing (NLP) Module)
8. Integrate System Components (P2) -- (depends on: Develop Data Acquisition and Processing Pipeline, Build Natural Language Processing (NLP) Module, Implement Legal Reasoning and Citation Engine, Develop User Interface and Interaction)
9. Create Documentation and User Guides (P3) -- (depends on: Integrate System Components)
10. Conduct System Testing and Evaluation (P2) -- (depends on: Integrate System Components)
11. Deploy and Maintain System (P2) -- (depends on: Conduct System Testing and Evaluation, Implement Security and Compliance Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AILegalResearchAssistant can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that conducts comprehensive legal research, analyzes case law, and provides relevant ci.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to legal professionals and compliance officers.
