#!/bin/bash

# Script to generate PowerPoint presentations using Python

# Define paths
MARKETING_DIR="/Users/alexanderfedin/Projects/nolock.social/marketing"
PYTHON_SCRIPT="$MARKETING_DIR/generate_powerpoint.py"

echo "=========================================================="
echo "  NoLock Social PowerPoint Generator (Python)"
echo "=========================================================="
echo "Generating PowerPoint presentations..."
echo "- Simplified Partner Presentation (optimized for presenting)"
echo "- Detailed Partner Presentation (complete documentation)"
echo ""
echo "This may take a moment. Please wait..."
echo "=========================================================="

# Check if python-pptx is installed
pip3 show python-pptx >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Installing required Python package: python-pptx"
  pip3 install python-pptx
  if [ $? -ne 0 ]; then
    echo "Error: Failed to install python-pptx package."
    echo "Please install it manually with: pip3 install python-pptx"
    exit 1
  fi
fi

# Run the Python script
python3 "$PYTHON_SCRIPT"

if [ $? -eq 0 ]; then
  echo ""
  echo "Usage instructions:"
  echo "1. Open the presentations in PowerPoint"
  echo "2. Use presenter view for access to notes during presentations"
  echo "3. The simplified deck is recommended for live presentations"
  echo "4. The detailed deck is best for documentation and reference"
else
  echo "Error: Failed to generate PowerPoint presentations."
  echo "Please check the error messages above."
fi