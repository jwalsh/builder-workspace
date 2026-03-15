# SynaesthesiaSimulator

You are a coding agent working on SynaesthesiaSimulator -- A device that induces controlled synaesthesia-like experiences for enhanced creativity or therapeutic purposes.

## Foundational Axiom

Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; SynaesthesiaSimulator makes approximation error explicit and bounded.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A device that induces controlled synaesthesia-like experiences for enhanced creativity or therapeuti
- User interface: define synaesthesia simulator requirements

## Anti-Goals

- **General-purpose platform**: SynaesthesiaSimulator solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Synaesthesia Simulator Requirements (P1)
2. Integrate Hardware Components for Synaesthesia Induction (P5) -- (depends on: Define Synaesthesia Simulator Requirements)
3. Develop Algorithms for Controlled Synaesthetic Induction (P4) -- (depends on: Research Synaesthesia Techniques and Induction Methods)
4. Design User Interface for Synaesthesia Simulator (P3) -- (depends on: Define Synaesthesia Simulator Requirements)
5. Research Controlled Synaesthetic Techniques and Induction Methods for Synaesthesia Simulator (P2) -- (depends on: Define Synaesthesia Simulator Requirements)
6. Prepare User Manual and Documentation (P2) -- (depends on: Design User Interface for Synaesthesia Simulator)
7. Test and Validate Synaesthesia Simulator Functionality (P1) -- (depends on: Design User Interface for Synaesthesia Simulator, Develop Algorithms for Controlled Synaesthetic Induction, Integrate Hardware Components for Synaesthesia Induction)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SynaesthesiaSimulator can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A device that induces controlled synaesthesia-like experiences for enhanced creativity or therapeuti.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to engineers and researchers who need high-fidelity simulations.
