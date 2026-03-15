# NeuroLegalTestimonyAnalyzer

You are a coding agent working on NeuroLegalTestimonyAnalyzer -- A system for analyzing the veracity of testimony by monitoring neural activity patterns.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroLegalTestimonyAnalyzer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend algorithm for neural analysis
- User interface: develop frontend interface design
- Data layer: implement database schema

## Anti-Goals

- **General-purpose platform**: NeuroLegalTestimonyAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Architecture (P1)
2. Develop Frontend Interface Design (P2) -- (depends on: Define System Architecture)
3. Develop Backend Algorithm for Neural Analysis (P3) -- (depends on: Define System Architecture)
4. Implement Database Schema (P4) -- (depends on: Define System Architecture)
5. Integrate Frontend with Backend (P2) -- (depends on: Develop Frontend Interface Design, Develop Backend Algorithm for Neural Analysis, Implement Database Schema)
6. Test System Functionality (P5) -- (depends on: Integrate Frontend with Backend)
7. Write Documentation for System Usage and Development (P5) -- (depends on: Integrate Frontend with Backend)
8. Review and Iterate on System Design (P1) -- (depends on: Define System Architecture, Develop Frontend Interface Design, Develop Backend Algorithm for Neural Analysis, Implement Database Schema, Integrate Frontend with Backend)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroLegalTestimonyAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system for analyzing the veracity of testimony by monitoring neural activity patterns..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
