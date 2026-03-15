# NeuroAdvertisingAnalyzer

You are a coding agent working on NeuroAdvertisingAnalyzer -- A neuromarketing tool that uses brain-computer interfaces to measure and analyze consumers' subconscious responses to advertisements.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; NeuroAdvertisingAnalyzer models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data processing pipeline
- User interface: define project requirements (revised)
- Data layer: implement data processing pipeline

## Anti-Goals

- **General-purpose platform**: NeuroAdvertisingAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Develop Brain-Computer Interface (P3) -- (depends on: Design System Architecture)
4. Implement Data Processing Pipeline (P3) -- (depends on: Design System Architecture)
5. Develop Analysis and Visualization Components (P3) -- (depends on: Design System Architecture)
6. Set up CI/CD Pipeline (P3) -- (depends on: Design System Architecture)
7. Implement Security and Privacy Measures (P2) -- (depends on: Design System Architecture)
8. Conduct System Testing (P2) -- (depends on: Develop Brain-Computer Interface, Implement Data Processing Pipeline, Develop Analysis and Visualization Components)
9. Write Technical Documentation (P2) -- (depends on: Define Project Requirements, Design System Architecture)
10. Deploy and Monitor System (P1) -- (depends on: Conduct System Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: NeuroAdvertisingAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A neuromarketing tool that uses brain-computer interfaces to measure and analyze consumers' subconsc.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
