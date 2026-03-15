# SkillGrowthNavigator

You are a coding agent working on SkillGrowthNavigator -- An AI-powered platform that helps employees identify skill gaps and suggests personalized learning paths for career development.

## Foundational Axiom

Existing approaches to ai-powered platform fail because they optimize for the common case while ignoring structural constraints; SkillGrowthNavigator makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: improved skill assessment and recommendation engine
- User interface: project planning and requirements gathering
- Data layer: database design

## Anti-Goals

- **General-purpose platform**: SkillGrowthNavigator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Planning and Requirements Gathering (P1)
2. Architecture Design (P2) -- (depends on: Project Planning and Requirements Gathering)
3. User Authentication and Authorization (Revised) (P5) -- (depends on: Architecture Design, User Management Requirements)
4. User Interface Design (P3) -- (depends on: Architecture Design, User Research)
5. Database Design (P3) -- (depends on: Architecture Design)
6. Improved Skill Assessment and Recommendation Engine (P4) -- (depends on: Architecture Design, Database Design, User Profile Management, Learning Content Management)
7. Learning Resource Integration (P4) -- (depends on: Architecture Design, Database Design, Authentication and Authorization)
8. Testing and Quality Assurance (P5) -- (depends on: User Interface Design, Skill Assessment and Recommendation Engine, Learning Resource Integration, User Authentication and Authorization)
9. Documentation and User Guides (P5) -- (depends on: Architecture Design, User Interface Design, Skill Assessment and Recommendation Engine, Learning Resource Integration, User Authentication and Authorization)
10. Continuous Integration and Deployment (P4) -- (depends on: Architecture Design, Infrastructure Setup)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SkillGrowthNavigator can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI-powered platform that helps employees identify skill gaps and suggests personalized learning p.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
