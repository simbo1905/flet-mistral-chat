# Flet Controls Showcase

A comprehensive demonstration application showcasing the interactive UI controls available in Flet 0.80.0, a Python framework for building beautiful cross-platform applications.

## Quick Start

```bash
uv sync
uv run main.py
```

## Features

This showcase demonstrates a wide variety of Flet controls organized into expandable panels:

### Basic Controls
- Text formatting (normal, italic, bold, colored)
- Text input fields (single-line, password, multiline)
- Buttons (Button, FilledButton, OutlinedButton, TextButton)
- **Interactive heart icon** - Click to toggle between grey and red

### Input Controls
- Checkboxes and switches
- **Radio button groups** - Properly wrapped RadioGroup example
- Sliders with value labels
- Progress indicators (bar and ring/spinner)
- Dropdown menus

### Display Controls
- Icons in various colors
- Images with border radius
- Chips with click handlers
- Badges on icons
- Tooltips on hover

### Layout Controls
- Containers with borders and styling
- Row and Column layouts
- **Interactive Card** - Action buttons display feedback when clicked
- Gradient and shadow effects

### Lists & Grids
- **Interactive ListTiles** - Click to switch between animal images (Kitten, Puppy, Duckling)
- Data tables with sample data
- Grid view with responsive layout

### Navigation
- Navigation bar with multiple destinations
- Tabs with TabBar and TabBarView structure

### Dialogs & Overlays
- Alert dialogs
- SnackBar notifications
- Banners with actions

## Installation

### Prerequisites
- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd fal.ia.flet
```

2. Install dependencies:
```bash
uv sync
```

3. Run the application:
```bash
uv run main.py
```

The application will open in a desktop window.

## Project Structure

```
.
├── assets/          # Local image assets
│   ├── kitten.jpg
│   ├── puppy.jpg
│   └── duckling.jpg
├── main.py          # Main application code
├── pyproject.toml   # Project configuration
├── AGENTS.md        # Agent development guide
├── CLAUDE.md        # Symlink to AGENTS.md
└── README.md        # This file
```

## Interactive Features

### Heart Button
Located in the Basic Controls section. Click the heart icon to toggle it between grey (unliked) and red (liked).

### Card Actions
In the Layout Controls section, the card has two action buttons. Click either "Action 1" or "Action 2" to see a message appear in the card.

### Animal Image Selector
The Lists & Grids section features three clickable list items:
- **Kitten** - Shows a cute kitten image
- **Puppy** - Shows a cute puppy image
- **Duckling** - Shows a cute duckling image

Click any item to update the image displayed on the right side of the panel.

### Theme Toggle
Click the theme icon in the top-right corner to switch between light and dark modes.

## Technology Stack

- **Framework**: [Flet](https://flet.dev) 0.80.0
- **Language**: Python 3.12+
- **UI Engine**: Flutter
- **Package Manager**: uv

## Key Flet 0.80.0 Patterns

This showcase demonstrates modern Flet patterns including:

- Proper RadioGroup usage for radio buttons
- TabBar/TabBarView structure for tabs
- Badge as a property on controls
- Tooltip as a property on controls
- Asset management with local files
- State management with closures
- Event handlers for interactivity

## Development

### Running in Development Mode

```bash
uv run main.py
```

### Adding New Controls

1. Locate the appropriate ExpansionPanel in `main.py`
2. Add your control with proper configuration
3. For interactive controls, add event handlers
4. Call `page.update()` to refresh the UI

See `AGENTS.md` for detailed development guidelines.

## Browser Support

When run as a web app, Flet supports:
- Chrome/Edge (recommended)
- Firefox
- Safari

## License

This project is provided as-is for demonstration and educational purposes.

## Acknowledgments

Built with [Flet](https://flet.dev), a framework for building cross-platform apps in Python.
