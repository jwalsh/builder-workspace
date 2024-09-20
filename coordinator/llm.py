import json
import logging
import os
import random
from datetime import datetime, timedelta
from typing import Optional

from .llms.factory import create_llm_provider
from .models import LLMConfig, LLMProvider

CONFIG_FILE = "llm_config.json"

class LLMManager:
    def __init__(self):
        self.config = self.load_config()
        self.provider = None

    def load_config(self) -> LLMConfig:
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    config_data = json.load(f)
                return LLMConfig.parse_obj(config_data)
            except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
                logging.warning(f"Invalid config file: {e}. Creating a new configuration.")
        return self.create_default_config()

    def create_default_config(self) -> LLMConfig:
        config = LLMConfig(
            provider=LLMProvider.OLLAMA,
            ollama_healthy=True,
            claude_healthy=True,
            last_check=datetime.now()
        )
        self.save_config(config)
        return config

    def save_config(self, config: LLMConfig):
        with open(CONFIG_FILE, "w") as f:
            json.dump(config.dict(), f, default=str)

    async def update_health_status(self, force_check=False):
        if force_check or (datetime.now() - self.config.last_check) > timedelta(hours=4):
            self.config.ollama_healthy = await create_llm_provider("ollama").health_check()
            self.config.claude_healthy = await create_llm_provider("claude").health_check()
            self.config.last_check = datetime.now()
            self.save_config(self.config)

    def get_active_provider(self) -> Optional[str]:
        if self.config.provider == LLMProvider.RANDOM:
            available_providers = [
                provider for provider, is_healthy in {
                    "ollama": self.config.ollama_healthy,
                    "claude": self.config.claude_healthy,
                }.items() if is_healthy
            ]
            return random.choice(available_providers) if available_providers else None
        elif getattr(self.config, f"{self.config.provider.value}_healthy", False):
            return self.config.provider.value
        else:
            logging.error(f"No healthy providers found for {self.config.provider}")
            return None

    async def run_llm_command(self, prompt: str, cache_key: str, role: str, **kwargs) -> str:
        providers_to_try = [self.config.provider.value]
        if self.config.provider != LLMProvider.OLLAMA:
            providers_to_try.append("ollama")  # Fallback to Ollama if it's not the primary choice

        for provider_name in providers_to_try:
            if not getattr(self.config, f"{provider_name}_healthy", False):
                continue

            try:
                provider = create_llm_provider(provider_name)
                result = await provider.generate(prompt, cache_key=cache_key, role=role, **kwargs)
                return result
            except Exception as e:
                logging.error(f"Error with {provider_name} provider: {str(e)}")
                setattr(self.config, f"{provider_name}_healthy", False)
                self.save_config(self.config)

        logging.error("All providers failed. Unable to process the request.")
        return ""

# Create a singleton instance of LLMManager
llm_manager = LLMManager()

# Export the run_llm_command function to maintain backwards compatibility
async def run_llm_command(prompt: str, cache_key: str, role: str, **kwargs) -> str:
    return await llm_manager.run_llm_command(prompt, cache_key, role, **kwargs)
