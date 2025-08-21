#!/usr/bin/env python3

"""
Simple Google Slides Update Script

This script updates Google Slides with content from markdown files, with a focus on
reliability and clear user feedback.

Usage:
  python simple_update_slides.py [slide_number]

Features:
- Updates a single slide at a time
- Provides clear feedback at each step
- Uses keyboard shortcuts for more reliable navigation
- Allows manual verification between steps
"""

import os
import sys
import re
import time
import json
import pyautogui

# Configuration
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
DELAY = 2.0  # seconds between actions

# Configure PyAutoGUI
pyautogui.PAUSE = 0.5  # pause between PyAutoGUI commands
pyautogui.FAILSAFE = True  # move to upper-left corner to abort

def print_header(message):
    """Print a header message."""
    print("\n" + "=" * 70)
    print(message.center(70))
    print("=" * 70)

def print_status(message):
    """Print status message."""
    print(f"[STATUS] {message}")

def load_coordinates():
    """Load coordinates from file."""
    if not os.path.exists("slide_coordinates.json"):
        print("Error: slide_coordinates.json not found")
        print("Run get_coordinates.py first to capture coordinates")
        sys.exit(1)
    
    with open("slide_coordinates.json", "r") as f:
        coords = json.load(f)
    
    print_status("Loaded coordinates:")
    for key, value in coords.items():
        print(f"  {key}: {value}")
    
    return coords

def load_slide_content(slide_num):
    """Load slide content from export file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_num:02d}_export.md")
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}")
        sys.exit(1)
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract all remaining content for main section
    main_content = ""
    
    # Extract summary
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    if summary_match:
        main_content += summary_match.group(1).strip() + "\n\n"
    
    # Extract bullet points
    bullet_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    if bullet_match:
        main_content += bullet_match.group(1).strip() + "\n\n"
    
    # Extract quotes
    quotes_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    if quotes_match:
        main_content += quotes_match.group(1).strip() + "\n\n"
    
    # Extract sources
    sources_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    if sources_match:
        main_content += sources_match.group(1).strip()
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "main_content": main_content.strip()
    }

def navigate_to_slide(slide_num):
    """Navigate to specific slide using keyboard shortcuts."""
    print_header(f"NAVIGATING TO SLIDE {slide_num}")
    
    # First go to slide 1
    print_status("Pressing HOME key to go to first slide")
    pyautogui.press('home')
    time.sleep(DELAY)
    
    # Then go to specific slide if not slide 1
    if slide_num > 1:
        print_status(f"Moving to slide {slide_num} by pressing RIGHT arrow {slide_num-1} times")
        for i in range(slide_num - 1):
            print_status(f"  Press RIGHT arrow ({i+1}/{slide_num-1})")
            pyautogui.press('right')
            time.sleep(DELAY)

def edit_text_element(element_name, coords, new_text):
    """Edit a text element on the slide."""
    print_header(f"EDITING {element_name.upper()}")
    
    # Show what we're about to edit
    print_status(f"About to edit {element_name} with text: {new_text[:50]}...")
    print_status(f"Will click at position: {coords}")
    
    # Wait before clicking
    time.sleep(DELAY)
    
    # Click to select the element
    print_status(f"Double-clicking {element_name}")
    pyautogui.click(x=coords[0], y=coords[1], clicks=2)
    time.sleep(DELAY)
    
    # Select all existing text
    print_status("Pressing COMMAND+A to select all text")
    pyautogui.hotkey('command', 'a')
    time.sleep(DELAY)
    
    # Type new text
    print_status(f"Typing new text for {element_name}")
    pyautogui.typewrite(new_text)
    time.sleep(DELAY)
    
    # Press Escape to finish editing
    print_status("Pressing ESCAPE to finish editing")
    pyautogui.press('escape')
    time.sleep(DELAY)
    
    print_status(f"Finished editing {element_name}")

def update_slide(slide_num, coords, content):
    """Update a single slide with new content."""
    print_header(f"UPDATING SLIDE {slide_num}")
    
    # Update title
    if content["title"]:
        edit_text_element("title", coords["title"], content["title"])
    
    # Update subtitle
    if content["subtitle"]:
        edit_text_element("subtitle", coords["subtitle"], content["subtitle"])
    
    # Update main content
    if content["main_content"]:
        edit_text_element("content", coords["content"], content["main_content"])
    
    print_status(f"Slide {slide_num} update complete!")

def main():
    """Main function."""
    # Parse command line arguments
    slide_num = 1
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        slide_num = int(sys.argv[1])
        if slide_num < 1 or slide_num > 21:
            print("Error: Slide number must be between 1 and 21")
            sys.exit(1)
    
    print_header("GOOGLE SLIDES SIMPLE UPDATE SCRIPT")
    print(f"Will update slide {slide_num}")
    
    # Load coordinates
    coords = load_coordinates()
    
    # Load slide content
    content = load_slide_content(slide_num)
    
    # Show what will be updated
    print_status("Will update slide with the following content:")
    print(f"  Title: {content['title']}")
    print(f"  Subtitle: {content['subtitle']}")
    print(f"  Main Content: {content['main_content'][:50]}...")
    
    # Confirm before proceeding
    try:
        input("\nPress Enter to begin updating slide (or Ctrl+C to abort)...")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation aborted.")
        sys.exit(0)
    
    # Countdown
    print_status("Starting in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # Run the update
    try:
        # Navigate to the slide
        navigate_to_slide(slide_num)
        
        # Update the slide
        update_slide(slide_num, coords, content)
        
        print_header("UPDATE COMPLETE")
        print(f"Slide {slide_num} has been updated successfully!")
    
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Update failed. Try running again or check the coordinates.")

if __name__ == "__main__":
    main()