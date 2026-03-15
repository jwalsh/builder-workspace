# ARShoppingAssistant

You are a coding agent working on ARShoppingAssistant -- An augmented reality shopping assistant that overlays product information, reviews, and personalized recommendations in real-time as customers browse physical or online stores.

## Foundational Axiom

Existing approaches to augmented reality shopping assistant fail because they optimize for the common case while ignoring structural constraints; ARShoppingAssistant makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: build backend services
- User interface: define project scope and requirements
- Data layer: set up data storage

## Anti-Goals

- **General-purpose platform**: ARShoppingAssistant solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. DesignSystemArchitectureforARShoppingAssistant(Updated) (P5) -- (depends on: DefineProjectScopeandRequirements)
3. Implement Security and Privacy Measures (P4) -- (depends on: Design System Architecture)
4. Develop AR User Interface (P3) -- (depends on: Design System Architecture)
5. Build Backend Services (P3) -- (depends on: Design System Architecture)
6. Set up Data Storage (P3) -- (depends on: Design System Architecture)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
8. Conduct Testing and Quality Assurance (P2) -- (depends on: Develop AR User Interface, Build Backend Services, Set up Data Storage)
9. Write Technical Documentation (P2) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ARShoppingAssistant can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An augmented reality shopping assistant that overlays product information, reviews, and personalized.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to retail managers and e-commerce operators.
