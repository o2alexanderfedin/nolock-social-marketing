#!/bin/bash

# Script to update a specific PowerPoint slide using osascript

# Default to slide 2 if no argument provided
SLIDE_NUM=${1:-2}

# Format slide number with leading zero if needed
SLIDE_NUM_PADDED=$(printf "%02d" $SLIDE_NUM)

# Define paths
MARKDOWN_PATH="/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides/slide${SLIDE_NUM_PADDED}.md"
PPT_PATH="/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"

# Check if markdown file exists
if [ ! -f "$MARKDOWN_PATH" ]; then
    echo "Error: Source content file not found: $MARKDOWN_PATH"
    exit 1
fi

# Extract title and subtitle
TITLE=$(grep -m 1 "^# " "$MARKDOWN_PATH" | sed 's/^# //')
SUBTITLE=$(grep -m 1 "^## " "$MARKDOWN_PATH" | sed 's/^## //')

echo "Updating slide $SLIDE_NUM with:"
echo "Title: $TITLE"
echo "Subtitle: $SUBTITLE"

# Create temporary AppleScript
TMP_SCRIPT=$(mktemp)
cat > "$TMP_SCRIPT" << EOL
tell application "Microsoft PowerPoint"
    activate
    open "$PPT_PATH"
    delay 2
    
    set activePresentation to active presentation
    
    tell slide $SLIDE_NUM of activePresentation
        -- Update title
        try
            tell shape 1
                if has text frame then
                    tell text frame
                        tell text range
                            set content to "$TITLE"
                        end tell
                    end tell
                end if
            end tell
        end try
        
        -- Update subtitle
        try
            tell shape 2
                if has text frame then
                    tell text frame
                        tell text range
                            set content to "$SUBTITLE"
                        end tell
                    end tell
                end if
            end tell
        end try
    end tell
    
    -- Save the presentation
    save activePresentation
end tell
EOL

# Run the AppleScript
osascript "$TMP_SCRIPT"

# Clean up
rm "$TMP_SCRIPT"

echo "Slide $SLIDE_NUM updated successfully!"