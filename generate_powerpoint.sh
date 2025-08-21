#!/bin/bash

# Script to generate PowerPoint presentations from slide content

# Define paths
MARKETING_DIR="/Users/alexanderfedin/Projects/nolock.social/marketing"
APPLESCRIPT_PATH="$MARKETING_DIR/generate_powerpoint_enhanced.applescript"

# Check if user wants to use the basic version instead
if [ "$1" == "--basic" ]; then
  APPLESCRIPT_PATH="$MARKETING_DIR/generate_powerpoint_presentations.applescript"
  echo "Using basic PowerPoint generator..."
fi

# Ensure PowerPoint is installed
if ! [ -d "/Applications/Microsoft PowerPoint.app" ]; then
  echo "Error: Microsoft PowerPoint is not installed."
  echo "Please install Microsoft PowerPoint and try again."
  exit 1
fi

echo "=========================================================="
echo "  NoLock Social PowerPoint Generator"
echo "=========================================================="
echo "Generating PowerPoint presentations..."
echo "- Simplified Partner Presentation (optimized for presenting)"
echo "- Detailed Partner Presentation (complete documentation)"
echo ""
echo "This may take a moment. Please wait..."
echo "=========================================================="

# Run the AppleScript
osascript "$APPLESCRIPT_PATH"

if [ $? -eq 0 ]; then
  echo ""
  echo "=========================================================="
  echo "✅ PowerPoint presentations generated successfully!"
  echo "=========================================================="
  echo ""
  echo "Output files:"
  echo "- $MARKETING_DIR/NoLock_Partner_Simplified.pptx"
  echo "- $MARKETING_DIR/NoLock_Partner_Detailed.pptx"
  echo ""
  echo "Features included:"
  echo "- Proper slide layouts and formatting"
  echo "- Bullet points formatted correctly"
  echo "- Design elements included in notes"
  echo "- Pitch notes included in presenter view"
  echo "- Title slide with generation date"
  echo ""
  echo "Usage instructions:"
  echo "1. Open the presentations in PowerPoint"
  echo "2. Use presenter view for access to notes during presentations"
  echo "3. The simplified deck is recommended for live presentations"
  echo "4. The detailed deck is best for documentation and reference"
else
  echo "Error: Failed to generate PowerPoint presentations."
  echo "Please check the AppleScript for errors."
  echo "You can try the basic version with: ./generate_powerpoint.sh --basic"
fi