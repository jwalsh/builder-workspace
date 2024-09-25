# RFC 009: Adding Gemini Support

## Background

As our project evolves, we aim to expand our language model capabilities by integrating Google's Gemini AI. This RFC outlines the process of adding Gemini support to our existing LLM provider framework.

## Motivation

Integrating Gemini will:
1. Diversify our AI model options
2. Potentially improve performance in certain tasks
3. Provide a fallback option if other providers are unavailable

## Proposal

We propose to add Gemini support through the following steps:

1. API Key Management
2. Gemini Provider Implementation
3. Factory Updates
4. Test File Modifications
5. Makefile Updates
6. Dependency Management

### 1. API Key Management

Add the Gemini API key to environment variables:

```bash
export GOOGLE_API_KEY=your_gemini_api_key_here
```

Update `secrets-example.json` to include a placeholder for the Gemini API key:

```json
{
  // ... existing entries ...
  "GOOGLE_API_KEY": "your_gemini_api_key_here"
}
```

### 2. Gemini Provider Implementation

Create a new file `coordinator/llms/gemini.py`:

```python
import os
import google.generativeai as genai
from .provider import LLMProvider

class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "gemini-pro"):
        self.api_key = api_key or os.environ.get("GOOGLE_API_KEY")
        self.model = model
        genai.configure(api_key=self.api_key)

    async def generate(self, prompt: str, cache_key: str = "", role: str = "", **kwargs) -> str:
        try:
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")

    async def embed(self, text: str, **kwargs) -> list[float]:
        try:
            model = genai.GenerativeModel('embedding-001')
            result = model.embed_content(text)
            return result['embedding']
        except Exception as e:
            raise Exception(f"Gemini Embedding API error: {str(e)}")

    async def health_check(self) -> bool:
        try:
            await self.generate("Hello", cache_key="health_check", role="system")
            return True
        except Exception:
            return False
```

### 3. Factory Updates

Update `coordinator/llms/factory.py`:

```python
from .gemini import GeminiProvider

def create_llm_provider(provider: str, **kwargs) -> LLMProvider:
    # ... existing providers ...
    elif provider == "gemini":
        return GeminiProvider(
            api_key=kwargs.get("api_key"),
            model=kwargs.get("model", "gemini-pro"),
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")
```

### 4. Test File Modifications

Update `tests/test_llm_providers.py`:

```python
from coordinator.llms.gemini import GeminiProvider

@pytest.mark.asyncio
async def test_gemini_provider():
    provider = GeminiProvider()
    await test_llm_provider(provider)
```

### 5. Makefile Updates

Add a new target for testing the Gemini provider:

```makefile
test-gemini: ## Test Gemini provider
	pytest tests/test_llm_providers.py::test_gemini_provider

.PHONY: test-gemini

# Update the test-all target to include Gemini
test-all: ## Run all LLM provider tests
	pytest tests/test_llm_providers.py
```

### 6. Dependency Management

Update `pyproject.toml`:

```toml
[tool.poetry.dependencies]
google-generativeai = "^0.3.0"
```

Run `poetry update` to install the new dependency.

## Implementation Plan

1. Create the `GeminiProvider` class in `coordinator/llms/gemini.py`
2. Update the factory in `coordinator/llms/factory.py`
3. Add Gemini tests to `tests/test_llm_providers.py`
4. Update the Makefile with new Gemini-related targets
5. Update `pyproject.toml` and run `poetry update`
6. Update `secrets-example.json` and documentation for API key management
7. Test the implementation thoroughly
8. Update any relevant documentation or README files

## Security Considerations

- Ensure the Gemini API key is handled securely and not exposed in logs or error messages
- Review Gemini's usage policies and ensure compliance

## Alternatives Considered

- Using a different Google AI model
- Implementing Gemini support through a third-party library

## Open Questions

- Are there any specific use cases where Gemini would be preferred over existing providers?
- How does Gemini's pricing compare to our current providers?

## Future Work

- Implement more advanced Gemini features as they become available
- Explore Gemini's multimodal capabilities for potential future use

## Conclusion

Adding Gemini support will enhance our project's capabilities and provide more flexibility in choosing AI models. This implementation follows our existing patterns for LLM providers, ensuring consistency and ease of maintenance.
