# assistantFormationSimulation

You are a coding agent working on assistantFormationSimulation -- Un assistant qui crée des simulations interactives pour des formations en temps réel via la réalité virtuelle.

## Foundational Axiom

Educational tools fail when they optimize for content delivery over understanding; assistantFormationSimulation closes the gap between instruction and verified comprehension.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services for real-time data processing
- User interface: define project scope and requirements
- Data layer: develop backend services for real-time data processing

## Anti-Goals

- **General-purpose platform**: assistantFormationSimulation solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Real-time Interactive Simulation System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend for Interactive Simulation User Interface (P3) -- (depends on: Design Real-time Interactive Simulation System Architecture)
4. Develop Backend Services for Real-time Data Processing (P3) -- (depends on: Design Real-time Interactive Simulation System Architecture)
5. Integrate Virtual Reality Technology for Immersion (P4) -- (depends on: Design Real-time Interactive Simulation System Architecture)
6. Test and Validate the Simulation System (P5) -- (depends on: Develop Frontend for Interactive Simulation User Interface, Develop Backend Services for Real-time Data Processing, Integrate Virtual Reality Technology for Immersion)
7. Deploy and Monitor the assistantFormationSimulation System (P5) -- (depends on: Test and Validate the Simulation System)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: assistantFormationSimulation can deliver its core value proposition as described
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

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un assistant qui crée des simulations interactives pour des formations en temps réel via la réalité .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to educators and learners in structured learning environments.
