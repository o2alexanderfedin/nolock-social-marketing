#!/usr/bin/env python3

"""
Type text at the current cursor position.
Usage: python type_text.py "Text to type"
Example: python type_text.py "Hello, world!"

For long texts, you can save the text in a file and use:
python type_text.py --file filename.txt
"""

import pyautogui
import sys
import time
import argparse

# Configure parser
parser = argparse.ArgumentParser(description='Type text at the current cursor position')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('text', nargs='?', help='Text to type')
group.add_argument('--file', help='File containing text to type')
args = parser.parse_args()

# Get the text to type
if args.file:
    try:
        with open(args.file, 'r') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
else:
    text = args.text

# Print preview
print(f"Will type the following text:")
preview = text if len(text) < 100 else text[:97] + "..."
print(f"---\n{preview}\n---")

# Countdown
print("Starting in 3 seconds...")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

# Type the text
print("Typing text...")
pyautogui.typewrite(text)

print("Typing complete!")
print("Done!")