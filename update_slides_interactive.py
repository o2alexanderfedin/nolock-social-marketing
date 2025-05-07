#!/usr/bin/env python3

import os
import re
import time
import webbrowser

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"

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
    
    print(f"\n===== Slide {slide_number}: {slide_data['title']} =====\n")
    
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
    
    print("\033[1;33m----------------------------------------------\033[0m")
    print("\033[1;33mPress Enter when you're done editing this slide\033[0m")
    print("\033[1;33mType 'q' to quit or a slide number to jump to it\033[0m")
    print("\033[1;33m----------------------------------------------\033[0m")

def main():
    """Main function to assist with updating Google Slides."""
    # Open the Google Slides presentation
    print(f"Opening Google Slides: {SLIDES_URL}")
    webbrowser.open(SLIDES_URL)
    
    # Wait for the browser to open
    time.sleep(3)
    
    # Process each slide (starting from slide 1)
    num_slides = 21  # Total number of slides to process
    start_slide = int(input("Enter slide number to start with (1-21): ") or "1")
    
    if start_slide < 1 or start_slide > num_slides:
        start_slide = 1
    
    slide_num = start_slide
    
    while slide_num <= num_slides:
        # Display the current slide content
        display_slide_content(slide_num)
        
        # Get user input
        user_input = input().strip().lower()
        
        if user_input == 'q':
            print("Exiting...")
            break
        elif user_input.isdigit():
            new_slide = int(user_input)
            if 1 <= new_slide <= num_slides:
                slide_num = new_slide
                continue
            else:
                print(f"Invalid slide number. Must be between 1 and {num_slides}")
                time.sleep(2)
        else:
            # Move to the next slide
            slide_num += 1
    
    print("\nAll done! You can continue editing the slides in your browser.")

if __name__ == "__main__":
    main()