#!/usr/bin/env python3

import os
import time
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
INVESTOR_SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides"
SLIDES_ORDER = [f"slide{i:02d}.md" for i in range(1, 22)]  # slide01.md to slide21.md

def parse_markdown_slide(file_path):
    """Extract title, subtitle, and content from a markdown slide file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract title, subtitle, and content
    title_match = re.search(r'# (.+)', content)
    subtitle_match = re.search(r'## (.+)', content)
    summary_match = re.search(r'\*([^*]+)\*', content)
    
    title = title_match.group(1) if title_match else ""
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    summary = summary_match.group(1) if summary_match else ""
    
    # Extract bullet points and other content (simplified for now)
    content_section = content.split('![')[0].split('##')[2] if '##' in content else ""
    content_section = '\n'.join([line for line in content_section.split('\n') if line.strip() and not line.strip().startswith('[') and not line.strip().startswith('*')])
    
    return {
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "content": content_section
    }

def setup_webdriver():
    """Set up and configure the Chrome WebDriver."""
    chrome_options = Options()
    # Uncomment the line below if you want to run in headless mode
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Install and set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_to_google(driver):
    """Handle Google login (if needed)."""
    # This is a placeholder. Google login can be complex due to various security measures
    # You might need to update this based on your specific login flow
    
    try:
        # Check if login is needed
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        )
        
        # Enter email
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys("YOUR_EMAIL@gmail.com")  # Replace with your email
        email_input.send_keys(Keys.RETURN)
        
        # Wait for password field and enter password
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("YOUR_PASSWORD")  # Replace with your password
        password_input.send_keys(Keys.RETURN)
        
        # Wait for login to complete
        time.sleep(5)
    except TimeoutException:
        # Login page not found, already logged in
        print("No login needed or already logged in")
        pass

def update_slide_content(driver, slide_num, slide_data):
    """Update the content of a specific slide."""
    # Select the slide
    print(f"Updating slide {slide_num}...")
    
    # Locate the slide and click on it
    try:
        # This is a simplified approach - you might need to adjust the selectors
        slide_selector = f"div.punch-viewer-content div.punch-viewer-slide:nth-child({slide_num})"
        slide = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, slide_selector))
        )
        slide.click()
        time.sleep(1)  # Wait for slide to be active
        
        # Double-click to edit title
        title_element = slide.find_element(By.CSS_SELECTOR, ".punch-viewer-title")
        ActionChains(driver).double_click(title_element).perform()
        # Clear existing content and type new title
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        ActionChains(driver).send_keys(slide_data["title"]).perform()
        
        # Similar approach for subtitle and content
        # Note: This is simplified and might need adjustment based on the actual structure
        
        print(f"Updated slide {slide_num}")
    except Exception as e:
        print(f"Error updating slide {slide_num}: {e}")

def main():
    """Main function to update Google Slides."""
    # Load slide data
    slides_data = []
    for slide_file in SLIDES_ORDER:
        file_path = os.path.join(INVESTOR_SLIDES_DIR, slide_file)
        if os.path.exists(file_path):
            slide_data = parse_markdown_slide(file_path)
            slides_data.append(slide_data)
    
    # Set up WebDriver
    driver = setup_webdriver()
    
    try:
        # Open the Google Slides presentation
        driver.get(SLIDES_URL)
        time.sleep(5)  # Wait for page to load
        
        # Handle login if needed
        login_to_google(driver)
        
        # Wait for the presentation to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.punch-viewer-content"))
        )
        
        # Update each slide
        for slide_num, slide_data in enumerate(slides_data, start=1):
            update_slide_content(driver, slide_num, slide_data)
            time.sleep(1)  # Pause between slides
        
        print("Slides update completed!")
        
    except Exception as e:
        print(f"Error during slides update: {e}")
    finally:
        # Keep the browser open for a while to see the results
        time.sleep(10)
        driver.quit()

if __name__ == "__main__":
    main()