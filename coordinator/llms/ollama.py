import aiohttp
from .provider import LLMProvider

class OllamaProvider(LLMProvider):
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "mistral:latest"):
        self.base_url = base_url
        self.model = model

    async def generate(self, prompt: str, cache_key: str = "", role: str = "", **kwargs) -> str:
        system_message = f"Cache key: {cache_key}\nRole: {role}\n\n"
        full_prompt = system_message + prompt
        
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model, "prompt": full_prompt, "stream": False},
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("response", "")
                else:
                    return f"Error: {response.status}"

    async def embed(self, text: str, **kwargs) -> list[float]:
        # Ollama doesn't support embeddings natively, so this is a placeholder
        raise NotImplementedError("Ollama does not support embeddings")

    async def health_check(self) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/api/version") as response:
                return response.status == 200
