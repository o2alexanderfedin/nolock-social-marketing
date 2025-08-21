# NoLock Social Slides Update Instructions

This document explains how to use the scripts for updating Google Slides with content from the NoLock Social investor pitch deck.

## Prerequisites

- Python 3.6+ installed
- PyAutoGUI installed (`pip install pyautogui`)
- Web browser (Chrome, Firefox, or Safari)
- Google Slides presentation open and ready: [Presentation Link](https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit)

## Available Scripts

### 1. Update a Single Slide

```bash
python update_one_slide.py [slide_number]
```

This script allows you to update a single slide. If you don't provide a slide number, it will prompt you to enter one interactively.

**Examples:**
```bash
python update_one_slide.py 5     # Update slide 5
python update_one_slide.py       # Interactive mode
```

### 2. Update Multiple Slides

```bash
python update_all_slides.py
```

This script will guide you through updating a range of slides. It will ask for:
- Starting slide number
- Ending slide number
- Delay factor (higher value = slower updates, useful if you encounter timing issues)

### 3. Advanced Usage

For more advanced options, you can use the main script directly:

```bash
python update_slides_pyautogui.py [options]
```

**Options:**
- `--start N`: Starting slide number (default: 1)
- `--end N`: Ending slide number (default: 21)
- `--no-browser`: Skip opening the browser (if it's already open)
- `--keyboard-nav`: Use keyboard navigation (arrow keys) instead of mouse clicks
- `--single-slide N`: Update only a single slide
- `--delay F`: Multiplier for delay between actions (default: 1.0)

## Important Instructions

1. Make sure Google Slides is already open and visible in the browser
2. The presentation should be in edit mode (not presentation mode)
3. Position the browser window so all slide elements are visible
4. SAFETY: Move mouse to the upper-left corner of the screen to abort
5. Keep hands off keyboard and mouse once the script starts running

## Troubleshooting

If the script is clicking in the wrong places:
1. The script uses default coordinates scaled to your screen size
2. You can adjust them in the `slide_coordinates.json` file that gets created
3. Try running with a higher delay factor (`--delay 2.0`) if timing issues occur

## Content Sources

The slide content comes from the `/slides_export/` directory, which contains formatted Markdown files for each slide.