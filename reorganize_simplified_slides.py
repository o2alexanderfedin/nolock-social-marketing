#!/usr/bin/env python3
"""
Script to reorganize simplified slides into a separate directory.
"""

import os
import shutil
import glob
import re

# Base directory for customer-partner deck
BASE_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-decks/customer-partner"

def create_directory_structure():
    """Create separate directories for regular and simplified slides."""
    # Create simplified directory
    simplified_dir = os.path.join(BASE_DIR, "slides-simplified")
    os.makedirs(simplified_dir, exist_ok=True)
    
    # Regular slides directory already exists at BASE_DIR/slides
    
    print(f"Created directory: {simplified_dir}")
    return simplified_dir

def move_simplified_slides(simplified_dir):
    """Move simplified slides to their own directory."""
    slides_dir = os.path.join(BASE_DIR, "slides")
    simplified_slides = glob.glob(os.path.join(slides_dir, "*_simplified.md"))
    
    for slide_path in simplified_slides:
        filename = os.path.basename(slide_path)
        # Convert slide01_simplified.md to slide01.md in the simplified directory
        new_filename = filename.replace("_simplified", "")
        dest_path = os.path.join(simplified_dir, new_filename)
        
        # Copy the file (using copy instead of move to preserve original during testing)
        shutil.copy2(slide_path, dest_path)
        print(f"Copied {slide_path} to {dest_path}")
    
    return len(simplified_slides)

def update_navigation_paths(simplified_dir):
    """Update navigation paths in simplified slides to point within their directory."""
    slide_files = sorted(glob.glob(os.path.join(simplified_dir, "slide*.md")))
    
    for file_path in slide_files:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Update navigation links:
        # 1. Change slide01_simplified.md to slide01.md
        # 2. Keep ../README.md links pointing to parent directory
        updated_content = re.sub(
            r'\[⬅️ Previous Slide\]\(slide(\d+)_simplified\.md\)',
            r'[⬅️ Previous Slide](slide\1.md)', 
            content
        )
        
        updated_content = re.sub(
            r'\[➡️ Next Slide\]\(slide(\d+)_simplified\.md\)',
            r'[➡️ Next Slide](slide\1.md)', 
            updated_content
        )
        
        with open(file_path, 'w') as f:
            f.write(updated_content)
        
        print(f"Updated navigation in: {file_path}")

def update_readme_links():
    """Update README.md and other files to point to the new simplified slides location."""
    readme_path = os.path.join(BASE_DIR, "README.md")
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Update links from slides/slideXX_simplified.md to slides-simplified/slideXX.md
    updated_content = re.sub(
        r'\[View\]\(slides/slide(\d+)_simplified\.md\)',
        r'[View](slides-simplified/slide\1.md)', 
        content
    )
    
    with open(readme_path, 'w') as f:
        f.write(updated_content)
    
    print(f"Updated links in: {readme_path}")
    
    # Also update SLIDE_ORDER.md if it exists
    slide_order_path = os.path.join(BASE_DIR, "SLIDE_ORDER.md")
    if os.path.exists(slide_order_path):
        with open(slide_order_path, 'r') as f:
            content = f.read()
        
        updated_content = re.sub(
            r'\[View\]\(slides/slide(\d+)_simplified\.md\)',
            r'[View](slides-simplified/slide\1.md)', 
            content
        )
        
        with open(slide_order_path, 'w') as f:
            f.write(updated_content)
        
        print(f"Updated links in: {slide_order_path}")
    
    # Update SIMPLIFIED_DECK_README.md if it exists
    simplified_readme_path = os.path.join(BASE_DIR, "SIMPLIFIED_DECK_README.md")
    if os.path.exists(simplified_readme_path):
        with open(simplified_readme_path, 'r') as f:
            content = f.read()
        
        updated_content = re.sub(
            r'\[.*?\]\(slides/slide(\d+)_simplified\.md\)',
            r'[Title](slides-simplified/slide\1.md)', 
            content
        )
        
        with open(simplified_readme_path, 'w') as f:
            f.write(updated_content)
        
        print(f"Updated links in: {simplified_readme_path}")

def create_navigation_guide():
    """Create a README.md in the simplified slides directory."""
    simplified_dir = os.path.join(BASE_DIR, "slides-simplified")
    readme_content = """# Simplified Customer & Partner Slides

This directory contains all simplified slides for the Customer & Partner pitch deck. These slides follow presentation best practices with reduced text and enhanced visual focus.

## Slide Navigation

All slides include navigation headers and footers:
- **Previous Slide**: Go to the previous slide
- **Deck Home**: Return to the main deck README
- **Next Slide**: Go to the next slide

## Complete Slide Set

| # | Title | Purpose |
|---|-------|---------|
| [01](slide01.md) | NoLock Social | Introduction |
| [02](slide02.md) | Why Partner With Us | Value Proposition |
| [03](slide03.md) | Content Verification Crisis | Problem Statement |
| [04](slide04.md) | Storage Costs Out of Control | Problem Statement |
| [05](slide05.md) | Integration Complexity & Lock-in | Problem Statement |
| [06](slide06.md) | Our Approach: Content-Addressable Architecture | Solution |
| [07](slide07.md) | Technical Architecture | Technology |
| [08](slide08.md) | Content-Addressable Storage for Partners | Technology |
| [09](slide09.md) | Flexible Integration Options | Technology |
| [10](slide10.md) | Comprehensive Developer Resources | Technology |
| [11](slide11.md) | Enterprise-Grade Security | Value Proposition |
| [12](slide12.md) | Partner Success Stories | Social Proof |
| [13](slide13.md) | Proven Partner Benefits | Value Proposition |
| [14](slide14.md) | AI Integration Advantages | Value Proposition |
| [15](slide15.md) | Partnership Models | Business Model |
| [16](slide16.md) | Implementation Process | Process |
| [17](slide17.md) | Comprehensive Partner Resources | Support |
| [18](slide18.md) | Industry-Specific Solutions | Value Proposition |
| [19](slide19.md) | Next Steps | Call to Action |
| [20](slide20.md) | Partnership Team | Credibility |
| [21](slide21.md) | Technical Specifications | Reference |

## Design Principles

These slides follow specific design principles:
- Maximum 5 bullet points per slide
- Brief bullet points (5-7 words each)
- Visual priority (reduced text, enhanced visuals)
- Detailed speaker notes for verbal delivery

[Return to Main Deck](../README.md)
"""
    
    with open(os.path.join(simplified_dir, "README.md"), 'w') as f:
        f.write(readme_content)
    
    print(f"Created README.md in {simplified_dir}")

def main():
    """Execute the reorganization process."""
    # Create directory structure
    simplified_dir = create_directory_structure()
    
    # Move simplified slides
    num_slides = move_simplified_slides(simplified_dir)
    print(f"Moved {num_slides} simplified slides to separate directory")
    
    # Update navigation paths in the moved slides
    update_navigation_paths(simplified_dir)
    
    # Update README links
    update_readme_links()
    
    # Create a README for the simplified slides directory
    create_navigation_guide()
    
    print("Reorganization completed successfully.")

if __name__ == "__main__":
    main()