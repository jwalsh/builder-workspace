import os
import aiohttp
import json
from typing import List, Dict, Any

from .provider import LLMProvider


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str = None, model: str = "gemini-2.0-flash"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.model = model
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        
    async def generate(
        self, prompt: str, cache_key: str = "", role: str = "", **kwargs
    ) -> str:
        try:
            url = f"{self.base_url}/models/{self.model}:generateContent"
            
            # Prepare the request
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": self.api_key
            }
            
            # Build the message with optional role/cache context
            system_context = []
            if cache_key:
                system_context.append(f"Cache key: {cache_key}")
            if role:
                system_context.append(f"Role: {role}")
            
            parts = []
            if system_context:
                parts.append({"text": "\n".join(system_context) + "\n\n"})
            parts.append({"text": prompt})
            
            data = {
                "contents": [{
                    "parts": parts
                }],
                "generationConfig": {
                    "temperature": kwargs.get("temperature", 0.7),
                    "maxOutputTokens": kwargs.get("max_tokens", 8192),
                    "topP": kwargs.get("top_p", 0.95),
                    "topK": kwargs.get("top_k", 40)
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"Gemini API error: {response.status} - {error_text}")
                    
                    result = await response.json()
                    
                    # Extract the generated text
                    if "candidates" in result and result["candidates"]:
                        candidate = result["candidates"][0]
                        if "content" in candidate and "parts" in candidate["content"]:
                            parts = candidate["content"]["parts"]
                            if parts and "text" in parts[0]:
                                return parts[0]["text"]
                    
                    raise Exception("Unexpected response format from Gemini API")
                    
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")
    
    async def embed(self, text: str, **kwargs) -> List[float]:
        """Generate embeddings using Gemini's embedding model"""
        try:
            # Use the text embedding model
            url = f"{self.base_url}/models/text-embedding-004:embedContent"
            
            headers = {
                "Content-Type": "application/json",
                "X-goog-api-key": self.api_key
            }
            
            data = {
                "content": {
                    "parts": [{
                        "text": text
                    }]
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"Gemini Embedding API error: {response.status} - {error_text}")
                    
                    result = await response.json()
                    
                    # Extract the embedding
                    if "embedding" in result and "values" in result["embedding"]:
                        return result["embedding"]["values"]
                    
                    raise Exception("Unexpected response format from Gemini Embedding API")
                    
        except Exception as e:
            raise Exception(f"Gemini Embedding API error: {str(e)}")
    
    async def health_check(self) -> bool:
        """Check if the Gemini API is accessible"""
        try:
            if not self.api_key:
                return False
            await self.generate("Hello", cache_key="health_check", role="system", max_tokens=10)
            return True
        except Exception:
            return False