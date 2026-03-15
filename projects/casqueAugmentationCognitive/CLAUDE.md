# casqueAugmentationCognitive

You are a coding agent working on casqueAugmentationCognitive -- Un casque qui améliore les capacités cognitives grâce à la neurostimulation.

## Foundational Axiom

Brain-computer interfaces fail when they treat neural signals as simple input streams; casqueAugmentationCognitive models the bidirectional adaptation between brain and system.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un casque qui améliore les capacités cognitives grâce à la neurostimulation.
- User interface: define project scope and requirements

## Anti-Goals

- **General-purpose platform**: casqueAugmentationCognitive solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P1)
2. Design Cognitive Enhancing Headphone Prototype (P3) -- (depends on: Define Project Scope and Requirements)
3. Develop Mobile Application Interface (P5) -- (depends on: Design Cognitive Enhancing Headphone Prototype)
4. Develop Neurostimulation Algorithm (P4) -- (depends on: Design Cognitive Enhancing Headphone Prototype)
5. Research and Gather Existing Solutions (P2) -- (depends on: Define Project Scope and Requirements)
6. Review and Approve Design Documents (P2) -- (depends on: Design Cognitive Enhancing Headphone Prototype)
7. Perform Quality Assurance Tests (P1) -- (depends on: Develop Neurostimulation Algorithm, Develop Mobile Application Interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: casqueAugmentationCognitive can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un casque qui améliore les capacités cognitives grâce à la neurostimulation..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to neuroscientists and clinical researchers working with neural interfaces.
