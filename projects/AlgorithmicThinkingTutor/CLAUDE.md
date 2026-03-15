# AlgorithmicThinkingTutor

You are a coding agent working on AlgorithmicThinkingTutor -- An AI-powered tutor that guides users through the process of developing algorithmic thinking skills, from problem analysis to solution design.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; AlgorithmicThinkingTutor closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: ai engine development
- User interface: project planning and requirements gathering
- Data layer: data storage and management

## Anti-Goals

- **General-purpose platform**: AlgorithmicThinkingTutor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for AlgorithmicThinkingTutor - Revised (P5) -- (depends on: Project Planning and Requirements Gathering)
3. AI Engine Development (P3) -- (depends on: System Architecture Design)
4. User Interface Design and Development (P3) -- (depends on: System Architecture Design)
5. Data Storage and Management (P3) -- (depends on: System Architecture Design)
6. Security and Compliance (P3) -- (depends on: System Architecture Design, Data Storage and Management)
7. Testing and Quality Assurance (P2) -- (depends on: AI Engine Development, User Interface Design and Development, Data Storage and Management)
8. Deployment and DevOps (P2) -- (depends on: AI Engine Development, User Interface Design and Development, Data Storage and Management, Testing and Quality Assurance, Security and Compliance)
9. Documentation and User Support (P2) -- (depends on: AI Engine Development, User Interface Design and Development, Data Storage and Management)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AlgorithmicThinkingTutor can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- PostgreSQL
- MongoDB
- Redis
- Docker
- AWS

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered tutor that guides users through the process of developing algorithmic thinking skills,.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
