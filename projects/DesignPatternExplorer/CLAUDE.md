# DesignPatternExplorer

You are a coding agent working on DesignPatternExplorer -- An interactive system for learning and practicing common software design patterns through coding exercises.

## Foundational Axiom

Existing approaches to interactive system fail because they optimize for the common case while ignoring structural constraints; DesignPatternExplorer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements - revised
- Data layer: set up database

## Anti-Goals

- **General-purpose platform**: DesignPatternExplorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - REVISED (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend (P3) -- (depends on: Design System Architecture)
4. Develop Backend (P3) -- (depends on: Design System Architecture)
5. Set up Database (P3) -- (depends on: Design System Architecture)
6. Set up CI/CD Pipeline (P3) -- (depends on: Develop Frontend, Develop Backend)
7. Implement Security Measures (P3) -- (depends on: Develop Frontend, Develop Backend)
8. Implement Design Pattern Exercises (P2) -- (depends on: Develop Backend)
9. Write Documentation (P2) -- (depends on: Implement Design Pattern Exercises)
10. Conduct Testing (P2) -- (depends on: Implement Design Pattern Exercises, Write Documentation)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DesignPatternExplorer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An interactive system for learning and practicing common software design patterns through coding exe.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
