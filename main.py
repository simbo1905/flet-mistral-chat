"""Main application entry point."""

import argparse
import logging
import sys
import flet as ft
from screens.provider_screen import ProviderScreen


# Configure logging
logger = logging.getLogger(__name__)


def setup_logging(log_level: str = "INFO") -> None:
    """Setup logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
    logger.info(f"Logging configured with level: {log_level}")


def main(page: ft.Page) -> None:
    """Main application entry point.
    
    Args:
        page: Flet page instance.
    """
    logger.info("Starting Mistral AI Provider Settings application")
    page.title = "Mistral AI Provider Settings"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    
    # Initialize provider screen
    logger.info("Initializing provider screen")
    provider_screen = ProviderScreen(page)
    
    # Add the screen to the page
    logger.info("Building and adding provider screen to page")
    page.add(provider_screen.build())
    
    logger.info("Application started successfully")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Mistral AI Provider Settings")
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)",
    )
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.log_level)
    
    # Run the application
    logger.info(f"Running application with log level: {args.log_level}")
    ft.run(main)
