# PersonalizedSummaryTailor

You are a coding agent working on PersonalizedSummaryTailor -- An AI system that tailors document summaries based on the reader's role, interests, and prior knowledge.

## Foundational Axiom

Existing approaches to ai system fail because they optimize for the common case while ignoring structural constraints; PersonalizedSummaryTailor makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: implement document processing
- User interface: define system requirements - rfc draft update

## Anti-Goals

- **General-purpose platform**: PersonalizedSummaryTailor solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define System Requirements - RFC DRAFT Update (P5)
2. Design System Architecture (P4) -- (depends on: Define System Requirements)
3. Set up Development Environment (P3)
4. Implement User Management (P2) -- (depends on: Design System Architecture, Set up Development Environment)
5. Implement Document Processing (P2) -- (depends on: Design System Architecture, Set up Development Environment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: PersonalizedSummaryTailor can deliver its core value proposition as described
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
2. End-to-end workflow demonstrates core value: An AI system that tailors document summaries based on the reader's role, interests, and prior knowle.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
