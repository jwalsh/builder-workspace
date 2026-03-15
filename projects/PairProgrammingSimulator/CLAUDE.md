# PairProgrammingSimulator

You are a coding agent working on PairProgrammingSimulator -- A virtual environment that simulates pair programming scenarios, teaching collaboration and communication skills in coding.

## Foundational Axiom

The bottleneck in virtual environment is not compute or data but the feedback loop between intent and artifact; PairProgrammingSimulator compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend
- User interface: define project scope and requirements
- Data layer: set up database

## Anti-Goals

- **General-purpose platform**: PairProgrammingSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture for PairProgrammingSimulator: REVISED (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Authentication and Authorization (P4) -- (depends on: Design System Architecture)
4. Develop Frontend (P3) -- (depends on: Design System Architecture)
5. Develop Backend (P3) -- (depends on: Design System Architecture)
6. Set up Database (P3) -- (depends on: Design System Architecture)
7. Create Testing Framework (P3) -- (depends on: Develop Frontend, Develop Backend)
8. Implement Continuous Integration and Deployment (P3) -- (depends on: Create Testing Framework)
9. Write Documentation (P2) -- (depends on: Develop Frontend, Develop Backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PairProgrammingSimulator can deliver its core value proposition as described
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

- Python + Flask or FastAPI for backend
- HTML/CSS/JavaScript for frontend (vanilla JS or Alpine.js, no heavy frameworks)
- SQLite for persistence (via sqlite3 standard library)
- Jinja2 for server-side templates
- Replit-compatible: no external services, single `main.py` entry point

## Implementation Notes

This project is designed for deployment on Replit.
- Single entry point: `main.py` with Flask/FastAPI app
- Use `.replit` file for run configuration
- SQLite database in `data/` directory for persistence
- Static files in `static/`, templates in `templates/`
- Environment variables via `.env` (never commit secrets)
- Must work with Replit's free tier constraints (512MB RAM, shared CPU)
- Include a `replit.nix` for system dependencies if needed
- Support both local development and Replit deployment

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A virtual environment that simulates pair programming scenarios, teaching collaboration and communic.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
