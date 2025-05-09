#!/usr/bin/env python3
"""
Script to add navigation headers and footers to all slide files.
"""

import os
import re
import glob

# Directory containing the slides
SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-customer-partner/slides"

def format_slide_num(num):
    """Format slide number with leading zero if needed."""
    return f"{num:02d}"

def add_navigation(file_path, total_slides=21):
    """Add navigation headers and footers to a slide file."""
    
    # Extract the slide number from the filename
    match = re.search(r'slide(\d+)_simplified\.md', os.path.basename(file_path))
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
    nav_header = f"[⬅️ Previous Slide](slide{prev_num}_simplified.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}_simplified.md)"
    if nav_header in content:
        print(f"Skipping {file_path} - navigation already added")
        return
    
    # Create navigation header and footer
    nav_header = f"<!-- Navigation Header -->\n[⬅️ Previous Slide](slide{prev_num}_simplified.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}_simplified.md)\n\n"
    nav_footer = f"\n\n<!-- Navigation Footer -->\n[⬅️ Previous Slide](slide{prev_num}_simplified.md) | [🏠 Deck Home](../README.md) | [➡️ Next Slide](slide{next_num}_simplified.md)"
    
    # Add navigation to content
    new_content = nav_header + content + nav_footer
    
    # Write the updated content back to the file
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")

def main():
    """Process all simplified slide files."""
    # Get all simplified slide files
    slide_files = sorted(glob.glob(os.path.join(SLIDES_DIR, "slide*_simplified.md")))
    
    # Count total slides for wraparound navigation
    total_slides = len(slide_files)
    print(f"Found {total_slides} slides to process")
    
    # Process each slide
    for file_path in slide_files:
        add_navigation(file_path, total_slides)
    
    print("Navigation added to all slides.")

if __name__ == "__main__":
    main()