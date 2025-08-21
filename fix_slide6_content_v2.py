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
        "A rapidly growing $12B market projected to reach $101B by 2033 with clear TAM/SAM/SOM breakdown.",
        "",
        "Market Analysis:",
        "",
        "Total Addressable Market (TAM):",
        "• $12.13 billion in 2023",
        "• Projected to reach $101.2 billion by 2033",
        "• 25% CAGR",
        "• Source: Market Research Future (MRFR)",
        "",
        "Serviceable Addressable Market (SAM):",
        "• $4.8 billion (40% of TAM)",
        "• Identity & content verification segments",
        "• Source: Grand View Research",
        "",
        "Serviceable Obtainable Market (SOM):",
        "• Year 1: $24 million (0.5% of SAM)",
        "• Year 3: $240 million (5% of SAM)",
        "• Based on projected adoption rates for Web3 technologies"
    ]
    
    # Define formatting indexes
    italic_indexes = [0]
    bold_indexes = [2, 4, 10, 15]
    url_indexes = [8, 13, 18]
    
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
    
    # Add each paragraph with its formatting
    for i, text in enumerate(content):
        # Add paragraph
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        
        # Set paragraph text
        p.text = text
        
        # Only format non-empty paragraphs
        if text:
            # Add formatting to the run
            run = p.runs[0]
            
            # Apply formatting based on index
            if i in bold_indexes:
                run.font.bold = True
                run.font.size = Pt(12)
            else:
                run.font.bold = False
                run.font.size = Pt(11)
                
            if i in italic_indexes:
                run.font.italic = True
            else:
                run.font.italic = False
                
            if i in url_indexes:
                run.font.color.rgb = RGBColor(0, 0, 255)
                run.font.underline = True
                run.font.size = Pt(10)
    
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