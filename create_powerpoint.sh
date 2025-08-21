#!/bin/bash

# Simple script to generate PowerPoint presentations

# Define paths
MARKETING_DIR="/Users/alexanderfedin/Projects/nolock.social/marketing"
APPLESCRIPT_PATH="$MARKETING_DIR/create_powerpoint.applescript"

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
echo "- Simplified Partner Presentation"
echo "- Detailed Partner Presentation"
echo ""
echo "This script will create sample PowerPoint decks with:"
echo "- Title slides"
echo "- Content slides with sample bullet points"
echo "- Notes sections for presentation tips"
echo ""
echo "Note: This is a simplified version that creates"
echo "PowerPoint files with placeholder content."
echo "You will need to manually customize these files."
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
  echo "Next steps:"
  echo "1. Open the presentations in PowerPoint"
  echo "2. Replace the placeholder content with actual slide content"
  echo "3. Add images and other visual elements"
  echo "4. Customize the design as needed"
else
  echo "Error: Failed to generate PowerPoint presentations."
  echo "Please ensure PowerPoint is installed and running."
fi