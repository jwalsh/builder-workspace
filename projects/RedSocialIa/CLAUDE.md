# RedSocialIa

You are a coding agent working on RedSocialIa -- Una red social inteligente que propone conexiones y contenidos basados en los intereses y comportamiento del usuario.

## Foundational Axiom

Existing approaches to una red social inteligente que propone conexiones y contenid fail because they optimize for the common case while ignoring structural constraints; RedSocialIa makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Una red social inteligente que propone conexiones y contenidos basados en los intereses y comportami
- User interface: design user interface for interest and behavior prediction
- Data layer: create a data collection and storage strategy

## Anti-Goals

- **General-purpose platform**: RedSocialIa solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Create a Data Collection and Storage Strategy (P5)
2. Review Data Collection and Storage Strategy (P5) -- (depends on: Create a Data Collection and Storage Strategy)
3. Define User Interest and Behavior Model (P1)
4. Implement Connection Suggestion Feature (P4) -- (depends on: Define User Interest and Behavior Model)
5. Develop Algorithm for Content Recommendation (P3) -- (depends on: Define User Interest and Behavior Model)
6. Design User Interface for Interest and Behavior Prediction (P2) -- (depends on: Define User Interest and Behavior Model)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: RedSocialIa can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Una red social inteligente que propone conexiones y contenidos basados en los intereses y comportami.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
