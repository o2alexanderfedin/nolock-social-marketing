#!/usr/bin/env python3

import os
import re
from pathlib import Path

def add_navigation(slide_dir, num_slides):
    """Add header and footer navigation to slides in the specified directory."""
    
    for i in range(1, num_slides + 1):
        slide_num = f"{i:02d}"
        slide_path = os.path.join(slide_dir, f"slide{slide_num}.md")
        
        if not os.path.exists(slide_path):
            print(f"Warning: Slide {slide_path} does not exist. Skipping.")
            continue
            
        # Read the slide content
        with open(slide_path, 'r') as f:
            content = f.read()
        
        # Determine previous and next slide numbers
        prev_num = f"{i-1:02d}" if i > 1 else f"{num_slides:02d}"
        next_num = f"{i+1:02d}" if i < num_slides else "01"
        
        # Create header with navigation
        header = f"""[← Previous](slide{prev_num}.md) | [↑ Overview](../README.md) | [Next →](slide{next_num}.md)

---

"""
        
        # Create footer with navigation
        footer = f"""
---

[← Previous](slide{prev_num}.md) | [↑ Overview](../README.md) | [Next →](slide{next_num}.md)
"""
        
        # Check if navigation is already present
        if content.startswith("[←"):
            print(f"Navigation already exists in {slide_path}. Skipping.")
            continue
            
        # Add header and footer to content
        updated_content = header + content
        
        # Replace the existing footer (if any) or add a new one
        back_to_deck_pattern = r"\[Back to Deck Overview\]\(../README\.md\)"
        if re.search(back_to_deck_pattern, updated_content):
            updated_content = re.sub(back_to_deck_pattern, footer, updated_content)
        else:
            updated_content += footer
        
        # Write the updated content back to the file
        with open(slide_path, 'w') as f:
            f.write(updated_content)
            
        print(f"Added navigation to {slide_path}")

if __name__ == "__main__":
    # Add navigation to the condensed investor pitch deck (12 slides)
    print("Adding navigation to condensed investor pitch deck...")
    add_navigation("/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor/slides", 12)
    
    # Add navigation to the full investor pitch deck (21 slides)
    print("\nAdding navigation to full investor pitch deck...")
    add_navigation("/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides", 21)
    
    print("\nNavigation has been added to all slides successfully!")