#!/usr/bin/env python3
"""
Script to comprehensively fix all slides with proper content extraction and formatting
"""

import os
import re
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import time
import datetime

class SlideContentFixer:
    """Class to fix slide content with comprehensive extraction from markdown"""
    
    def __init__(self):
        """Initialize the slide content fixer"""
        self.ppt_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
        self.markdown_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/"
        
        # Create backup of the entire presentation
        self.create_backup()
        
        # Load the presentation
        print(f"Loading presentation: {self.ppt_path}")
        self.prs = Presentation(self.ppt_path)
    
    def create_backup(self):
        """Create a backup of the entire presentation"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL_backup_comprehensive_{timestamp}.pptx"
        
        # Copy the file for backup
        print(f"Creating backup: {backup_path}")
        import shutil
        shutil.copy2(self.ppt_path, backup_path)
    
    def extract_comprehensive_content(self, slide_num):
        """Extract comprehensive content from markdown file for a slide"""
        formatted_num = f"{slide_num:02d}"
        md_path = os.path.join(self.markdown_dir, f"slide{formatted_num}.md")
        
        # Check if markdown file exists
        if not os.path.exists(md_path):
            print(f"Warning: Markdown file not found: {md_path}")
            return None
        
        # Read markdown content
        with open(md_path, 'r') as f:
            content = f.read()
        
        # Extract title (first # heading)
        title_match = re.search(r'^# (.+?)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else ""
        
        # Extract subtitle (first ## heading that isn't a section header)
        subtitle = ""
        subtitle_matches = re.finditer(r'^## ([^:]+?)$', content, re.MULTILINE)
        for match in subtitle_matches:
            potential_subtitle = match.group(1)
            if not any(header in potential_subtitle for header in ["Analysis", "Critical", "Key Points", "Technology", "Market", "Approach", "Key", "Obtaining", "Building", "Core"]):
                subtitle = potential_subtitle
                break
        
        # Extract summary (content right after subtitle - usually in italics)
        summary = ""
        summary_match = re.search(r'^## .+?\n\*(.+?)\*', content, re.DOTALL)
        if summary_match:
            summary = summary_match.group(1).strip()
        
        # Extract all sections (## headings with colons)
        sections = []
        section_matches = re.finditer(r'^## (.+?):$', content, re.MULTILINE)
        for match in section_matches:
            section_name = match.group(1)
            section_start = match.end()
            
            # Find the end of the section
            next_section = re.search(r'^##', content[section_start:], re.MULTILINE)
            horizonal_rule = re.search(r'^---', content[section_start:], re.MULTILINE)
            
            if next_section:
                section_end = section_start + next_section.start()
            elif horizonal_rule:
                section_end = section_start + horizonal_rule.start()
            else:
                section_end = len(content)
            
            section_content = content[section_start:section_end].strip()
            sections.append({
                "name": section_name,
                "content": section_content
            })
        
        # Extract all bullet points (- or * at start of line)
        bullet_points = []
        in_section = False
        current_section = ""
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Check for section headers
            section_match = re.match(r'^## (.+?):$', line)
            if section_match:
                in_section = True
                current_section = section_match.group(1)
                continue
            
            # Check for end of section
            if in_section and (line.startswith('##') or line.startswith('---')):
                in_section = False
                current_section = ""
                continue
            
            # Process bullets within sections
            if in_section and re.match(r'^[ \t]*[-*]\s+', line):
                # Check for bold formatting
                is_bold = '**' in line
                
                # Check for links
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
                link_text = link_match.group(1) if link_match else None
                link_url = link_match.group(2) if link_match else None
                
                # Clean the bullet text
                bullet_text = re.sub(r'^[ \t]*[-*]\s+', '', line)
                
                # Determine indentation level
                level = 1 if line.startswith('  ') else 0
                
                # Add to bullet points
                bullet_points.append({
                    "text": bullet_text,
                    "section": current_section,
                    "level": level,
                    "bold": is_bold,
                    "link_text": link_text,
                    "link_url": link_url
                })
        
        # Extract quote if present
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
            'sections': sections,
            'bullet_points': bullet_points,
            'quote': quote
        }
    
    def clean_bullet_text(self, bullet):
        """Clean bullet point text by removing markdown formatting"""
        # Replace markdown links with just the text
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', bullet["text"])
        
        # Remove emphasis markers
        text = text.replace('**', '').replace('*', '')
        
        return text
    
    def fix_slide_content(self, slide_num):
        """Fix content on a specific slide"""
        print(f"\n===== Fixing Slide {slide_num} =====")
        
        # Extract content
        content = self.extract_comprehensive_content(slide_num)
        if not content:
            print(f"Skipping slide {slide_num} - no content found")
            return False
        
        # Get the slide (0-indexed)
        if slide_num > len(self.prs.slides):
            print(f"Error: Slide {slide_num} does not exist (total slides: {len(self.prs.slides)})")
            return False
        
        slide = self.prs.slides[slide_num - 1]
        
        # Print what we found
        print(f"Title: {content['title']}")
        print(f"Subtitle: {content['subtitle']}")
        print(f"Summary: {content['summary'][:50]}..." if len(content['summary']) > 50 else f"Summary: {content['summary']}")
        print(f"Sections: {len(content['sections'])}")
        print(f"Bullet Points: {len(content['bullet_points'])}")
        if content['quote']:
            print(f"Quote: \"{content['quote'][:50]}..." if len(content['quote']) > 50 else f"Quote: \"{content['quote']}\"")
        
        # Remove any previously added textboxes (shapes after original shapes)
        shapes = list(slide.shapes)
        if len(shapes) > 3:
            print(f"Removing {len(shapes) - 3} previously added shapes")
            for i in range(len(shapes) - 1, 2, -1):
                shape = shapes[i]
                # We can't directly remove shapes, but we can make them invisible
                shape.left = -10000000
                shape.width = 0
                shape.height = 0
        
        # Update title and subtitle
        if content['title'] and len(shapes) >= 1:
            title_shape = shapes[0]
            print(f"Updating title to: {content['title']}")
            if hasattr(title_shape, 'text_frame'):
                title_shape.text_frame.text = content['title']
        
        if content['subtitle'] and len(shapes) >= 2:
            subtitle_shape = shapes[1]
            print(f"Updating subtitle to: {content['subtitle']}")
            if hasattr(subtitle_shape, 'text_frame'):
                subtitle_shape.text_frame.text = content['subtitle']
        
        # Create a single text box for all content
        print("Creating comprehensive content text box")
        content_textbox = slide.shapes.add_textbox(
            Inches(1),       # left
            Inches(2.5),     # top
            Inches(8),       # width
            Inches(4.5)      # height
        )
        
        tf = content_textbox.text_frame
        tf.word_wrap = True
        
        # Add summary if available
        if content['summary']:
            p = tf.paragraphs[0]
            p.text = content['summary']
            p.alignment = PP_ALIGN.LEFT
            
            # Format summary
            run = p.runs[0]
            run.font.italic = True
            run.font.size = Pt(12)
            
            # Add a blank line
            tf.add_paragraph()
        else:
            # Clear first paragraph if no summary
            tf.paragraphs[0].text = ""
        
        # Add sections with their bullet points
        for section in content['sections']:
            # Add section name
            p = tf.add_paragraph()
            p.text = f"{section['name']}:"
            p.alignment = PP_ALIGN.LEFT
            p.space_before = Pt(12)  # Add space before section
            
            # Format section name
            run = p.runs[0]
            run.font.bold = True
            run.font.size = Pt(12)
            
            # Add a blank line
            tf.add_paragraph()
            
            # Add bullet points for this section
            section_bullets = [b for b in content['bullet_points'] if b['section'] == section['name']]
            
            for bullet in section_bullets:
                p = tf.add_paragraph()
                
                # Format based on indentation level
                if bullet['level'] > 0:
                    p.text = f"   • {self.clean_bullet_text(bullet)}"
                    p.level = bullet['level']
                else:
                    p.text = f"• {self.clean_bullet_text(bullet)}"
                
                # Format run
                run = p.runs[0]
                run.font.bold = bullet.get('bold', False)
                run.font.size = Pt(11) if bullet['level'] == 0 else Pt(10)
                
                # Format hyperlinks
                if bullet['link_text']:
                    if "Source:" in bullet['text']:
                        run.font.color.rgb = RGBColor(0, 0, 255)
                        run.font.underline = True
                        run.font.size = Pt(9)
                    elif "projected adoption rates" in bullet['text'] or "fund allocation" in bullet['text'] or "adoption curves" in bullet['text'] or "metrics" in bullet['text'] or "benchmarks" in bullet['text'] or "valuations" in bullet['text']:
                        run.font.color.rgb = RGBColor(0, 0, 255)
                        run.font.underline = True
            
            # Add a blank line after the section
            tf.add_paragraph()
        
        # Add any bullet points not in a section
        unsectioned_bullets = [b for b in content['bullet_points'] if not b['section']]
        if unsectioned_bullets:
            for bullet in unsectioned_bullets:
                p = tf.add_paragraph()
                
                # Format based on indentation level
                if bullet['level'] > 0:
                    p.text = f"   • {self.clean_bullet_text(bullet)}"
                    p.level = bullet['level']
                else:
                    p.text = f"• {self.clean_bullet_text(bullet)}"
                
                # Format run
                run = p.runs[0]
                run.font.bold = bullet.get('bold', False)
                run.font.size = Pt(11) if bullet['level'] == 0 else Pt(10)
                
                # Format hyperlinks
                if bullet['link_text']:
                    if "Source:" in bullet['text']:
                        run.font.color.rgb = RGBColor(0, 0, 255)
                        run.font.underline = True
                        run.font.size = Pt(9)
                    elif "projected adoption rates" in bullet['text'] or "fund allocation" in bullet['text'] or "adoption curves" in bullet['text'] or "metrics" in bullet['text'] or "benchmarks" in bullet['text'] or "valuations" in bullet['text']:
                        run.font.color.rgb = RGBColor(0, 0, 255)
                        run.font.underline = True
        
        # Add quote at the end if available
        if content['quote']:
            # Add a blank line before quote
            tf.add_paragraph()
            
            p = tf.add_paragraph()
            p.text = f"\"{content['quote']}\""
            p.alignment = PP_ALIGN.CENTER
            
            # Format quote
            run = p.runs[0]
            run.font.italic = True
            run.font.size = Pt(11)
        
        return True
    
    def fix_all_slides(self):
        """Fix all slides in the presentation"""
        # Get total number of slides
        total_slides = len(self.prs.slides)
        print(f"Fixing all {total_slides} slides")
        
        # Process each slide
        fixed_count = 0
        for slide_num in range(1, total_slides + 1):
            success = self.fix_slide_content(slide_num)
            if success:
                fixed_count += 1
        
        # Save the presentation
        print(f"\nSaving presentation with {fixed_count} fixed slides")
        self.prs.save(self.ppt_path)
        print("All slides fixed successfully!")
        
        return fixed_count
    
    def open_powerpoint(self, slide_num=None):
        """Open PowerPoint with the presentation"""
        if slide_num:
            # Use AppleScript to open PowerPoint and go to specific slide
            script = f'''
            tell application "Microsoft PowerPoint"
                activate
                open "{self.ppt_path}"
                tell active presentation
                    go to slide {slide_num}
                end tell
            end tell
            '''
            os.system(f"osascript -e '{script}'")
            print(f"PowerPoint opened to slide {slide_num}")
        else:
            os.system(f"open -a 'Microsoft PowerPoint' '{self.ppt_path}'")
            print("PowerPoint opened with the presentation")

def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Fix all slides content comprehensively')
    parser.add_argument('--slide', type=int, help='Fix a specific slide')
    parser.add_argument('--all', action='store_true', help='Fix all slides')
    parser.add_argument('--open', action='store_true', help='Open PowerPoint after fixing')
    
    args = parser.parse_args()
    
    # Create slide fixer
    fixer = SlideContentFixer()
    
    try:
        # Fix slides
        if args.slide:
            # Fix a specific slide
            success = fixer.fix_slide_content(args.slide)
            if success:
                # Save the presentation
                print(f"Saving presentation")
                fixer.prs.save(fixer.ppt_path)
                print(f"Slide {args.slide} fixed successfully!")
                
                # Open PowerPoint if requested
                if args.open:
                    fixer.open_powerpoint(args.slide)
        elif args.all:
            # Fix all slides
            fixer.fix_all_slides()
            
            # Open PowerPoint if requested
            if args.open:
                fixer.open_powerpoint()
        else:
            print("Please specify either --slide or --all")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()