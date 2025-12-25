"""Main application entry point."""

import flet as ft
from screens.provider_screen import ProviderScreen


def main(page: ft.Page) -> None:
    """Main application entry point.
    
    Args:
        page: Flet page instance.
    """
    page.title = "Mistral AI Provider Settings"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    
    # Initialize provider screen
    provider_screen = ProviderScreen(page)
    
    # Add the screen to the page
    page.add(provider_screen.build())


if __name__ == "__main__":
    ft.run(main)
