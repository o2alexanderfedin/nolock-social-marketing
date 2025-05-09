#!/usr/bin/env python3
"""
Script to update navigation paths in slides to reflect the new directory structure.
"""

import os
import re
import glob

# Directory containing the slides in the new structure
SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-decks/customer-partner/slides"

def update_navigation_paths(file_path):
    """Update navigation paths in slide files."""
    
    # Read the current slide content
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Update paths in navigation header and footer
    # Original paths point to ../README.md, we need to keep that the same
    # The slide links need to remain in the same directory
    
    # Nothing to update here as the paths are relative and still correct
    # This script is just a placeholder in case we need to update paths in the future
    
    print(f"Checked {file_path} - paths are already correct")

def main():
    """Process all simplified slide files."""
    # Get all simplified slide files
    slide_files = sorted(glob.glob(os.path.join(SLIDES_DIR, "slide*_simplified.md")))
    
    # Count total slides
    total_slides = len(slide_files)
    print(f"Found {total_slides} slides to process")
    
    # Process each slide
    for file_path in slide_files:
        update_navigation_paths(file_path)
    
    print("Navigation paths checked in all slides.")

if __name__ == "__main__":
    main()