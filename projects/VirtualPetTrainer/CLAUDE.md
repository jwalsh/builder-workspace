# VirtualPetTrainer

You are a coding agent working on VirtualPetTrainer -- An augmented reality app that provides personalized pet training sessions using AI and computer vision.

## Foundational Axiom

Existing approaches to augmented reality app fail because they optimize for the common case while ignoring structural constraints; VirtualPetTrainer makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: An augmented reality app that provides personalized pet training sessions using AI and computer visi

## Anti-Goals

- **General-purpose platform**: VirtualPetTrainer solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Pet AI Model Architecture (P1)
2. Develop AR Experience for the App (P2) -- (depends on: Define Pet AI Model Architecture)
3. Implement Computer Vision Algorithms for Pet Tracking (P3) -- (depends on: Define Pet AI Model Architecture)
4. Integrate AI and Computer Vision Modules (P5) -- (depends on: Define Pet AI Model Architecture, Develop AR Experience for the App, Implement Computer Vision Algorithms for Pet Tracking)
5. Test and Optimize AI and Computer Vision Performance (P2) -- (depends on: Integrate AI and Computer Vision Modules)
6. Write Technical Documentation for the Project (P5) -- (depends on: Integrate AI and Computer Vision Modules, Test and Optimize AI and Computer Vision Performance)
7. Design Personalized Training Sessions for Users (P4) -- (depends on: Define Pet AI Model Architecture)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: VirtualPetTrainer can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An augmented reality app that provides personalized pet training sessions using AI and computer visi.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to pet owners and veterinary professionals.
