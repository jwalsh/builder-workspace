# ProgrammingLanguageSandbox

You are a coding agent working on ProgrammingLanguageSandbox -- A safe environment for experimenting with various programming languages, complete with interactive tutorials and challenges.

## Foundational Axiom

The bottleneck in safe environment is not compute or data but the feedback loop between intent and artifact; ProgrammingLanguageSandbox compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: ProgrammingLanguageSandbox solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Frontend Development (P3) -- (depends on: System Architecture Design)
4. Backend Development (P3) -- (depends on: System Architecture Design)
5. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
6. Security and Compliance (P3) -- (depends on: System Architecture Design)
7. Infrastructure Setup and Deployment (P2) -- (depends on: Frontend Development, Backend Development, Database Design and Implementation)
8. Testing and Quality Assurance (P2) -- (depends on: Frontend Development, Backend Development, Database Design and Implementation)
9. Documentation and User Guides (P2) -- (depends on: Frontend Development, Backend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ProgrammingLanguageSandbox can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python
- TypeScript/JavaScript
- Java

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A safe environment for experimenting with various programming languages, complete with interactive t.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
