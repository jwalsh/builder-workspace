# SmartCompostBin

You are a coding agent working on SmartCompostBin -- An IoT-enabled compost bin that optimizes the composting process and alerts users when compost is ready.

## Foundational Axiom

Existing approaches to iot-enabled compost bin fail because they optimize for the common case while ignoring structural constraints; SmartCompostBin makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: develop backend services
- User interface: define project requirements

## Anti-Goals

- **General-purpose platform**: SmartCompostBin solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Requirements (P1)
2. Design IoT Hardware Architecture (P2) -- (depends on: Define Project Requirements)
3. Develop Backend Services (P4) -- (depends on: Define Project Requirements)
4. Integrate IoT Hardware with Backend Services (P5) -- (depends on: Design IoT Hardware Architecture, Develop Backend Services)
5. Test and Validate System Functionality (P2) -- (depends on: Integrate IoT Hardware with Backend Services)
6. Refine and Optimize Design (P4) -- (depends on: Test and Validate System Functionality)
7. Prepare Documentation (P5) -- (depends on: Refine and Optimize Design)
8. Develop Mobile Application Interface (P3) -- (depends on: Define Project Requirements)
9. Implement Notification System (P3) -- (depends on: Develop Backend Services)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: SmartCompostBin can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An IoT-enabled compost bin that optimizes the composting process and alerts users when compost is re.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
