"""Tests for Provider Screen UI."""

import pytest
import flet as ft
from screens.provider_screen import ProviderScreen
from screens.chat_screen import ChatScreen
from unittest.mock import Mock, MagicMock


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


def test_test_provider_settings_success() -> None:
    """Test that test_provider_settings shows success banner."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    page.banner = None
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Mock the API to return success
    provider_screen.mistral_api.list_models = Mock(return_value={"data": [{"id": "model1"}, {"id": "model2"}]})
    
    # Create a mock event
    mock_event = Mock()
    
    # Call test_provider_settings
    provider_screen.test_provider_settings(mock_event)
    
    # Verify banner was set
    assert page.banner is not None
    assert page.banner.open is True
    assert "Successfully connected" in page.banner.content.value
    assert "2 models" in page.banner.content.value
    assert page.banner.bgcolor == ft.Colors.GREEN_100


def test_test_provider_settings_error() -> None:
    """Test that test_provider_settings shows error banner."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    page.banner = None
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Mock the API to raise an error
    provider_screen.mistral_api.list_models = Mock(side_effect=Exception("API error"))
    
    # Create a mock event
    mock_event = Mock()
    
    # Call test_provider_settings
    provider_screen.test_provider_settings(mock_event)
    
    # Verify error banner was set
    assert page.banner is not None
    assert page.banner.open is True
    assert "Failed to connect" in page.banner.content.value
    assert "API error" in page.banner.content.value
    assert page.banner.bgcolor == ft.Colors.RED_100


def test_close_banner() -> None:
    """Test that _close_banner closes the banner."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    page.banner = Mock()
    page.banner.open = True
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Call _close_banner
    provider_screen._close_banner()
    
    # Verify banner was closed
    assert page.banner.open is False


def test_chat_screen_initialization() -> None:
    """Test that ChatScreen can be initialized."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # This should not raise an exception
    chat_screen = ChatScreen(page)
    
    # Verify the screen was initialized
    assert chat_screen is not None
    assert chat_screen.page == page
    assert chat_screen.mistral_api is not None
    assert len(chat_screen.messages) == 0


def test_chat_screen_build() -> None:
    """Test that ChatScreen.build() works without errors."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize chat screen
    chat_screen = ChatScreen(page)
    
    # This should not raise an exception
    dialog = chat_screen.build()
    
    # Verify the dialog is an AlertDialog
    assert isinstance(dialog, ft.AlertDialog)
    assert dialog.title.value == "Mistral AI Chat"
    
    # Verify the dialog has content
    assert dialog.content is not None
    assert isinstance(dialog.content, ft.Column)


def test_chat_screen_icons() -> None:
    """Test that all chat screen icons are valid."""
    # Create a mock page
    page = Mock(spec=ft.Page)
    
    # Initialize chat screen
    chat_screen = ChatScreen(page)
    
    # Build the dialog
    dialog = chat_screen.build()
    
    # Get the content column
    content = dialog.content
    assert isinstance(content, ft.Column)
    
    # Find the row with the input field and send button
    input_row = None
    for control in content.controls:
        if isinstance(control, ft.Row):
            input_row = control
            break
    
    assert input_row is not None, "Input row not found"
    
    # Find the send button
    send_button = None
    for control in input_row.controls:
        if isinstance(control, ft.IconButton):
            send_button = control
            break
    
    assert send_button is not None, "Send button not found"
    
    # Verify the icon is valid
    icon = send_button.icon
    assert hasattr(icon, 'name'), f"Invalid icon: {icon}"
    assert hasattr(ft.Icons, icon.name), f"Invalid icon name: {icon.name}"
