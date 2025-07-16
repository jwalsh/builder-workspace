# Gemini 2.0 Flash Integration Setup

## Overview
The BuilderAgents system now supports Google's Gemini 2.0 Flash model with its larger context window for enhanced task decomposition and processing.

## Setup Instructions

### 1. Set your API key
```bash
export GEMINI_API_KEY=your_api_key_here
```

### 2. Test the integration
```bash
poetry run python test_gemini.py
```

### 3. Use Gemini with the coordinator
```bash
# Use Gemini as the LLM provider
poetry run python -m coordinator --use-llm gemini --name "MyProject" --description "A test project"

# Check health status of all providers
poetry run python -m coordinator --check-health
```

## Configuration

The Gemini provider supports the following configuration options:

- **Model**: `gemini-2.0-flash` (default)
- **API Key**: Retrieved from `GEMINI_API_KEY` environment variable
- **Base URL**: `https://generativelanguage.googleapis.com/v1beta`

## Features

### Text Generation
- Uses the `/generateContent` endpoint
- Supports configurable parameters:
  - `temperature` (default: 0.7)
  - `max_tokens` (default: 8192)
  - `top_p` (default: 0.95)
  - `top_k` (default: 40)

### Embeddings
- Uses the `text-embedding-004` model
- Supports the `/embedContent` endpoint
- Returns high-dimensional embeddings for text similarity

### Health Checking
- Automatically validates API connectivity
- Integrates with the existing health monitoring system

## Usage Examples

### Basic Project Creation
```bash
# Create a new project using Gemini
poetry run python -m coordinator \
  --use-llm gemini \
  --name "DataAnalysisFramework" \
  --description "A comprehensive data analysis framework with ML capabilities"
```

### Random Provider Selection
```bash
# Use random provider selection (includes Gemini)
poetry run python -m coordinator --use-llm random --name "TestProject" --description "Test"
```

## API Reference

The Gemini provider follows the same interface as other LLM providers:

```python
from coordinator.llms.gemini import GeminiProvider

# Initialize provider
provider = GeminiProvider(api_key="your_key", model="gemini-2.0-flash")

# Generate text
response = await provider.generate(
    prompt="Your prompt here",
    cache_key="optional_cache_key",
    role="assistant",
    max_tokens=1000
)

# Generate embeddings
embedding = await provider.embed("Text to embed")

# Health check
is_healthy = await provider.health_check()
```

## Benefits of Gemini 2.0 Flash

1. **Larger Context Window**: Better handling of complex project descriptions
2. **Improved Performance**: Faster response times for task decomposition
3. **Enhanced Understanding**: Better comprehension of technical requirements
4. **Cost Effective**: Optimized for high-volume usage

## Troubleshooting

### Common Issues

1. **API Key Not Set**
   ```
   Error: GEMINI_API_KEY environment variable not set
   ```
   Solution: Set the environment variable with your API key

2. **Health Check Fails**
   ```
   Gemini health: Unhealthy
   ```
   Solution: Verify API key is correct and you have quota remaining

3. **Generation Errors**
   ```
   Gemini API error: 400 - Bad Request
   ```
   Solution: Check prompt format and parameter values

### Debug Mode
Run with debug logging to see detailed API interactions:
```bash
PYTHONPATH=. python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
from coordinator.llms.gemini import GeminiProvider
async def test():
    provider = GeminiProvider()
    await provider.health_check()
asyncio.run(test())
"
```

## Contributing

To extend the Gemini provider:

1. Edit `coordinator/llms/gemini.py`
2. Update tests in `tests/test_llm_providers.py`
3. Add any new configuration options to `coordinator/models.py`
4. Update documentation as needed

## Related Files

- `coordinator/llms/gemini.py` - Main provider implementation
- `coordinator/llms/factory.py` - Provider factory
- `coordinator/models.py` - Configuration models
- `coordinator/llm.py` - LLM manager
- `test_gemini.py` - Test script