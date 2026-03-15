# AIJobRecruiter

You are a coding agent working on AIJobRecruiter -- An AI-powered HR platform that screens candidates and matches them with job openings.

## Foundational Axiom

Existing approaches to ai-powered hr platform fail because they optimize for the common case while ignoring structural constraints; AIJobRecruiter makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: build job matching and recommendation engine
- User interface: define project scope and requirements
- Data layer: set up data storage and management

## Anti-Goals

- **General-purpose platform**: AIJobRecruiter solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design System Architecture for AIJobRecruiter (P2) -- (depends on: Define Project Scope and Requirements, Research and Evaluate AI Technologies)
3. Develop AI Candidate Screening Module (P3) -- (depends on: Design System Architecture)
4. Build Job Matching and Recommendation Engine (P3) -- (depends on: Design System Architecture)
5. Implement User Interfaces (P4) -- (depends on: Design System Architecture)
6. Set up Data Storage and Management (P3) -- (depends on: Design System Architecture)
7. Integrate with Existing HR Systems (P4) -- (depends on: Design System Architecture)
8. Implement Security and Access Controls (P4) -- (depends on: Design System Architecture)
9. Conduct Quality Assurance and Testing (P5) -- (depends on: Develop AI Candidate Screening Module, Build Job Matching and Recommendation Engine, Implement User Interfaces, Set up Data Storage and Management, Integrate with Existing HR Systems, Implement Security and Access Controls)
10. Set up Continuous Integration and Deployment (P4) -- (depends on: Design System Architecture)
11. Write Technical Documentation (P4) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: AIJobRecruiter can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Docker
- Kubernetes

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered HR platform that screens candidates and matches them with job openings..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to hr professionals and talent acquisition teams.
