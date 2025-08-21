#!/usr/bin/env python3

"""
Extract content from a slide's Markdown file and save it to text files
for easy use with type_text.py.

Usage: python extract_slide_content.py [slide_number]
Example: python extract_slide_content.py 1
"""

import os
import sys
import re

# Configuration
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
OUTPUT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slide_content"

def ensure_output_dir():
    """Ensure output directory exists."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

def extract_content(slide_num):
    """Extract content from a slide's Markdown file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_num:02d}_export.md")
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find {file_path}")
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract summary
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    summary = summary_match.group(1).strip() if summary_match else ""
    
    # Extract bullet points
    bullet_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    bullet_points = bullet_match.group(1).strip() if bullet_match else ""
    
    # Extract quotes
    quotes_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    quotes = quotes_match.group(1).strip() if quotes_match else ""
    
    # Extract sources
    sources_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
    sources = sources_match.group(1).strip() if sources_match else ""
    
    # Combine main content
    main_content = ""
    if summary:
        main_content += summary + "\n\n"
    if bullet_points:
        main_content += bullet_points + "\n\n"
    if quotes:
        main_content += quotes + "\n\n"
    if sources:
        main_content += sources
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "main_content": main_content.strip()
    }

def save_content(slide_num, content):
    """Save content to separate text files."""
    ensure_output_dir()
    
    base_path = os.path.join(OUTPUT_DIR, f"slide{slide_num:02d}")
    
    # Save title
    if content["title"]:
        with open(f"{base_path}_title.txt", "w") as f:
            f.write(content["title"])
        print(f"Saved title to: {base_path}_title.txt")
    
    # Save subtitle
    if content["subtitle"]:
        with open(f"{base_path}_subtitle.txt", "w") as f:
            f.write(content["subtitle"])
        print(f"Saved subtitle to: {base_path}_subtitle.txt")
    
    # Save main content
    if content["main_content"]:
        with open(f"{base_path}_content.txt", "w") as f:
            f.write(content["main_content"])
        print(f"Saved main content to: {base_path}_content.txt")

def main():
    """Main function."""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python extract_slide_content.py [slide_number]")
        print("Example: python extract_slide_content.py 1")
        sys.exit(1)
    
    slide_num = int(sys.argv[1])
    if slide_num < 1 or slide_num > 21:
        print("Error: Slide number must be between 1 and 21")
        sys.exit(1)
    
    # Extract content
    print(f"Extracting content for slide {slide_num}...")
    content = extract_content(slide_num)
    
    if not content:
        print("Failed to extract content.")
        sys.exit(1)
    
    # Print preview
    print("\nContent preview:")
    print(f"Title: {content['title']}")
    print(f"Subtitle: {content['subtitle']}")
    print(f"Main content: {content['main_content'][:100]}...")
    
    # Save content to files
    save_content(slide_num, content)
    
    print("\nContent extraction complete!")
    print(f"You can now use these files with type_text.py. For example:")
    print(f"python type_text.py --file {OUTPUT_DIR}/slide{slide_num:02d}_title.txt")

if __name__ == "__main__":
    main()