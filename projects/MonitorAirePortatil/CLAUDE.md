# MonitorAirePortatil

You are a coding agent working on MonitorAirePortatil -- Un dispositivo portátil que monitorea la calidad del aire y alerta al usuario sobre niveles peligrosos.

## Foundational Axiom

Existing approaches to un dispositivo portátil que monitorea la calidad del aire y fail because they optimize for the common case while ignoring structural constraints; MonitorAirePortatil makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: Un dispositivo portátil que monitorea la calidad del aire y alerta al usuario sobre niveles peligros
- User interface: develop user interface for monitoraireportatil
- Data layer: develop cloud platform for data storage and alerts

## Anti-Goals

- **General-purpose platform**: MonitorAirePortatil solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Design MonitorAirePortatil Architecture (P2) -- (depends on: Define Project Requirements)
2. Develop User Interface for MonitorAirePortatil (P3) -- (depends on: Design MonitorAirePortatil Architecture)
3. Implement Device Firmware for Air Quality Sensors (P3) -- (depends on: Design MonitorAirePortatil Architecture)
4. Integrate Wireless Communication Module (P3) -- (depends on: Design MonitorAirePortatil Architecture)
5. Develop Cloud Platform for Data Storage and Alerts (P4) -- (depends on: Design MonitorAirePortatil Architecture)
6. Test MonitorAirePortatil Components (P4) -- (depends on: Develop User Interface for MonitorAirePortatil, Implement Device Firmware for Air Quality Sensors, Integrate Wireless Communication Module, Develop Cloud Platform for Data Storage and Alerts)
7. Perform System Integration Testing (P5) -- (depends on: Test MonitorAirePortatil Components)
8. Prepare Technical Documentation (P5) -- (depends on: Develop User Interface for MonitorAirePortatil, Implement Device Firmware for Air Quality Sensors, Integrate Wireless Communication Module, Develop Cloud Platform for Data Storage and Alerts)
9. Conduct Security Audit of MonitorAirePortatil (P5) -- (depends on: Develop User Interface for MonitorAirePortatil, Implement Device Firmware for Air Quality Sensors, Integrate Wireless Communication Module, Develop Cloud Platform for Data Storage and Alerts)
10. Define Comprehensive and Detailed Project Requirements for MonitorAirePortatil (P1)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: MonitorAirePortatil can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: Un dispositivo portátil que monitorea la calidad del aire y alerta al usuario sobre niveles peligros.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
