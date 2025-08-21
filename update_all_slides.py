#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    # Check if pyautogui script exists
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "update_slides_pyautogui.py")
    if not os.path.exists(script_path):
        print(f"ERROR: Could not find {script_path}")
        return 1
    
    print("=== NoLock Social Slides Updater ===")
    print("This script will update all slides in the Google Slides presentation.")
    print("Make sure you have the Google Slides presentation open in your browser.")
    
    try:
        start_slide = int(input("Enter starting slide number (1-21, default: 1): ") or "1")
        if start_slide < 1 or start_slide > 21:
            print("ERROR: Start slide must be between 1 and 21. Using 1.")
            start_slide = 1
    except ValueError:
        print("Invalid input. Using start slide 1.")
        start_slide = 1
    
    try:
        end_slide = int(input("Enter ending slide number (1-21, default: 21): ") or "21")
        if end_slide < start_slide or end_slide > 21:
            print(f"ERROR: End slide must be between {start_slide} and 21. Using 21.")
            end_slide = 21
    except ValueError:
        print("Invalid input. Using end slide 21.")
        end_slide = 21
    
    try:
        delay = float(input("Enter delay factor (higher value = slower updates, default: 1.5): ") or "1.5")
        if delay <= 0:
            print("ERROR: Delay must be positive. Using 1.5.")
            delay = 1.5
    except ValueError:
        print("Invalid input. Using delay factor 1.5.")
        delay = 1.5
    
    print(f"\nPreparing to update slides {start_slide} to {end_slide} with delay factor {delay}...")
    
    # Ask for confirmation
    confirm = input("\nStart updating slides? (y/n): ").lower().strip()
    if confirm != 'y':
        print("Operation cancelled.")
        return 1
    
    # Prepare command arguments
    cmd = [
        "python3", 
        script_path,
        "--start", str(start_slide),
        "--end", str(end_slide),
        "--no-browser",
        "--delay", str(delay)
    ]
    
    # Run the command
    print("Running command:", " ".join(cmd))
    return subprocess.call(cmd)

if __name__ == "__main__":
    sys.exit(main())