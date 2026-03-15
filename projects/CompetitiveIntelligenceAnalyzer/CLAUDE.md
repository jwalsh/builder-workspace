# CompetitiveIntelligenceAnalyzer

You are a coding agent working on CompetitiveIntelligenceAnalyzer -- An AI-driven tool that gathers and analyzes data about competitors to provide strategic insights.

## Foundational Axiom

Existing approaches to ai-driven tool fail because they optimize for the common case while ignoring structural constraints; CompetitiveIntelligenceAnalyzer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement data processing and analysis component
- User interface: define project scope and requirements (revised)
- Data layer: implement data collection component

## Anti-Goals

- **General-purpose platform**: CompetitiveIntelligenceAnalyzer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (Revised) (P1)
2. Design System Architecture (P2) -- (depends on: Define Project Scope and Requirements)
3. Create Test Plans and Test Cases (P4) -- (depends on: Design System Architecture)
4. Conduct System Testing and Quality Assurance (P5) -- (depends on: Create Test Plans and Test Cases)
5. Implement Data Collection Component (P4) -- (depends on: Design System Architecture)
6. Implement Data Processing and Analysis Component (P4) -- (depends on: Design System Architecture)
7. Design and Implement User Interface (P4) -- (depends on: Design System Architecture)
8. Set up Data Storage and Management (P4) -- (depends on: Design System Architecture)
9. Implement Security and Access Control (P4) -- (depends on: Design System Architecture)
10. Deploy and Monitor the System (P5) -- (depends on: Implement Data Collection Component, Implement Data Processing and Analysis Component, Design and Implement User Interface, Set up Data Storage and Management, Implement Security and Access Control, Conduct System Testing and Quality Assurance)
11. Prepare Documentation and User Guides (P4) -- (depends on: Design System Architecture)
12. Set up Development Environment (P3)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CompetitiveIntelligenceAnalyzer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-driven tool that gathers and analyzes data about competitors to provide strategic insights..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
