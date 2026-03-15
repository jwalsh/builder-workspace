# DataSyncIntegrityVerifier

You are a coding agent working on DataSyncIntegrityVerifier -- A system that ensures data integrity during synchronization processes across multiple platforms or databases.

## Foundational Axiom

Existing approaches to system fail because they optimize for the common case while ignoring structural constraints; DataSyncIntegrityVerifier makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Core system: A system that ensures data integrity during synchronization processes across multiple platforms or d
- User interface: define project scope and requirements
- Data layer: implement data synchronization module

## Anti-Goals

- **General-purpose platform**: DataSyncIntegrityVerifier solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Define Project Scope and Requirements (P5)
2. Design System Architecture (P4) -- (depends on: Define Project Scope and Requirements)
3. Implement Data Synchronization Module (P3) -- (depends on: Design System Architecture)
4. Develop Platform-Specific Adapters (P3) -- (depends on: Design System Architecture)
5. Implement Security Measures (P3) -- (depends on: Design System Architecture)
6. Implement Monitoring and Logging (P2) -- (depends on: Implement Data Synchronization Module, Develop Platform-Specific Adapters)
7. Design and Implement User Interface (P2) -- (depends on: Design System Architecture)
8. Develop Test Suite (P3) -- (depends on: Implement Data Synchronization Module, Develop Platform-Specific Adapters, Implement Monitoring and Logging, Design and Implement User Interface, Implement Security Measures)
9. Set up Continuous Integration and Deployment (P2) -- (depends on: Implement Data Synchronization Module, Develop Platform-Specific Adapters, Implement Monitoring and Logging, Design and Implement User Interface, Implement Security Measures)
10. Conduct System Testing and Validation (P2) -- (depends on: Develop Test Suite)
11. Prepare Documentation (P2) -- (depends on: Define Project Scope and Requirements, Design System Architecture, Implement Data Synchronization Module, Develop Platform-Specific Adapters, Implement Monitoring and Logging, Design and Implement User Interface, Implement Security Measures)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: DataSyncIntegrityVerifier can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: System meets real-time latency requirements under load
  - Falsification: P95 latency exceeds target under simulated production load
- **C-004**: Architecture scales horizontally to meet projected demand
  - Falsification: Load test shows non-linear degradation before target throughput
- **C-005**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Babashka (bb) — Clojure scripting for CLI
- clojure.tools.cli for argument parsing
- babashka.fs for file operations
- babashka.process for shell interop
- cheshire for JSON processing

## Implementation Notes

This project is implemented as a babashka script. Key constraints:
- Single-file `bb.edn` + `src/<name>.clj` entry point
- Use `babashka.cli` for argument parsing, not manual arg processing
- Output structured results as EDN or JSON (use cheshire)
- Exit code 0 for success, 1 for issues found, 2 for errors
- Support `--format json|edn|text` flag for output format
- Support reading from stdin or file arguments
- Include a `bb.edn` with `:tasks` for common operations

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: A system that ensures data integrity during synchronization processes across multiple platforms or d.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to domain professionals who need specialized tooling.
