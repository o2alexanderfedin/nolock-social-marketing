#!/usr/bin/env python3

import os
import re
import time
import webbrowser
import pyautogui
import sys

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
DELAY_BETWEEN_ACTIONS = 1  # seconds to wait between actions
PAUSE_AFTER_SLIDE = 3  # seconds to pause after completing a slide

# Set PyAutoGUI settings
pyautogui.PAUSE = 0.5  # Pause 0.5 seconds between PyAutoGUI commands
pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort

def print_status(message):
    """Print status messages with a consistent format."""
    print(f"[STATUS] {message}")

def load_slide_data(slide_number):
    """Load slide data from the exported markdown file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_number:02d}_export.md")
    
    if not os.path.exists(file_path):
        print(f"Warning: Could not find {file_path}")
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract bullet points section
    bullet_points = ""
    if "## Bullet Points" in content:
        bp_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if bp_match:
            bullet_points = bp_match.group(1).strip()
    
    # Extract quotes
    quotes = ""
    if "## Quotes" in content:
        q_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if q_match:
            quotes = q_match.group(1).strip()
    
    # Extract sources
    sources = ""
    if "## Sources" in content:
        s_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if s_match:
            sources = s_match.group(1).strip()
    
    # Combine all content for the main slide content
    main_content = ""
    if summary_match:
        main_content = summary_match.group(1).strip() + "\n\n"
    if bullet_points:
        main_content += bullet_points + "\n\n"
    if quotes:
        main_content += quotes + "\n\n"
    if sources:
        main_content += sources
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "main_content": main_content.strip()
    }

def wait_and_click(x, y, clicks=1, description=""):
    """Wait, then click at specified coordinates."""
    print_status(f"Clicking {description} at ({x}, {y})")
    time.sleep(DELAY_BETWEEN_ACTIONS)
    pyautogui.click(x=x, y=y, clicks=clicks)
    time.sleep(DELAY_BETWEEN_ACTIONS)

def select_all_and_replace(text):
    """Select all text and replace it with new text."""
    # Select all text
    print_status("Selecting all text")
    pyautogui.hotkey('command', 'a')  # Use 'ctrl' instead of 'command' on Windows
    time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Type new text
    print_status(f"Typing new text: {text[:30]}..." if len(text) > 30 else f"Typing new text: {text}")
    pyautogui.typewrite(text)
    time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Press escape to finish editing
    pyautogui.press('escape')
    time.sleep(DELAY_BETWEEN_ACTIONS)

def get_screen_info():
    """Get and print screen information to help with coordinates."""
    screen_width, screen_height = pyautogui.size()
    mouse_x, mouse_y = pyautogui.position()
    
    print(f"Screen size: {screen_width}x{screen_height}")
    print(f"Current mouse position: ({mouse_x}, {mouse_y})")
    return screen_width, screen_height

def interactive_coordinate_selection(element_name):
    """Allow the user to interactively select coordinates for an element."""
    print(f"\n=== COORDINATE SELECTION FOR {element_name.upper()} ===")
    print("Move your mouse to the position where you want to click and press Enter")
    print("(You have 5 seconds after pressing Enter to position the mouse)")
    
    input("Press Enter when ready...")
    print("Pausing for 5 seconds - move mouse to desired position")
    time.sleep(5)
    
    x, y = pyautogui.position()
    print(f"Selected coordinates for {element_name}: ({x}, {y})")
    return x, y

def setup_coordinates():
    """Set up coordinates for various elements interactively."""
    print("\n=== COORDINATE SETUP ===")
    print("We need to set up coordinates for various elements on the slide.")
    print("Make sure the Google Slides presentation is open and visible.")
    
    # Get screen info
    get_screen_info()
    
    # Set up coordinates for each element
    title_x, title_y = interactive_coordinate_selection("slide title")
    subtitle_x, subtitle_y = interactive_coordinate_selection("slide subtitle")
    content_x, content_y = interactive_coordinate_selection("main content")
    next_slide_x, next_slide_y = interactive_coordinate_selection("next slide button")
    
    coords = {
        "title": (title_x, title_y),
        "subtitle": (subtitle_x, subtitle_y),
        "content": (content_x, content_y),
        "next_slide": (next_slide_x, next_slide_y)
    }
    
    # Save coordinates to a file for future use
    with open("slide_coordinates.json", "w") as f:
        import json
        json.dump(coords, f)
    
    print("Coordinates have been saved to slide_coordinates.json")
    return coords

def load_coordinates():
    """Load coordinates from file or use defaults."""
    coord_file = "slide_coordinates.json"
    
    if os.path.exists(coord_file):
        try:
            with open(coord_file, "r") as f:
                import json
                coords = json.load(f)
            print("Loaded coordinates from file.")
            return coords
        except Exception as e:
            print(f"Error loading coordinates: {e}")
    
    # Use default coordinates for a 1920x1080 screen
    # These are estimates and may need to be adjusted for different screen sizes
    print("Using default coordinates for a 1920x1080 screen")
    screen_width, screen_height = pyautogui.size()
    scale_x = screen_width / 1920
    scale_y = screen_height / 1080
    
    default_coords = {
        "title": (int(960 * scale_x), int(250 * scale_y)),
        "subtitle": (int(960 * scale_x), int(350 * scale_y)),
        "content": (int(960 * scale_x), int(540 * scale_y)),
        "next_slide": (int(1800 * scale_x), int(540 * scale_y))
    }
    
    print(f"Default coordinates (scaled to your screen {screen_width}x{screen_height}):")
    for key, value in default_coords.items():
        print(f"  {key}: {value}")
    
    # Save these default coordinates for future use
    with open(coord_file, "w") as f:
        import json
        json.dump(default_coords, f)
    
    return default_coords

def update_slide(slide_data, coords):
    """Update a slide with the given data using PyAutoGUI."""
    # Click outside first to ensure no element is selected
    print_status("Clicking outside to ensure no element is selected")
    pyautogui.click(10, 10)
    time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Update title
    if slide_data["title"]:
        print_status(f"Updating title: {slide_data['title']}")
        wait_and_click(coords["title"][0], coords["title"][1], clicks=2, description="title")
        select_all_and_replace(slide_data["title"])
        
        # Click outside to deselect
        pyautogui.click(10, 10)
        time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Update subtitle
    if slide_data["subtitle"]:
        print_status(f"Updating subtitle: {slide_data['subtitle']}")
        wait_and_click(coords["subtitle"][0], coords["subtitle"][1], clicks=2, description="subtitle")
        select_all_and_replace(slide_data["subtitle"])
        
        # Click outside to deselect
        pyautogui.click(10, 10)
        time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Update main content
    if slide_data["main_content"]:
        print_status("Updating main content")
        wait_and_click(coords["content"][0], coords["content"][1], clicks=2, description="main content")
        select_all_and_replace(slide_data["main_content"])
        
        # Click outside to deselect
        pyautogui.click(10, 10)
        time.sleep(DELAY_BETWEEN_ACTIONS)
    
    # Pause to let user see the changes
    print_status(f"Pausing for {PAUSE_AFTER_SLIDE} seconds...")
    time.sleep(PAUSE_AFTER_SLIDE)

def go_to_next_slide(coords, use_keyboard=True):
    """Navigate to the next slide using keyboard arrow or clicking next slide button."""
    print_status("Going to next slide")
    
    if use_keyboard:
        # Use right arrow key to advance slides
        print_status("Using keyboard right arrow to advance")
        pyautogui.press('right')
    else:
        # Use mouse click on the next slide button
        wait_and_click(coords["next_slide"][0], coords["next_slide"][1], description="next slide button")
    
    time.sleep(DELAY_BETWEEN_ACTIONS * 2)  # Extra delay for slide transition

def navigate_to_first_slide():
    """Navigate to the first slide using keyboard shortcut."""
    print_status("Navigating to first slide (Home key)")
    pyautogui.press('home')
    time.sleep(DELAY_BETWEEN_ACTIONS * 2)

def navigate_to_slide(slide_num, coords):
    """Navigate to a specific slide."""
    # First go to slide 1
    navigate_to_first_slide()
    
    # Then go forward to desired slide
    if slide_num > 1:
        print_status(f"Moving to slide {slide_num}")
        for _ in range(slide_num - 1):
            go_to_next_slide(coords)
            time.sleep(DELAY_BETWEEN_ACTIONS)  # Extra wait between slide changes

def update_all_slides(start_slide, end_slide, coords):
    """Update a range of slides."""
    # Navigate to the first slide in the range
    navigate_to_slide(start_slide, coords)
    
    # Process each slide
    for slide_num in range(start_slide, end_slide + 1):
        print_status(f"\n=== UPDATING SLIDE {slide_num} ===")
        
        # Load slide data
        slide_data = load_slide_data(slide_num)
        if not slide_data:
            print(f"Skipping slide {slide_num} - no data found")
            if slide_num < end_slide:
                go_to_next_slide(coords)
            continue
        
        # Update the current slide
        update_slide(slide_data, coords)
        
        # Ask for confirmation before continuing to next slide
        print_status(f"Slide {slide_num} update completed. Waiting 3 seconds before continuing...")
        time.sleep(3)
        
        # Navigate to the next slide if not the last one
        if slide_num < end_slide:
            go_to_next_slide(coords)

def show_important_instructions():
    """Display important instructions for the user."""
    print("\n" + "="*70)
    print("IMPORTANT INSTRUCTIONS".center(70))
    print("="*70)
    
    print("""
1. Make sure Google Slides is already open and visible in the browser
2. The presentation should be in edit mode (not presentation mode)
3. Position the browser window so all slide elements are visible
4. SAFETY: Move mouse to the upper-left corner of the screen to abort
5. CONTROL: This script will use keyboard shortcuts to navigate slides
6. EXPECT: The script will:
   - Start from the first slide (or specified start slide)
   - Update title, subtitle, and content of each slide
   - Automatically advance to the next slide
7. WARNING: Keep hands off keyboard and mouse once script starts running
8. Slide coordinates are estimates - adjust if needed in slide_coordinates.json
    """)
    
    print("="*70 + "\n")

def main():
    """Main function to update Google Slides."""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Update Google Slides with new content using PyAutoGUI')
    parser.add_argument('--start', type=int, default=1, help='Starting slide number (default: 1)')
    parser.add_argument('--end', type=int, default=21, help='Ending slide number (default: 21)')
    parser.add_argument('--setup', action='store_true', help='Force setup of coordinates')
    parser.add_argument('--no-browser', action='store_true', help='Skip opening the browser (assume it is already open)')
    parser.add_argument('--keyboard-nav', action='store_true', help='Use keyboard navigation instead of clicking (default: True)')
    parser.add_argument('--single-slide', type=int, help='Update only a single slide number')
    parser.add_argument('--delay', type=float, default=1.0, help='Multiplier for delay between actions (default: 1.0)')
    args = parser.parse_args()
    
    # Apply delay multiplier
    global DELAY_BETWEEN_ACTIONS, PAUSE_AFTER_SLIDE
    DELAY_BETWEEN_ACTIONS *= args.delay
    PAUSE_AFTER_SLIDE *= args.delay
    
    # Handle single slide mode
    if args.single_slide:
        args.start = args.single_slide
        args.end = args.single_slide
    
    # Check if export directory exists
    if not os.path.exists(EXPORT_DIR):
        print(f"ERROR: Export directory not found: {EXPORT_DIR}")
        return
    
    # Show important instructions
    show_important_instructions()
    
    # Open Google Slides (unless skipped)
    if not args.no_browser:
        print_status(f"Opening Google Slides: {SLIDES_URL}")
        webbrowser.open(SLIDES_URL)
        
        # Wait for the browser to open
        print_status("Waiting 5 seconds for browser to open...")
        time.sleep(5)
    else:
        print_status("Skipping browser launch - assuming Google Slides is already open")
    
    # Load coordinates (using defaults if needed)
    coords = load_coordinates()
    
    # Show confirmation and countdown
    print_status(f"\nReady to update slides {args.start} to {args.end}")
    print_status(f"Using {'keyboard' if args.keyboard_nav else 'mouse'} navigation")
    print_status(f"Delay factor: {args.delay}x")
    print_status("Starting in 5 seconds... (Move mouse to upper-left corner to abort)")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    try:
        # Update slides
        update_all_slides(args.start, args.end, coords)
        print_status("\nSlide updates completed!")
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Script aborted. Try running with --delay 2.0 for slower execution if timing was an issue.")

if __name__ == "__main__":
    main()