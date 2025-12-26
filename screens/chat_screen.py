"""Chat window screen."""

import logging

import flet as ft

from services.mistral_api import MistralAPI

# Configure logging
logger = logging.getLogger(__name__)



class ChatScreen:
    """Chat window UI and logic."""

    def __init__(self, page: ft.Page, provider_name: str = "MistralMedium") -> None:
        """Initialize chat screen.
        
        Args:
            page: Flet page instance.
            provider_name: Name of provider to use.
        """
        self.page = page
        self.provider_name = provider_name
        self.mistral_api = MistralAPI()
        self.messages: list[dict[str, str]] = []

    def build(self) -> ft.AlertDialog:
        """Build the chat window dialog.
        
        Returns:
            Flet AlertDialog containing the chat UI.
        """
        # Message list
        message_list = ft.ListView(
            controls=[],
            expand=True,
            spacing=10,
            auto_scroll=True,
        )

        # Input field
        input_field = ft.TextField(
            hint_text="Type a message...",
            expand=True,
            on_submit=lambda e: self.send_message(input_field.value, input_field, message_list),
        )

        # Send button
        send_button = ft.IconButton(
            icon=ft.Icons.SEND,
            on_click=lambda e: self.send_message(input_field.value, input_field, message_list),
        )

        return ft.AlertDialog(
            title=ft.Text("Mistral AI Chat"),
            content=ft.Column(
                controls=[
                    message_list,
                    ft.Row(
                        controls=[
                            input_field,
                            send_button,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                height=400,
                width=500,
                expand=True,
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: self.close_chat()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def send_message(
        self,
        message: str,
        input_field: ft.TextField,
        message_list: ft.ListView,
    ) -> None:
        """Send a message to Mistral API.
        
        Args:
            message: Message text to send.
            input_field: Input field control.
            message_list: Message list control.
        """
        if not message.strip():
            logger.info("Empty message, not sending")
            return

        logger.info(f"Sending message: {message}")

        # Add user message to UI
        user_message = ft.Container(
            content=ft.Text(message, size=14),
            padding=10,
            bgcolor=ft.colors.BLUE_100,
            border_radius=10,
            alignment=ft.Alignment.CENTER_RIGHT,
        )
        message_list.controls.append(user_message)

        # Clear input
        input_field.value = ""
        input_field.focus()

        # Add user message to history
        self.messages.append({"role": "user", "content": message})

        # Show typing indicator
        typing_indicator = ft.Container(
            content=ft.Text("...", size=14),
            padding=10,
            bgcolor=ft.colors.GREY_200,
            border_radius=10,
            alignment=ft.Alignment.CENTER_LEFT,
        )
        message_list.controls.append(typing_indicator)
        self.page.update()

        # Call Mistral API
        try:
            logger.info("Calling Mistral API for chat completion")
            # Get response from API
            response = self.mistral_api.chat_completion(self.messages)
            logger.info("Received response from Mistral API")

            # Extract assistant message
            assistant_message = response.get("choices", [{}])[0].get("message", {}).get("content", "")

            # Add to message history
            self.messages.append({"role": "assistant", "content": assistant_message})

            # Update UI with response
            message_list.controls.remove(typing_indicator)
            response_container = ft.Container(
                content=ft.Text(assistant_message, size=14),
                padding=10,
                bgcolor=ft.colors.GREY_200,
                border_radius=10,
                alignment=ft.Alignment.CENTER_LEFT,
            )
            message_list.controls.append(response_container)

        except Exception as e:
            # Show error
            message_list.controls.remove(typing_indicator)
            error_container = ft.Container(
                content=ft.Text(f"Error: {e!s}", size=14, color=ft.colors.RED),
                padding=10,
                bgcolor=ft.colors.RED_50,
                border_radius=10,
                alignment=ft.Alignment.CENTER_LEFT,
            )
            message_list.controls.append(error_container)

        self.page.update()

    def close_chat(self) -> None:
        """Close the chat window."""
        self.page.dialog.open = False
        self.page.update()
