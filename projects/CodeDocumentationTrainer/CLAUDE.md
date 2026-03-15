# CodeDocumentationTrainer

You are a coding agent working on CodeDocumentationTrainer -- A tool that challenges users to write clear and comprehensive documentation for given code snippets, teaching good documentation practices.

## Foundational Axiom

The bottleneck in tool is not compute or data but the feedback loop between intent and artifact; CodeDocumentationTrainer compresses that loop.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A tool that challenges users to write clear and comprehensive documentation for given code snippets,
- User interface: project planning and requirements gathering
- Data layer: database design and implementation

## Anti-Goals

- **General-purpose platform**: CodeDocumentationTrainer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P5)
2. System Architecture Design (P5) -- (depends on: Project Planning and Requirements Gathering)
3. Design System Architecture for CodeExplanationGenerator (P5) -- (depends on: Define Project Scope and Requirements)
4. User Interface Design (P3) -- (depends on: System Architecture Design)
5. Code Snippet Management (P3) -- (depends on: System Architecture Design)
6. Documentation Evaluation and Feedback (P3) -- (depends on: System Architecture Design)
7. User Authentication and Authorization (P3) -- (depends on: System Architecture Design)
8. Database Design and Implementation (P3) -- (depends on: System Architecture Design)
9. Continuous Integration and Deployment (P2) -- (depends on: System Architecture Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CodeDocumentationTrainer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
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
2. End-to-end workflow demonstrates core value: A tool that challenges users to write clear and comprehensive documentation for given code snippets,.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to software developers working in professional development environments.
