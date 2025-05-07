#!/usr/bin/env python3

import os
import re
import time
import json
import markdown
from pathlib import Path
from playwright.sync_api import sync_playwright

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
INVESTOR_SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides"
SLIDES_ORDER = [f"slide{i:02d}.md" for i in range(1, 22)]  # slide01.md to slide21.md

def parse_markdown_slide(file_path):
    """Extract title, subtitle, summary and content from a markdown slide file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Remove navigation links and separators
    content = re.sub(r'\[← Previous\].+?\[Next →\].+?---', '', content, flags=re.DOTALL)
    content = re.sub(r'---\s+\[← Previous\].+?\[Next →\].*$', '', content, flags=re.DOTALL)
    
    # Extract title, subtitle, and summary
    title_match = re.search(r'# (.+)', content)
    subtitle_match = re.search(r'## (.+)', content)
    summary_match = re.search(r'\*([^*]+)\*', content)
    
    title = title_match.group(1) if title_match else ""
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    summary = summary_match.group(1).strip() if summary_match else ""
    
    # Extract content (everything after the summary)
    if summary_match:
        content_parts = content.split(f"*{summary}*", 1)
        if len(content_parts) > 1:
            content_section = content_parts[1].strip()
        else:
            content_section = ""
    else:
        content_parts = content.split('##', 2)
        if len(content_parts) > 2:
            content_section = content_parts[2].strip()
        else:
            content_section = ""
    
    # Clean up content section to remove image references and navigation links
    content_section = re.sub(r'!\[.*?\]\(.*?\)', '', content_section)
    content_section = re.sub(r'\[Back to Deck Overview\]\(.*?\)', '', content_section)
    
    # Convert markdown to plaintext (simple approach)
    # In a more sophisticated version, you would parse and format the markdown properly
    plaintext = content_section
    
    # Clean up content lines
    content_lines = []
    for line in plaintext.split('\n'):
        line = line.strip()
        if line:
            content_lines.append(line)
    
    formatted_content = "\n".join(content_lines)
    
    return {
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "content": formatted_content
    }

def main():
    """Main function to update Google Slides using Playwright."""
    # Load slide data
    print("Loading slide data...")
    slides_data = []
    for slide_file in SLIDES_ORDER:
        file_path = os.path.join(INVESTOR_SLIDES_DIR, slide_file)
        if os.path.exists(file_path):
            slide_data = parse_markdown_slide(file_path)
            slides_data.append(slide_data)
            print(f"Processed {slide_file}")
        else:
            print(f"Warning: Could not find {file_path}")
    
    # Launch browser with Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for production
        context = browser.new_context()
        page = context.new_page()
        
        # Go to Google Slides
        print(f"Navigating to {SLIDES_URL}...")
        page.goto(SLIDES_URL)
        
        # Wait for the presentation to load - this selector will depend on the actual structure
        page.wait_for_selector('.punch-viewer-svgpage-a', timeout=60000)
        
        # Wait a moment for everything to fully load
        time.sleep(5)
        
        print("Presentation loaded. Starting to update slides...")
        
        # Loop through each slide
        for slide_index, slide_data in enumerate(slides_data, start=1):
            try:
                print(f"\nUpdating slide {slide_index} - {slide_data['title']}...")
                
                # Navigate to the specific slide
                page.goto(f"{SLIDES_URL}#slide=id.p{slide_index}")
                page.wait_for_selector('.punch-viewer-svgpage-a', timeout=10000)
                time.sleep(2)  # Wait for slide to fully load
                
                # Enter edit mode (double click on the slide)
                slide_element = page.locator('.punch-viewer-svgpage-a').first
                slide_element.dblclick()
                time.sleep(1)
                
                # Now in edit mode, update title, subtitle, etc.
                # Note: The actual implementation will depend on Google Slides' structure
                # These are placeholder implementations that will need adjustment
                
                # Update title
                title_element = page.locator('text="Click to add title"').first
                if title_element:
                    title_element.click()
                    page.keyboard.press("Control+a")  # Select all text
                    page.keyboard.type(slide_data["title"])
                
                # Update subtitle
                subtitle_element = page.locator('text="Click to add subtitle"').first
                if subtitle_element:
                    subtitle_element.click()
                    page.keyboard.press("Control+a")  # Select all text
                    page.keyboard.type(f"{slide_data['subtitle']}\n\n{slide_data['summary']}")
                
                # Update content
                content_element = page.locator('text="Click to add text"').first
                if content_element:
                    content_element.click()
                    page.keyboard.press("Control+a")  # Select all text
                    page.keyboard.type(slide_data["content"])
                
                # Save changes (Google Slides auto-saves, but let's ensure it has time)
                time.sleep(2)
                
                print(f"Updated slide {slide_index}")
            
            except Exception as e:
                print(f"Error updating slide {slide_index}: {e}")
                # Continue with the next slide if there's an error
        
        print("\nAll slides updated!")
        
        # Close the browser
        time.sleep(5)  # Give a moment to see the final state
        browser.close()

if __name__ == "__main__":
    main()