from .azure_openai import AzureOpenAIProvider
from .bedrock import BedrockProvider
from .claude import ClaudeProvider
from .gemini import GeminiProvider
from .ollama import OllamaProvider
from .openai import OpenAIProvider
from .provider import LLMProvider


def create_llm_provider(provider: str, **kwargs) -> LLMProvider:
    if provider == "ollama":
        return OllamaProvider(
            base_url=kwargs.get("base_url", "http://localhost:11434"),
            model=kwargs.get("model", "mistral:latest"),
        )
    elif provider == "claude":
        return ClaudeProvider(
            api_key=kwargs.get("api_key"),
            model=kwargs.get("model", "claude-3-sonnet-20240229"),
        )
    elif provider == "openai":
        return OpenAIProvider(
            api_key=kwargs.get("api_key"),
            model=kwargs.get("model", "gpt-3.5-turbo"),
        )
    elif provider == "azure_openai":
        return AzureOpenAIProvider(
            api_key=kwargs.get("api_key"),
            endpoint=kwargs.get("endpoint"),
            deployment_name=kwargs.get("deployment_name"),
        )
    elif provider == "bedrock":
        return BedrockProvider(
            model=kwargs.get("model", "amazon.titan-tg1-large"),
        )
    elif provider == "gemini":
        return GeminiProvider(
            api_key=kwargs.get("api_key"),
            model=kwargs.get("model", "gemini-2.0-flash"),
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")
