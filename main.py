import flet as ft


def main(page: ft.Page):
    page.title = "Flet Controls Showcase"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # State for heart button
    heart_liked = False

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    def toggle_heart(e):
        nonlocal heart_liked
        heart_liked = not heart_liked
        e.control.icon_color = ft.Colors.RED if heart_liked else ft.Colors.GREY
        page.update()

    # Card action message
    card_message = ft.Text("")

    def card_action(action_name):
        def handler(e):
            card_message.value = f"You pressed {action_name}"
            page.update()
        return handler

    # Animal images state (using local assets)
    animal_images = {
        "Kitten": "/kitten.jpg",
        "Puppy": "/puppy.jpg",
        "Duckling": "/duckling.jpg"
    }
    selected_animal_image = ft.Image(
        src="/kitten.jpg",
        width=300,
        height=300,
        border_radius=10,
        fit=ft.BoxFit.COVER,
    )

    def select_animal(animal_name):
        def handler(e):
            selected_animal_image.src = animal_images[animal_name]
            page.update()
        return handler

    # Header
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("Flet Controls Showcase", size=32, weight=ft.FontWeight.BOLD),
                ft.IconButton(
                    icon=ft.Icons.DARK_MODE,
                    tooltip="Toggle theme",
                    on_click=toggle_theme,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.Padding.only(bottom=20),
    )

    # Basic Controls Panel
    basic_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Basic Controls", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Text Examples:", weight=ft.FontWeight.BOLD),
                    ft.Text("Normal text"),
                    ft.Text("Italic text", italic=True),
                    ft.Text("Bold text", weight=ft.FontWeight.BOLD),
                    ft.Text("Colored text", color=ft.Colors.BLUE),
                    ft.Divider(),
                    ft.TextField(label="Text Field", hint_text="Enter text here"),
                    ft.TextField(label="Password Field", password=True, can_reveal_password=True),
                    ft.TextField(
                        label="Multiline TextField",
                        multiline=True,
                        min_lines=3,
                        max_lines=5,
                    ),
                    ft.Divider(),
                    ft.Button("Elevated Button", icon=ft.Icons.ADD),
                    ft.FilledButton("Filled Button", icon=ft.Icons.SAVE),
                    ft.OutlinedButton("Outlined Button", icon=ft.Icons.EDIT),
                    ft.TextButton("Text Button", icon=ft.Icons.DELETE),
                    ft.IconButton(
                        icon=ft.Icons.FAVORITE,
                        icon_color=ft.Colors.GREY,
                        tooltip="Like",
                        on_click=toggle_heart,
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Input Controls Panel
    input_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Input Controls", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Checkbox(label="Checkbox", value=True),
                    ft.Switch(label="Switch", value=False),
                    ft.RadioGroup(
                        content=ft.Column([
                            ft.Radio(value="option1", label="Radio Option 1"),
                            ft.Radio(value="option2", label="Radio Option 2"),
                        ])
                    ),
                    ft.Divider(),
                    ft.Text("Slider:", weight=ft.FontWeight.BOLD),
                    ft.Slider(min=0, max=100, divisions=10, label="{value}%"),
                    ft.Text("ProgressBar (70% complete):", weight=ft.FontWeight.BOLD),
                    ft.ProgressBar(value=0.7, width=300),
                    ft.Text("ProgressRing (loading spinner):", weight=ft.FontWeight.BOLD),
                    ft.ProgressRing(width=30, height=30, stroke_width=4),
                    ft.Divider(),
                    ft.Dropdown(
                        label="Dropdown",
                        options=[
                            ft.dropdown.Option("Option 1"),
                            ft.dropdown.Option("Option 2"),
                            ft.dropdown.Option("Option 3"),
                        ],
                        width=200,
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Display Controls Panel
    display_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Display Controls", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Icons:", weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE),
                            ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.RED),
                            ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.GREEN),
                            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.ORANGE),
                        ]
                    ),
                    ft.Divider(),
                    ft.Image(
                        src="https://picsum.photos/200/200",
                        width=200,
                        height=200,
                        border_radius=10,
                        fit=ft.BoxFit.COVER,
                    ),
                    ft.Divider(),
                    ft.Chip(
                        label=ft.Text("Chip"),
                        leading=ft.Icon(ft.Icons.TAG),
                        on_click=lambda e: print("Chip clicked"),
                    ),
                    ft.Divider(),
                    ft.Icon(ft.Icons.NOTIFICATIONS, badge=ft.Badge(label="3")),
                    ft.Divider(),
                    ft.VerticalDivider(),
                    ft.Text("Hover over me", tooltip="This is a tooltip"),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Container & Layout Panel
    layout_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Layout Controls", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Container with border and padding:", weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=ft.Text("Content inside container"),
                        border=ft.Border.all(2, ft.Colors.BLUE),
                        border_radius=10,
                        padding=20,
                        bgcolor=ft.Colors.BLUE_50,
                    ),
                    ft.Divider(),
                    ft.Text("Row Layout:", weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("1"), bgcolor=ft.Colors.RED_200, padding=10
                            ),
                            ft.Container(
                                content=ft.Text("2"), bgcolor=ft.Colors.GREEN_200, padding=10
                            ),
                            ft.Container(
                                content=ft.Text("3"), bgcolor=ft.Colors.BLUE_200, padding=10
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Divider(),
                    ft.Text("Column Layout:", weight=ft.FontWeight.BOLD),
                    ft.Column(
                        [
                            ft.Container(
                                content=ft.Text("A"), bgcolor=ft.Colors.AMBER_200, padding=10
                            ),
                            ft.Container(
                                content=ft.Text("B"), bgcolor=ft.Colors.PURPLE_200, padding=10
                            ),
                            ft.Container(
                                content=ft.Text("C"), bgcolor=ft.Colors.PINK_200, padding=10
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Divider(),
                    ft.Text("Card:", weight=ft.FontWeight.BOLD),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.ALBUM),
                                        title=ft.Text("Card Title"),
                                        subtitle=ft.Text("Card subtitle with description"),
                                    ),
                                    card_message,
                                    ft.Row(
                                        [
                                            ft.TextButton("Action 1", on_click=card_action("Action 1")),
                                            ft.TextButton("Action 2", on_click=card_action("Action 2")),
                                        ],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                            padding=10,
                        )
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # List & Grid Panel
    list_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Lists & Grids", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Interactive ListTiles:", weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.PETS),
                                        title=ft.Text("Kitten"),
                                        subtitle=ft.Text("Click to see a cute kitten"),
                                        on_click=select_animal("Kitten"),
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.PETS),
                                        title=ft.Text("Puppy"),
                                        subtitle=ft.Text("Click to see a cute puppy"),
                                        on_click=select_animal("Puppy"),
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.Icons.CRUELTY_FREE),
                                        title=ft.Text("Duckling"),
                                        subtitle=ft.Text("Click to see a cute duckling"),
                                        on_click=select_animal("Duckling"),
                                    ),
                                ],
                                expand=1,
                            ),
                            ft.Container(
                                content=selected_animal_image,
                                alignment=ft.Alignment.CENTER,
                                expand=1,
                            ),
                        ],
                    ),
                    ft.Divider(),
                    ft.Text("DataTable:", weight=ft.FontWeight.BOLD),
                    ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Name")),
                            ft.DataColumn(ft.Text("Age")),
                            ft.DataColumn(ft.Text("City")),
                        ],
                        rows=[
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("John")),
                                    ft.DataCell(ft.Text("30")),
                                    ft.DataCell(ft.Text("New York")),
                                ]
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Jane")),
                                    ft.DataCell(ft.Text("25")),
                                    ft.DataCell(ft.Text("Paris")),
                                ]
                            ),
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text("Bob")),
                                    ft.DataCell(ft.Text("35")),
                                    ft.DataCell(ft.Text("London")),
                                ]
                            ),
                        ],
                    ),
                    ft.Divider(),
                    ft.Text("GridView:", weight=ft.FontWeight.BOLD),
                    ft.GridView(
                        controls=[
                            ft.Container(
                                content=ft.Text("Grid 1"),
                                bgcolor=ft.Colors.BLUE_100,
                                padding=20,
                                border_radius=5,
                            ),
                            ft.Container(
                                content=ft.Text("Grid 2"),
                                bgcolor=ft.Colors.GREEN_100,
                                padding=20,
                                border_radius=5,
                            ),
                            ft.Container(
                                content=ft.Text("Grid 3"),
                                bgcolor=ft.Colors.RED_100,
                                padding=20,
                                border_radius=5,
                            ),
                            ft.Container(
                                content=ft.Text("Grid 4"),
                                bgcolor=ft.Colors.YELLOW_100,
                                padding=20,
                                border_radius=5,
                            ),
                        ],
                        runs_count=2,
                        max_extent=150,
                        child_aspect_ratio=1,
                        spacing=10,
                        run_spacing=10,
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Navigation Controls Panel
    navigation_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Navigation Controls", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("NavigationBar:", weight=ft.FontWeight.BOLD),
                    ft.NavigationBar(
                        destinations=[
                            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
                            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
                        ],
                        selected_index=0,
                    ),
                    ft.Divider(),
                    ft.Text("Tabs:", weight=ft.FontWeight.BOLD),
                    ft.Tabs(
                        selected_index=0,
                        length=3,
                        expand=False,
                        height=200,
                        content=ft.Column(
                            controls=[
                                ft.TabBar(
                                    tabs=[
                                        ft.Tab(label="Tab 1", icon=ft.Icons.HOME),
                                        ft.Tab(label="Tab 2", icon=ft.Icons.SEARCH),
                                        ft.Tab(label="Tab 3", icon=ft.Icons.SETTINGS),
                                    ]
                                ),
                                ft.TabBarView(
                                    expand=True,
                                    controls=[
                                        ft.Container(content=ft.Text("Content 1"), alignment=ft.Alignment.CENTER),
                                        ft.Container(content=ft.Text("Content 2"), alignment=ft.Alignment.CENTER),
                                        ft.Container(content=ft.Text("Content 3"), alignment=ft.Alignment.CENTER),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Dialog & Overlay Panel
    def show_dialog(e):
        dialog = ft.AlertDialog(
            title=ft.Text("Alert Dialog"),
            content=ft.Text("This is a sample alert dialog"),
            actions=[
                ft.TextButton("Cancel", on_click=lambda e: close_dialog(dialog)),
                ft.TextButton("OK", on_click=lambda e: close_dialog(dialog)),
            ],
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    def show_snackbar(e):
        snackbar = ft.SnackBar(
            content=ft.Text("This is a SnackBar!"),
            action="OK",
        )
        page.overlay.append(snackbar)
        snackbar.open = True
        page.update()

    def show_banner(e):
        banner = ft.Banner(
            leading=ft.Icon(ft.Icons.WARNING, color=ft.Colors.AMBER, size=40),
            content=ft.Text("This is a banner message"),
            actions=[
                ft.TextButton("Dismiss", on_click=lambda e: close_banner(banner)),
            ],
        )
        page.overlay.append(banner)
        banner.open = True
        page.update()

    def close_banner(banner):
        banner.open = False
        page.update()

    overlay_controls = ft.ExpansionPanel(
        header=ft.ListTile(title=ft.Text("Dialogs & Overlays", weight=ft.FontWeight.BOLD)),
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Button("Show Alert Dialog", on_click=show_dialog),
                    ft.Button("Show SnackBar", on_click=show_snackbar),
                    ft.Button("Show Banner", on_click=show_banner),
                ],
                spacing=10,
            ),
            padding=10,
        ),
    )

    # Expansion Panel List
    panel_list = ft.ExpansionPanelList(
        controls=[
            basic_controls,
            input_controls,
            display_controls,
            layout_controls,
            list_controls,
            navigation_controls,
            overlay_controls,
            
        ],
        expand_icon_color=ft.Colors.BLUE,
    )

    # Main content
    page.add(
        ft.Column(
            [
                header,
                ft.Container(
                    content=panel_list,
                    expand=True,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
    )


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
