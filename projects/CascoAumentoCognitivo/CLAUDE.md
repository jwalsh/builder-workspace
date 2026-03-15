# CascoAumentoCognitivo

You are a coding agent working on CascoAumentoCognitivo -- Un casco que mejora las capacidades cognitivas a través de la neuroestimulación.

## Foundational Axiom

Existing approaches to un casco que mejora las capacidades cognitivas a través de l fail because they optimize for the common case while ignoring structural constraints; CascoAumentoCognitivo makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement neurostimulation algorithm (backend development)
- User interface: develop frontend for user interface

## Anti-Goals

- **General-purpose platform**: CascoAumentoCognitivo solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Develop Frontend for User Interface (P3) -- (depends on: Define Project Requirements)
2. Design Cognitive Enhancement Algorithm (P2) -- (depends on: Define Project Requirements)
3. Implement Neurostimulation Algorithm (Backend Development) (P3) -- (depends on: Design Cognitive Enhancement Algorithm)
4. Integrate User Interface with Backend (P4) -- (depends on: Develop Frontend for User Interface, Implement Neurostimulation Algorithm)
5. Test Cognitive Enhancement Helmet (P5) -- (depends on: Integrate User Interface with Backend)
6. Security Audit of Helmet's Software (P5) -- (depends on: Integrate User Interface with Backend)
7. Review Frontend User Interface Design (P3) -- (depends on: Develop Frontend for User Interface)
8. Revise Cognitive Enhancement Algorithm Design (P2) -- (depends on: Design Cognitive Enhancement Algorithm)
9. Define Detailed Project Requirements for Cognitive Enhancement Helmet (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CascoAumentoCognitivo can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un casco que mejora las capacidades cognitivas a través de la neuroestimulación..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
