#!/usr/bin/env python3

"""
Press a key or key combination.
Usage: python key_press.py key1 [key2]
Examples:
  python key_press.py enter     # Press Enter key
  python key_press.py esc       # Press Escape key
  python key_press.py cmd a     # Press Command+A (select all)
  python key_press.py right     # Press right arrow
  python key_press.py home      # Press Home key
"""

import pyautogui
import sys
import time

if len(sys.argv) < 2:
    print("Usage: python key_press.py key1 [key2]")
    print("Examples:")
    print("  python key_press.py enter     # Press Enter key")
    print("  python key_press.py esc       # Press Escape key")
    print("  python key_press.py cmd a     # Press Command+A (select all)")
    print("  python key_press.py right     # Press right arrow")
    print("  python key_press.py home      # Press Home key")
    sys.exit(1)

# Map common key names to pyautogui key names
key_map = {
    'cmd': 'command',
    'ctrl': 'control',
    'esc': 'escape',
    'return': 'enter',
}

# Convert arguments to proper key names
keys = []
for i in range(1, len(sys.argv)):
    key = sys.argv[i].lower()
    keys.append(key_map.get(key, key))

if len(keys) == 1:
    # Single key press
    print(f"Pressing key: {keys[0]}")
    pyautogui.press(keys[0])
else:
    # Hotkey combination
    print(f"Pressing key combination: {'+'.join(keys)}")
    pyautogui.hotkey(*keys)

print("Key press complete!")
print("Done!")