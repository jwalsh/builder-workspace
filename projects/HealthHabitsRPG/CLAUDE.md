# HealthHabitsRPG

You are a coding agent working on HealthHabitsRPG -- A role-playing game that encourages healthy habits and lifestyle changes through quests and character development.

## Foundational Axiom

Healthcare tools fail when they optimize for data collection over clinical workflow; HealthHabitsRPG embeds clinical reasoning into the system's structure.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A role-playing game that encourages healthy habits and lifestyle changes through quests and characte
- User interface: define project scope and requirements - healthhabitsrpg
- Data layer: implement data storage and management

## Anti-Goals

- **General-purpose platform**: HealthHabitsRPG solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define project scope and requirements - HealthHabitsRPG (P5)
2. Design game architecture for HealthHabitsRPG (P4) -- (depends on: Define project scope and requirements)
3. Design user interface and experience (Revised) (P4) -- (depends on: Define project scope and requirements, Gather feedback from various stakeholders)
4. Set up development and testing environments (P4)
5. Develop game mechanics and rules (P3) -- (depends on: Design game architecture)
6. Implement user interface and experience (P3) -- (depends on: Design user interface and experience)
7. Integrate with health tracking apps and devices (P3) -- (depends on: Design game architecture)
8. Implement data storage and management (P3) -- (depends on: Design game architecture)
9. Conduct security audits and testing (P3) -- (depends on: Develop game mechanics and rules, Implement user interface and experience, Integrate with health tracking apps and devices, Implement data storage and management)
10. Implement game analytics and reporting (P2) -- (depends on: Develop game mechanics and rules, Implement user interface and experience, Integrate with health tracking apps and devices, Implement data storage and management)
11. Conduct quality assurance and testing (P2) -- (depends on: Develop game mechanics and rules, Implement user interface and experience, Integrate with health tracking apps and devices, Implement data storage and management)
12. Prepare documentation and user guides (P2) -- (depends on: Develop game mechanics and rules, Implement user interface and experience, Integrate with health tracking apps and devices)
13. Plan and execute marketing and launch strategies (P2) -- (depends on: Conduct quality assurance and testing)
14. Deploy and release the game (P1) -- (depends on: Conduct quality assurance and testing, Prepare documentation and user guides)
15. Plan and implement post-launch support and updates (P2) -- (depends on: Deploy and release the game)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: HealthHabitsRPG can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-004**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A role-playing game that encourages healthy habits and lifestyle changes through quests and characte.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to healthcare professionals (clinicians, administrators) in clinical settings.
