#!/usr/bin/env python3

import os
import re
import time
import webbrowser

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
DISPLAY_TIME = 30  # seconds to display each slide content

def load_slide_data(slide_number):
    """Load slide data from the exported markdown file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_number:02d}_export.md")
    
    if not os.path.exists(file_path):
        print(f"Warning: Could not find {file_path}")
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

def display_slide_content(slide_number):
    """Display the content of a slide for easy copying."""
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        print(f"Skipping slide {slide_number} - no data found")
        return
    
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n===== Slide {slide_number}/{21}: {slide_data['title']} =====\n")
    
    print("\033[1;34m=== TITLE ===\033[0m")
    print(f"{slide_data['title']}\n")
    
    print("\033[1;34m=== SUBTITLE ===\033[0m")
    print(f"{slide_data['subtitle']}\n")
    
    print("\033[1;34m=== SUMMARY ===\033[0m")
    print(f"{slide_data['summary']}\n")
    
    if slide_data['bullet_points']:
        print("\033[1;34m=== BULLET POINTS ===\033[0m")
        print(slide_data['bullet_points'] + "\n")
    
    if slide_data['quotes']:
        print("\033[1;34m=== QUOTES ===\033[0m")
        print(slide_data['quotes'] + "\n")
    
    if slide_data['sources']:
        print("\033[1;34m=== SOURCES ===\033[0m")
        print(slide_data['sources'] + "\n")

def main():
    """Main function to display slides in sequence."""
    # Open the Google Slides presentation
    print(f"Opening Google Slides: {SLIDES_URL}")
    webbrowser.open(SLIDES_URL)
    
    # Wait for the browser to open
    time.sleep(3)
    
    # Process each slide
    num_slides = 21  # Total number of slides
    
    print("\n===== AUTOMATIC SLIDE DISPLAY MODE =====")
    print(f"Each slide will be shown for {DISPLAY_TIME} seconds")
    print("Copy the content you need for each slide")
    print("Press Ctrl+C at any time to exit")
    print("\nStarting in 3 seconds...")
    time.sleep(3)
    
    try:
        for slide_num in range(1, num_slides + 1):
            # Display the current slide content
            display_slide_content(slide_num)
            
            # Show countdown
            for i in range(DISPLAY_TIME, 0, -1):
                print(f"\r\033[1;33mNext slide in {i} seconds... Press Ctrl+C to exit\033[0m", end="")
                time.sleep(1)
            print("\r" + " " * 60 + "\r", end="")  # Clear the countdown line
    
    except KeyboardInterrupt:
        print("\n\nExiting the slide display...")
    
    print("\nAll done! You can continue editing the slides in your browser.")

if __name__ == "__main__":
    main()