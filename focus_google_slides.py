#!/usr/bin/env python3

"""
This script helps to focus and position the Google Slides window
before attempting any automation.

Instructions:
1. Make sure Google Slides is open in your browser
2. Run this script
3. Follow the interactive prompts to focus and position the window
"""

import pyautogui
import time
import sys

def print_status(message):
    """Print status messages with a consistent format."""
    print(f"[STATUS] {message}")

def wait_for_input(message="Press Enter to continue..."):
    """Wait for user input or timeout if in non-interactive environment."""
    try:
        return input(message)
    except EOFError:
        print("Waiting 5 seconds before continuing...")
        time.sleep(5)
        return ""

def main():
    print("\n" + "="*70)
    print("GOOGLE SLIDES WINDOW FOCUS AND POSITIONING".center(70))
    print("="*70)
    
    print("""
IMPORTANT: This script will help you position your Google Slides window
before attempting any automation.

Before proceeding:
1. Open Google Slides in your browser
2. Make sure the presentation is in edit mode (not presentation mode)
3. Position your browser window so it takes up most of the screen
4. Click INSIDE the Google Slides editor area to ensure it has focus
""")
    
    wait_for_input("\nPress Enter when your Google Slides window is ready...")
    
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    print_status(f"Screen dimensions: {screen_width}x{screen_height}")
    
    # Get current mouse position
    mouse_x, mouse_y = pyautogui.position()
    print_status(f"Current mouse position: ({mouse_x}, {mouse_y})")
    
    # Ask if this position is inside Google Slides
    print("\nIS YOUR MOUSE CURRENTLY INSIDE THE GOOGLE SLIDES EDITING AREA?")
    response = wait_for_input("Enter 'y' if yes, or 'n' if no: ").lower()
    
    if response == 'y':
        print_status("Great! Let's use this position as a reference.")
        ref_x, ref_y = mouse_x, mouse_y
    else:
        print_status("Please move your mouse to the center of the Google Slides editing area.")
        print_status("You have 5 seconds to position your mouse...")
        time.sleep(5)
        ref_x, ref_y = pyautogui.position()
        print_status(f"Reference position set to: ({ref_x}, {ref_y})")
    
    # Click to ensure focus
    print_status("Clicking once to ensure Google Slides has focus...")
    pyautogui.click(ref_x, ref_y)
    time.sleep(1)
    
    # Press Escape to cancel any potential selection
    print_status("Pressing Escape to cancel any active selections...")
    pyautogui.press('escape')
    time.sleep(1)
    
    # Go to first slide
    print_status("Pressing Home key to go to first slide...")
    pyautogui.press('home')
    time.sleep(2)
    
    print("\n" + "="*70)
    print("FOCUS AND POSITIONING COMPLETE".center(70))
    print("="*70)
    
    print("""
Now your Google Slides window should be:
1. Properly focused
2. On the first slide
3. Ready for automation

You can now run the update script.
""")

if __name__ == "__main__":
    main()