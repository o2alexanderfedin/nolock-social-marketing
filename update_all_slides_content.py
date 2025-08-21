#!/usr/bin/env python3
"""
Script to update all PowerPoint slides with content from markdown files
"""

import os
import re
import sys
import argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import datetime

class SlideUpdater:
    """Class to handle slide updates with content from markdown files"""
    
    def __init__(self):
        """Initialize the slide updater"""
        self.ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
        self.markdown_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/"
        self.slides_export_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export/"
        self.current_slide = 0
        
        # Create backup
        self.create_backup()
        
        # Load the presentation
        print(f"Loading presentation: {self.ppt_path}")
        self.prs = Presentation(self.ppt_path)
        
    def create_backup(self):
        """Create a backup of the presentation"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL_backup_{timestamp}.pptx"
        
        # Copy the file for backup
        print(f"Creating backup: {backup_path}")
        import shutil
        shutil.copy2(self.ppt_path, backup_path)
        
    def extract_markdown_content(self, slide_num):
        """Extract content from markdown file for a slide"""
        formatted_num = f"{slide_num:02d}"
        md_path = os.path.join(self.markdown_dir, f"slide{formatted_num}.md")
        export_path = os.path.join(self.slides_export_dir, f"slide{formatted_num}_export.md")
        
        # Check if markdown file exists
        if not os.path.exists(md_path):
            print(f"Warning: Markdown file not found for slide {slide_num}: {md_path}")
            return None
        
        # Read markdown content
        with open(md_path, 'r') as f:
            content = f.read()
        
        # Extract title (first # heading)
        title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else ""
        
        # Extract subtitle (first ## heading)
        subtitle_match = re.search(r'^## (.+?)$', content, re.MULTILINE)
        subtitle = subtitle_match.group(1) if subtitle_match else ""
        
        # Extract summary (content right after subtitle - usually in italics)
        summary = ""
        summary_match = re.search(r'^## .+?\n\*(.+?)\*', content, re.DOTALL)
        if summary_match:
            summary = summary_match.group(1).strip()
        
        # Also try to get summary from export file if it exists
        if os.path.exists(export_path):
            with open(export_path, 'r') as f:
                export_content = f.read()
            
            export_summary_match = re.search(r'## Summary\n(.*?)(?=\n\n|\Z)', export_content, re.DOTALL)
            if export_summary_match and not summary:
                summary = export_summary_match.group(1).strip()
        
        # Extract bullet points (starting with - or * in main content area)
        bullet_points = []
        
        # Look for common section headers in investor pitch deck
        section_headers = [
            "## Critical Issues:", "## Key Points:", "## Core Technology:", 
            "## Market Analysis:", "## Two-Pronged Approach:", "## Core Technology:",
            "## Three Critical Market Failures:", "## Building a New Trust Layer:",
            "## Serious Vulnerabilities:", "## Fundamental Design Flaws:",
            "## Key Milestones", "## Use of Funds", "## Seeking"
        ]
        
        section_match = None
        for header in section_headers:
            if header in content:
                section_match = re.search(re.escape(header), content)
                if section_match:
                    break
        
        if section_match:
            section_start = section_match.start()
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
                    bullet_points.append({
                        "text": bullet_text,
                        "bold": "**" in line,
                        "level": 0 if not line.startswith("  ") else 1,
                        "italic": "*" in line and not line.startswith("*"),
                        "color": "blue" if "Source:" in line or "source:" in line else None
                    })
        
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
            'quote': quote
        }
    
    def update_slide(self, slide_num):
        """Update a specific slide with content from markdown"""
        self.current_slide = slide_num
        print(f"\n===== Updating Slide {slide_num} =====")
        
        # Extract content
        content = self.extract_markdown_content(slide_num)
        if not content:
            print(f"Skipping slide {slide_num} - no content found")
            return False
        
        # Print extracted content summary
        print(f"Extracted content:")
        print(f"  Title: {content['title']}")
        print(f"  Subtitle: {content['subtitle']}")
        print(f"  Summary: {content['summary'][:50]}..." if len(content['summary']) > 50 else f"  Summary: {content['summary']}")
        print(f"  Bullet Points: {len(content['bullet_points'])}")
        if content['quote']:
            print(f"  Quote: \"{content['quote'][:50]}..." if len(content['quote']) > 50 else f"  Quote: \"{content['quote']}\"")
        
        # Get the slide (0-indexed)
        if slide_num > len(self.prs.slides):
            print(f"Error: Slide {slide_num} does not exist (total slides: {len(self.prs.slides)})")
            return False
        
        slide = self.prs.slides[slide_num - 1]
        
        # Update the slide
        self.apply_content_to_slide(slide, content)
        
        return True
    
    def apply_content_to_slide(self, slide, content):
        """Apply content to a slide"""
        # Get original shapes
        original_shapes = list(slide.shapes)
        
        # Record how many shapes were originally on the slide
        original_shape_count = len(original_shapes)
        print(f"Original shape count: {original_shape_count}")
        
        # Clear any previously added text boxes (optional)
        if original_shape_count > 3:  # Assuming first 3 are title, subtitle, and image
            print(f"Removing {original_shape_count - 3} previously added shapes")
            for i in range(len(original_shapes) - 1, 2, -1):
                shape = original_shapes[i]
                # We can't directly remove shapes, but we can make them invisible
                shape.left = -10000000
                shape.width = 0
                shape.height = 0
        
        # Update title and subtitle (shapes 1 and 2)
        if original_shape_count >= 1 and content['title']:
            title_shape = original_shapes[0]
            print(f"Updating title to: {content['title']}")
            if hasattr(title_shape, 'text_frame'):
                title_shape.text_frame.text = content['title']
        
        if original_shape_count >= 2 and content['subtitle']:
            subtitle_shape = original_shapes[1]
            print(f"Updating subtitle to: {content['subtitle']}")
            if hasattr(subtitle_shape, 'text_frame'):
                subtitle_shape.text_frame.text = content['subtitle']
        
        # Add summary text box
        if content['summary']:
            print("Adding summary text box")
            summary_textbox = slide.shapes.add_textbox(
                Inches(1),       # left
                Inches(2.5),     # top
                Inches(8),       # width
                Inches(0.75)     # height
            )
            summary_textbox.text_frame.text = content['summary']
            # Format paragraph
            p = summary_textbox.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.runs[0]
            run.font.italic = True
            run.font.size = Pt(12)
        
        # Add bullet points if any
        if content['bullet_points']:
            print(f"Adding bullet points text box ({len(content['bullet_points'])} points)")
            bullets_textbox = slide.shapes.add_textbox(
                Inches(1),       # left
                Inches(3.5 if content['summary'] else 2.8),  # top (adjust based on summary)
                Inches(7),       # width
                Inches(2.5)      # height
            )
            
            # Add bullet points with proper formatting
            tf = bullets_textbox.text_frame
            tf.text = ""  # Clear default text
            
            for i, point in enumerate(content['bullet_points']):
                p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
                p.text = point["text"]
                p.level = point.get("level", 0)
                
                # Format run
                run = p.runs[0]
                run.font.bold = point.get("bold", False)
                run.font.italic = point.get("italic", False)
                run.font.size = Pt(11) if point.get("level", 0) == 0 else Pt(10)
                
                if point.get("color") == "blue":
                    run.font.color.rgb = RGBColor(0, 0, 255)
                    run.font.size = Pt(9)  # Smaller for source references
        
        # Add quote if any
        if content['quote']:
            print(f"Adding quote text box: \"{content['quote'][:30]}...\"" if len(content['quote']) > 30 else f"Adding quote text box: \"{content['quote']}\"")
            quote_textbox = slide.shapes.add_textbox(
                Inches(1),       # left
                Inches(6),       # top
                Inches(8),       # width
                Inches(0.75)     # height
            )
            quote_textbox.text_frame.text = f"\"{content['quote']}\""
            # Format paragraph
            p = quote_textbox.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            run = p.runs[0]
            run.font.italic = True
            run.font.size = Pt(11)
    
    def update_all_slides(self):
        """Update all slides in the presentation"""
        # Get total number of slides
        total_slides = len(self.prs.slides)
        print(f"Updating all {total_slides} slides")
        
        # Process each slide
        updated_count = 0
        for slide_num in range(1, total_slides + 1):
            success = self.update_slide(slide_num)
            if success:
                updated_count += 1
        
        # Save the presentation
        print(f"\nSaving presentation with {updated_count} updated slides")
        self.prs.save(self.ppt_path)
        print("All slides updated successfully!")
        
        return updated_count
    
    def open_powerpoint(self):
        """Open PowerPoint with the presentation"""
        os.system(f"open -a 'Microsoft PowerPoint' '{self.ppt_path}'")
        print("PowerPoint opened with the presentation")
    
    def goto_slide(self, slide_num):
        """Go to a specific slide in PowerPoint (via AppleScript)"""
        # Construct and run the AppleScript
        script = f'''
        tell application "Microsoft PowerPoint"
            activate
            tell document 1
                go to slide {slide_num}
            end tell
        end tell
        '''
        os.system(f"osascript -e '{script}'")
        print(f"Navigated to slide {slide_num}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Update PowerPoint slides with content from markdown files')
    parser.add_argument('--slide', type=int, help='Update a specific slide')
    parser.add_argument('--all', action='store_true', help='Update all slides')
    parser.add_argument('--open', action='store_true', help='Open PowerPoint after update')
    
    args = parser.parse_args()
    
    # Create slide updater
    updater = SlideUpdater()
    
    # Update slides
    if args.slide:
        # Update a specific slide
        success = updater.update_slide(args.slide)
        if success:
            # Save the presentation
            print(f"Saving presentation")
            updater.prs.save(updater.ppt_path)
            print(f"Slide {args.slide} updated successfully!")
            
            # Open PowerPoint if requested
            if args.open:
                updater.open_powerpoint()
                # Try to go to the specific slide
                updater.goto_slide(args.slide)
    elif args.all:
        # Update all slides
        updated_count = updater.update_all_slides()
        
        # Open PowerPoint if requested
        if args.open:
            updater.open_powerpoint()
    else:
        print("Please specify either --slide or --all")

if __name__ == "__main__":
    main()