from .provider import LLMProvider
from .ollama import OllamaProvider
from .claude import ClaudeProvider


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
    else:
        raise ValueError(f"Unknown provider: {provider}")
