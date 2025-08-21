#!/usr/bin/env python3

"""
Simple utility to show current mouse position.
Run this script and move your mouse to see coordinates in real-time.
Press Ctrl+C to exit.
"""

import pyautogui
import time

print("=== MOUSE POSITION TRACKER ===")
print("Move your mouse to see coordinates")
print("Press Ctrl+C to exit")
print("-" * 30)

try:
    while True:
        x, y = pyautogui.position()
        position = f"X: {x} Y: {y}"
        print(position, end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone!")