import flet as ft

def main(page: ft.Page):
    page.title = "Preferences - Add-ons"
    page.theme_mode = ft.ThemeMode.DARK

    # Sidebar Navigation
    nav_items = [
        ft.NavigationRailDestination(icon=ft.icons.DASHBOARD_OUTLINED, label="Interface"),
        ft.NavigationRailDestination(icon=ft.icons.VIEW_IN_AR_OUTLINED, label="Viewport"),
        ft.NavigationRailDestination(icon=ft.icons.LIGHT_MODE_OUTLINED, label="Lights"),
        ft.NavigationRailDestination(icon=ft.icons.ANIMATION_OUTLINED, label="Animation"),
        ft.NavigationRailDestination(icon=ft.icons.EXTENSION_OUTLINED, label="Add-ons", selected_icon=ft.icons.EXTENSION),
        ft.NavigationRailDestination(icon=ft.icons.PALETTE_OUTLINED, label="Themes"),
        ft.NavigationRailDestination(icon=ft.icons.INPUT_OUTLINED, label="Input"),
        ft.NavigationRailDestination(icon=ft.icons.SYSTEM_SECURITY_UPDATE_OUTLINED, label="System"),
    ]

    nav_rail = ft.NavigationRail(
        selected_index=3,  # Add-ons selected by default
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=nav_items,
    )

    # Search Bar
    search_bar = ft.TextField(
        hint_text="Search Add-ons",
        expand=True,
        border_color=ft.colors.GREY_700,
    )

    # Add-on List Item (Example)
    def create_addon_item(name, description, version, file_path, enabled=True):
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Checkbox(value=enabled),
                        ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                        ft.IconButton(icon=ft.icons.EXPAND_MORE, icon_size=20),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row([ft.Text(description, size=12, color=ft.colors.GREY_500)]),
                ft.Row(
                    [
                        ft.Text(f"Version: {version}", size=12),
                        ft.Text(f"File: {file_path}", size=12, color=ft.colors.GREY_600),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
            ],
            spacing=5,
        )

    # Main Content: Add-ons List
    addons_list = ft.Column(
        [
            ft.Row([search_bar], alignment=ft.MainAxisAlignment.END),
            ft.Divider(),
            create_addon_item(
                name="Blender MCP",
                description="Connect Blender to Claude via MCP.",
                version="1.2",
                file_path="/Users/simon/Library/Application Support/Blender/5.0/scripts/addons/addon.py",
                enabled=True,
            ),
            create_addon_item(
                name="Cycles Render Engine",
                description="Cycles render engine integration.",
                version="1.0",
                file_path="/path/to/cycles.py",
                enabled=True,
            ),
            create_addon_item(
                name="Pose Library",
                description="Manage and apply pose libraries.",
                version="1.1",
                file_path="/path/to/pose.py",
                enabled=True,
            ),
            create_addon_item(
                name="Node Wrangler",
                description="Enhanced node editing tools.",
                version="3.4",
                file_path="/path/to/node_wrangler.py",
                enabled=False,
            ),
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    # Main Layout
    page.add(
        ft.Row(
            [
                nav_rail,
                ft.VerticalDivider(width=1),
                addons_list,
            ],
            expand=True,
        )
    )

ft.run(main)
