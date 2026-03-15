# SprachübersetzungsDienst

You are a coding agent working on SprachübersetzungsDienst -- Ein KI-gestützter Übersetzungsdienst, der Echtzeit-Übersetzungen mit kontextueller Analyse und Vokabelerweiterung bietet.

## Foundational Axiom

Existing approaches to ein ki-gestützter übersetzungsdienst, der echtzeit-übersetzu fail because they optimize for the common case while ignoring structural constraints; SprachübersetzungsDienst makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Ein KI-gestützter Übersetzungsdienst, der Echtzeit-Übersetzungen mit kontextueller Analyse und Vokab
- User interface: develop frontend interface

## Anti-Goals

- **General-purpose platform**: SprachübersetzungsDienst solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Goals - Revised (P1)
2. Develop Frontend Interface (P5) -- (depends on: Define Project Scope and Goals)
3. Design AI Translation Algorithm (P2) -- (depends on: Define Project Scope and Goals)
4. Develop Contextual Analysis Module (P3) -- (depends on: Design AI Translation Algorithm)
5. Create Vocabulary Expansion Feature (P4) -- (depends on: Design AI Translation Algorithm)
6. Test and Iterate AI Translation Algorithm (P2) -- (depends on: Develop Contextual Analysis Module, Create Vocabulary Expansion Feature)
7. Implement Security Measures (P1) -- (depends on: Develop Frontend Interface)
8. Deploy and Monitor SprachübersetzungsDienst (P5) -- (depends on: Test and Iterate AI Translation Algorithm, Implement Security Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SprachübersetzungsDienst can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Ein KI-gestützter Übersetzungsdienst, der Echtzeit-Übersetzungen mit kontextueller Analyse und Vokab.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
