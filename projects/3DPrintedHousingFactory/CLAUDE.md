You are a coding agent working on **3DPrintedHousingFactory** -- a facility control system that uses large-scale 3D printing technology to rapidly produce affordable, customizable housing components. The primary users are manufacturing engineers and production managers. The stack is Python.

## Foundational Axiom

Existing approaches to facility automation fail because they optimize for the common case while ignoring structural constraints; 3DPrintedHousingFactory makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read this file and `spec.org` in full.
2. You understand the current build step and its acceptance test.
3. You will not skip a failing acceptance test.

## What You Are Building

- A cloud-native microservices system for controlling large-scale 3D printers, managing housing component designs, and orchestrating production workflows.
- A customizable housing component library with structural, interior, and exterior elements that can be configured and 3D printed.
- An integrated production pipeline covering order management, material handling, quality control, logistics, and compliance.

## Anti-Goals

- **General-purpose platform**: Solve the specific 3D-printed housing problem, not a platform for all manufacturing domains.
- **Manual-first workflow**: If a human must babysit routine operations, the automation has failed.
- **Demo-ware**: Optimize for production reliability, not impressive demos that break under real conditions.

## Build Order

1. Define Project Scope and Requirements (P5, project-manager)
2. Design 3D Printing System Architecture (P5, code-architect) -- depends on 1
3. Develop 3D Printing Software (P3, backend-developer) -- depends on 2
4. Design and Implement Housing Component Library (P3, frontend-developer) -- depends on 1
5. Establish Production Workflow and Processes (P3, project-manager) -- depends on 1
6. Implement Security and Compliance Measures (P3, security-specialist) -- depends on 1
7. Develop Testing and Quality Assurance Plan (P3, qa-tester) -- depends on 1
8. Set up Infrastructure and Facilities (P2, devops-engineer) -- depends on 1
9. Create User Documentation and Training Materials (P2, technical-writer) -- depends on 1, 3, 4
10. Plan and Execute Pilot Production Run (P2, project-manager) -- depends on 3, 4, 5, 6, 7, 8

### Failure Handler

If an acceptance test fails, **stop**. Document what failed, what you tried, and what the blocker is. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

| ID    | Claim                                                        | Falsification                                                              |
|-------|--------------------------------------------------------------|----------------------------------------------------------------------------|
| C-001 | Core value proposition can be delivered end-to-end           | Integration test of end-to-end workflow fails to produce expected output   |
| C-002 | AI/ML components achieve sufficient accuracy for production  | Model accuracy on held-out test set falls below domain-specific threshold  |
| C-003 | Architecture scales horizontally to meet projected demand    | Load test shows non-linear degradation before target throughput            |
| C-004 | Security implementation meets compliance requirements        | Penetration test or security audit reveals critical vulnerability          |

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: rapid production of affordable, customizable housing components.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to manufacturing engineers and production managers.
