from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        pass

    @abstractmethod
    async def embed(self, text: str, **kwargs) -> list[float]:
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        pass
