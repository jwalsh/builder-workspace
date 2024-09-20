import os
from anthropic import AsyncAnthropic
from .provider import LLMProvider

class ClaudeProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "claude-3-sonnet-20240229"):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self.client = AsyncAnthropic(api_key=self.api_key)

    async def generate(self, prompt: str, cache_key: str = "", role: str = "", **kwargs) -> str:
        system_message = f"Cache key: {cache_key}\nRole: {role}\n\n"
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=kwargs.get("max_tokens", 1000),
                system=system_message,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except Exception as e:
            return f"Error: {str(e)}"

    async def embed(self, text: str, **kwargs) -> list[float]:
        # Claude doesn't have a separate embedding API, so this is a placeholder
        raise NotImplementedError("Claude does not support separate embedding API")

    async def health_check(self) -> bool:
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{"role": "user", "content": "Hello"}],
            )
            return True
        except Exception:
            return False
