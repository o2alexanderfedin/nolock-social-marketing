# NoLock Social Google Slides Update Tools

This document explains the various tools available for updating the NoLock Social Google Slides presentation with content from markdown files.

## Quick Start

The easiest way to start is to use the launcher script, which will guide you through the update process:

```bash
python update_slides_launcher.py
```

This launcher will detect available dependencies and present appropriate options for updating slides.

## Available Tools

### Core Tools

| Script | Description | Dependencies |
|--------|-------------|--------------|
| `update_slides_launcher.py` | Central entry point for all update tools | None |
| `display_slides_auto.py` | Display slide content for reference | None |
| `update_slides_interactive_improved.py` | Interactive guidance for manual updates | None |
| `simple_update_slides.py` | Semi-automated single slide updates | PyAutoGUI |
| `update_all_slides.py` | Fully automated multi-slide updates | PyAutoGUI |

### Utility Tools

| Script | Description | Dependencies |
|--------|-------------|--------------|
| `mouse_position.py` | Show mouse coordinates in real-time | PyAutoGUI |
| `mouse_click.py` | Click at specified coordinates | PyAutoGUI |
| `mouse_move.py` | Move mouse to specified coordinates | PyAutoGUI |
| `key_press.py` | Send keyboard key presses | PyAutoGUI |
| `type_text.py` | Type text at current cursor position | PyAutoGUI |
| `open_browser.py` | Open browser and navigate to URL | None |
| `get_coordinates.py` | Calibrate click positions for slides | PyAutoGUI |

## Update Methods

### 1. Manual Update with Interactive Display

This method displays slide content in the terminal while you manually update the Google Slides presentation:

```bash
python display_slides_auto.py
```

**Features:**
- Shows slide content in the terminal
- Automatically advances to next slide after a set time
- No automation dependencies required

### 2. Guided Manual Update

This method provides step-by-step instructions for manually updating each slide:

```bash
python update_slides_interactive_improved.py [slide_number]
```

**Features:**
- Detailed instructions for each slide element
- Keyboard navigation between slides
- No automation dependencies required

### 3. Semi-Automated Single Slide Update

This method uses PyAutoGUI to help update a single slide:

```bash
python simple_update_slides.py [slide_number]
```

**Features:**
- Update a single slide with automation assistance
- Confirms each step before proceeding
- Requires PyAutoGUI library

### 4. Fully Automated Multiple Slide Update

This method automatically updates a range of slides:

```bash
python update_all_slides.py
```

**Features:**
- Update multiple slides automatically
- Interactive configuration of start/end slides and delay
- Requires PyAutoGUI library

## Step-By-Step Update Process

For a more granular step-by-step update process, see the detailed instructions in:

- `STEP_BY_STEP_INSTRUCTIONS.md` - Detailed manual steps
- `SLIDES_UPDATE_INSTRUCTIONS.md` - General update instructions

## Utility Usage Examples

### Get Mouse Position

```bash
python mouse_position.py
```

### Click at Coordinates

```bash
python mouse_click.py 500 500     # Single click
python mouse_click.py 500 500 2   # Double click
```

### Press Keys

```bash
python key_press.py enter     # Press Enter key
python key_press.py cmd a     # Press Command+A (select all)
```

### Type Text

```bash
python type_text.py "Hello, world!"
```

## Requirements

- Python 3.6+
- For automated methods: PyAutoGUI (`pip install pyautogui`)
- Internet connection to access Google Slides
- Access to NoLock Social Google Slides presentation

## Troubleshooting

- **Clicking Wrong Locations**: Run `get_coordinates.py` to recalibrate click positions
- **Text Not Updating**: Increase delay factor for slower, more reliable updates
- **Script Crashes**: Move mouse to upper-left corner to abort any automated script
- **PyAutoGUI Not Available**: Install it with `pip install pyautogui`

## Safety Tips

- Always save your presentation before running automated updates
- Keep hands off mouse and keyboard during automated scripts
- Move mouse to upper-left corner to abort automation
- Start with a single slide to test before updating multiple slides