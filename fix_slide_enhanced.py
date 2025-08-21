#!/usr/bin/env python3
"""
Enhanced script to fix PowerPoint slides with better content extraction and application
"""

import os
import re
import sys
import argparse
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import datetime
import subprocess

def extract_markdown_content(markdown_path):
    """Extract comprehensive content from markdown file"""
    with open(markdown_path, 'r') as f:
        content = f.read()
    
    # Extract title (first # heading)
    title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else None
    
    # Extract subtitle (first ## heading)
    subtitle_match = re.search(r'^## (.+?)$', content, re.MULTILINE)
    subtitle = subtitle_match.group(1) if subtitle_match else None
    
    # Extract summary (content right after subtitle - usually in italics)
    summary = ""
    summary_match = re.search(r'^## .+?\n\*(.+?)\*', content, re.DOTALL)
    if summary_match:
        summary = summary_match.group(1).strip()
    
    # Extract bullet points (starting with - or * in main content area)
    bullet_points = []
    bullet_section = re.search(r'## Critical Issues:|## Key Points:|## Core Technology:|## Market Analysis:|## Two-Pronged Approach:|## Core Technology:', content)
    if bullet_section:
        section_start = bullet_section.start()
        section_text = content[section_start:]
        # Find end of section (next heading or end of file)
        end_match = re.search(r'\n\n>|\n\n---', section_text)
        if end_match:
            section_text = section_text[:end_match.start()]
        
        # Extract all bullet points
        lines = section_text.split('\n')
        for line in lines:
            # Match lines starting with bullet indicators and possibly having nested bullets
            if re.match(r'^\s*[-*•]\s+(.+)$', line):
                bullet_text = re.sub(r'^\s*[-*•]\s+', '', line).strip()
                # Remove markdown links but keep the text
                bullet_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', bullet_text)
                bullet_points.append(bullet_text)
            # Capture nested bullets with more indent
            elif re.match(r'^\s+[-*•]\s+(.+)$', line):
                bullet_text = re.sub(r'^\s+[-*•]\s+', '  • ', line).strip()
                bullet_text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', bullet_text)
                bullet_points.append(bullet_text)
    
    # Extract quote (if any)
    quote = ""
    quote_match = re.search(r'> *(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if quote_match:
        quote = quote_match.group(1).strip()
        # Clean up the quote
        quote = quote.replace('*', '').strip()
    
    return {
        'title': title,
        'subtitle': subtitle,
        'summary': summary,
        'bullet_points': bullet_points,
        'quote': quote,
        'full_content': content  # Keep full content for reference
    }

def print_shape_info(shapes):
    """Print information about shapes for debugging"""
    print("\nShape information:")
    for i, shape in enumerate(shapes):
        shape_type = "Unknown"
        if shape.shape_type == MSO_SHAPE_TYPE.PLACEHOLDER:
            shape_type = "Placeholder"
        elif shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
            shape_type = "AutoShape"
        elif shape.shape_type == MSO_SHAPE_TYPE.TEXT_BOX:
            shape_type = "TextBox"
            
        text = ""
        if hasattr(shape, 'text'):
            text = shape.text[:50] + "..." if len(shape.text) > 50 else shape.text
            
        print(f"Shape {i+1}: Type={shape_type}, Text=\"{text}\"")

def clean_and_update_slide(slide_num):
    """Clean and update a specific slide in the PowerPoint presentation"""
    # File paths
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    formatted_num = f"{slide_num:02d}"
    md_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide{formatted_num}.md"
    
    # Create backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/slide_{formatted_num}_backup_{timestamp}.pptx"
    
    # Check if markdown file exists
    if not os.path.exists(md_path):
        print(f"Error: Markdown file not found: {md_path}")
        return False
    
    # Extract content from markdown
    content = extract_markdown_content(md_path)
    print(f"\nExtracted content for slide {slide_num}:")
    print(f"  Title: {content['title']}")
    print(f"  Subtitle: {content['subtitle']}")
    print(f"  Summary: {content['summary']}")
    print(f"  Bullet points: {len(content['bullet_points'])}")
    for i, bp in enumerate(content['bullet_points']):
        print(f"    - {bp[:60]}..." if len(bp) > 60 else f"    - {bp}")
    if content['quote']:
        print(f"  Quote: \"{content['quote']}\"")
    
    # Load the presentation
    print(f"\nLoading presentation: {ppt_path}")
    prs = Presentation(ppt_path)
    
    # Save backup
    print(f"Saving backup to: {backup_path}")
    prs.save(backup_path)
    
    # Get the slide (0-indexed)
    if slide_num > len(prs.slides):
        print(f"Error: Slide {slide_num} does not exist (total slides: {len(prs.slides)})")
        return False
    
    slide = prs.slides[slide_num - 1]
    
    # Analyze slide shapes
    shapes = list(slide.shapes)
    print_shape_info(shapes)
    
    # Clean and update the slide
    print(f"\nUpdating slide {slide_num}...")
    
    # Try to identify shapes based on their text content and position
    title_shape = None
    subtitle_shape = None
    summary_shape = None
    content_shapes = []
    quote_shape = None
    
    # First two shapes with text are usually title and subtitle
    text_shapes = [s for s in shapes if hasattr(s, 'text') and s.text.strip()]
    
    if len(text_shapes) >= 1:
        title_shape = text_shapes[0]
    
    if len(text_shapes) >= 2:
        subtitle_shape = text_shapes[1]
    
    # Look for a shape that contains a quote (often at the bottom)
    for shape in text_shapes[2:] if len(text_shapes) > 2 else []:
        if shape.text.strip().startswith('"') or shape.text.strip().startswith('*') or '—' in shape.text:
            quote_shape = shape
            break
    
    # Remaining shapes with text are potential content areas
    content_shapes = [s for s in text_shapes[2:] if s != quote_shape]
    
    # Update title and subtitle
    if title_shape and content['title']:
        print(f"  - Setting title: '{content['title']}'")
        title_shape.text = content['title']
    
    if subtitle_shape and content['subtitle']:
        print(f"  - Setting subtitle: '{content['subtitle']}'")
        subtitle_shape.text = content['subtitle']
    
    # Update summary if available
    if len(content_shapes) >= 1 and content['summary']:
        summary_shape = content_shapes[0]
        print(f"  - Setting summary: '{content['summary']}'")
        summary_shape.text = content['summary']
        content_shapes = content_shapes[1:]
    
    # Update bullet points if available
    if content_shapes and content['bullet_points']:
        main_content_shape = content_shapes[0]
        bullet_text = '\n'.join([f"• {point}" for point in content['bullet_points']])
        print(f"  - Setting {len(content['bullet_points'])} bullet points to shape")
        main_content_shape.text = bullet_text
    
    # Update quote if available
    if quote_shape and content['quote']:
        print(f"  - Setting quote: '{content['quote']}'")
        quote_shape.text = f"\"{content['quote']}\""
    
    # Save the updated presentation
    print(f"\nSaving updated presentation")
    prs.save(ppt_path)
    print(f"Slide {slide_num} updated successfully!")
    
    return True

def open_powerpoint():
    """Open PowerPoint and the presentation"""
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    os.system(f"open -a 'Microsoft PowerPoint' '{ppt_path}'")
    print(f"PowerPoint opened with the presentation")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix a specific PowerPoint slide with enhanced content')
    parser.add_argument('slide_num', type=int, help='Slide number to fix')
    parser.add_argument('--open', action='store_true', help='Open PowerPoint after update')
    
    args = parser.parse_args()
    
    # Update the slide
    success = clean_and_update_slide(args.slide_num)
    
    # Open PowerPoint if requested and update was successful
    if success and args.open:
        open_powerpoint()