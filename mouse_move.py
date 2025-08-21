#!/usr/bin/env python3

"""
Move the mouse to a specific position.
Usage: python mouse_move.py X Y
Example: python mouse_move.py 500 500
"""

import pyautogui
import sys
import time

if len(sys.argv) != 3:
    print("Usage: python mouse_move.py X Y")
    print("Example: python mouse_move.py 500 500")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print("Error: X and Y must be integers")
    sys.exit(1)

# Get current position
current_x, current_y = pyautogui.position()
print(f"Current position: X: {current_x} Y: {current_y}")

# Move to new position
print(f"Moving to: X: {x} Y: {y}")
pyautogui.moveTo(x, y, duration=1)

# Verify new position
new_x, new_y = pyautogui.position()
print(f"New position: X: {new_x} Y: {new_y}")
print("Done!")