#!/bin/bash

# Script to update a specific PowerPoint slide using osascript with more verbose output and explicit save

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

# Create temporary AppleScript with explicit save and close
TMP_SCRIPT=$(mktemp)
cat > "$TMP_SCRIPT" << EOL
tell application "Microsoft PowerPoint"
    set wasRunning to running
    activate
    
    -- Check if file is already open
    set fileAlreadyOpen to false
    set presentationName to "REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pptx"
    
    if wasRunning then
        try
            -- Check if presentation is already open
            set fileAlreadyOpen to (exists presentation presentationName)
        end try
    end if
    
    -- Open the presentation if it's not open
    if not fileAlreadyOpen then
        open "$PPT_PATH"
        delay 2
    end if
    
    -- Get the active presentation
    set activePresentation to presentation presentationName
    
    -- Update slide
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
            
            -- Log success
            log "Updated title successfully"
        on error errMsg
            log "Error updating title: " & errMsg
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
            
            -- Log success
            log "Updated subtitle successfully"
        on error errMsg
            log "Error updating subtitle: " & errMsg
        end try
    end tell
    
    -- Save the presentation with explicit save
    save activePresentation
    delay 1
    
    -- Force another save to be sure
    save activePresentation in "$PPT_PATH"
    delay 1
    
    -- Log completion
    log "Slide $SLIDE_NUM updated and saved"
    
    -- No need to close if it was already open
    if not fileAlreadyOpen then
        close activePresentation saving yes
    end if
end tell
EOL

# Run the AppleScript with verbose output
osascript -s o "$TMP_SCRIPT"

# Clean up
rm "$TMP_SCRIPT"

echo "Slide $SLIDE_NUM updated and saved."