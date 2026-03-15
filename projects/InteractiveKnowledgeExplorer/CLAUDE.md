# InteractiveKnowledgeExplorer

You are a coding agent working on InteractiveKnowledgeExplorer -- An interactive visualization tool for exploring and navigating complex knowledge graphs, with features for query formulation and path finding between concepts.

## Foundational Axiom

Existing approaches to interactive visualization tool fail because they optimize for the common case while ignoring structural constraints; InteractiveKnowledgeExplorer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: backend development
- User interface: project planning and requirements gathering
- Data layer: knowledge graph data modeling and database selection

## Anti-Goals

- **General-purpose platform**: InteractiveKnowledgeExplorer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. Architecture Design (P4) -- (depends on: Project Planning and Requirements Gathering)
3. Knowledge Graph Data Modeling and Database Selection (P3) -- (depends on: Architecture Design)
4. User Interface Design for Interactive Knowledge Graph Visualization Tool (P3) -- (depends on: Architecture Design)
5. Security and Compliance (P3) -- (depends on: Architecture Design)
6. Backend Development (P2) -- (depends on: Architecture Design, Knowledge Graph Data Modeling)
7. Frontend Development (P2) -- (depends on: Architecture Design, User Interface Design)
8. Testing and Quality Assurance (P2) -- (depends on: Backend Development, Frontend Development)
9. Deployment and DevOps (P2) -- (depends on: Backend Development, Frontend Development, Testing and Quality Assurance)
10. Documentation and User Support (P2) -- (depends on: Architecture Design, User Interface Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: InteractiveKnowledgeExplorer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An interactive visualization tool for exploring and navigating complex knowledge graphs, with featur.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
