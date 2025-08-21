#!/usr/bin/env python3

"""
Master script for Google Slides automation
------------------------------------------

This script guides you through the complete workflow for updating Google Slides:
1. Open Chrome and navigate to Google Slides
2. Set up coordinates for slide elements
3. Update slides one by one

Usage:
  python update_slides_master.py

The script provides clear instructions at each step and doesn't proceed
until you confirm that each step is working properly.
"""

import os
import sys
import subprocess
import time

def print_header(message):
    """Print a header message."""
    print("\n" + "=" * 70)
    print(message.center(70))
    print("=" * 70)

def print_status(message):
    """Print status message."""
    print(f"[STATUS] {message}")

def wait_for_input(message="Press Enter to continue (or Ctrl+C to abort)..."):
    """Wait for user input with error handling."""
    try:
        return input(message)
    except (EOFError, KeyboardInterrupt):
        print("\nOperation aborted.")
        sys.exit(0)

def run_script(script_name, args=None):
    """Run a Python script and return its exit code."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    
    if not os.path.exists(script_path):
        print(f"Error: Script not found: {script_path}")
        return 1
    
    cmd = [sys.executable, script_path]
    if args:
        cmd.extend(args)
    
    print_status(f"Running: {' '.join(cmd)}")
    
    try:
        return subprocess.call(cmd)
    except Exception as e:
        print(f"Error running script: {e}")
        return 1

def main():
    """Main function to guide through the entire workflow."""
    print_header("GOOGLE SLIDES UPDATE MASTER SCRIPT")
    
    print("""
This script will guide you through the complete process of updating the NoLock Social
Google Slides presentation. The process has several steps, and you'll be asked to 
confirm each step is working before proceeding to the next.

REQUIREMENTS:
- You need to be logged into your Google account
- Internet connection is required
- The slides_export directory must contain the slide content

STEPS:
1. Open Chrome and navigate to Google Slides
2. Capture coordinates for slide elements
3. Update slides one by one
""")
    
    wait_for_input()
    
    # Step 1: Open Chrome and Google Slides
    print_header("STEP 1: OPEN CHROME AND GOOGLE SLIDES")
    print("This will open Chrome and navigate to the Google Slides presentation.")
    
    if wait_for_input("Start this step? (y/n): ").lower() != 'y':
        print("Skipping this step.")
    else:
        if run_script("open_google_slides.py") != 0:
            print("Failed to open Google Slides. Please do it manually before continuing.")
        
        if wait_for_input("Did Chrome open and navigate to Google Slides? (y/n): ").lower() != 'y':
            print("Please open Chrome and navigate to Google Slides manually before continuing.")
    
    # Step 2: Capture coordinates
    print_header("STEP 2: CAPTURE SLIDE ELEMENT COORDINATES")
    print("""
This step will help you capture the coordinates of slide elements (title, subtitle, etc.).
You'll need to position your mouse over each element when prompted.

IMPORTANT:
- Make sure Google Slides is open and visible
- Move your mouse to each element when prompted, and hold it still
- The script will capture the position after a countdown
""")
    
    if wait_for_input("Start this step? (y/n): ").lower() != 'y':
        print("Skipping this step.")
    elif not os.path.exists("slide_coordinates.json"):
        if run_script("get_coordinates.py") != 0:
            print("Failed to capture coordinates. You can try again or continue with default coordinates.")
    else:
        print("Coordinate file already exists. Do you want to recapture coordinates?")
        if wait_for_input("Recapture coordinates? (y/n): ").lower() == 'y':
            if run_script("get_coordinates.py") != 0:
                print("Failed to capture coordinates. Using existing coordinates.")
    
    # Step 3: Update slides
    print_header("STEP 3: UPDATE SLIDES")
    print("""
This step will update the slides one by one. You'll be asked which slide to update,
and the script will handle the rest.

IMPORTANT:
- Make sure Google Slides is in focus
- Don't move the mouse during the update process
- Move the mouse to the upper-left corner to abort if needed
""")
    
    if wait_for_input("Start this step? (y/n): ").lower() != 'y':
        print("Skipping this step.")
    else:
        # Get slide number
        while True:
            try:
                slide_input = wait_for_input("Enter slide number to update (1-21, or 'all' for all slides): ")
                
                if slide_input.lower() == 'all':
                    print("Updating all slides is not recommended for first attempt.")
                    print("Let's start with one slide to make sure everything works.")
                    continue
                
                slide_num = int(slide_input)
                if 1 <= slide_num <= 21:
                    break
                else:
                    print("Error: Slide number must be between 1 and 21.")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        # Update the selected slide
        if run_script("simple_update_slides.py", [str(slide_num)]) != 0:
            print(f"Failed to update slide {slide_num}.")
        else:
            print(f"Slide {slide_num} updated successfully!")
    
    print_header("PROCESS COMPLETE")
    print("""
The Google Slides update process is complete.

- If the update was successful, you can update more slides by running:
  python simple_update_slides.py [slide_number]

- If there were issues, you may need to adjust the coordinates by running:
  python get_coordinates.py

Thank you for using the NoLock Social slides update tool!
""")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())