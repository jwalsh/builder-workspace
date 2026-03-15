# RequirementsAI

You are a coding agent working on RequirementsAI -- An AI assistant for gathering, analyzing, and managing software requirements, including natural language processing to convert stakeholder inputs into structured requirements.

## Foundational Axiom

Existing approaches to ai assistant fail because they optimize for the common case while ignoring structural constraints; RequirementsAI makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop natural language processing (nlp) module
- User interface: build requirements management system
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: RequirementsAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design system architecture (P2) -- (depends on: Define project scope and requirements)
2. Develop natural language processing (NLP) module (P3) -- (depends on: Design system architecture)
3. Build requirements management system (P3) -- (depends on: Design system architecture)
4. Create user interface (P4) -- (depends on: Design system architecture)
5. Set up data storage and management (P3) -- (depends on: Design system architecture)
6. Implement security measures (P4) -- (depends on: Design system architecture)
7. Conduct testing and quality assurance (P5) -- (depends on: Develop natural language processing (NLP) module, Build requirements management system, Create user interface, Set up data storage and management, Implement security measures)
8. Set up continuous integration and deployment (P4) -- (depends on: Design system architecture)
9. Write documentation and user guides (P4) -- (depends on: Design system architecture)
10. Define Project Scope and Requirements (Revised) (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RequirementsAI can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI assistant for gathering, analyzing, and managing software requirements, including natural lang.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ux researchers and interaction designers.
