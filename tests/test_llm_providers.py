import pytest

from coordinator.llms.azure_openai import AzureOpenAIProvider
from coordinator.llms.bedrock import BedrockProvider
from coordinator.llms.claude import ClaudeProvider
from coordinator.llms.ollama import OllamaProvider
from coordinator.llms.openai import OpenAIProvider
from coordinator.llms.provider import LLMProvider


@pytest.mark.asyncio
async def test_llm_provider(provider: LLMProvider):
    # Test generation
    response = await provider.generate("Hello, world!", cache_key="test", role="user")
    assert isinstance(response, str)
    assert len(response) > 0

    # Test embedding (if supported)
    try:
        embedding = await provider.embed("Test embedding")
        assert isinstance(embedding, list)
        assert all(isinstance(x, float) for x in embedding)
    except NotImplementedError:
        pass  # Embedding not supported for this provider

    # Test health check
    health_status = await provider.health_check()
    assert isinstance(health_status, bool)


@pytest.mark.asyncio
async def test_claude_provider():
    provider = ClaudeProvider()
    await test_llm_provider(provider)


@pytest.mark.asyncio
async def test_openai_provider():
    provider = OpenAIProvider()
    await test_llm_provider(provider)


@pytest.mark.asyncio
async def test_azure_openai_provider():
    provider = AzureOpenAIProvider()
    await test_llm_provider(provider)


@pytest.mark.asyncio
async def test_bedrock_provider():
    provider = BedrockProvider()
    await test_llm_provider(provider)


@pytest.mark.asyncio
async def test_ollama_provider():
    provider = OllamaProvider()
    await test_llm_provider(provider)
