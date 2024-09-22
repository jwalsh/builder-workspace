from .provider import LLMProvider


class AzureOpenAIProvider(LLMProvider):
    def __init__(
        self, api_key: str = None, endpoint: str = None, deployment_name: str = None
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.deployment_name = deployment_name

    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        # Implement Azure OpenAI generation logic here
        raise NotImplementedError("Azure OpenAI provider not yet implemented")

    async def embed(self, text: str, **kwargs) -> list[float]:
        # Implement Azure OpenAI embedding logic here
        raise NotImplementedError("Azure OpenAI embedding not yet implemented")

    async def health_check(self) -> bool:
        # Implement Azure OpenAI health check logic here
        raise NotImplementedError("Azure OpenAI health check not yet implemented")
