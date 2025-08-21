#!/usr/bin/env python3

import pyautogui
import time
import json
import os
import sys

# Settings
PAUSE_BETWEEN_STEPS = 5  # seconds to wait between steps
HIGHLIGHT_DURATION = 0.5  # seconds to highlight position

# Configure PyAutoGUI
pyautogui.PAUSE = 0.5  # pause between PyAutoGUI commands
pyautogui.FAILSAFE = True  # move to corner to abort

def print_header(message):
    """Print a header message."""
    print("\n" + "=" * 70)
    print(message.center(70))
    print("=" * 70)

def print_status(message):
    """Print status message."""
    print(f"[STATUS] {message}")

def wait_for_continue():
    """Wait for user to press Enter to continue."""
    try:
        input("\nPress Enter to continue to next step (or Ctrl+C to abort)...")
    except EOFError:
        # If we can't get input (e.g., when run in a tool), just wait
        print("Waiting 5 seconds before continuing...")
        time.sleep(5)

def highlight_position(x, y, duration=HIGHLIGHT_DURATION):
    """Move mouse to position quickly to highlight it, then return."""
    original_x, original_y = pyautogui.position()
    pyautogui.moveTo(x, y, duration=duration)
    time.sleep(duration)
    return original_x, original_y

def load_coordinates():
    """Load coordinates from file or use defaults."""
    coord_file = "slide_coordinates.json"
    
    if os.path.exists(coord_file):
        try:
            with open(coord_file, "r") as f:
                coords = json.load(f)
            print_status("Loaded coordinates from file:")
            for key, value in coords.items():
                print(f"  {key}: {value}")
            return coords
        except Exception as e:
            print(f"Error loading coordinates: {e}")
    
    # Default coordinates
    screen_width, screen_height = pyautogui.size()
    default_coords = {
        "title": (screen_width // 2, screen_height // 4),
        "subtitle": (screen_width // 2, screen_height // 3),
        "content": (screen_width // 2, screen_height // 2),
        "next_slide": (screen_width - 100, screen_height // 2)
    }
    
    print_status("Using default coordinates")
    return default_coords

def navigate_to_slide(slide_num):
    """Navigate to a specific slide with visual feedback."""
    print_header(f"NAVIGATING TO SLIDE {slide_num}")
    
    # Go to first slide with Home key
    print_status("Pressing HOME key to go to first slide")
    pyautogui.press('home')
    print_status("Waiting to verify we're on slide 1...")
    time.sleep(PAUSE_BETWEEN_STEPS)
    
    # Move to desired slide if not slide 1
    if slide_num > 1:
        print_status(f"Moving to slide {slide_num} by pressing RIGHT arrow {slide_num-1} times")
        for i in range(slide_num - 1):
            print_status(f"  Pressing RIGHT arrow ({i+1}/{slide_num-1})")
            pyautogui.press('right')
            time.sleep(2)  # Wait between presses
        
        print_status(f"Should now be on slide {slide_num}")
        time.sleep(PAUSE_BETWEEN_STEPS)

def click_and_verify(x, y, element_name, double_click=False):
    """Click at position with visual verification."""
    print_header(f"CLICKING ON {element_name.upper()}")
    
    # Show where we're about to click
    print_status(f"About to click {element_name} at position ({x}, {y})")
    print_status("Moving mouse to highlight position...")
    orig_x, orig_y = highlight_position(x, y)
    time.sleep(1)
    
    # Perform the click
    clicks = 2 if double_click else 1
    print_status(f"Performing {'double' if double_click else 'single'} click on {element_name}")
    pyautogui.click(x=x, y=y, clicks=clicks)
    
    # Wait for verification
    print_status(f"Click complete. Observe the result - did it select the {element_name}?")
    time.sleep(PAUSE_BETWEEN_STEPS)
    
    return True

def click_outside():
    """Click outside any elements to deselect."""
    print_header("CLICKING OUTSIDE TO DESELECT")
    
    # Click in top-left corner to deselect
    print_status("Clicking in top-left corner to deselect any elements")
    pyautogui.click(10, 10)
    time.sleep(2)

def test_slide_elements(slide_num, coords):
    """Test clicking on each element of a slide with visual feedback."""
    # Navigate to slide
    navigate_to_slide(slide_num)
    
    # Click outside first
    click_outside()
    
    # Test each element
    elements = [
        ("title", coords["title"][0], coords["title"][1], True),
        ("subtitle", coords["subtitle"][0], coords["subtitle"][1], True),
        ("content", coords["content"][0], coords["content"][1], True)
    ]
    
    for name, x, y, double_click in elements:
        success = click_and_verify(x, y, name, double_click)
        
        if success:
            print_status(f"✅ Successfully clicked on {name}")
        else:
            print_status(f"❌ Failed to click on {name} - adjust coordinates")
        
        # Deselect after each element
        click_outside()

def main():
    """Main function to test clicking on slide elements with visual feedback."""
    print_header("VISUAL CLICK TEST")
    print("This script will help you verify the click positions for slide elements.")
    print("Watch carefully where the mouse clicks and what gets selected.")
    
    # Get slide number
    slide_num = 1
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        slide_num = int(sys.argv[1])
        if slide_num < 1 or slide_num > 21:
            print("Error: Slide number must be between 1 and 21. Using slide 1.")
            slide_num = 1
    
    print_status(f"Will test clicking on elements of slide {slide_num}")
    print_status("Starting in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # Load coordinates
    coords = load_coordinates()
    
    # Test clicking on slide elements
    test_slide_elements(slide_num, coords)
    
    print_header("TEST COMPLETE")
    print("Check if all elements were correctly selected when clicked.")
    print("If not, you may need to adjust the coordinates in slide_coordinates.json.")

if __name__ == "__main__":
    main()