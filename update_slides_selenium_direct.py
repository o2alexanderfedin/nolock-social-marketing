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
WAIT_BETWEEN_OPERATIONS = 1  # seconds to wait between Selenium operations
DEBUG = True  # Set to True for more verbose output

def debug_print(message):
    """Print debug messages if DEBUG is enabled."""
    if DEBUG:
        print(f"[DEBUG] {message}")

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
    
    # Combine all content for the main slide content
    main_content = ""
    if bullet_points:
        main_content += bullet_points + "\n\n"
    if quotes:
        main_content += quotes + "\n\n"
    if sources:
        main_content += sources
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "summary": summary_match.group(1).strip() if summary_match else "",
        "main_content": main_content.strip()
    }

def setup_driver():
    """Set up and configure the Chrome WebDriver."""
    print("Setting up Chrome WebDriver...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)  # Keep browser open after script finishes
    
    # Install and set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def wait_for_element(driver, by, selector, timeout=10):
    """Wait for an element to be present and visible on the page."""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )
        return element
    except TimeoutException:
        debug_print(f"Timeout waiting for element: {selector}")
        return None

def click_with_retry(driver, element, max_retries=3):
    """Click on an element with retry logic."""
    for attempt in range(max_retries):
        try:
            element.click()
            time.sleep(WAIT_BETWEEN_OPERATIONS)
            return True
        except (ElementNotInteractableException, StaleElementReferenceException) as e:
            debug_print(f"Click failed (attempt {attempt+1}/{max_retries}): {str(e)}")
            time.sleep(WAIT_BETWEEN_OPERATIONS)
    
    return False

def edit_text_content(driver, element, new_text):
    """Edit text content of an element."""
    try:
        # Click to focus on the element
        click_with_retry(driver, element)
        
        # Select all text and clear it
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(WAIT_BETWEEN_OPERATIONS)
        
        # Type the new text
        actions = ActionChains(driver)
        actions.send_keys(new_text).perform()
        time.sleep(WAIT_BETWEEN_OPERATIONS)
        
        # Press Enter to confirm and click away to ensure changes are saved
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        time.sleep(WAIT_BETWEEN_OPERATIONS)
        
        print(f"Updated text: '{new_text[:30]}...'")
        return True
    except Exception as e:
        debug_print(f"Error editing text: {str(e)}")
        return False

def go_to_slide(driver, slide_number):
    """Navigate to a specific slide in the presentation."""
    print(f"Navigating to slide {slide_number}...")
    
    try:
        # Try to navigate to the specific slide by URL
        driver.get(f"{SLIDES_URL}#slide=id.g{slide_number}")
        time.sleep(2)  # Wait for navigation
        
        # Verify we're on the correct slide (this could be improved based on actual slide structure)
        # For now, just check if we're on a slide page
        if "slide=id" in driver.current_url:
            debug_print(f"Successfully navigated to slide URL: {driver.current_url}")
            return True
    except Exception as e:
        debug_print(f"Error navigating to slide {slide_number}: {str(e)}")
        return False

def edit_slide(driver, slide_number, slide_data):
    """Edit the content of a slide."""
    print(f"\n===== Editing Slide {slide_number}: {slide_data['title']} =====")
    
    # Go to the specific slide
    if not go_to_slide(driver, slide_number):
        print(f"Failed to navigate to slide {slide_number}")
        return False
    
    # Wait for slide to load
    time.sleep(2)
    
    try:
        # Enter edit mode if needed by clicking on the slide
        slide_canvas = wait_for_element(driver, By.CSS_SELECTOR, "div.punch-viewer-content")
        if slide_canvas:
            debug_print("Found slide canvas, clicking to enter edit mode")
            click_with_retry(driver, slide_canvas)
            time.sleep(1)
        
        # Find and edit title
        title_element = wait_for_element(driver, By.CSS_SELECTOR, "div.punch-viewer-svgpage-a")
        if title_element and slide_data["title"]:
            debug_print(f"Editing title: {slide_data['title']}")
            # Double click to edit
            actions = ActionChains(driver)
            actions.double_click(title_element).perform()
            time.sleep(1)
            
            # Edit text
            edit_text_content(driver, title_element, slide_data["title"])
        
        # Find and edit subtitle
        # This is a simplified approach - in reality, we would need to identify the specific
        # elements on each slide, which might require different selectors for different slides
        subtitle_elements = driver.find_elements(By.CSS_SELECTOR, "div.punch-viewer-svgpage-a")
        if len(subtitle_elements) > 1 and slide_data["subtitle"]:
            debug_print(f"Editing subtitle: {slide_data['subtitle']}")
            subtitle_element = subtitle_elements[1]  # Assuming subtitle is the second text element
            
            # Double click to edit
            actions = ActionChains(driver)
            actions.double_click(subtitle_element).perform()
            time.sleep(1)
            
            # Edit text
            edit_text_content(driver, subtitle_element, slide_data["subtitle"])
        
        # Edit main content (combining summary, bullet points, etc.)
        if len(subtitle_elements) > 2 and slide_data["main_content"]:
            debug_print(f"Editing main content...")
            content_element = subtitle_elements[2]  # Assuming main content is the third text element
            
            # Double click to edit
            actions = ActionChains(driver)
            actions.double_click(content_element).perform()
            time.sleep(1)
            
            # Add summary first
            full_content = f"{slide_data['summary']}\n\n{slide_data['main_content']}"
            
            # Edit text
            edit_text_content(driver, content_element, full_content)
        
        print(f"Successfully updated slide {slide_number}")
        return True
    
    except Exception as e:
        print(f"Error editing slide {slide_number}: {str(e)}")
        return False

def update_slides(driver, start_slide=1, end_slide=21):
    """Update a range of slides in the presentation."""
    for slide_num in range(start_slide, end_slide + 1):
        # Load slide data
        slide_data = load_slide_data(slide_num)
        if not slide_data:
            print(f"Skipping slide {slide_num} - no data found")
            continue
        
        # Edit the slide
        edit_slide(driver, slide_num, slide_data)
        
        # Wait between slides to avoid overwhelming the browser
        time.sleep(2)

def main():
    """Main function to update Google Slides."""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Update Google Slides with new content using Selenium')
    parser.add_argument('--start', type=int, default=1, help='Starting slide number (default: 1)')
    parser.add_argument('--end', type=int, default=21, help='Ending slide number (default: 21)')
    args = parser.parse_args()
    
    # Check if export directory exists
    if not os.path.exists(EXPORT_DIR):
        print(f"ERROR: Export directory not found: {EXPORT_DIR}")
        return
    
    # Set up the WebDriver
    driver = setup_driver()
    
    try:
        # Open the Google Slides presentation
        print(f"Opening Google Slides: {SLIDES_URL}")
        driver.get(SLIDES_URL)
        
        # Wait for the presentation to load
        wait_for_element(driver, By.CSS_SELECTOR, "div.punch-viewer-content")
        print("Google Slides loaded. Starting slide updates...")
        
        # Update slides
        update_slides(driver, args.start, args.end)
        
        print("\nSlide updates completed!")
        print("Note: The browser will remain open so you can review the changes.")
        
    except Exception as e:
        print(f"Error during slides update: {str(e)}")
    
    # Browser will remain open due to the detach option

if __name__ == "__main__":
    main()