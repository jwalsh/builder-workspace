# ProductivityQuest

You are a coding agent working on ProductivityQuest -- A gamified task management system that turns daily tasks and goals into an epic quest.

## Foundational Axiom

Existing approaches to gamified task management system fail because they optimize for the common case while ignoring structural constraints; ProductivityQuest makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A gamified task management system that turns daily tasks and goals into an epic quest.
- User interface: design the user interface

## Anti-Goals

- **General-purpose platform**: ProductivityQuest solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define the gamification mechanics (P1)
2. Design the user interface (P2) -- (depends on: Define the gamification mechanics)
3. Implement basic functionality (P3) -- (depends on: Design the user interface, Define the gamification mechanics)
4. Develop the task creation and management system (P4) -- (depends on: Implement basic functionality)
5. Integrate the gamification mechanics into the system (P5) -- (depends on: Define the gamification mechanics, Develop the task creation and management system)
6. Review and provide feedback on gamification mechanics design (P5) -- (depends on: Define the gamification mechanics)
7. Test the application for functionality and usability (P1) -- (depends on: Implement basic functionality)
8. Deploy the application (P4) -- (depends on: Test the application for functionality and usability)
9. Secure the application (P3) -- (depends on: Implement basic functionality)
10. Write technical documentation (P2) -- (depends on: Implement basic functionality)
11. Review and provide feedback on basic functionality implementation (P2) -- (depends on: Implement basic functionality)
12. Review and provide feedback on user interface design (P1) -- (depends on: Design the user interface)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: ProductivityQuest can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A gamified task management system that turns daily tasks and goals into an epic quest..
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to game developers and interactive media designers.
