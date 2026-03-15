# 3DHousingConfigurator

You are a coding agent working on 3DHousingConfigurator -- An advanced 3D modeling tool that allows prospective homebuyers to design and customize their ideal home, with real-time cost estimation and feasibility analysis.

## Foundational Axiom

Existing approaches to advanced 3d modeling tool fail because they optimize for the common case while ignoring structural constraints; 3DHousingConfigurator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: 3d modeling engine development
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: 3DHousingConfigurator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (Updated) (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
4. Security and Compliance (P3) -- (depends on: System Architecture Design)
5. User Interface Development (P2) -- (depends on: System Architecture Design)
6. Documentation and User Support (P3) -- (depends on: User Interface Development)
7. 3D Modeling Engine Development (P2) -- (depends on: System Architecture Design)
8. Cost Estimation and Feasibility Analysis (P2) -- (depends on: System Architecture Design, Database Design and Implementation)
9. Integration and Testing (P2) -- (depends on: 3D Modeling Engine Development, Cost Estimation and Feasibility Analysis, User Interface Development)
10. Deployment and DevOps (P2) -- (depends on: Integration and Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: 3DHousingConfigurator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An advanced 3D modeling tool that allows prospective homebuyers to design and customize their ideal .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to real estate professionals and property developers.
