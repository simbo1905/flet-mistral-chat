"""Tests for Provider Screen UI."""

import pytest
import flet as ft
from screens.provider_screen import ProviderScreen
from unittest.mock import Mock


def test_provider_screen_initialization() -> None:
    """Test that ProviderScreen can be initialized."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # This should not raise an exception
    provider_screen = ProviderScreen(page)
    
    # Verify the screen was initialized
    assert provider_screen is not None
    assert provider_screen.page == page
    assert provider_screen.provider_manager is not None
    assert provider_screen.mistral_api is not None


def test_provider_screen_build() -> None:
    """Test that ProviderScreen.build() works without errors."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # This should not raise an exception
    screen = provider_screen.build()
    
    # Verify the screen is a Column
    assert isinstance(screen, ft.Column)
    assert len(screen.controls) > 0


def test_app_bar_icons() -> None:
    """Test that all app bar icons are valid."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Get the app bar
    app_bar = provider_screen._build_app_bar()
    
    # Verify it's a Row
    assert isinstance(app_bar, ft.Row)
    
    # Get all icon buttons from the app bar
    icon_buttons = []
    for control in app_bar.controls:
        if isinstance(control, ft.Row):
            for sub_control in control.controls:
                if isinstance(sub_control, ft.IconButton):
                    icon_buttons.append(sub_control)
    
    # Verify we have the expected number of icon buttons
    assert len(icon_buttons) == 4, f"Expected 4 icon buttons, got {len(icon_buttons)}"
    
    # Verify each icon button has a valid icon
    for icon_button in icon_buttons:
        icon = icon_button.icon
        assert hasattr(icon, 'name'), f"Invalid icon: {icon}"
        assert hasattr(ft.Icons, icon.name), f"Invalid icon name: {icon.name}"


def test_sidebar_provider_items() -> None:
    """Test that sidebar provider items are created correctly."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Get the sidebar
    sidebar = provider_screen._build_sidebar()
    
    # Verify it's a Column
    assert isinstance(sidebar, ft.Column)
    
    # Verify it has the expected structure
    assert len(sidebar.controls) >= 2  # Title + Divider + items


def test_provider_form_fields() -> None:
    """Test that provider form has all required fields."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Get the provider form
    provider_form = provider_screen._build_provider_form()
    
    # Verify it's a Column
    assert isinstance(provider_form, ft.Column)
    
    # Count text fields
    text_fields = [c for c in provider_form.controls if isinstance(c, ft.TextField)]
    assert len(text_fields) >= 6, f"Expected at least 6 text fields, got {len(text_fields)}"
    
    # Verify we have a test button
    buttons = [c for c in provider_form.controls if isinstance(c, ft.Button)]
    assert len(buttons) == 1, f"Expected 1 button, got {len(buttons)}"
