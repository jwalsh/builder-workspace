#!/usr/bin/env python3
"""
Test script for Gemini provider integration
"""
import asyncio
import os
from coordinator.llms.gemini import GeminiProvider


async def test_gemini_provider():
    """Test the Gemini provider implementation"""
    print("Testing Gemini Provider...")
    
    # Check if API key is available
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not set")
        print("   Set it with: export GEMINI_API_KEY=your_api_key_here")
        return False
    
    # Create provider instance
    provider = GeminiProvider(api_key=api_key)
    
    # Test health check
    print("🔍 Testing health check...")
    is_healthy = await provider.health_check()
    if is_healthy:
        print("✅ Health check passed!")
    else:
        print("❌ Health check failed!")
        return False
    
    # Test text generation
    print("🔍 Testing text generation...")
    try:
        response = await provider.generate(
            "Explain AI in 5 words",
            cache_key="test",
            role="assistant",
            max_tokens=50
        )
        print(f"✅ Generation successful: {response}")
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        return False
    
    # Test embedding
    print("🔍 Testing embeddings...")
    try:
        embedding = await provider.embed("Hello world")
        print(f"✅ Embedding successful: {len(embedding)} dimensions")
    except Exception as e:
        print(f"❌ Embedding failed: {e}")
        return False
    
    print("🎉 All tests passed!")
    return True


if __name__ == "__main__":
    asyncio.run(test_gemini_provider())