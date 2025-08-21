#!/usr/bin/env python3

"""
Click at a specific position.
Usage: python mouse_click.py X Y [clicks]
Examples: 
  python mouse_click.py 500 500     # Single click
  python mouse_click.py 500 500 2   # Double click
"""

import pyautogui
import sys
import time

if len(sys.argv) < 3:
    print("Usage: python mouse_click.py X Y [clicks]")
    print("Examples:")
    print("  python mouse_click.py 500 500     # Single click")
    print("  python mouse_click.py 500 500 2   # Double click")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    clicks = int(sys.argv[3]) if len(sys.argv) > 3 else 1
except ValueError:
    print("Error: X, Y, and clicks must be integers")
    sys.exit(1)

# Get current position
current_x, current_y = pyautogui.position()
print(f"Current position: X: {current_x} Y: {current_y}")

# Move to click position
print(f"Moving to: X: {x} Y: {y}")
pyautogui.moveTo(x, y, duration=1)
time.sleep(0.5)

# Perform the click
print(f"Clicking {clicks} time(s)...")
pyautogui.click(clicks=clicks)

print("Click action complete!")
print(f"Position after click: X: {pyautogui.position()[0]} Y: {pyautogui.position()[1]}")
print("Done!")