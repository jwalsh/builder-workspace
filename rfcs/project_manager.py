import json
import os


def load_secrets():
    if os.path.exists("secrets.json"):
        with open("secrets.json") as f:
            return json.load(f)
    else:
        return {
            "GOOGLE_AI_API_KEY": os.getenv("GOOGLE_AI_API_KEY"),
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"),
            "OLLAMA_API_BASE_URL": os.getenv(
                "OLLAMA_API_BASE_URL", "http://localhost:11434"
            ),
        }


secrets = load_secrets()
