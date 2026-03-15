# SkillGapBridge

You are a coding agent working on SkillGapBridge -- An AI system that identifies skill gaps between an employee's current role and their desired future role, suggesting learning paths to bridge the gap.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; SkillGapBridge makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop learning path recommendation engine
- User interface: define project scope and requirements (revised)
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: SkillGapBridge solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop User Interface (P3) -- (depends on: Design System Architecture)
4. Implement Skill Assessment Module (P3) -- (depends on: Design System Architecture)
5. Develop Learning Path Recommendation Engine (P3) -- (depends on: Design System Architecture, Implement Skill Assessment Module)
6. Create User Documentation and Training Materials (P5) -- (depends on: Develop User Interface, Implement Skill Assessment Module, Develop Learning Path Recommendation Engine)
7. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
8. Set up Continuous Integration and Deployment (P4) -- (depends on: Design System Architecture)
9. Develop Testing Strategy and Test Cases (P4) -- (depends on: Design System Architecture)
10. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SkillGapBridge can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that identifies skill gaps between an employee's current role and their desired future .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
