import os

from anthropic import AsyncAnthropic

from .provider import LLMProvider


class ClaudeProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "claude-3-sonnet-20240229"):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self.client = AsyncAnthropic(api_key=self.api_key)

    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        try:
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=kwargs.get("max_tokens", 1000),
                system=f"Cache key: {cache_key}\nRole: {role}",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except Exception as e:
            if "credit balance is too low" in str(e):
                raise Exception("Claude API credit balance too low") from e
            raise

    async def embed(self, text: str, **kwargs) -> list[float]:
        raise NotImplementedError("Claude does not support separate embedding API")

    async def health_check(self) -> bool:
        try:
            await self.generate("Hello", cache_key="health_check", role="system")
            return True
        except Exception:
            return False
