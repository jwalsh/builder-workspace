from .provider import LLMProvider

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model

    async def generate(self, prompt: str, cache_key: str = "", role: str = "", **kwargs) -> str:
        # Implement OpenAI generation logic here
        raise NotImplementedError("OpenAI provider not yet implemented")

    async def embed(self, text: str, **kwargs) -> list[float]:
        # Implement OpenAI embedding logic here
        raise NotImplementedError("OpenAI embedding not yet implemented")

    async def health_check(self) -> bool:
        # Implement OpenAI health check logic here
        raise NotImplementedError("OpenAI health check not yet implemented")
