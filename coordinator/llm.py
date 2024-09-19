import os
import json
import logging
import requests
import random
import anthropic
from datetime import datetime, timedelta
from .models import LLMConfig, LLMProvider

# Initialize Anthropic client
client = anthropic.Client(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Config file path
CONFIG_FILE = "llm_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config_data = json.load(f)
            config_data['last_check'] = datetime.fromisoformat(config_data['last_check'])
            return LLMConfig(**config_data)
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            logging.warning("Invalid config file. Creating a new configuration.")
    return create_default_config()

def create_default_config():
    config = LLMConfig(
        provider=LLMProvider.OLLAMA,
        ollama_healthy=True,
        claude_healthy=True,
        last_check=datetime.now()
    )
    save_config(config)
    return config

def save_config(config: LLMConfig):
    config_dict = config.dict()
    config_dict['last_check'] = config.last_check.isoformat()
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config_dict, f)

def update_health_status(config: LLMConfig, force_check=False):
    if force_check or (datetime.now() - config.last_check) > timedelta(hours=4):
        config.ollama_healthy = check_ollama_health()
        config.claude_healthy = check_claude_health()
        config.last_check = datetime.now()
        save_config(config)

def check_ollama_health():
    try:
        response = requests.get("http://localhost:11434/api/version")
        return response.status_code == 200
    except requests.RequestException:
        return False

def check_claude_health():
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hello"}]
        )
        return True
    except Exception:
        return False

def get_active_provider(config: LLMConfig):
    update_health_status(config)
    if config.provider == LLMProvider.RANDOM:
        available_providers = []
        if config.ollama_healthy:
            available_providers.append(LLMProvider.OLLAMA)
        if config.claude_healthy:
            available_providers.append(LLMProvider.CLAUDE)
        return random.choice(available_providers) if available_providers else None
    elif config.provider == LLMProvider.OLLAMA and config.ollama_healthy:
        return LLMProvider.OLLAMA
    elif config.provider == LLMProvider.CLAUDE and config.claude_healthy:
        return LLMProvider.CLAUDE
    else:
        return None

def run_llm_command(config: LLMConfig, prompt: str, cache_key: str, role: str) -> str:
    provider = get_active_provider(config)
    if provider == LLMProvider.OLLAMA:
        return run_ollama_command(prompt, cache_key, role)
    elif provider == LLMProvider.CLAUDE:
        return run_claude_command(prompt, cache_key, role)
    else:
        logging.error("No healthy LLM provider available")
        return ""

def run_ollama_command(prompt: str, cache_key: str, role: str) -> str:
    from .prompts import SYSTEM_PROMPTS
    system_message = f"Cache key: {cache_key}\n{SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS['default'])}"
    logging.info(f"{role}: {cache_key}")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:latest",
                "prompt": f"{system_message}\n\n{prompt}",
            },
        )
        response.raise_for_status()
        return response.json().get('response', '')
    except requests.RequestException as e:
        logging.error(f"Error calling Ollama API: {e}")
        return ""

def run_claude_command(prompt: str, cache_key: str, role: str) -> str:
    from .prompts import SYSTEM_PROMPTS
    system_message = f"Cache key: {cache_key}\n{SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS['default'])}"
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=2000,
            temperature=0.5,
            system=system_message,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        logging.error(f"Error calling Claude API: {e}")
        return ""
