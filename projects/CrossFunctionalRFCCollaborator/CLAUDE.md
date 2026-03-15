# CrossFunctionalRFCCollaborator

You are a coding agent working on CrossFunctionalRFCCollaborator -- a tool that facilitates collaboration on RFCs across different departments, ensuring comprehensive input and buy-in.

## Foundational Axiom

Existing approaches to cross-functional RFC collaboration fail because they optimize for the common case while ignoring structural constraints; CrossFunctionalRFCCollaborator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step status.
3. You will not skip a failing acceptance test.

## What You Are Building

- A backend service handling RFC submissions, collaboration workflows, and approval pipelines across departments.
- An authentication/authorization layer supporting role-based access per department.
- A frontend interface for submitting, viewing, commenting on, and approving RFCs with version control.

## Anti-Goals

- **General-purpose platform**: Solve the specific RFC collaboration problem, not all documentation problems.
- **Manual-first workflow**: If a human must babysit routine operations, the automation has failed.
- **Demo-ware**: Optimize for production reliability, not impressive demos.

## Build Order

1. Define Project Scope and Requirements (IN_PROGRESS)
2. Design System Architecture (depends on: 1)
3. Implement Authentication and Authorization (depends on: 2)
4. Develop Backend Services (depends on: 2)
5. Develop Frontend User Interface (depends on: 2)
6. Set up Database and Data Models (depends on: 2)
7. Integrate with Existing Systems (depends on: 4, 5, 6)
8. Write Documentation and User Guides (depends on: 4, 5)
9. Conduct Testing and Quality Assurance (depends on: 4, 5, 7)
10. Deploy and Monitor (depends on: 9)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and what the blocker is. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

| ID    | Claim                                                        | Falsification                                                              |
|-------|--------------------------------------------------------------|----------------------------------------------------------------------------|
| C-001 | Core value proposition can be delivered as described         | End-to-end integration test fails to produce expected output               |
| C-002 | AI/ML components achieve sufficient accuracy for production  | Model accuracy on held-out test set falls below domain-specific threshold  |
| C-003 | System meets real-time latency requirements under load       | P95 latency exceeds target under simulated production load                 |
| C-004 | Architecture scales horizontally to meet projected demand    | Load test shows non-linear degradation before target throughput            |
| C-005 | Security implementation meets compliance requirements        | Penetration test or security audit reveals critical vulnerability          |

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: cross-department RFC collaboration with comprehensive input and buy-in.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to primary users (technical writers and documentation teams).

## Primary Output Artifact

A production-ready tool with CLI and/or web interface.
