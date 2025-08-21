#!/usr/bin/env python3

import pyautogui
import time
import sys
import json
import os

# Configure PyAutoGUI
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True
DELAY_BETWEEN_ACTIONS = 2.0

def print_status(message):
    """Print status messages with consistent formatting."""
    print(f"[STATUS] {message}")

def navigate_to_slide(slide_num):
    """Navigate to a specific slide using Home key and then arrow keys."""
    # First, go to slide 1 using Home key
    print_status(f"Navigating to slide 1 (Home key)")
    pyautogui.press('home')
    time.sleep(2)
    
    # Then navigate forward to the desired slide
    if slide_num > 1:
        print_status(f"Moving to slide {slide_num} (pressing right arrow {slide_num-1} times)")
        for i in range(slide_num - 1):
            print_status(f"  Press {i+1}/{slide_num-1}")
            pyautogui.press('right')
            time.sleep(1)

def load_coordinates():
    """Load coordinates from saved file."""
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
    
    # Default coordinates if file not found
    print_status("Using default coordinates")
    return {
        "title": (1280, 360),
        "subtitle": (1280, 480),
        "content": (1280, 720),
        "next_slide": (2460, 720)
    }

def wait_and_click(x, y, clicks=1, description=""):
    """Wait, then click at specified coordinates."""
    print_status(f"Moving to {description} at ({x}, {y})")
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(DELAY_BETWEEN_ACTIONS)
    
    print_status(f"Clicking {description} at ({x}, {y}) with {clicks} clicks")
    pyautogui.click(x=x, y=y, clicks=clicks)
    time.sleep(DELAY_BETWEEN_ACTIONS)

def test_slide_elements(slide_num, coords):
    """Test clicking on different elements of a slide."""
    # Navigate to the slide
    navigate_to_slide(slide_num)
    
    # Test clicks on each element (without making actual edits)
    elements = [
        ("title", coords["title"][0], coords["title"][1], 1),
        ("subtitle", coords["subtitle"][0], coords["subtitle"][1], 1),
        ("content", coords["content"][0], coords["content"][1], 1)
    ]
    
    for name, x, y, clicks in elements:
        wait_and_click(x, y, clicks, name)
        # Click outside to deselect
        wait_and_click(10, 10, 1, "outside (to deselect)")

def main():
    """Main function to test clicking on slide elements."""
    # Parse arguments
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        slide_num = int(sys.argv[1])
        if 1 <= slide_num <= 21:
            # Load coordinates
            coords = load_coordinates()
            
            # Test clicking on the slide
            print_status(f"Testing clicks on slide {slide_num}")
            test_slide_elements(slide_num, coords)
        else:
            print(f"Error: Slide number must be between 1 and 21")
    else:
        print("Usage: python test_slide_clicks.py [slide_number]")
        print("Please specify a slide number between 1 and 21")

if __name__ == "__main__":
    print_status("Starting slide clicking test")
    print_status("Wait 3 seconds to prepare...")
    print_status("IMPORTANT: This script will click on slide elements!")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    main()
    print_status("Click test complete")