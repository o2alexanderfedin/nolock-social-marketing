#!/usr/bin/env python3

"""
Activate the Chrome window to ensure it's in focus.
"""

import subprocess
import time

print("Activating Chrome window...")

try:
    # AppleScript to bring Chrome to front
    script = """
    tell application "Google Chrome"
        activate
    end tell
    """
    subprocess.run(["osascript", "-e", script], check=True)
    print("Chrome should now be in focus")
except Exception as e:
    print(f"Error activating Chrome: {e}")
    print("Please click on Chrome window manually to ensure it's in focus")

print("Waiting 2 seconds for window to be ready...")
time.sleep(2)
print("Done!")