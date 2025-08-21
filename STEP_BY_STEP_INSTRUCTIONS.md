# Step-by-Step Google Slides Update

This guide will help you update Google Slides step by step, checking results after each action.

## Setup Tools

I've created several small, focused tools to help with the update:

- `mouse_position.py` - Shows current mouse position in real-time
- `mouse_move.py` - Moves mouse to specific coordinates
- `mouse_click.py` - Clicks at specific coordinates
- `key_press.py` - Presses keyboard keys
- `type_text.py` - Types text at the current cursor position
- `open_browser.py` - Opens a browser and navigates to a URL

## Update Process

### Step 1: Open Google Slides

First, open Google Slides in your browser:

```bash
python open_browser.py https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit
```

Wait for the presentation to load and ensure you're in edit mode.

### Step 2: Find Coordinates

Use the mouse position tracker to find the coordinates of slide elements:

```bash
python mouse_position.py
```

Move your mouse over the title, subtitle, and content areas to see their coordinates.
Write down these coordinates for later use.

### Step 3: Navigate to First Slide

Press the Home key to navigate to the first slide:

```bash
python key_press.py home
```

### Step 4: Update Slide Title

1. Move to the title area:
   ```bash
   python mouse_move.py [TITLE_X] [TITLE_Y]
   ```
   Replace `[TITLE_X]` and `[TITLE_Y]` with the coordinates you found.

2. Double-click to select the title:
   ```bash
   python mouse_click.py [TITLE_X] [TITLE_Y] 2
   ```

3. Select all existing text:
   ```bash
   python key_press.py cmd a
   ```

4. Type the new title:
   ```bash
   python type_text.py "NoLock Social"
   ```

5. Press Escape to finish editing:
   ```bash
   python key_press.py esc
   ```

### Step 5: Update Slide Subtitle

1. Move to the subtitle area:
   ```bash
   python mouse_move.py [SUBTITLE_X] [SUBTITLE_Y]
   ```

2. Double-click to select the subtitle:
   ```bash
   python mouse_click.py [SUBTITLE_X] [SUBTITLE_Y] 2
   ```

3. Select all existing text:
   ```bash
   python key_press.py cmd a
   ```

4. Type the new subtitle:
   ```bash
   python type_text.py "Rebuild Trust in the Digital Space"
   ```

5. Press Escape to finish editing:
   ```bash
   python key_press.py esc
   ```

### Step 6: Update Slide Content

1. Move to the content area:
   ```bash
   python mouse_move.py [CONTENT_X] [CONTENT_Y]
   ```

2. Double-click to select the content:
   ```bash
   python mouse_click.py [CONTENT_X] [CONTENT_Y] 2
   ```

3. Select all existing text:
   ```bash
   python key_press.py cmd a
   ```

4. For longer content, save it to a file first:
   ```bash
   echo "A next-generation platform rebuilding digital trust with decentralized identity in a $12B market." > content.txt
   python type_text.py --file content.txt
   ```

5. Press Escape to finish editing:
   ```bash
   python key_press.py esc
   ```

### Step 7: Navigate to Next Slide

Press the Right Arrow key to move to the next slide:

```bash
python key_press.py right
```

Repeat steps 4-7 for each slide you want to update.

## Tips

- Always check the result after each action to make sure it worked as expected
- If an action doesn't work, try adjusting the coordinates or timing
- Use `Ctrl+C` to abort any script if needed
- If the mouse moves to a corner, it's because PyAutoGUI's failsafe was triggered