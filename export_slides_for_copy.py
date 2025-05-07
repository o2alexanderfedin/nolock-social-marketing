#!/usr/bin/env python3

import os
import re
import json
from pathlib import Path

# Configuration
INVESTOR_SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides"
OUTPUT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
SLIDES_ORDER = [f"slide{i:02d}.md" for i in range(1, 22)]  # slide01.md to slide21.md

def parse_markdown_slide(file_path):
    """Extract title, subtitle, summary and content from a markdown slide file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Remove navigation links and separators
    content = re.sub(r'\[← Previous\].+?\[Next →\].+?---', '', content, flags=re.DOTALL)
    content = re.sub(r'---\s+\[← Previous\].+?\[Next →\].*$', '', content, flags=re.DOTALL)
    content = re.sub(r'\[Back to Deck Overview\]\(.*?\)', '', content)
    
    # Extract title, subtitle, and summary
    title_match = re.search(r'# (.+)', content)
    subtitle_match = re.search(r'## (.+)', content)
    summary_match = re.search(r'\*([^*]+)\*', content)
    
    title = title_match.group(1) if title_match else ""
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    summary = summary_match.group(1).strip() if summary_match else ""
    
    # Remove image reference
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    
    # Extract main content (everything after the summary)
    if summary_match:
        parts = content.split(f"*{summary}*", 1)
        main_content = parts[1].strip() if len(parts) > 1 else ""
    else:
        # If no summary, try to get content after subtitle
        if subtitle_match:
            parts = content.split(f"## {subtitle}", 1)
            main_content = parts[1].strip() if len(parts) > 1 else ""
        else:
            main_content = ""
    
    # Extract bullet points
    bullet_points = []
    for line in main_content.split('\n'):
        line = line.strip()
        if line.startswith('-') or line.startswith('*') or re.match(r'^\d+\.', line):
            bullet_points.append(line)
    
    # Process content to handle markdown syntax
    # Extract source links
    source_links = []
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(link_pattern, main_content):
        text, url = match.groups()
        source_links.append(f"{text}: {url}")
    
    # Handle blockquotes
    quotes = []
    quote_pattern = r'> *(.*)'
    for match in re.finditer(quote_pattern, main_content):
        quotes.append(match.group(1))
    
    return {
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "bullet_points": bullet_points,
        "source_links": source_links,
        "quotes": quotes,
        "raw_content": main_content
    }

def format_for_export(slide_data, slide_number):
    """Format slide data for easy copying into Google Slides."""
    formatted = f"# Slide {slide_number}: {slide_data['title']}\n\n"
    
    formatted += "## Title\n"
    formatted += slide_data['title'] + "\n\n"
    
    formatted += "## Subtitle\n"
    formatted += slide_data['subtitle'] + "\n\n"
    
    formatted += "## Summary\n"
    formatted += slide_data['summary'] + "\n\n"
    
    if slide_data['bullet_points']:
        formatted += "## Bullet Points\n"
        for point in slide_data['bullet_points']:
            formatted += point + "\n"
        formatted += "\n"
    
    if slide_data['source_links']:
        formatted += "## Sources\n"
        for link in slide_data['source_links']:
            formatted += link + "\n"
        formatted += "\n"
    
    if slide_data['quotes']:
        formatted += "## Quotes\n"
        for quote in slide_data['quotes']:
            formatted += "> " + quote + "\n"
        formatted += "\n"
    
    return formatted

def main():
    """Main function to export slides for easy copying."""
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Create a comprehensive export file
    all_slides_path = os.path.join(OUTPUT_DIR, "all_slides_export.md")
    all_slides_content = "# NoLock Social Investor Pitch Deck - Content for Google Slides\n\n"
    all_slides_content += "This document contains formatted content from all slides for easy copying into Google Slides.\n\n"
    all_slides_content += "---\n\n"
    
    # Process each slide
    for slide_index, slide_file in enumerate(SLIDES_ORDER, start=1):
        file_path = os.path.join(INVESTOR_SLIDES_DIR, slide_file)
        if os.path.exists(file_path):
            # Parse the slide content
            slide_data = parse_markdown_slide(file_path)
            
            # Format for export
            formatted_content = format_for_export(slide_data, slide_index)
            
            # Save individual slide export
            individual_slide_path = os.path.join(OUTPUT_DIR, f"slide{slide_index:02d}_export.md")
            with open(individual_slide_path, 'w') as f:
                f.write(formatted_content)
            
            # Add to comprehensive export
            all_slides_content += formatted_content
            all_slides_content += "---\n\n"
            
            print(f"Processed {slide_file}")
        else:
            print(f"Warning: Could not find {file_path}")
    
    # Save comprehensive export
    with open(all_slides_path, 'w') as f:
        f.write(all_slides_content)
    
    print(f"\nExport completed! All content is available in:\n{all_slides_path}")
    print(f"Individual slide exports are available in the {OUTPUT_DIR} directory.")

if __name__ == "__main__":
    main()