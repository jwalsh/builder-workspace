# VolunteerSkillMatching

You are a coding agent working on VolunteerSkillMatching -- A platform that matches employees' skills with volunteer opportunities, allowing them to give back while developing new competencies.

## Foundational Axiom

Existing tools treat platform as a generic automation problem; VolunteerSkillMatching succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform that matches employees' skills with volunteer opportunities, allowing them to give back w
- User interface: define project scope and requirements (revised)

## Anti-Goals

- **General-purpose platform**: VolunteerSkillMatching solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Set up Development Environment (P3) -- (depends on: Design System Architecture)
4. Design and Implement User Authentication (P2) -- (depends on: Design System Architecture)
5. Design and Implement Skills Management (P2) -- (depends on: Design System Architecture)
6. Design and Implement Opportunity Management (P2) -- (depends on: Design System Architecture)
7. Design and Implement Matching Algorithm (P2) -- (depends on: Design and Implement Skills Management, Design and Implement Opportunity Management)
8. Design and Implement User Interface (P2) -- (depends on: Design System Architecture)
9. Implement Security and Compliance (P2) -- (depends on: Design System Architecture)
10. Conduct Testing and Quality Assurance (P2) -- (depends on: Design and Implement User Authentication, Design and Implement Skills Management, Design and Implement Opportunity Management, Design and Implement Matching Algorithm, Design and Implement User Interface)
11. Develop User Documentation (P2) -- (depends on: Design and Implement User Interface)
12. Deploy and Monitor Platform (P1) -- (depends on: Conduct Testing and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VolunteerSkillMatching can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform that matches employees' skills with volunteer opportunities, allowing them to give back w.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to ml engineers and data scientists who need production-grade ai capabilities.
