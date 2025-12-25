# Agent Development Guide

This document provides guidance for AI agents working with this Flet Controls Showcase application.

## Project Overview

This is a Flet demonstration application showcasing various UI controls and interactive features. It serves as a reference implementation and testing ground for Flet UI components.

## Technology Stack

- **Framework**: Flet 0.80.0 (Python UI framework powered by Flutter)
- **Python Version**: 3.12+
- **Package Manager**: uv (DO NOT USE pip, poetry, or any other package manager)
- **Asset Management**: Local assets stored in `assets/` directory

## IMPORTANT: uv Project Guidelines

**THIS IS A uv PROJECT. DO NOT POLLUTE IT WITH OTHER DEPENDENCY MANAGEMENT TOOLS.**

### Working with uv

1. **Install Dependencies**: Use `uv sync` to install dependencies from `pyproject.toml`
2. **Run Applications**: Use `uv run <script.py>` to execute Python scripts
3. **Add Dependencies**: Update `pyproject.toml` and run `uv sync`
4. **Virtual Environment**: uv automatically manages a virtual environment in `.venv`

### Forbidden Actions

- ❌ Do NOT use `pip install`
- ❌ Do NOT use `poetry`
- ❌ Do NOT use `conda`
- ❌ Do NOT create separate virtual environments
- ❌ Do NOT modify `uv.lock` manually

### Required Actions

- ✅ Use `uv run main.py` to run the application
- ✅ Use `uv sync` to update dependencies
- ✅ Use `uv add <package>` to add new dependencies
- ✅ Use `uv remove <package>` to remove dependencies

## Project Structure

```
.
├── assets/          # Local image assets (kitten.jpg, puppy.jpg, duckling.jpg)
├── main.py          # Main application entry point
├── pyproject.toml   # Python project configuration and dependencies
└── uv.lock         # Locked dependency versions
```

## Key Features Implemented

### Interactive Controls

1. **Toggle Heart Button**: Icon button that changes color from grey to red on click
2. **Card Actions**: Action buttons that display feedback messages
3. **Animal Image Selector**: ListTiles that update an image display panel
4. **Radio Button Groups**: Properly wrapped in RadioGroup control
5. **Theme Toggle**: Switch between light and dark modes

### Control Categories

The application demonstrates:
- Basic Controls (Text, TextField, Buttons)
- Input Controls (Checkbox, Switch, Radio, Slider, ProgressBar, ProgressRing, Dropdown)
- Display Controls (Icons, Images, Chips, Badges, Tooltips)
- Layout Controls (Container, Row, Column, Card)
- Lists & Grids (Interactive ListTiles, DataTable, GridView)
- Navigation (NavigationBar, Tabs with TabBar/TabBarView)
- Dialogs & Overlays (AlertDialog, SnackBar, Banner)

## Important API Notes for Flet 0.80.0

### Breaking Changes from Previous Versions

1. **Icons**: Use `ft.Icons.ICON_NAME` (capital I), not `ft.icons.ICON_NAME`
2. **Colors**: Use `ft.Colors.COLOR_NAME` (capital C), not `ft.colors.COLOR_NAME`
3. **Border**: Use `ft.Border.all()` (capital B), not `ft.border.all()`
4. **Padding**: Use `ft.Padding.only()` (capital P), not `ft.padding.only()`
5. **ImageFit**: Use `ft.BoxFit.COVER` instead of `ft.ImageFit.COVER`
6. **Button**: Use `ft.Button` instead of deprecated `ft.ElevatedButton`
7. **Tab Structure**: Tabs now use `TabBar` and `TabBarView` within a `Tabs` container
8. **Badge**: Now a property on other controls (like Icon), not standalone
9. **Tooltip**: Now a property on controls, not a wrapping control
10. **App Entry**: Use `ft.run(main)` instead of deprecated `ft.app(target=main)`

### Asset Management

Local assets must be:
1. Stored in an `assets/` directory
2. Referenced with leading slash: `/filename.jpg`
3. Configured in `ft.run()`: `ft.run(main, assets_dir="assets")`

## Development Guidelines

### Project Setup

1. **Always use uv**: This project uses `uv` for dependency management. Never use `pip`, `poetry`, or other tools.
2. **Sync dependencies**: Run `uv sync` after pulling changes or modifying `pyproject.toml`.
3. **Run the app**: Use `uv run main.py` to start the application.

### Adding New Controls

1. Add control definitions within the appropriate `ft.ExpansionPanel`
2. For interactive controls, create event handlers in the `main()` function
3. Use state variables (with `nonlocal` if needed) to track control state
4. Call `page.update()` after state changes to refresh the UI
5. Test your changes with `uv run main.py`

### State Management

```python
# Define state at the top of main()
state_var = initial_value

def event_handler(e):
    nonlocal state_var
    state_var = new_value
    # Update UI elements
    page.update()
```

### Common Patterns

**Interactive ListTile with Image Display:**
```python
animal_image = ft.Image(src="/default.jpg", ...)

def select_item(item_name):
    def handler(e):
        animal_image.src = f"/{item_name}.jpg"
        page.update()
    return handler

ft.ListTile(title=ft.Text("Item"), on_click=select_item("item"))
```

**Toggle Button Colors:**
```python
is_active = False

def toggle(e):
    nonlocal is_active
    is_active = not is_active
    e.control.icon_color = ft.Colors.RED if is_active else ft.Colors.GREY
    page.update()
```

## Testing Strategy

1. **Visual Inspection**: Check all controls render correctly
2. **Interaction Testing**: Verify all interactive elements respond to clicks
3. **State Persistence**: Ensure state changes persist across interactions
4. **Theme Switching**: Test all controls in both light and dark modes
5. **Asset Loading**: Verify all local images load correctly

## Common Pitfalls

1. **Forgetting page.update()**: UI won't refresh without it
2. **Missing nonlocal**: State variables won't update in nested functions
3. **Incorrect asset paths**: Must use leading slash and configure assets_dir
4. **Deprecated APIs**: Check version-specific documentation
5. **Radio without RadioGroup**: Radio buttons must be wrapped in RadioGroup

## Debugging Tips

1. Use Python's print statements to debug state changes
2. Check browser console for Flet-specific errors (when running as web app)
3. Verify asset paths are correct and files exist
4. Ensure all event handlers have proper signatures: `def handler(e)`
5. Test controls incrementally - add one at a time

## Performance Considerations

1. **Minimize page.update() calls**: Batch state changes when possible
2. **Optimize images**: Keep asset file sizes reasonable
3. **Lazy loading**: Consider loading heavy controls only when needed
4. **Event debouncing**: For rapid events (like sliders), consider debouncing

## Future Enhancements

Potential areas for expansion:
- Add more control examples (Canvas, Charts, Maps)
- Implement form validation demonstrations
- Add drag-and-drop examples
- Create animations showcase
- Demonstrate routing and multi-page apps

## Resources

- [Flet Documentation](https://flet.dev/docs)
- [Flet GitHub](https://github.com/flet-dev/flet)
- [Flutter Widget Catalog](https://docs.flutter.dev/ui/widgets)
- [Material Design Guidelines](https://m3.material.io/)

## Agent Best Practices

When working with this codebase:

1. **Respect the uv setup**: NEVER use `pip`, `poetry`, or other dependency tools. Use `uv` exclusively.
2. **Read before modifying**: Always read the current state of files
3. **Test incrementally**: Make small changes and test frequently with `uv run main.py`
4. **Follow patterns**: Use existing code patterns for consistency
5. **Document changes**: Update this file when adding new patterns
6. **Check API versions**: Always verify API compatibility with Flet 0.80.0
7. **Keep it clean**: Do not introduce unnecessary dependencies or tools
