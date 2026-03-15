# PetDNAAnalyzer

You are a coding agent working on PetDNAAnalyzer -- A tool for analyzing pet DNA to provide insights into breed composition, potential health risks, and personalized care recommendations.

## Foundational Axiom

Existing approaches to tool fail because they optimize for the common case while ignoring structural constraints; PetDNAAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design and implement backend architecture
- User interface: define project scope and requirements - petdnaanalyzer (revised)

## Anti-Goals

- **General-purpose platform**: PetDNAAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements - PetDNAAnalyzer (Revised) (P1)
2. Design User Interface for PetDNAAnalyzer (P2) -- (depends on: Define Project Scope and Requirements)
3. Develop Frontend for PetDNAAnalyzer (P2) -- (depends on: Design User Interface for PetDNAAnalyzer)
4. Design and Implement Backend Architecture (P3) -- (depends on: Define Project Scope and Requirements)
5. Develop Backend for PetDNAAnalyzer (P3) -- (depends on: Design and Implement Backend Architecture)
6. Implement DNA Analysis Algorithm (P4) -- (depends on: Define Project Scope and Requirements)
7. Test PetDNAAnalyzer (P5) -- (depends on: Develop Frontend for PetDNAAnalyzer, Develop Backend for PetDNAAnalyzer, Implement DNA Analysis Algorithm)
8. Write Documentation for PetDNAAnalyzer (P5) -- (depends on: Develop Frontend for PetDNAAnalyzer, Develop Backend for PetDNAAnalyzer)
9. Review and Optimize Codebase (P5) -- (depends on: Develop Frontend for PetDNAAnalyzer, Develop Backend for PetDNAAnalyzer)
10. Integrate Frontend with Backend (P4) -- (depends on: Design and Implement Backend Architecture, Develop Frontend for PetDNAAnalyzer)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PetDNAAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A tool for analyzing pet DNA to provide insights into breed composition, potential health risks, and.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
