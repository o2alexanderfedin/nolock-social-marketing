#!/usr/bin/env python3
"""
Script to fix content on slide 6, preserving all section headers and formatting
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def fix_slide6_content():
    """Fix slide 6 content to include all section headers and formatting"""
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    
    # Create backup
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/slide_06_fixed_{timestamp}.pptx"
    
    # Load the presentation
    print(f"Loading presentation: {ppt_path}")
    prs = Presentation(ppt_path)
    
    # Save backup
    print(f"Saving backup to: {backup_path}")
    prs.save(backup_path)
    
    # Get slide 6
    slide = prs.slides[5]  # 0-indexed
    
    # Prepare comprehensive content with all formatting
    content = [
        {"text": "A rapidly growing $12B market projected to reach $101B by 2033 with clear TAM/SAM/SOM breakdown.", "bold": False, "italic": True, "size": 12},
        {"text": "", "bold": False, "italic": False, "size": 11},
        {"text": "Market Analysis:", "bold": True, "italic": False, "size": 12, "header": True},
        {"text": "", "bold": False, "italic": False, "size": 11},
        {"text": "Total Addressable Market (TAM):", "bold": True, "italic": False, "size": 11, "header": True},
        {"text": "• $12.13 billion in 2023", "bold": False, "italic": False, "size": 11},
        {"text": "• Projected to reach $101.2 billion by 2033", "bold": False, "italic": False, "size": 11},
        {"text": "• 25% CAGR", "bold": False, "italic": False, "size": 11},
        {"text": "• Source: Market Research Future (MRFR)", "bold": False, "italic": False, "size": 10, "url": True},
        {"text": "", "bold": False, "italic": False, "size": 11},
        {"text": "Serviceable Addressable Market (SAM):", "bold": True, "italic": False, "size": 11, "header": True},
        {"text": "• $4.8 billion (40% of TAM)", "bold": False, "italic": False, "size": 11},
        {"text": "• Identity & content verification segments", "bold": False, "italic": False, "size": 11},
        {"text": "• Source: Grand View Research", "bold": False, "italic": False, "size": 10, "url": True},
        {"text": "", "bold": False, "italic": False, "size": 11},
        {"text": "Serviceable Obtainable Market (SOM):", "bold": True, "italic": False, "size": 11, "header": True},
        {"text": "• Year 1: $24 million (0.5% of SAM)", "bold": False, "italic": False, "size": 11},
        {"text": "• Year 3: $240 million (5% of SAM)", "bold": False, "italic": False, "size": 11},
        {"text": "• Based on projected adoption rates for Web3 technologies", "bold": False, "italic": False, "size": 11, "url": True}
    ]
    
    # Identify all text shapes on the slide
    shapes = list(slide.shapes)
    
    # Remove previously added text boxes
    if len(shapes) > 3:
        print(f"Removing {len(shapes) - 3} previously added shapes")
        for i in range(len(shapes) - 1, 2, -1):
            shape = shapes[i]
            # We can't directly remove shapes, but we can make them invisible
            shape.left = -10000000
            shape.width = 0
            shape.height = 0
    
    # Add new comprehensive text box
    print("Adding new comprehensive text box")
    content_textbox = slide.shapes.add_textbox(
        Inches(1),       # left
        Inches(2.5),     # top
        Inches(8),       # width
        Inches(4.5)      # height
    )
    
    # Add content with proper formatting
    tf = content_textbox.text_frame
    tf.word_wrap = True
    
    # Add first paragraph
    p = tf.paragraphs[0]
    p.text = content[0]["text"]
    run = p.runs[0]
    run.font.bold = content[0].get("bold", False)
    run.font.italic = content[0].get("italic", False)
    run.font.size = Pt(content[0].get("size", 11))
    
    # Add remaining paragraphs
    for item in content[1:]:
        p = tf.add_paragraph()
        p.text = item["text"]
        
        # Format paragraph
        if item.get("header", False):
            p.space_before = Pt(6)  # Add space before headings
            
        # Format run
        run = p.runs[0]
        run.font.bold = item.get("bold", False)
        run.font.italic = item.get("italic", False)
        run.font.size = Pt(item.get("size", 11))
        
        # Mark URLs in blue
        if item.get("url", False):
            run.font.color.rgb = RGBColor(0, 0, 255)
            run.font.underline = True
    
    # Save the updated presentation
    print("Saving updated presentation")
    prs.save(ppt_path)
    print("Slide 6 content fixed!")
    
    return True

def open_powerpoint():
    """Open PowerPoint and the presentation"""
    ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    os.system(f"open -a 'Microsoft PowerPoint' '{ppt_path}'")
    print("PowerPoint opened with the presentation")

if __name__ == "__main__":
    # Fix slide 6
    success = fix_slide6_content()
    
    # Open PowerPoint
    if success:
        open_powerpoint()