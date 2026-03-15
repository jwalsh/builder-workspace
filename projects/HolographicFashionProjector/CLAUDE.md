# HolographicFashionProjector

You are a coding agent working on HolographicFashionProjector -- A wearable device that projects changeable holographic clothing and accessories, revolutionizing fashion.

## Foundational Axiom

Existing approaches to wearable device fail because they optimize for the common case while ignoring structural constraints; HolographicFashionProjector makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A wearable device that projects changeable holographic clothing and accessories, revolutionizing fas
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: HolographicFashionProjector solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design Holographic Projection System (P2) -- (depends on: Define Project Requirements)
3. Create Wearable Device Design Blueprints (P3) -- (depends on: Design Holographic Projection System)
4. Implement Wearable Device Firmware (P5) -- (depends on: Design Holographic Projection System, Create Wearable Device Design Blueprints)
5. Develop Mobile App for User Interaction (P2) -- (depends on: Design Holographic Projection System, Implement Wearable Device Firmware)
6. Perform System Integration Testing (P5) -- (depends on: Implement Wearable Device Firmware, Develop Mobile App for User Interaction)
7. Develop Holographic Clothing Models (P4) -- (depends on: Design Holographic Projection System)
8. Deploy HolographicFashionProjector to Users (P1) -- (depends on: Perform System Integration Testing)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HolographicFashionProjector can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A wearable device that projects changeable holographic clothing and accessories, revolutionizing fas.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to xr developers and spatial computing designers.
