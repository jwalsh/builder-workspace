# AIPersonalShopper

You are a coding agent working on AIPersonalShopper -- An AI-driven personal shopping service that learns user preferences, tracks fashion trends, and makes personalized product recommendations across multiple e-commerce platforms.

## Foundational Axiom

Existing approaches to ai-driven personal shopping service fail because they optimize for the common case while ignoring structural constraints; AIPersonalShopper makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: ai recommendation engine development
- User interface: project planning and requirements gathering
- Data layer: data model and database design for aipersonalshopper

## Anti-Goals

- **General-purpose platform**: AIPersonalShopper solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (Revised) (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Model and Database Design for AIPersonalShopper (P3) -- (depends on: System Architecture Design)
4. E-commerce Platform Integration (P2) -- (depends on: System Architecture Design)
5. User Interface and Experience Design (Revised) (P3) -- (depends on: System Architecture Design, E-commerce Platform Integration)
6. Security and Privacy Implementation - Revised (P3) -- (depends on: System Architecture Design)
7. AI Recommendation Engine Development (P2) -- (depends on: System Architecture Design, Data Model and Database Design)
8. Documentation and User Support (P3) -- (depends on: User Interface and Experience Design, AI Recommendation Engine Development, E-commerce Platform Integration)
9. Testing and Quality Assurance (P2) -- (depends on: AI Recommendation Engine Development, E-commerce Platform Integration, User Interface and Experience Design)
10. Deployment and DevOps (P2) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIPersonalShopper can deliver its core value proposition as described
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

- MongoDB
- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-driven personal shopping service that learns user preferences, tracks fashion trends, and make.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to retail managers and e-commerce operators.
