#!/usr/bin/env python3

import pyautogui
import time
import sys

# Configuration
PAUSE_TIME = 3  # seconds to pause at each position

def print_status(message):
    """Print status messages with consistent formatting."""
    print(f"[STATUS] {message}")

def get_screen_info():
    """Get and print screen information."""
    screen_width, screen_height = pyautogui.size()
    mouse_x, mouse_y = pyautogui.position()
    
    print(f"Screen size: {screen_width}x{screen_height}")
    print(f"Current mouse position: ({mouse_x}, {mouse_y})")
    return screen_width, screen_height

def move_and_pause(x, y, description):
    """Move mouse to the specified position and pause."""
    print_status(f"Moving to {description} ({x}, {y})")
    pyautogui.moveTo(x, y, duration=1)
    
    # Get current position after move (to verify)
    actual_x, actual_y = pyautogui.position()
    print_status(f"Actual position: ({actual_x}, {actual_y})")
    
    print_status(f"Pausing at {description} for {PAUSE_TIME} seconds")
    time.sleep(PAUSE_TIME)

def calibrate_corners():
    """Move mouse to each corner of the screen."""
    width, height = pyautogui.size()
    
    # Move to each corner
    corners = [
        (0, 0, "top-left corner"),
        (width-1, 0, "top-right corner"),
        (width-1, height-1, "bottom-right corner"),
        (0, height-1, "bottom-left corner"),
        (width//2, height//2, "center of screen")
    ]
    
    for x, y, description in corners:
        move_and_pause(x, y, description)

def test_navigation():
    """Test slide navigation using keyboard keys."""
    print_status("\n=== Testing Keyboard Navigation ===")
    print_status("Will press RIGHT arrow key to advance slides")
    
    # Press right arrow key 3 times with pauses
    for i in range(3):
        time.sleep(2)
        print_status(f"Pressing RIGHT arrow key ({i+1}/3)")
        pyautogui.press("right")
        time.sleep(3)
    
    # Press left arrow key to go back
    print_status("Now pressing LEFT arrow key 3 times to go back")
    for i in range(3):
        time.sleep(2)
        print_status(f"Pressing LEFT arrow key ({i+1}/3)")
        pyautogui.press("left")
        time.sleep(3)
    
    # Press Home key to return to first slide
    time.sleep(2)
    print_status("Pressing HOME key to return to first slide")
    pyautogui.press("home")
    time.sleep(3)

def test_click_positions():
    """Test clicking at various positions on the slide."""
    width, height = pyautogui.size()
    
    positions = [
        (width//2, height//4, "Title position"),
        (width//2, height//3, "Subtitle position"),
        (width//2, height//2, "Content middle position"),
        (width-100, height//2, "Right side (next slide)"),
        (100, height//2, "Left side (previous slide)")
    ]
    
    print_status("\n=== Testing Click Positions ===")
    print_status("Will move to various positions WITHOUT clicking")
    
    for x, y, description in positions:
        move_and_pause(x, y, description)

def main():
    """Main function to calibrate the mouse and test navigation."""
    # Disable failsafe temporarily
    original_failsafe = pyautogui.FAILSAFE
    pyautogui.FAILSAFE = False
    
    try:
        print_status("Starting mouse calibration")
        print_status("=== SCREEN INFORMATION ===")
        get_screen_info()
        
        print_status("\n=== CORNER CALIBRATION ===")
        print_status("Will move the mouse to each corner of the screen")
        print_status("Watch the mouse to verify it's moving to the correct positions")
        
        # Wait for user to be ready
        print_status("Starting in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        
        # Run calibrations
        calibrate_corners()
        
        # Parse command line arguments to determine what to test
        import sys
        test_nav = "--nav" in sys.argv
        test_click = "--click" in sys.argv
        save_coords = "--save" in sys.argv
        
        # Test navigation if requested
        if test_nav:
            test_navigation()
        
        # Test click positions if requested
        if test_click:
            test_click_positions()
        
        # Save suggested coordinates
        width, height = pyautogui.size()
        
        suggested_coords = {
            "title": (width//2, height//4),
            "subtitle": (width//2, height//3),
            "content": (width//2, height//2),
            "next_slide": (width-100, height//2)
        }
        
        print("\n=== SUGGESTED COORDINATES ===")
        for key, value in suggested_coords.items():
            print(f"  {key}: {value}")
        
        if save_coords:
            import json
            with open("slide_coordinates.json", "w") as f:
                json.dump(suggested_coords, f)
            print("Coordinates saved to slide_coordinates.json")
        
        print_status("\nCalibration complete!")
    
    finally:
        # Restore original failsafe setting
        pyautogui.FAILSAFE = original_failsafe

if __name__ == "__main__":
    main()