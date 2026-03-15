# CognitiveEnhancementSupplements

You are a coding agent working on CognitiveEnhancementSupplements -- Nutritional supplements designed to enhance brain function and cognitive performance.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; CognitiveEnhancementSupplements models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Nutritional supplements designed to enhance brain function and cognitive performance.
- User interface: market research and requirements gathering

## Anti-Goals

- **General-purpose platform**: CognitiveEnhancementSupplements solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Market Research and Requirements Gathering (P2)
2. Product Design and Formulation (P3) -- (depends on: Market Research and Requirements Gathering)
3. Regulatory Compliance and Legal Review (P4) -- (depends on: Product Design and Formulation)
4. Manufacturing and Supply Chain (P4) -- (depends on: Product Design and Formulation, Regulatory Compliance and Legal Review)
5. Branding and Marketing Strategy (P3) -- (depends on: Market Research and Requirements Gathering)
6. E-commerce Platform Development (P4) -- (depends on: Branding and Marketing Strategy)
7. Quality Assurance and Testing (P4) -- (depends on: Product Design and Formulation, E-commerce Platform Development)
8. Launch and Deployment (P5) -- (depends on: Manufacturing and Supply Chain, E-commerce Platform Development, Quality Assurance and Testing)
9. Post-Launch Support and Maintenance (P4) -- (depends on: Launch and Deployment)
10. Project Planning and Management (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CognitiveEnhancementSupplements can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Nutritional supplements designed to enhance brain function and cognitive performance..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
