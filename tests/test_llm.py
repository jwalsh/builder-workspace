import pytest

from coordinator.llm import llm_manager, run_llm_command
from coordinator.models import LLMProvider


@pytest.fixture
def mock_llm_manager(mocker):
    mocker.patch.object(llm_manager, "run_llm_command", return_value="Mocked response")
    return llm_manager


async def test_run_llm_command(mock_llm_manager):
    result = await run_llm_command("Test prompt", "test_cache_key", "test_role")
    assert result == "Mocked response"
    mock_llm_manager.run_llm_command.assert_called_once_with(
        "Test prompt", "test_cache_key", "test_role"
    )


def test_create_default_config():
    config = llm_manager.create_default_config()
    assert config.provider == LLMProvider.OLLAMA
    assert config.ollama_healthy == True
    assert config.claude_healthy == True


@pytest.mark.asyncio
async def test_update_health_status(mocker):
    mocker.patch.object(llm_manager, "save_config")
    mocker.patch("coordinator.llms.factory.create_llm_provider")

    await llm_manager.update_health_status(force_check=True)

    llm_manager.save_config.assert_called_once()
    assert llm_manager.config.last_check is not None


def test_get_active_provider():
    llm_manager.config.provider = LLMProvider.OLLAMA
    llm_manager.config.ollama_healthy = True
    assert llm_manager.get_active_provider() == "ollama"

    llm_manager.config.provider = LLMProvider.CLAUDE
    llm_manager.config.claude_healthy = False
    assert llm_manager.get_active_provider() is None


@pytest.mark.asyncio
async def test_llm_manager_run_llm_command(mocker):
    mocker.patch.object(llm_manager, "get_active_provider", return_value="ollama")
    mocker.patch("coordinator.llms.factory.create_llm_provider")

    result = await llm_manager.run_llm_command(
        "Test prompt", "test_cache_key", "test_role"
    )

    assert result != ""  # The actual return value will depend on your mocked provider
