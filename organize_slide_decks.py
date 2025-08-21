#!/usr/bin/env python3
"""
Script to organize slide decks into proper directory structure.
"""

import os
import shutil
import glob

# Base directory
BASE_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing"

# Source directories with existing content
SOURCE_DIRS = {
    "customer-partner": os.path.join(BASE_DIR, "pitch-deck-customer-partner"),
    "investor": os.path.join(BASE_DIR, "pitch-deck-investor"),
    "investor-full": os.path.join(BASE_DIR, "pitch-deck-investor-full"),
    "original": os.path.join(BASE_DIR, "pitch-deck"),
}

# Target directory structure
TARGET_DIR = os.path.join(BASE_DIR, "pitch-decks")

def create_directory_structure():
    """Create the new directory structure."""
    for deck_type in ["customer-partner", "investor", "investor-full", "original"]:
        os.makedirs(os.path.join(TARGET_DIR, deck_type, "slides"), exist_ok=True)
        os.makedirs(os.path.join(TARGET_DIR, deck_type, "images"), exist_ok=True)

def copy_files():
    """Copy files from source directories to target directories."""
    
    # Copy files for each deck type
    for deck_type, source_dir in SOURCE_DIRS.items():
        if not os.path.exists(source_dir):
            print(f"Source directory {source_dir} does not exist, skipping.")
            continue
            
        target_deck_dir = os.path.join(TARGET_DIR, deck_type)
        
        # Copy README.md and other top-level markdown files
        for md_file in glob.glob(os.path.join(source_dir, "*.md")):
            filename = os.path.basename(md_file)
            shutil.copy2(md_file, os.path.join(target_deck_dir, filename))
            print(f"Copied {md_file} to {os.path.join(target_deck_dir, filename)}")
        
        # Copy slides
        if os.path.exists(os.path.join(source_dir, "slides")):
            for slide_file in glob.glob(os.path.join(source_dir, "slides", "*.md")):
                filename = os.path.basename(slide_file)
                shutil.copy2(slide_file, os.path.join(target_deck_dir, "slides", filename))
                print(f"Copied {slide_file} to {os.path.join(target_deck_dir, 'slides', filename)}")
        
        # Copy images
        if os.path.exists(os.path.join(source_dir, "images")):
            for img_file in glob.glob(os.path.join(source_dir, "images", "*")):
                if os.path.isfile(img_file):
                    filename = os.path.basename(img_file)
                    shutil.copy2(img_file, os.path.join(target_deck_dir, "images", filename))
                    print(f"Copied {img_file} to {os.path.join(target_deck_dir, 'images', filename)}")

def create_master_index():
    """Create a master index file for all slide decks."""
    index_content = """# NoLock Social Presentation Decks

This directory contains organized presentation materials for NoLock Social, arranged by audience type and purpose.

## Available Decks

| Deck | Purpose | Slides | README |
|------|---------|--------|--------|
| [Customer & Partner Deck](customer-partner/README.md) | Partner-focused pitch with integration emphasis | [View Slides](customer-partner/slides/) | [View README](customer-partner/README.md) |
| [Investor Deck](investor/README.md) | Focused investor pitch (12 slides) | [View Slides](investor/slides/) | [View README](investor/README.md) |
| [Full Investor Deck](investor-full/README.md) | Comprehensive investor presentation (21 slides) | [View Slides](investor-full/slides/) | [View README](investor-full/README.md) |
| [Original Pitch Deck](original/README.md) | General presentation for all audiences | [View Slides](original/slides/) | [View README](original/README.md) |

## Directory Structure

Each presentation deck follows a consistent structure:

```
pitch-decks/
├── customer-partner/     # Partner-focused pitch deck
│   ├── images/           # Slide images
│   ├── slides/           # Individual slide markdown files
│   └── README.md         # Deck-specific documentation
├── investor/             # Investor-focused pitch deck
│   ├── images/
│   ├── slides/
│   └── README.md
├── investor-full/        # Comprehensive investor deck
│   ├── images/
│   ├── slides/
│   └── README.md
└── original/             # Original general-purpose deck
    ├── images/
    ├── slides/
    └── README.md
```

## Navigation

All slides include navigation headers and footers for easy browsing:
- Previous Slide: Move to the prior slide
- Deck Home: Return to the deck's README
- Next Slide: Advance to the next slide

## Usage Notes

1. For partnership discussions, use the [Customer & Partner Deck](customer-partner/README.md)
2. For investor pitches, use either:
   - [Investor Deck](investor/README.md) (brief 12-slide version)
   - [Full Investor Deck](investor-full/README.md) (comprehensive 21-slide version)
3. For general presentations, use the [Original Pitch Deck](original/README.md)

Each deck includes detailed speaker notes to guide verbal presentation.
"""
    
    with open(os.path.join(TARGET_DIR, "README.md"), "w") as f:
        f.write(index_content)
    
    print(f"Created master index at {os.path.join(TARGET_DIR, 'README.md')}")

def main():
    """Execute the organization process."""
    # Create directory structure
    create_directory_structure()
    
    # Copy files
    copy_files()
    
    # Create master index
    create_master_index()
    
    print("Slide decks organized successfully.")

if __name__ == "__main__":
    main()