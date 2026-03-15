# AIAssistantDeveloper

You are a coding agent working on AIAssistantDeveloper -- A platform for learning how to develop AI-powered coding assistants, combining coding skills with AI and natural language processing.

## Foundational Axiom

The bottleneck in platform is not compute or data but the feedback loop between intent and artifact; AIAssistantDeveloper compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform for learning how to develop AI-powered coding assistants, combining coding skills with AI
- User interface: define project scope and requirements - revised
- Data layer: set up database and data storage

## Anti-Goals

- **General-purpose platform**: AIAssistantDeveloper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop AI and NLP Components (P3) -- (depends on: Design System Architecture)
4. Implement User Interface (P3) -- (depends on: Design System Architecture)
5. Set up Database and Data Storage (P3) -- (depends on: Design System Architecture)
6. Implement Security and Access Controls (P2) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P2) -- (depends on: Design System Architecture)
8. Write Documentation and Tutorials (P2) -- (depends on: Define Project Scope and Requirements)
9. Test and Quality Assurance (P2) -- (depends on: Develop AI and NLP Components, Implement User Interface, Set up Database and Data Storage, Implement Security and Access Controls)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIAssistantDeveloper can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Rust
- GraphQL
- REST API

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for learning how to develop AI-powered coding assistants, combining coding skills with AI.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
