"""Provider management service."""

from dataclasses import dataclass


@dataclass
class ProviderSettings:
    """Provider configuration settings."""
    name: str
    api_key: str
    authorization: bool = True
    auth_prefix: str = "Bearer"
    url: str = "https://api.mistral.ai/v1/"
    path: str = "/chat/completions"
    model: str = "mistral-medium-latest"
    max_tokens: int = 4096
    temperature: float = 0.7
    top_p: float = 1.0
    reasoning_effort: str = "med"
    enable_thinking: bool = True


class ProviderManager:
    """Manage provider CRUD operations."""

    def __init__(self) -> None:
        """Initialize provider manager."""
        self.providers: dict[str, ProviderSettings] = {}

    def add_provider(self, settings: ProviderSettings) -> None:
        """Add a new provider.
        
        Args:
            settings: Provider settings to add.
        """
        self.providers[settings.name] = settings

    def delete_provider(self, name: str) -> bool:
        """Delete a provider.
        
        Args:
            name: Name of provider to delete.
            
        Returns:
            True if deleted, False if not found.
        """
        if name in self.providers:
            del self.providers[name]
            return True
        return False

    def get_provider(self, name: str) -> ProviderSettings | None:
        """Get provider by name.
        
        Args:
            name: Name of provider to retrieve.
            
        Returns:
            ProviderSettings if found, None otherwise.
        """
        return self.providers.get(name)

    def list_providers(self) -> list[ProviderSettings]:
        """List all providers.
        
        Returns:
            List of all provider settings.
        """
        return list(self.providers.values())

    def update_provider(self, name: str, settings: ProviderSettings) -> bool:
        """Update provider settings.
        
        Args:
            name: Name of provider to update.
            settings: New settings.
            
        Returns:
            True if updated, False if not found.
        """
        if name in self.providers:
            self.providers[name] = settings
            return True
        return False
