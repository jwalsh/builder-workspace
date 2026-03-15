# EmotionalIntelligenceCoach

You are a coding agent working on EmotionalIntelligenceCoach -- An AI system that provides real-time coaching on emotional intelligence during simulated leadership challenges.

## Foundational Axiom

Environmental tools fail when they model systems in isolation; EmotionalIntelligenceCoach captures the cross-domain interactions that determine real-world outcomes.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop ai coaching engine
- User interface: define project scope and requirements - emotional intelligence coach ai system (revised)
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: EmotionalIntelligenceCoach solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - Emotional Intelligence Coach AI System (Revised) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop User Interface (P4) -- (depends on: Design System Architecture)
4. Establish Security and Privacy Measures (P4) -- (depends on: Design System Architecture)
5. Develop AI Coaching Engine (P3) -- (depends on: Design System Architecture)
6. Build Simulation Environment (P3) -- (depends on: Design System Architecture)
7. Conduct Quality Assurance and Testing (P4) -- (depends on: Develop AI Coaching Engine, Build Simulation Environment, Develop User Interface)
8. Write User Documentation (P4) -- (depends on: Develop User Interface)
9. Implement Data Storage and Management (P3) -- (depends on: Design System Architecture)
10. Set up Continuous Integration and Deployment (P3) -- (depends on: Design System Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: EmotionalIntelligenceCoach can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI system that provides real-time coaching on emotional intelligence during simulated leadership .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to environmental scientists and sustainability officers.
