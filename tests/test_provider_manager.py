"""Tests for Provider Manager."""

import pytest
from services.provider_manager import ProviderManager, ProviderSettings


@pytest.fixture
def provider_manager() -> ProviderManager:
    """Create provider manager instance for testing."""
    return ProviderManager()


def test_add_provider(provider_manager: ProviderManager) -> None:
    """Test adding a provider."""
    settings = ProviderSettings(
        name="TestProvider",
        api_key="test_key_123",
        model="test-model",
    )
    
    provider_manager.add_provider(settings)
    
    # Verify provider was added
    provider = provider_manager.get_provider("TestProvider")
    assert provider is not None
    assert provider.name == "TestProvider"
    assert provider.api_key == "test_key_123"
    assert provider.model == "test-model"


def test_delete_provider(provider_manager: ProviderManager) -> None:
    """Test deleting a provider."""
    # Add a provider first
    settings = ProviderSettings(name="DeleteMe", api_key="key")
    provider_manager.add_provider(settings)
    
    # Delete the provider
    result = provider_manager.delete_provider("DeleteMe")
    assert result is True
    
    # Verify it's gone
    provider = provider_manager.get_provider("DeleteMe")
    assert provider is None
    
    # Try deleting non-existent provider
    result = provider_manager.delete_provider("NonExistent")
    assert result is False


def test_update_provider(provider_manager: ProviderManager) -> None:
    """Test updating a provider."""
    # Add a provider
    settings = ProviderSettings(name="UpdateMe", api_key="old_key")
    provider_manager.add_provider(settings)
    
    # Update the provider
    new_settings = ProviderSettings(name="UpdateMe", api_key="new_key", model="new-model")
    result = provider_manager.update_provider("UpdateMe", new_settings)
    assert result is True
    
    # Verify update
    provider = provider_manager.get_provider("UpdateMe")
    assert provider is not None
    assert provider.api_key == "new_key"
    assert provider.model == "new-model"
    
    # Try updating non-existent provider
    result = provider_manager.update_provider("NonExistent", new_settings)
    assert result is False


def test_list_providers(provider_manager: ProviderManager) -> None:
    """Test listing all providers."""
    # Add some providers
    provider_manager.add_provider(ProviderSettings(name="Provider1", api_key="key1"))
    provider_manager.add_provider(ProviderSettings(name="Provider2", api_key="key2"))
    
    # List providers
    providers = provider_manager.list_providers()
    assert len(providers) == 2
    assert providers[0].name == "Provider1"
    assert providers[1].name == "Provider2"


def test_provider_settings_defaults() -> None:
    """Test provider settings defaults."""
    settings = ProviderSettings(name="Test", api_key="key")
    
    assert settings.authorization is True
    assert settings.auth_prefix == "Bearer"
    assert settings.url == "https://api.mistral.ai/v1/"
    assert settings.path == "/chat/completions"
    assert settings.model == "mistral-medium-latest"
    assert settings.max_tokens == 4096
    assert settings.temperature == 0.7
    assert settings.top_p == 1.0
    assert settings.reasoning_effort == "med"
    assert settings.enable_thinking is True
