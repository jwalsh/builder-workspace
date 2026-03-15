# KI-LiteraturAssistent

You are a coding agent working on KI-LiteraturAssistent -- Ein KI-gestützter Assistent für Autoren, der bei der Erstellung, Übersetzung und Analyse von literarischen Werken hilft.

## Foundational Axiom

Existing approaches to ein ki-gestützter assistent für autoren, der bei der erstell fail because they optimize for the common case while ignoring structural constraints; KI-LiteraturAssistent makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement backend services
- User interface: requirements gathering and analysis

## Anti-Goals

- **General-purpose platform**: KI-LiteraturAssistent solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Requirements Gathering and Analysis (P1)
2. Design KI-LiteraturAssistent Architecture (P2) -- (depends on: Requirements Gathering and Analysis)
3. Implement Backend Services (P4) -- (depends on: Design KI-LiteraturAssistent Architecture)
4. Create and Train Machine Learning Models (P5) -- (depends on: Implement Backend Services)
5. Develop User Interface Design (P3) -- (depends on: Design KI-LiteraturAssistent Architecture)
6. Perform Unit and Integration Testing (P4) -- (depends on: Implement Backend Services, Develop User Interface Design)
7. Deploy KI-LiteraturAssistent to Production Environment (P5) -- (depends on: Perform Unit and Integration Testing)
8. Integrate External APIs and Services (P4) -- (depends on: Implement Backend Services)
9. Document KI-LiteraturAssistent Functionality (P3) -- (depends on: Perform Unit and Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: KI-LiteraturAssistent can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: Ein KI-gestützter Assistent für Autoren, der bei der Erstellung, Übersetzung und Analyse von literar.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
