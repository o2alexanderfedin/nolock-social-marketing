#!/usr/bin/env python3

"""
Manual coordinate capture tool - use this to get the exact coordinates
for slide elements by positioning your mouse and pressing Enter.

This script does not perform any mouse movements, only captures positions.
"""

import pyautogui
import time
import json
import os

def print_header(message):
    """Print a header message."""
    print("\n" + "=" * 70)
    print(message.center(70))
    print("=" * 70)

def get_mouse_position():
    """Get and return the current mouse position."""
    # Wait a moment for mouse to be positioned
    time.sleep(0.5)
    
    # Get position
    x, y = pyautogui.position()
    return x, y

def capture_coordinates():
    """Capture coordinates for slide elements."""
    coords = {}
    
    elements = [
        "title",
        "subtitle", 
        "content",
        "next_slide"
    ]
    
    print_header("MANUAL COORDINATE CAPTURE")
    print("""
INSTRUCTIONS:
1. This script will ask you to position your mouse over each slide element
2. When prompted, position the mouse where you want to click for that element
3. The script will capture the current mouse position after each countdown
4. DO NOT CLICK - just position the mouse and wait for the countdown
5. Keep your Google Slides window in focus during this process
""")
    
    # Give user time to read instructions
    print("Starting in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # Capture positions for each element
    for element in elements:
        print_header(f"CAPTURING {element.upper()} POSITION")
        print(f"Position your mouse over the {element} element in the slide.")
        print("DO NOT CLICK - just position the mouse and watch the countdown.")
        
        # Countdown
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        
        # Get position
        x, y = get_mouse_position()
        coords[element] = [x, y]
        print(f"Captured position for {element}: ({x}, {y})")
    
    return coords

def save_coordinates(coords):
    """Save coordinates to a file."""
    # Save to file
    with open("slide_coordinates.json", "w") as f:
        json.dump(coords, f, indent=2)
    
    print_header("COORDINATES SAVED")
    print("Coordinates have been saved to slide_coordinates.json:")
    for element, pos in coords.items():
        print(f"  {element}: ({pos[0]}, {pos[1]})")

def main():
    print_header("GOOGLE SLIDES COORDINATE CAPTURE")
    print("""
This tool helps you capture the exact coordinates of slide elements for automation.

BEFORE STARTING:
1. Open Google Slides in your browser
2. Make sure it's in edit mode and visible on screen
3. Navigate to the first slide
4. Have the window properly positioned
""")
    
    # Wait for user to be ready
    try:
        input("Press Enter when ready to begin capturing coordinates...")
    except EOFError:
        print("Waiting 5 seconds before beginning...")
        time.sleep(5)
    
    # Capture coordinates
    coords = capture_coordinates()
    
    # Save coordinates
    save_coordinates(coords)
    
    print("\nCoordinates have been saved successfully!")
    print("You can now run the update script with these coordinates.")

if __name__ == "__main__":
    main()