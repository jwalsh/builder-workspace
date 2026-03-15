# FeedbackLanguageOptimizer

You are a coding agent working on FeedbackLanguageOptimizer -- An AI tool that helps in constructing feedback to ensure it's constructive and unbiased before submission.

## Foundational Axiom

Existing approaches to ai tool fail because they optimize for the common case while ignoring structural constraints; FeedbackLanguageOptimizer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An AI tool that helps in constructing feedback to ensure it's constructive and unbiased before submi
- User interface: defineprojectrequirementsforfeedbacklanguageoptimizer(revised)
- Data layer: implement data storage and retrieval

## Anti-Goals

- **General-purpose platform**: FeedbackLanguageOptimizer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. DefineProjectRequirementsforFeedbackLanguageOptimizer(Revised) (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Requirements)
3. Develop AI Model (P3) -- (depends on: Design System Architecture)
4. Build User Interface (P3) -- (depends on: Design System Architecture)
5. Implement Data Storage and Retrieval (P3) -- (depends on: Design System Architecture)
6. Integrate Components (P2) -- (depends on: Develop AI Model, Build User Interface, Implement Data Storage and Retrieval)
7. Implement Security Measures (P3) -- (depends on: Integrate Components)
8. Test and Quality Assurance (P2) -- (depends on: Integrate Components, Implement Security Measures)
9. Write Documentation (P2) -- (depends on: Test and Quality Assurance)
10. Deploy and Monitor (P1) -- (depends on: Test and Quality Assurance)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: FeedbackLanguageOptimizer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI tool that helps in constructing feedback to ensure it's constructive and unbiased before submi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
