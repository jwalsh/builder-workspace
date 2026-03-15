# CrossCulturalChatbot

You are a coding agent working on CrossCulturalChatbot -- An AI-powered chatbot capable of engaging in culturally appropriate conversations across multiple languages and cultures.

## Foundational Axiom

Existing approaches to ai-powered chatbot capable of engaging in culturally appropr fail because they optimize for the common case while ignoring structural constraints; CrossCulturalChatbot makes those constraints first-class.

## Confirmation Gate

Before writing any code, confirm:
1. You have read `spec.org` in this directory.
2. You understand the build order and current step.
3. You will not skip a failing acceptance test.

## What You Are Building

- Backend services: integrate frontend with backend development
- User interface: requirements gathering & analysis

## Anti-Goals

- **General-purpose platform**: CrossCulturalChatbot solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.
- **Manual-first workflow**: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.
- **Demo-ware**: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.

## Build Order

1. Project Kickoff Meeting (P1)
2. Requirements Gathering & Analysis (P2) -- (depends on: Project Kickoff Meeting)
3. Create User Interface Designs (P5) -- (depends on: Requirements Gathering & Analysis)
4. Design AI Model Architecture (P3) -- (depends on: Requirements Gathering & Analysis)
5. Research & Integrate Multilingual Libraries (P4) -- (depends on: Design AI Model Architecture)
6. Develop Cross-Cultural Conversational Logic (P4) -- (depends on: Design AI Model Architecture, Research & Integrate Multilingual Libraries)
7. Integrate Frontend with Backend Development (P5) -- (depends on: Create User Interface Designs, Develop Cross-Cultural Conversational Logic)
8. Documentation & Knowledge Base Creation (Revised) (P5) -- (depends on: Integrate Frontend with Backend Development)
9. Security Review & Audit (P3) -- (depends on: Develop Cross-Cultural Conversational Logic)
10. Perform Unit Tests & Code Reviews (P2) -- (depends on: Develop Cross-Cultural Conversational Logic, Integrate Frontend with Backend Development)
11. Testing & Deployment Preparation (P1) -- (depends on: Perform Unit Tests & Code Reviews, Security Review & Audit)
12. Deploy CrossCulturalChatbot to Staging Environment (P1) -- (depends on: Testing & Deployment Preparation)
13. User Acceptance Testing (UAT) (P1) -- (depends on: Deploy CrossCulturalChatbot to Staging Environment)
14. Address Feedback & Iterate (P2) -- (depends on: User Acceptance Testing (UAT))
15. Prepare for Production Deployment (P1) -- (depends on: Address Feedback & Iterate)
16. Production Deployment of CrossCulturalChatbot (P1) -- (depends on: Prepare for Production Deployment)

### Failure Handler

If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.

## Open Conjectures

- **C-001**: CrossCulturalChatbot can deliver its core value proposition as described
  - Falsification: Integration test of end-to-end workflow fails to produce expected output
- **C-002**: AI/ML components achieve sufficient accuracy for production use
  - Falsification: Model accuracy on held-out test set falls below domain-specific threshold
- **C-003**: Security implementation meets compliance requirements
  - Falsification: Penetration test or security audit reveals critical vulnerability

## Stack

- Python (default)

## Success Criteria

1. All build steps completed with passing acceptance tests.
2. End-to-end workflow demonstrates core value: An AI-powered chatbot capable of engaging in culturally appropriate conversations across multiple la.
3. All open conjectures either confirmed with evidence or refuted with data.
4. System deployed and accessible to content creators and community managers.
