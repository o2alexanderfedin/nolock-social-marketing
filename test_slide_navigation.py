#!/usr/bin/env python3

import pyautogui
import time
import sys

# Configure PyAutoGUI
pyautogui.PAUSE = 1.0
pyautogui.FAILSAFE = True

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

def test_sequential_navigation():
    """Test navigating through slides in sequence."""
    # Go to first slide
    print_status("Going to first slide (Home key)")
    pyautogui.press('home')
    time.sleep(2)
    
    # Navigate forward 5 slides
    print_status("Testing forward navigation (5 slides)")
    for i in range(5):
        print_status(f"Slide {i+1} → {i+2}")
        pyautogui.press('right')
        time.sleep(2)
    
    # Navigate back 5 slides
    print_status("Testing backward navigation (5 slides)")
    for i in range(5):
        print_status(f"Slide {6-i} → {5-i}")
        pyautogui.press('left')
        time.sleep(2)

def main():
    """Main function to test slide navigation."""
    # Parse arguments
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        slide_num = int(sys.argv[1])
        if 1 <= slide_num <= 21:
            print_status(f"Will navigate to slide {slide_num}")
            navigate_to_slide(slide_num)
        else:
            print(f"Error: Slide number must be between 1 and 21")
    else:
        # Test sequential navigation
        print_status("Testing sequential navigation through slides")
        test_sequential_navigation()

if __name__ == "__main__":
    print_status("Starting slide navigation test")
    print_status("Wait 3 seconds to prepare...")
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    main()
    print_status("Navigation test complete")