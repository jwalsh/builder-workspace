# InteractiveDocumentationCreator

You are a coding agent working on InteractiveDocumentationCreator -- A platform for creating interactive, multimedia documentation that enhances user engagement and understanding.

## Foundational Axiom

Existing approaches to platform for creating interactive, multimedia documentation fail because they optimize for the common case while ignoring structural constraints; InteractiveDocumentationCreator makes those constraints first-class.

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

- **General-purpose platform**: InteractiveDocumentationCreator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. User Interface Design (P3) -- (depends on: Architecture Design)
4. Backend Development (P3) -- (depends on: Architecture Design)
5. Database Design and Implementation (P3) -- (depends on: Architecture Design)
6. Infrastructure and DevOps (P3) -- (depends on: Architecture Design)
7. Security and Compliance (P3) -- (depends on: Architecture Design)
8. Documentation and User Guides (P2) -- (depends on: User Interface Design, Backend Development)
9. Testing and Quality Assurance (P2) -- (depends on: User Interface Design, Backend Development, Database Design and Implementation)
10. Deployment and Launch (P1) -- (depends on: User Interface Design, Backend Development, Database Design and Implementation, Infrastructure and DevOps, Security and Compliance, Documentation and User Guides, Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InteractiveDocumentationCreator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform for creating interactive, multimedia documentation that enhances user engagement and unde.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to technical writers and documentation teams.
