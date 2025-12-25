"""Mistral AI API client wrapper."""

import os
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from mistralai import Mistral


class MistralAPI:
    """Wrapper for Mistral AI API."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Initialize Mistral API client.
        
        Args:
            api_key: Optional API key. If not provided, loads from .env.
        """
        load_dotenv()
        self.api_key = self._clean_api_key(api_key or os.getenv("MISTRAL_API_KEY"))
        if not self.api_key:
            raise ValueError("MISTRAL_API_KEY not found in environment or .env file")
        
        self.client = Mistral(api_key=self.api_key)

    def _clean_api_key(self, api_key: Optional[str]) -> str:
        """Clean API key by removing surrounding quotes if present.
        
        Args:
            api_key: API key potentially wrapped in quotes.
            
        Returns:
            Cleaned API key without surrounding quotes.
        """
        if not api_key:
            return ""
        
        # Remove surrounding single or double quotes
        api_key = api_key.strip()
        if (api_key.startswith('"') and api_key.endswith('"')) or \
           (api_key.startswith("'") and api_key.endswith("'")):
            api_key = api_key[1:-1]
        
        return api_key

    def list_models(self) -> Dict[str, Any]:
        """List available models from Mistral API.
        
        Returns:
            Dictionary containing model information.
        """
        try:
            models = self.client.models.list()
            return models.model_dump() if hasattr(models, 'model_dump') else models.dict()
        except Exception as e:
            raise RuntimeError(f"Failed to list models: {str(e)}")

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "mistral-medium-latest",
        max_tokens: int = 4096,
        temperature: float = 0.7,
        top_p: float = 1.0,
    ) -> Dict[str, Any]:
        """Get chat completion from Mistral API.
        
        Args:
            messages: List of chat messages (dict with role and content).
            model: Model name.
            max_tokens: Maximum tokens to generate.
            temperature: Sampling temperature.
            top_p: Nucleus sampling probability.
            
        Returns:
            Dictionary containing chat completion response.
        """
        try:
            response = self.client.chat.complete(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )
            return response.model_dump() if hasattr(response, 'model_dump') else response.dict()
        except Exception as e:
            raise RuntimeError(f"Chat completion failed: {str(e)}")
