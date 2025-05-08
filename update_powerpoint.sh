#!/bin/bash

# Script to automate PowerPoint updates using AppleScript

echo "Starting PowerPoint update script..."

# Path to AppleScript file
APPLESCRIPT_PATH="/Users/alexanderfedin/Projects/nolock.social/marketing/update_powerpoint.applescript"

# Run the AppleScript
echo "Running AppleScript to update PowerPoint presentation..."
osascript "$APPLESCRIPT_PATH"

echo "Script execution complete."