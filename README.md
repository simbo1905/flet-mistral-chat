# Flet Controls Showcase

A comprehensive demonstration application showcasing the interactive UI controls available in Flet 0.80.0, a Python framework for building beautiful cross-platform applications.

## Quick Start

### Before Running

1. **Check Python version**: Requires Python 3.12+
   ```bash
   python3 --version
   ```

2. **Install uv**: If not already installed
   ```bash
   pip install uv
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

### Run the Application

```bash
uv run main.py
```

### Run the Original Demo

```bash
uv run demo.py
```

### Check Code Quality

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .
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
cd flet-mistral-chat
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

### Verify Setup

```bash
# Check Python version
python3 --version

# Check uv version
uv --version

# Check Flet installation
python3 -c "import flet; print(f'Flet version: {flet.__version__}')"
```

## Project Structure

```
.
├── assets/          # Local image assets
│   ├── kitten.jpg
│   ├── puppy.jpg
│   └── duckling.jpg
├── demo.py          # Original Flet Controls Showcase
├── main.py          # TUUI-inspired UI (Blender Preferences style)
├── pyproject.toml   # Project configuration and dependencies
├── AGENTS.md        # Development guidelines and conventions
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

## Troubleshooting

### Common Issues

**Issue: `uv` command not found**
```bash
pip install uv
```

**Issue: Python version too old**
```bash
# Install Python 3.12+ from python.org
# Or use pyenv:
pyenv install 3.12.0
pyenv global 3.12.0
```

**Issue: Flet not installed**
```bash
uv sync
```

**Issue: Application not starting**
```bash
# Check for errors
uv run main.py 2>&1

# Try running the demo instead
uv run demo.py
```

### Code Quality Checks

```bash
# Format all code
uv run ruff format .

# Check for linting errors
uv run ruff check .

# Fix automatically fixable issues
uv run ruff check . --fix
```

## License

This project is provided as-is for demonstration and educational purposes.

## Acknowledgments

Built with [Flet](https://flet.dev), a framework for building cross-platform apps in Python.
