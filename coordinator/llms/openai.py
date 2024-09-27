import os

import openai

from .provider import LLMProvider


class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = model
        openai.api_key = self.api_key

    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": f"Cache key: {cache_key}\nRole: {role}",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=kwargs.get("max_tokens", 1000),
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

    async def embed(self, text: str, **kwargs) -> list[float]:
        try:
            response = await openai.Embedding.acreate(
                input=text, model="text-embedding-ada-002"
            )
            return response["data"][0]["embedding"]
        except Exception as e:
            raise Exception(f"OpenAI Embedding API error: {str(e)}")

    async def health_check(self) -> bool:
        try:
            await self.generate("Hello", cache_key="health_check", role="system")
            return True
        except Exception:
            return False
