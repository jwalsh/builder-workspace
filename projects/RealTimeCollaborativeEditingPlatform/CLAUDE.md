# RealTimeCollaborativeEditingPlatform

You are a coding agent working on RealTimeCollaborativeEditingPlatform -- A platform enabling thousands of users to collaboratively edit documents in real-time with conflict resolution and version control.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; RealTimeCollaborativeEditingPlatform captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend infrastructure for real-time updates
- User interface: define core requirements

## Anti-Goals

- **General-purpose platform**: RealTimeCollaborativeEditingPlatform solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Core Requirements (P1)
2. Develop User Interface for Collaborative Editing (P1) -- (depends on: Define Core Requirements)
3. Design Real-time Collaboration Mechanism (P2) -- (depends on: Define Core Requirements)
4. Develop Backend Infrastructure for Real-time Updates (P2) -- (depends on: Design Real-time Collaboration Mechanism)
5. Perform Security Audit (P5) -- (depends on: Develop User Interface for Collaborative Editing, Develop Backend Infrastructure for Real-time Updates)
6. Develop Conflict Resolution Algorithm (P4) -- (depends on: Design Real-time Collaboration Mechanism)
7. Create Comprehensive Technical Documentation for RealTimeCollaborativeEditingPlatform (P4) -- (depends on: Develop User Interface for Collaborative Editing, Develop Backend Infrastructure for Real-time Updates)
8. Implement Version Control System (P3) -- (depends on: Define Core Requirements)
9. Set Up Continuous Integration/Continuous Deployment (CI/CD) Pipeline (P3) -- (depends on: Implement Version Control System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeCollaborativeEditingPlatform can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform enabling thousands of users to collaboratively edit documents in real-time with conflict .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
