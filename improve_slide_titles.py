#!/usr/bin/env python3

import os
import re

# Define slide summaries for the condensed investor deck
condensed_summaries = {
    "slide01.md": "A next-generation platform rebuilding digital trust with decentralized identity in a $12B market.",
    "slide02.md": "Digital trust is fundamentally broken with centralized control, content manipulation, and privacy exploitation.",
    "slide03.md": "Our solution provides user-controlled identity, immutable content verification, and trust-based filtering.",
    "slide04.md": "A rapidly growing $12B market projected to reach $101B by 2033 with clear TAM/SAM/SOM breakdown.",
    "slide05.md": "Dual revenue streams combining B2C freemium subscriptions and B2B technology licensing.",
    "slide06.md": "Our comprehensive product stack includes consumer applications and enterprise infrastructure.",
    "slide07.md": "Proprietary technology creates barriers to entry with 3x efficiency over blockchain alternatives.",
    "slide08.md": "We provide unique advantages over both centralized platforms and decentralized alternatives.",
    "slide09.md": "Three-phase GTM strategy from developer adoption to mainstream users with clear metrics.",
    "slide10.md": "Demonstrated progress with early partnerships, developer traction, and clear roadmap.",
    "slide11.md": "Experienced leadership team with technical expertise and successful entrepreneurial track record.",
    "slide12.md": "Seeking $2.5M pre-seed funding to reach key milestones toward Series A readiness."
}

# Define slide summaries for the full investor deck
full_summaries = {
    "slide01.md": "A next-generation platform rebuilding digital trust with decentralized identity in a $12B market.",
    "slide02.md": "Content authenticity issues and lack of ownership create fundamental digital trust challenges.",
    "slide03.md": "Centralized data vulnerabilities and the surveillance economy compromise user privacy and security.",
    "slide04.md": "Current digital systems require blind trust in central authorities without transparency.",
    "slide05.md": "Building a new trust layer based on cryptographic proof rather than blind trust.",
    "slide06.md": "A rapidly growing $12B market projected to reach $101B by 2033 with clear TAM/SAM/SOM breakdown.",
    "slide07.md": "Our core technology uses content-addressable storage with superior efficiency and security.",
    "slide08.md": "Dual revenue streams combining B2C freemium subscriptions and B2B technology licensing.",
    "slide09.md": "DISOT enables mutable data with immutable history through digital signatures.",
    "slide10.md": "Networks of Trust mirror how humans naturally establish trust relationships in the real world.",
    "slide11.md": "FunctionalScript provides a 40% performance improvement for content-addressable operations.",
    "slide12.md": "Blockset democratizes industrial-grade content-addressable storage for everyday use.",
    "slide13.md": "Delfin delivers a decentralized social network with user-owned identity and content.",
    "slide14.md": "Our platform offers future-proof technology, offline functionality, and verifiable content.",
    "slide15.md": "Content-addressable AI ensures provenance and transparency for training data and models.",
    "slide16.md": "Our dual product strategy creates a complete ecosystem from infrastructure to user experience.",
    "slide17.md": "Our key differentiators include proprietary technology with patent protection.",
    "slide18.md": "We combine the best elements of centralized usability and decentralized security.",
    "slide19.md": "Three-phase GTM strategy from developer adoption to mainstream users with clear metrics.",
    "slide20.md": "Demonstrated progress with early partnerships, developer traction, and clear roadmap.",
    "slide21.md": "Seeking $2.5M pre-seed funding to reach key milestones toward Series A readiness."
}

def improve_slide_titles(slides_dir, summaries):
    """Add one-sentence summaries to slide pages."""
    
    for slide_id, summary in summaries.items():
        slide_path = os.path.join(slides_dir, slide_id)
        
        if not os.path.exists(slide_path):
            print(f"Warning: Slide {slide_path} does not exist. Skipping.")
            continue
            
        # Read the slide content
        with open(slide_path, 'r') as f:
            content = f.read()
        
        # Extract the title and subtitle
        title_match = re.search(r'# (.+)', content)
        subtitle_match = re.search(r'## (.+)', content)
        
        if not title_match:
            print(f"Warning: Could not find title in {slide_path}. Skipping.")
            continue
            
        title = title_match.group(1)
        subtitle = subtitle_match.group(1) if subtitle_match else ""
        
        # Find the position after the navigation header
        nav_end_idx = content.find('---\n\n#')
        if nav_end_idx == -1:
            print(f"Warning: Could not find navigation end in {slide_path}. Skipping.")
            continue
            
        # Find the position after the subtitle (if there is one)
        if subtitle:
            subtitle_idx = content.find(f"## {subtitle}")
            if subtitle_idx != -1:
                subtitle_end_idx = content.find('\n\n', subtitle_idx)
                if subtitle_end_idx != -1:
                    # Insert the summary after the subtitle
                    updated_content = (
                        content[:subtitle_end_idx + 2] + 
                        f"*{summary}*\n\n" + 
                        content[subtitle_end_idx + 2:]
                    )
                    
                    # Write the updated content back to the file
                    with open(slide_path, 'w') as f:
                        f.write(updated_content)
                    
                    print(f"Added summary to {slide_path}")
                else:
                    print(f"Warning: Could not find end of subtitle in {slide_path}. Skipping.")
            else:
                print(f"Warning: Could not find subtitle in {slide_path}. Skipping.")
        else:
            # If there's no subtitle, insert after the title
            title_idx = content.find(f"# {title}")
            if title_idx != -1:
                title_end_idx = content.find('\n\n', title_idx)
                if title_end_idx != -1:
                    # Insert the summary after the title
                    updated_content = (
                        content[:title_end_idx + 2] + 
                        f"*{summary}*\n\n" + 
                        content[title_end_idx + 2:]
                    )
                    
                    # Write the updated content back to the file
                    with open(slide_path, 'w') as f:
                        f.write(updated_content)
                    
                    print(f"Added summary to {slide_path}")
                else:
                    print(f"Warning: Could not find end of title in {slide_path}. Skipping.")
            else:
                print(f"Warning: Could not find title in {slide_path}. Skipping.")

def update_slide_generators():
    """Update the slide generator scripts to include summaries in future slides."""
    
    # Update condensed investor slides generator
    generator_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/generate_investor_slides.py"
    if os.path.exists(generator_path):
        with open(generator_path, 'r') as f:
            content = f.read()
            
        for slide_id, summary in condensed_summaries.items():
            slide_num = slide_id.replace(".md", "")
            # Find the slide definition
            slide_def_pattern = f'"{slide_num}": {{'
            slide_def_idx = content.find(slide_def_pattern)
            
            if slide_def_idx != -1:
                # Find the content key
                content_key_pattern = '"content": """'
                content_key_idx = content.find(content_key_pattern, slide_def_idx)
                
                if content_key_idx != -1:
                    # Insert summary at the beginning of the content
                    updated_content = (
                        content[:content_key_idx + len(content_key_pattern)] + 
                        f"\n*{summary}*\n\n" + 
                        content[content_key_idx + len(content_key_pattern):]
                    )
                    content = updated_content
        
        with open(generator_path, 'w') as f:
            f.write(content)
        print(f"Updated {generator_path} with summaries")
            
    # Update full investor slides generator
    generator_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/generate_investor_slides_full.py"
    if os.path.exists(generator_path):
        with open(generator_path, 'r') as f:
            content = f.read()
            
        for slide_id, summary in full_summaries.items():
            slide_num = slide_id.replace(".md", "")
            # Find the slide definition
            slide_def_pattern = f'"{slide_num}": {{'
            slide_def_idx = content.find(slide_def_pattern)
            
            if slide_def_idx != -1:
                # Find the content key
                content_key_pattern = '"content": """'
                content_key_idx = content.find(content_key_pattern, slide_def_idx)
                
                if content_key_idx != -1:
                    # Insert summary at the beginning of the content
                    updated_content = (
                        content[:content_key_idx + len(content_key_pattern)] + 
                        f"\n*{summary}*\n\n" + 
                        content[content_key_idx + len(content_key_pattern):]
                    )
                    content = updated_content
        
        with open(generator_path, 'w') as f:
            f.write(content)
        print(f"Updated {generator_path} with summaries")

if __name__ == "__main__":
    # Add summaries to the condensed investor pitch deck slides
    print("Adding summaries to condensed investor pitch deck...")
    improve_slide_titles("/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor/slides", condensed_summaries)
    
    # Add summaries to the full investor pitch deck slides
    print("\nAdding summaries to full investor pitch deck...")
    improve_slide_titles("/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides", full_summaries)
    
    # Update the slide generator scripts
    print("\nUpdating slide generator scripts...")
    update_slide_generators()
    
    print("\nSlide titles have been improved successfully!")