import os

from openai import AzureOpenAI

from .provider import LLMProvider


class AzureOpenAIProvider(LLMProvider):
    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        deployment_name: str = None,
    ):
        self.api_key = api_key or os.environ.get("AZURE_OPENAI_API_KEY")
        self.endpoint = endpoint or os.environ.get("AZURE_OPENAI_ENDPOINT")
        self.deployment_name = deployment_name or os.environ.get(
            "AZURE_OPENAI_DEPLOYMENT_NAME"
        )
        self.client = AzureOpenAI(
            api_key=self.api_key, api_version="2023-05-15", azure_endpoint=self.endpoint
        )

    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=self.deployment_name,
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
            raise Exception(f"Azure OpenAI API error: {str(e)}")

    async def embed(self, text: str, **kwargs) -> list[float]:
        try:
            response = await self.client.embeddings.create(
                input=text, model=self.deployment_name
            )
            return response.data[0].embedding
        except Exception as e:
            raise Exception(f"Azure OpenAI Embedding API error: {str(e)}")

    async def health_check(self) -> bool:
        try:
            await self.generate("Hello", cache_key="health_check", role="system")
            return True
        except Exception:
            return False
