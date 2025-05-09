#!/usr/bin/env python3
"""
Script to add navigation headers and footers to all slide decks.
"""

import os
import re
import glob

# Base directory for all slide decks
BASE_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-decks"

# Deck types to process
DECK_TYPES = ["investor", "investor-full", "original"]

def format_slide_num(num):
    """Format slide number with leading zero if needed."""
    return f"{num:02d}"

def add_navigation(file_path, total_slides=21):
    """Add navigation headers and footers to a slide file."""
    
    # Extract the slide number from the filename
    match = re.search(r'slide(\d+)\.md', os.path.basename(file_path))
    if not match:
        print(f"Skipping {file_path} - doesn't match expected pattern")
        return
    
    slide_num = int(match.group(1))
    
    # Calculate previous and next slide numbers with wraparound
    prev_num = format_slide_num(total_slides if slide_num == 1 else slide_num - 1)
    next_num = format_slide_num(1 if slide_num == total_slides else slide_num + 1)
    
    # Read the current slide content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if navigation is already added
    nav_header = f"[⬅️ Previous Slide](slide{prev_num}.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}.md)"
    if nav_header in content:
        print(f"Skipping {file_path} - navigation already added")
        return
    
    # Create navigation header and footer
    nav_header = f"<!-- Navigation Header -->\n[⬅️ Previous Slide](slide{prev_num}.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}.md)\n\n"
    nav_footer = f"\n\n<!-- Navigation Footer -->\n[⬅️ Previous Slide](slide{prev_num}.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}.md)"
    
    # Add navigation to content
    new_content = nav_header + content + nav_footer
    
    # Write the updated content back to the file
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")

def process_deck(deck_type):
    """Process all slides in a specific deck."""
    slides_dir = os.path.join(BASE_DIR, deck_type, "slides")
    
    # Get all slide files (not including _simplified files)
    slide_files = sorted([f for f in glob.glob(os.path.join(slides_dir, "slide*.md")) 
                         if not "_simplified" in f and not "_readme" in f])
    
    # Count total slides for wraparound navigation
    total_slides = len(slide_files)
    print(f"Found {total_slides} slides to process in {deck_type} deck")
    
    # Process each slide
    for file_path in slide_files:
        add_navigation(file_path, total_slides)

def main():
    """Process all decks."""
    for deck_type in DECK_TYPES:
        print(f"\nProcessing {deck_type} deck...")
        process_deck(deck_type)
    
    print("\nNavigation added to all slide decks.")

if __name__ == "__main__":
    main()