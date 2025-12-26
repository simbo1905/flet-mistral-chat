"""Provider settings screen."""

import logging
import flet as ft
from typing import Callable, Optional

from services.mistral_api import MistralAPI
from services.provider_manager import ProviderManager, ProviderSettings
from screens.chat_screen import ChatScreen


# Configure logging
logger = logging.getLogger(__name__)


class ProviderScreen:
    """Provider settings screen UI and logic."""

    def __init__(self, page: ft.Page) -> None:
        """Initialize provider screen.
        
        Args:
            page: Flet page instance.
        """
        self.page = page
        self.provider_manager = ProviderManager()
        self.mistral_api = MistralAPI()
        
        # Initialize with a default provider
        self._initialize_default_provider()

    def _initialize_default_provider(self) -> None:
        """Initialize with a default Mistral provider."""
        default_settings = ProviderSettings(
            name="MistralMedium",
            api_key="",  # Will be loaded from .env
        )
        self.provider_manager.add_provider(default_settings)

    def build(self) -> ft.Column:
        """Build the provider settings screen.
        
        Returns:
            Flet Column containing the screen UI.
        """
        return ft.Column(
            controls=[
                self._build_app_bar(),
                ft.Divider(),
                self._build_main_content(),
            ],
            expand=True,
        )

    def _build_app_bar(self) -> ft.Row:
        """Build the top app bar.
        
        Returns:
            Flet Row containing app bar controls.
        """
        return ft.Row(
            controls=[
                ft.Text("Provider Settings Screen", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.SETTINGS_OUTLINED,
                            tooltip="Provider Settings",
                            on_click=lambda e: logger.info("Settings icon clicked"),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.VIEW_MODULE_OUTLINED,
                            tooltip="MCP Config",
                            on_click=lambda e: logger.info("MCP Config icon clicked"),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CHAT_OUTLINED,
                            tooltip="Open Chat",
                            on_click=self.open_chat_window,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.HELP_OUTLINED,
                            tooltip="Placeholder",
                            on_click=lambda e: logger.info("Placeholder icon clicked"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def _build_main_content(self) -> ft.Row:
        """Build the main content area.
        
        Returns:
            Flet Row containing sidebar and form.
        """
        return ft.Row(
            controls=[
                self._build_sidebar(),
                ft.VerticalDivider(width=1),
                self._build_provider_form(),
            ],
            expand=True,
        )

    def _build_sidebar(self) -> ft.Column:
        """Build the left sidebar with provider list.
        
        Returns:
            Flet Column containing provider list.
        """
        providers = self.provider_manager.list_providers()
        
        provider_items = []
        for provider in providers:
            provider_items.append(
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Text(provider.name[0], size=16, weight=ft.FontWeight.BOLD),
                            width=30,
                            height=30,
                            bgcolor=ft.Colors.BLUE_200,
                            border_radius=15,
                            alignment=ft.Alignment.CENTER,
                        ),
                        ft.Text(provider.name, size=16),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINED,
                            icon_color=ft.Colors.RED_500,
                            tooltip=f"Delete {provider.name}",
                            on_click=lambda e, name=provider.name: self.confirm_delete_provider(name),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        
        return ft.Column(
            controls=[
                ft.Text("Providers", size=18, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                *provider_items,
            ],
            width=300,
            expand=False,
        )

    def _build_provider_form(self) -> ft.Column:
        """Build the provider settings form.
        
        Returns:
            Flet Column containing form fields.
        """
        # Get the first provider for now
        provider = self.provider_manager.list_providers()[0] if self.provider_manager.list_providers() else None
        
        return ft.Column(
            controls=[
                ft.Text("Provider Settings", size=18, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                
                # Name field
                ft.TextField(
                    label="Name",
                    value=provider.name if provider else "",
                    expand=True,
                ),
                
                # API Key field
                ft.TextField(
                    label="API Key",
                    value="",  # Will be loaded from .env, not displayed
                    password=True,
                    can_reveal_password=True,
                    expand=True,
                ),
                
                # Authorization
                ft.Row(
                    controls=[
                        ft.Switch(label="Authorization"),
                        ft.Dropdown(
                            label="Prefix",
                            options=[ft.dropdown.Option("Bearer")],
                            value="Bearer",
                            width=200,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                # URL
                ft.TextField(
                    label="URL",
                    value=provider.url if provider else "https://api.mistral.ai/v1/",
                    expand=True,
                ),
                
                # Path
                ft.TextField(
                    label="Path",
                    value=provider.path if provider else "/chat/completions",
                    expand=True,
                ),
                
                # Model
                ft.Dropdown(
                    label="Model",
                    options=[
                        ft.dropdown.Option("mistral-medium-latest"),
                        ft.dropdown.Option("mistral-small-latest"),
                        ft.dropdown.Option("mistral-tiny-latest"),
                    ],
                    value=provider.model if provider else "mistral-medium-latest",
                    expand=True,
                ),
                
                # Max Tokens
                ft.TextField(
                    label="Max Tokens",
                    value=str(provider.max_tokens) if provider else "4096",
                    expand=True,
                ),
                
                # Temperature
                ft.TextField(
                    label="Temperature",
                    value=str(provider.temperature) if provider else "0.7",
                    expand=True,
                ),
                
                # Top P
                ft.TextField(
                    label="Top P",
                    value=str(provider.top_p) if provider else "1.0",
                    expand=True,
                ),
                
                # Reasoning Effort
                ft.RadioGroup(
                    content=ft.Row(
                        controls=[
                            ft.Radio(value="min", label="Min"),
                            ft.Radio(value="low", label="Low"),
                            ft.Radio(value="med", label="Med"),
                            ft.Radio(value="high", label="High"),
                        ],
                    ),
                    value=provider.reasoning_effort if provider else "med",
                ),
                
                # Enable Thinking
                ft.Checkbox(
                    label="Enable Thinking",
                    value=provider.enable_thinking if provider else True,
                ),
                
                # Test button
                ft.Button(
                    content=ft.Text("Test"),
                    icon=ft.Icons.PLAY_ARROW,
                    on_click=self.test_provider_settings,
                    expand=True,
                ),
            ],
            spacing=10,
            expand=True,
        )

    def open_chat_window(self, e: ft.ControlEvent) -> None:
        """Open the chat window.
        
        Args:
            e: Control event.
        """
        logger.info("Opening chat window")
        chat_screen = ChatScreen(self.page)
        dialog = chat_screen.build()
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        logger.info("Chat window opened successfully")

    def confirm_delete_provider(self, name: str) -> None:
        """Show delete confirmation dialog.
        
        Args:
            name: Name of provider to delete.
        """
        def on_delete(e: ft.ControlEvent) -> None:
            if self.provider_manager.delete_provider(name):
                print(f"Deleted provider: {name}")
                self.page.update()
            dialog.open = False
            self.page.update()
        
        dialog = ft.AlertDialog(
            title=ft.Text(f"Delete {name}?"),
            content=ft.Text("Are you sure you want to delete this provider?"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: self._close_dialog(dialog)),
                ft.TextButton("Delete", on_click=on_delete, style=ft.ButtonStyle(color=ft.colors.RED)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def _close_dialog(self, dialog: ft.AlertDialog) -> None:
        """Close dialog.
        
        Args:
            dialog: Dialog to close.
        """
        dialog.open = False
        self.page.update()

    def test_provider_settings(self, e: ft.ControlEvent) -> None:
        """Test provider settings by calling Mistral API.
        
        Args:
            e: Control event.
        """
        logger.info("Testing provider settings")
        try:
            models = self.mistral_api.list_models()
            model_count = len(models.get('data', []))
            logger.info(f"Successfully connected to Mistral API. Found {model_count} models.")
            
            # Show success banner
            self.page.banner = ft.Banner(
                bgcolor=ft.Colors.GREEN_100,
                leading=ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINED, color=ft.Colors.GREEN_700, size=40),
                content=ft.Text(
                    f"✓ Successfully connected to Mistral API! Found {model_count} models.",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                ),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: self._close_banner()),
                ],
            )
            self.page.banner.open = True
            self.page.update()
        except Exception as ex:
            print(f"Error testing provider: {str(ex)}")
            
            # Show error banner
            self.page.banner = ft.Banner(
                bgcolor=ft.Colors.RED_100,
                leading=ft.Icon(ft.Icons.ERROR_OUTLINED, color=ft.Colors.RED_700, size=40),
                content=ft.Text(
                    f"✗ Failed to connect: {str(ex)}",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                ),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: self._close_banner()),
                ],
            )
            self.page.banner.open = True
            self.page.update()

    def _close_banner(self) -> None:
        """Close the banner."""
        if self.page.banner:
            self.page.banner.open = False
            self.page.update()
