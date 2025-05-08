#!/bin/bash

# Script to update all PowerPoint slides in sequence

echo "Starting presentation update..."

# Define the total number of slides to update
TOTAL_SLIDES=21

# Loop through each slide
for ((i=1; i<=$TOTAL_SLIDES; i++))
do
    echo "Processing slide $i of $TOTAL_SLIDES..."
    
    # Run the update script for each slide
    /Users/alexanderfedin/Projects/nolock.social/marketing/update_slide.sh $i
    
    # Add a small delay between updates
    sleep 1
done

echo "All slides have been updated successfully!"