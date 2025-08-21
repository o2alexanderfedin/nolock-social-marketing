#!/usr/bin/env python3

import os
import sys
import subprocess

def show_usage():
    print("""
USAGE: python update_one_slide.py [slide_number]

Updates a single slide in the Google Slides presentation.
If no slide number is provided, you will be prompted to enter one.

Examples:
  python update_one_slide.py 5     # Update slide 5
  python update_one_slide.py       # Interactive mode
    """)

def main():
    # Check if pyautogui script exists
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "update_slides_pyautogui.py")
    if not os.path.exists(script_path):
        print(f"ERROR: Could not find {script_path}")
        return 1
    
    # Get slide number
    slide_num = None
    if len(sys.argv) > 1:
        try:
            slide_num = int(sys.argv[1])
            if slide_num < 1 or slide_num > 21:
                print("ERROR: Slide number must be between 1 and 21")
                return 1
        except ValueError:
            print("ERROR: Invalid slide number")
            show_usage()
            return 1
    else:
        # Interactive mode
        while True:
            try:
                slide_input = input("Enter slide number to update (1-21): ")
                slide_num = int(slide_input)
                if 1 <= slide_num <= 21:
                    break
                else:
                    print("ERROR: Slide number must be between 1 and 21")
            except ValueError:
                print("ERROR: Please enter a valid number")
    
    print(f"Preparing to update slide {slide_num}...")
    
    # Prepare command arguments
    cmd = [
        "python3", 
        script_path,
        "--single-slide", str(slide_num),
        "--no-browser",
        "--delay", "1.5"
    ]
    
    # Run the command
    print("Running command:", " ".join(cmd))
    return subprocess.call(cmd)

if __name__ == "__main__":
    sys.exit(main())