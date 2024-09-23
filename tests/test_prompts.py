from coordinator.prompts import SYSTEM_PROMPTS, AVAILABLE_AGENTS


def test_system_prompts_exist():
    assert "coordinator" in SYSTEM_PROMPTS
    assert "default" in SYSTEM_PROMPTS
    assert "task-decomposer" in SYSTEM_PROMPTS
    assert "project-manager" in SYSTEM_PROMPTS
    assert "code-architect" in SYSTEM_PROMPTS


def test_system_prompts_content():
    assert (
        "You are an AI Project Coordinator named Coordinator"
        in SYSTEM_PROMPTS["coordinator"]
    )
    assert "You are a Task Decomposer AI" in SYSTEM_PROMPTS["task-decomposer"]
    assert "You are a Project Manager AI" in SYSTEM_PROMPTS["project-manager"]
    assert "You are a Code Architect AI" in SYSTEM_PROMPTS["code-architect"]


def test_available_agents():
    expected_agents = [
        "task-decomposer",
        "project-manager",
        "code-architect",
        "frontend-developer",
        "backend-developer",
        "database-specialist",
        "devops-engineer",
        "qa-tester",
        "security-specialist",
        "technical-writer",
    ]
    assert set(AVAILABLE_AGENTS) == set(expected_agents)


def test_all_agents_have_prompts():
    for agent in AVAILABLE_AGENTS:
        assert agent in SYSTEM_PROMPTS, f"Missing system prompt for {agent}"
