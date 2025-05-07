#!/usr/bin/env python3

import os
import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
WAIT_BETWEEN_SLIDES = 15  # seconds to wait between processing slides
WAIT_BETWEEN_ACTIONS = 2  # seconds to wait between each action on a slide

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

def setup_driver():
    """Set up and configure the Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)  # Keep browser open after script finishes
    
    # Install and set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def go_to_slide(driver, slide_number):
    """Navigate to a specific slide in the presentation."""
    # Check if we're already on the correct slide
    current_url = driver.current_url
    if f"slide=id.g" in current_url or f"slide=id.p" in current_url:
        # Already on a specific slide, navigate to the target slide
        script = f'window.location.href = "{SLIDES_URL}#slide=id.p{slide_number}";'
        driver.execute_script(script)
    else:
        # Not on a specific slide yet, append the slide ID to the URL
        driver.get(f"{SLIDES_URL}#slide=id.p{slide_number}")
    
    time.sleep(WAIT_BETWEEN_ACTIONS)
    return True

def process_slide(driver, slide_number):
    """Process a single slide in the presentation."""
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        print(f"Skipping slide {slide_number} - no data found")
        return
    
    print(f"\n===== Processing Slide {slide_number}: {slide_data['title']} =====")
    
    # Navigate to the slide
    if not go_to_slide(driver, slide_number):
        print(f"Failed to navigate to slide {slide_number}")
        return
    
    # Wait for user action - this gives the user time to click on elements manually
    print("\nPlease click on the title textbox and press Enter when ready...")
    time.sleep(WAIT_BETWEEN_SLIDES)
    
    # Print instructions for the user
    print("\nCopy and paste these components manually:")
    print(f"\n1. TITLE: {slide_data['title']}")
    print(f"\n2. SUBTITLE: {slide_data['subtitle']}")
    print(f"\n3. SUMMARY: {slide_data['summary']}")
    
    if slide_data['bullet_points']:
        print("\n4. BULLET POINTS:")
        print(slide_data['bullet_points'])
    
    if slide_data['quotes']:
        print("\n5. QUOTES:")
        print(slide_data['quotes'])
    
    if slide_data['sources']:
        print("\n6. SOURCES:")
        print(slide_data['sources'])
    
    print("\nWhen you're done with this slide, press Enter to continue to the next slide...")
    input()  # Wait for user to press Enter

def main():
    """Main function to update Google Slides."""
    # Set up the WebDriver
    driver = setup_driver()
    
    try:
        # Open the Google Slides presentation
        print(f"Opening Google Slides: {SLIDES_URL}")
        driver.get(SLIDES_URL)
        
        # Wait for the presentation to load
        time.sleep(5)
        
        # Process each slide (starting from slide 1)
        num_slides = 21  # Total number of slides to process
        start_slide = int(input("Enter slide number to start with (1-21): ") or "1")
        
        for slide_num in range(start_slide, num_slides + 1):
            process_slide(driver, slide_num)
        
        print("\nAll slides have been processed!")
        print("The browser will remain open so you can make any final adjustments.")
        
    except Exception as e:
        print(f"Error during slides update: {e}")

if __name__ == "__main__":
    main()