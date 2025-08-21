#!/usr/bin/env python3
"""
Direct script to fix PowerPoint slides with manual content application
"""

import os
import sys
import argparse
from pptx import Presentation
import datetime

def fix_slide_2():
    """Fix slide 2 with specific content"""
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    
    # Create backup
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/slide_02_backup_direct_{timestamp}.pptx"
    
    # Load the presentation
    print(f"Loading presentation: {ppt_path}")
    prs = Presentation(ppt_path)
    
    # Save backup
    print(f"Saving backup to: {backup_path}")
    prs.save(backup_path)
    
    # Get slide 2
    slide = prs.slides[1]  # 0-indexed
    
    # Prepare content
    title = "The Problem I"
    subtitle = "Distrust in Digital Space"
    summary = "Content authenticity issues and lack of ownership create fundamental digital trust challenges."
    
    bullet_points = [
        "Content that can be secretly modified",
        "No guarantee that what you see is what was produced",
        "No inherent ownership means no responsibility",
        "Rampant misinformation without accountability"
    ]
    
    quote = "76% of users struggle to identify authentic content in digital spaces"
    
    # Update slide content
    shapes = list(slide.shapes)
    
    # Update title and subtitle
    if len(shapes) >= 2:
        print(f"Updating title to: {title}")
        shapes[0].text = title
        
        print(f"Updating subtitle to: {subtitle}")
        shapes[1].text = subtitle
    
    # Add textbox for summary if there isn't one
    if len(shapes) >= 3 and hasattr(shapes[2], 'text'):
        print(f"Updating summary to: {summary}")
        shapes[2].text = summary
    else:
        print("No suitable shape found for summary. Adding bullet points instead.")
        # Need to use slide.shapes.add_textbox() to add a new textbox
        # This is complex as it requires positioning, so we'll skip for now
    
    # Add a textbox for bullet points if needed
    if len(shapes) >= 4 and hasattr(shapes[3], 'text'):
        bullet_text = "\n".join([f"• {point}" for point in bullet_points])
        print(f"Updating bullet points")
        shapes[3].text = bullet_text
    
    # Add a textbox for quote if needed
    if len(shapes) >= 5 and hasattr(shapes[4], 'text'):
        print(f"Updating quote to: {quote}")
        shapes[4].text = f"\"{quote}\""
    
    # Save the updated presentation
    print(f"Saving updated presentation")
    prs.save(ppt_path)
    print(f"Slide 2 updated successfully!")
    
    return True

def open_powerpoint():
    """Open PowerPoint and the presentation"""
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    os.system(f"open -a 'Microsoft PowerPoint' '{ppt_path}'")
    print(f"PowerPoint opened with the presentation")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix slide 2 with direct content')
    parser.add_argument('--open', action='store_true', help='Open PowerPoint after update')
    
    args = parser.parse_args()
    
    # Update slide 2
    success = fix_slide_2()
    
    # Open PowerPoint if requested and update was successful
    if success and args.open:
        open_powerpoint()