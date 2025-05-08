#!/usr/bin/env python3

import os
import re
import time
import webbrowser
import sys
import datetime

# Enable detailed tracing
def trace(message):
    """Print a timestamped trace message."""
    timestamp = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
    print(f"[TRACE {timestamp}] {message}", flush=True)

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"

# Check if a display time is provided as a command line argument
import sys
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    DISPLAY_TIME = int(sys.argv[1])
    trace(f"Using command line provided display time: {DISPLAY_TIME} seconds")
else:
    DISPLAY_TIME = 30  # seconds to display each slide content
    trace(f"Using default display time: {DISPLAY_TIME} seconds")

def load_slide_data(slide_number):
    """Load slide data from the exported markdown file."""
    trace(f"Loading slide data for slide {slide_number}")
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_number:02d}_export.md")
    
    if not os.path.exists(file_path):
        trace(f"WARNING: Could not find {file_path}")
        return None
    
    trace(f"Reading file: {file_path}")
    with open(file_path, 'r') as f:
        content = f.read()
    
    trace("Extracting section data from file")
    # Extract the sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract bullet points section
    bullet_points = ""
    if "## Bullet Points" in content:
        trace("Extracting bullet points")
        bp_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if bp_match:
            bullet_points = bp_match.group(1).strip()
    
    # Extract quotes
    quotes = ""
    if "## Quotes" in content:
        trace("Extracting quotes")
        q_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if q_match:
            quotes = q_match.group(1).strip()
    
    # Extract sources
    sources = ""
    if "## Sources" in content:
        trace("Extracting sources")
        s_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if s_match:
            sources = s_match.group(1).strip()
    
    trace("Slide data extraction complete")
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
    trace(f"Displaying content for slide {slide_number}")
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        trace(f"No data found for slide {slide_number}, skipping")
        print(f"Skipping slide {slide_number} - no data found")
        return
    
    # Clear the terminal
    trace("Clearing terminal screen")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    trace("Displaying slide header")
    print(f"\n===== Slide {slide_number}/{21}: {slide_data['title']} =====\n")
    
    trace("Displaying title section")
    print("\033[1;34m=== TITLE ===\033[0m")
    print(f"{slide_data['title']}\n")
    
    trace("Displaying subtitle section")
    print("\033[1;34m=== SUBTITLE ===\033[0m")
    print(f"{slide_data['subtitle']}\n")
    
    trace("Displaying summary section")
    print("\033[1;34m=== SUMMARY ===\033[0m")
    print(f"{slide_data['summary']}\n")
    
    if slide_data['bullet_points']:
        trace("Displaying bullet points section")
        print("\033[1;34m=== BULLET POINTS ===\033[0m")
        print(slide_data['bullet_points'] + "\n")
    
    if slide_data['quotes']:
        trace("Displaying quotes section")
        print("\033[1;34m=== QUOTES ===\033[0m")
        print(slide_data['quotes'] + "\n")
    
    if slide_data['sources']:
        trace("Displaying sources section")
        print("\033[1;34m=== SOURCES ===\033[0m")
        print(slide_data['sources'] + "\n")
    
    trace("Slide content display complete")

def main():
    """Main function to display slides in sequence."""
    trace("Starting script execution")
    
    # Check if export directory exists
    trace(f"Checking export directory: {EXPORT_DIR}")
    if not os.path.exists(EXPORT_DIR):
        trace(f"ERROR: Export directory not found: {EXPORT_DIR}")
        print(f"ERROR: Export directory not found: {EXPORT_DIR}")
        return
    
    # Open the Google Slides presentation
    trace(f"Opening Google Slides: {SLIDES_URL}")
    print(f"Opening Google Slides: {SLIDES_URL}")
    
    try:
        webbrowser.open(SLIDES_URL)
        trace("Browser command executed")
    except Exception as e:
        trace(f"ERROR opening browser: {str(e)}")
        print(f"ERROR opening browser: {str(e)}")
        return
    
    # Wait for the browser to open
    trace("Waiting for browser to open (3 seconds)")
    time.sleep(3)
    
    # Process each slide
    num_slides = 21  # Total number of slides
    trace(f"Will process {num_slides} slides with {DISPLAY_TIME} seconds per slide")
    
    print("\n===== AUTOMATIC SLIDE DISPLAY MODE =====")
    print(f"Each slide will be shown for {DISPLAY_TIME} seconds")
    print("Copy the content you need for each slide")
    print("Press Ctrl+C at any time to exit")
    print("\nStarting in 3 seconds...")
    
    trace("Starting 3 second countdown before displaying slides")
    time.sleep(3)
    
    try:
        for slide_num in range(1, num_slides + 1):
            trace(f"Starting to process slide {slide_num}/{num_slides}")
            
            # Display the current slide content
            display_slide_content(slide_num)
            
            # Show countdown
            trace(f"Starting countdown of {DISPLAY_TIME} seconds")
            for i in range(DISPLAY_TIME, 0, -1):
                if i % 5 == 0:  # Only trace every 5 seconds to reduce log volume
                    trace(f"Countdown: {i} seconds remaining")
                print(f"\r\033[1;33mNext slide in {i} seconds... Press Ctrl+C to exit\033[0m", end="", flush=True)
                sys.stdout.flush()
                time.sleep(1)
            
            trace("Countdown complete, clearing line")
            print("\r" + " " * 60 + "\r", end="", flush=True)  # Clear the countdown line
    
    except KeyboardInterrupt:
        trace("KeyboardInterrupt detected, exiting loop")
        print("\n\nExiting the slide display...")
    except Exception as e:
        trace(f"Unexpected error: {str(e)}")
        print(f"\nError: {str(e)}")
    
    trace("Script execution completed")
    print("\nAll done! You can continue editing the slides in your browser.")

if __name__ == "__main__":
    main()