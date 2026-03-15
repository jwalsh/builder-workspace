# VirtualSurgeonAI

You are a coding agent working on VirtualSurgeonAI -- Create an AI-powered virtual reality platform for surgical training and planning, using real patient data to simulate complex procedures.

## Foundational Axiom

Existing approaches to create an ai-powered virtual reality platform fail because they optimize for the common case while ignoring structural constraints; VirtualSurgeonAI makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Create an AI-powered virtual reality platform for surgical training and planning, using real patient
- User interface: define project scope and requirements
- Data layer: integrate patient data

## Anti-Goals

- **General-purpose platform**: VirtualSurgeonAI solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (Revised) (P5) -- (depends on: Define Project Scope and Requirements, Gather and Analyze Real Patient Data)
3. ImplementComprehensiveSecurityandPrivacyMeasures (P5) -- (depends on: DesignSystemArchitecture)
4. Develop Virtual Reality Environment (P3) -- (depends on: Design System Architecture)
5. Integrate Patient Data (P3) -- (depends on: Design System Architecture)
6. Design User Interface and Experience - Updated (P3) -- (depends on: Design System Architecture, Define User Roles and Permissions)
7. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)
8. Implement Surgical Procedure Modeling (P2) -- (depends on: Integrate Patient Data)
9. Create Testing and Validation Framework (P3) -- (depends on: Implement Surgical Procedure Modeling)
10. Document and Provide Training Materials (P2) -- (depends on: Design User Interface and Experience)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualSurgeonAI can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Create an AI-powered virtual reality platform for surgical training and planning, using real patient.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
