# IncidentResponseOrchestrator

You are a coding agent working on IncidentResponseOrchestrator -- A platform that automates and orchestrates incident response processes across multiple tools and teams.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; IncidentResponseOrchestrator models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A platform that automates and orchestrates incident response processes across multiple tools and tea
- User interface: define project scope and requirements - revised
- Data layer: develop data models and database schema

## Anti-Goals

- **General-purpose platform**: IncidentResponseOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Revised (P5)
2. Design System Architecture for IncidentResponseOrchestrator (P5) -- (depends on: Define Project Scope and Requirements, Identify External Tools and Systems)
3. Implement Security and Access Control (P4) -- (depends on: Design System Architecture)
4. Develop Data Models and Database Schema (P3) -- (depends on: Design System Architecture)
5. Implement Core Incident Management Functionality (P2) -- (depends on: Design System Architecture, Develop Data Models and Database Schema)
6. Build User Interface and Dashboard (P3) -- (depends on: Design System Architecture, Implement Core Incident Management Functionality)
7. Develop Automation and Orchestration Workflows (P2) -- (depends on: Design System Architecture, Implement Core Incident Management Functionality)
8. Set up Continuous Integration and Deployment (P3) -- (depends on: Implement Core Incident Management Functionality, Develop Automation and Orchestration Workflows, Build User Interface and Dashboard, Implement Security and Access Control)
9. Prepare Documentation and User Guides (P3) -- (depends on: Implement Core Incident Management Functionality, Develop Automation and Orchestration Workflows, Build User Interface and Dashboard)
10. Conduct Comprehensive Testing (P2) -- (depends on: Implement Core Incident Management Functionality, Develop Automation and Orchestration Workflows, Build User Interface and Dashboard, Implement Security and Access Control)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: IncidentResponseOrchestrator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A platform that automates and orchestrates incident response processes across multiple tools and tea.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
