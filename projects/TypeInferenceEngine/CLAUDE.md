# TypeInferenceEngine

You are a coding agent working on TypeInferenceEngine -- An advanced type inference engine for a functional language, supporting complex types and type-level programming.

## Foundational Axiom

Existing approaches to advanced type inference engine fail because they optimize for the common case while ignoring structural constraints; TypeInferenceEngine makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: design architecture for typeinferenceengine

## Anti-Goals

- **General-purpose platform**: TypeInferenceEngine solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design Architecture for TypeInferenceEngine (P1)
2. Implement Core Functionality of TypeInferenceEngine (P1) -- (depends on: Design Architecture for TypeInferenceEngine)
3. Test Core Functionality of TypeInferenceEngine (P4) -- (depends on: Implement Core Functionality of TypeInferenceEngine)
4. Document Core Functionality of TypeInferenceEngine (P5) -- (depends on: Test Core Functionality of TypeInferenceEngine)
5. Create RFC for TypeInferenceEngine Design (P2) -- (depends on: Design Architecture for TypeInferenceEngine)
6. Review RFC for TypeInferenceEngine Design (P3) -- (depends on: Create RFC for TypeInferenceEngine Design)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: TypeInferenceEngine can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An advanced type inference engine for a functional language, supporting complex types and type-level.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
