#!/usr/bin/env python3

import os
import re
import time
import webbrowser

# Print function to ensure immediate output
def print_flush(message, end="\n"):
    print(message, end=end, flush=True)

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"

def load_slide_data(slide_number):
    """Load slide data from the exported markdown file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_number:02d}_export.md")
    
    if not os.path.exists(file_path):
        print_flush(f"Warning: Could not find {file_path}")
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract bullet points section
    bullet_points = ""
    if "## Bullet Points" in content:
        bp_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if bp_match:
            bullet_points = bp_match.group(1).strip()
    
    # Extract quotes
    quotes = ""
    if "## Quotes" in content:
        q_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if q_match:
            quotes = q_match.group(1).strip()
    
    # Extract sources
    sources = ""
    if "## Sources" in content:
        s_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if s_match:
            sources = s_match.group(1).strip()
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "summary": summary_match.group(1).strip() if summary_match else "",
        "bullet_points": bullet_points,
        "quotes": quotes,
        "sources": sources,
    }

def print_slide_content(slide_number):
    """Print the content of a slide for easy copying."""
    print_flush(f"LOADING SLIDE {slide_number}...")
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        print_flush(f"Skipping slide {slide_number} - no data found")
        return
    
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_flush("-" * 80)
    print_flush(f"SLIDE {slide_number}/21: {slide_data['title']}")
    print_flush("-" * 80)
    
    print_flush("\n=== TITLE ===")
    print_flush(f"{slide_data['title']}")
    
    print_flush("\n=== SUBTITLE ===")
    print_flush(f"{slide_data['subtitle']}")
    
    print_flush("\n=== SUMMARY ===")
    print_flush(f"{slide_data['summary']}")
    
    if slide_data['bullet_points']:
        print_flush("\n=== BULLET POINTS ===")
        print_flush(slide_data['bullet_points'])
    
    if slide_data['quotes']:
        print_flush("\n=== QUOTES ===")
        print_flush(slide_data['quotes'])
    
    if slide_data['sources']:
        print_flush("\n=== SOURCES ===")
        print_flush(slide_data['sources'])
    
    print_flush("\n" + "-" * 80)
    print_flush("COPY THE CONTENT ABOVE INTO YOUR GOOGLE SLIDE")
    print_flush("-" * 80)

def print_all_slides():
    """Print content for all slides."""
    # Open the Google Slides presentation
    print_flush(f"Opening Google Slides: {SLIDES_URL}")
    try:
        webbrowser.open(SLIDES_URL)
    except Exception as e:
        print_flush(f"Error opening browser: {e}")
    
    # Print content for each slide
    print_flush("\nPrinting content for all slides...")
    
    for slide_num in range(1, 22):
        print_slide_content(slide_num)
        
        # Wait for user to press Enter to continue
        try:
            input("\nPress Enter to continue to the next slide (or Ctrl+C to exit)... ")
        except KeyboardInterrupt:
            print_flush("\nExiting...")
            break
    
    print_flush("\nAll slides have been printed.")

def print_single_slide(slide_num):
    """Print content for a single slide."""
    if slide_num < 1 or slide_num > 21:
        print_flush(f"Invalid slide number: {slide_num}")
        return
    
    # Open the Google Slides presentation
    print_flush(f"Opening Google Slides: {SLIDES_URL}")
    try:
        webbrowser.open(SLIDES_URL)
    except Exception as e:
        print_flush(f"Error opening browser: {e}")
    
    # Print content for the specified slide
    print_slide_content(slide_num)

def main():
    """Main function to print slide content."""
    # Check if export directory exists
    if not os.path.exists(EXPORT_DIR):
        print_flush(f"ERROR: Export directory not found: {EXPORT_DIR}")
        return
    
    # Check if a specific slide number is provided
    import sys
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        slide_num = int(sys.argv[1])
        print_single_slide(slide_num)
    else:
        print_all_slides()

if __name__ == "__main__":
    main()