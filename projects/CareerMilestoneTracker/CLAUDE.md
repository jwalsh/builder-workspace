# CareerMilestoneTracker

You are a coding agent working on CareerMilestoneTracker -- A system that celebrates and rewards employees' career milestones and achievements.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; CareerMilestoneTracker makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend components
- User interface: define project scope and requirements
- Data layer: design database schema for careermilestonetracker system

## Anti-Goals

- **General-purpose platform**: CareerMilestoneTracker solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Implement Comprehensive Security Measures (P5) -- (depends on: Design System Architecture)
4. Design Database Schema for CareerMilestoneTracker System (P3) -- (depends on: Design System Architecture, Define Data Model for CareerMilestoneTracker)
5. Develop Backend Components (P4) -- (depends on: Design System Architecture, Design Database Schema)
6. Develop Frontend Components (P4) -- (depends on: Design System Architecture)
7. Set up CI/CD Pipeline (P4)
8. Develop Comprehensive Test Suite for CareerMilestoneTracker (P4) -- (depends on: Design System Architecture)
9. Write Detailed Documentation (P4) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Implement Core Functionality)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CareerMilestoneTracker can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: A system that celebrates and rewards employees' career milestones and achievements..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
