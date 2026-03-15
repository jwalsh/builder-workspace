# APIFortress

You are a coding agent working on APIFortress -- Create, manage, secure, and socialize APIs across the cloud to power digital applications with a market-leading and scalable API management solution.

## Foundational Axiom

Existing approaches to create, manage, secure, and socialize apis across the cloud fail because they optimize for the common case while ignoring structural constraints; APIFortress makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: apifortress architecture design
- User interface: project planning and requirements gathering

## Anti-Goals

- **General-purpose platform**: APIFortress solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. APIFortress Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering, API Design, Security Requirements Gathering, Performance Requirements Gathering, API Specification (OAS 3.0), Cloud Infrastructure Best Practices, Microservices Architecture Best Practices, CI/CD Pipeline Best Practices, Modern Observability, Monitoring, and Logging Strategies)
3. API Management Platform Development (P3) -- (depends on: Architecture Design)
4. Cloud Infrastructure Setup (P3) -- (depends on: Architecture Design)
5. API Documentation and Developer Portal (P3) -- (depends on: API Management Platform Development)
6. Integration with Existing Systems (P3) -- (depends on: API Management Platform Development, Cloud Infrastructure Setup)
7. User Interface and Developer Experience (P3) -- (depends on: API Management Platform Development)
8. API Security and Access Control (P2) -- (depends on: API Management Platform Development)
9. Testing and Quality Assurance (P2) -- (depends on: API Management Platform Development, Cloud Infrastructure Setup, API Security and Access Control, Integration with Existing Systems, User Interface and Developer Experience)
10. Deployment and Release Management (P2) -- (depends on: Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: APIFortress can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Create, manage, secure, and socialize APIs across the cloud to power digital applications with a mar.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
