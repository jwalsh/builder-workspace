# RealTimeSyncOrchestrator

You are a coding agent working on RealTimeSyncOrchestrator -- A platform that ensures real-time synchronization of data and processes across multiple systems and departments.

## Foundational Axiom

Infrastructure tools fail when they treat configuration as static; RealTimeSyncOrchestrator models infrastructure as a continuously evolving system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: data synchronization mechanism design - review and improvements

## Anti-Goals

- **General-purpose platform**: RealTimeSyncOrchestrator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design for RealTimeSyncOrchestrator (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Data Synchronization Mechanism Design - Review and Improvements (P5) -- (depends on: System Architecture Design)
4. Security and Access Control (P5) -- (depends on: System Architecture Design, Data Modeling and Integration)
5. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
6. Backend Development (P3) -- (depends on: Data Synchronization Mechanism Design, Database Design and Implementation)
7. Frontend Development (P2) -- (depends on: Backend Development)
8. Testing and Quality Assurance (P3) -- (depends on: Backend Development, Frontend Development)
9. Deployment and DevOps (P2) -- (depends on: Backend Development, Frontend Development, Testing and Quality Assurance)
10. Documentation and Training (P2) -- (depends on: Backend Development, Frontend Development)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RealTimeSyncOrchestrator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Go with Bubble Tea (charmbracelet/bubbletea) for TUI framework
- Lip Gloss (charmbracelet/lipgloss) for styling
- Bubbles (charmbracelet/bubbles) for common TUI components
- Go standard library for backend logic

## Implementation Notes

This project is implemented as a terminal user interface (TUI) application.
- Use Bubble Tea's Model-Update-View (MVU) architecture
- Main views: dashboard (default), detail, help
- Support keyboard navigation (j/k for up/down, enter for select, q to quit, ? for help)
- Use Lip Gloss for consistent styling with a dark theme
- Refresh data on a configurable tick interval (default 5s)
- Support `--json` flag for non-interactive headless output
- Include a Makefile with `build`, `run`, `test` targets

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A platform that ensures real-time synchronization of data and processes across multiple systems and .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to devops engineers and infrastructure operators.
