# BiorhythmOptimizer

You are a coding agent working on BiorhythmOptimizer -- An AI system that analyzes personal biorhythms to optimize daily schedules for peak performance and wellbeing.

## Foundational Axiom

Biotech tools fail when they treat biological systems as deterministic; BiorhythmOptimizer embraces stochasticity as a design constraint.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI system that analyzes personal biorhythms to optimize daily schedules for peak performance and 
- User interface: gather requirements for biorhythmoptimizer system
- Data layer: implement data ingestion

## Anti-Goals

- **General-purpose platform**: BiorhythmOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Gather Requirements for BiorhythmOptimizer System (P5)
2. DesignSystemArchitectureforBiorhythmOptimizer (P5) -- (depends on: GatherRequirements)
3. Implement Data Ingestion (P2) -- (depends on: Design System Architecture)
4. Develop Biorhythm Analysis (P2) -- (depends on: Design System Architecture)
5. Implement Scheduling Optimization (P2) -- (depends on: Design System Architecture, Develop Biorhythm Analysis)
6. Design User Interfaces - RFC (Revised) (P3) -- (depends on: Design System Architecture, Define User Personas and Use Cases)
7. Implement User Interfaces (P2) -- (depends on: Design User Interfaces)
8. Conduct Security Audits (P4) -- (depends on: Implement Data Ingestion, Develop Biorhythm Analysis, Implement Scheduling Optimization, Implement User Interfaces)
9. Set up Development Environment (P3)
10. Set up Testing Framework (P3)
11. Write Documentation (P2) -- (depends on: Design System Architecture, Design User Interfaces)
12. Deploy and Monitor (P1) -- (depends on: Implement Data Ingestion, Develop Biorhythm Analysis, Implement Scheduling Optimization, Implement User Interfaces, Conduct Security Audits)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: BiorhythmOptimizer can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that analyzes personal biorhythms to optimize daily schedules for peak performance and .
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to biotechnology researchers and lab scientists.
