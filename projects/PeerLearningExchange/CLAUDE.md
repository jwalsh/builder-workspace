# PeerLearningExchange

You are a coding agent working on PeerLearningExchange -- A system facilitating peer-to-peer learning sessions where employees can teach and learn from each other.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; PeerLearningExchange closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system facilitating peer-to-peer learning sessions where employees can teach and learn from each o
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: PeerLearningExchange solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. System Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. User Authentication and Authorization (P4) -- (depends on: System Architecture Design)
4. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
5. Learning Session Management (P4) -- (depends on: System Architecture Design, Database Design and Implementation)
6. User Profile and Skill Management (P4) -- (depends on: System Architecture Design, Database Design and Implementation)
7. Notification and Communication System (P3) -- (depends on: System Architecture Design, Database Design and Implementation)
8. User Interface Design and Development (P4) -- (depends on: System Architecture Design, Learning Session Management, User Profile and Skill Management)
9. Testing and Quality Assurance (P4) -- (depends on: User Authentication and Authorization, Learning Session Management, User Profile and Skill Management, Notification and Communication System, User Interface Design and Development)
10. Deployment and DevOps (P5) -- (depends on: Testing and Quality Assurance)
11. Security and Compliance (P4) -- (depends on: System Architecture Design, User Authentication and Authorization)
12. Documentation and User Support (P3) -- (depends on: User Interface Design and Development, Learning Session Management, User Profile and Skill Management)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PeerLearningExchange can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system facilitating peer-to-peer learning sessions where employees can teach and learn from each o.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
