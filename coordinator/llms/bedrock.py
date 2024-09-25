import json
import os

import boto3

from .provider import LLMProvider


class BedrockProvider(LLMProvider):
    def __init__(self, model: str = "amazon.titan-tg1-large"):
        self.model = model
        self.client = boto3.client("bedrock-runtime")

    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        try:
            system_message = f"Cache key: {cache_key}\nRole: {role}\n\n"
            full_prompt = system_message + prompt

            response = await self.client.invoke_model_async(
                modelId=self.model,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(
                    {
                        "prompt": full_prompt,
                        "max_tokens_to_sample": kwargs.get("max_tokens", 1000),
                    }
                ),
            )

            response_body = json.loads(await response["body"].read())
            return response_body["completion"]
        except Exception as e:
            raise Exception(f"Bedrock API error: {str(e)}")

    async def embed(self, text: str, **kwargs) -> list[float]:
        # Note: As of my last update, Bedrock didn't have a separate embedding API.
        # You might need to use a specific model or method for embeddings.
        raise NotImplementedError("Bedrock embedding not yet implemented")

    async def health_check(self) -> bool:
        try:
            await self.generate("Hello", cache_key="health_check", role="system")
            return True
        except Exception:
            return False
