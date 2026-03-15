# ServerlessComputeEngine

You are a coding agent working on ServerlessComputeEngine -- A next-generation serverless computing platform that automatically scales and manages backend resources.

## Foundational Axiom

Existing approaches to next-generation serverless computing platform fail because they optimize for the common case while ignoring structural constraints; ServerlessComputeEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement serverless compute engine
- User interface: define project scope and requirements - updated

## Anti-Goals

- **General-purpose platform**: ServerlessComputeEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - UPDATED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Security and Access Control (P4) -- (depends on: Design System Architecture)
4. Implement Serverless Compute Engine (P3) -- (depends on: Design System Architecture)
5. Develop Resource Management and Auto-scaling (P3) -- (depends on: Design System Architecture)
6. Design and Develop User Interface (P3) -- (depends on: Define Project Scope and Requirements)
7. Implement Monitoring and Logging (P3) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P3)
9. Conduct System Testing and Quality Assurance (P2) -- (depends on: Implement Serverless Compute Engine, Develop Resource Management and Auto-scaling, Implement Security and Access Control, Design and Develop User Interface, Implement Monitoring and Logging)
10. Document and Publish Developer Resources (P2) -- (depends on: Implement Serverless Compute Engine, Develop Resource Management and Auto-scaling, Implement Security and Access Control, Design and Develop User Interface, Implement Monitoring and Logging)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ServerlessComputeEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A next-generation serverless computing platform that automatically scales and manages backend resour.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
