#!/usr/bin/env python3

"""
This script opens Chrome, navigates to Google Slides, and ensures it's properly positioned
before running any automation.
"""

import os
import subprocess
import webbrowser
import time
import sys

# Google Slides presentation URL
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"

def print_status(message):
    """Print status messages with consistent formatting."""
    print(f"[STATUS] {message}")

def open_chrome():
    """Open Chrome browser on macOS."""
    print_status("Opening Chrome browser...")
    
    try:
        # Try to open Chrome using AppleScript
        script = """
        tell application "Google Chrome"
            activate
        end tell
        """
        subprocess.run(["osascript", "-e", script], check=True)
        print_status("Chrome opened successfully using AppleScript")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"AppleScript failed: {e}")
        
        # Fallback to using webbrowser module
        print_status("Trying fallback method to open Chrome...")
        try:
            # Try to use Chrome directly
            chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            if os.path.exists(chrome_path):
                subprocess.Popen([chrome_path, '--new-window'])
                print_status("Chrome opened with subprocess")
                time.sleep(2)
                return True
            
            # Try with webbrowser module
            webbrowser.get('chrome').open_new('')
            print_status("Chrome opened with webbrowser module")
            time.sleep(2)
            return True
        except Exception as e2:
            print(f"Fallback failed: {e2}")
            
            # Last resort - try default browser
            print_status("Trying to open with default browser...")
            webbrowser.open_new('')
            time.sleep(2)
            return True
    
    return False

def navigate_to_slides():
    """Navigate to Google Slides."""
    print_status(f"Navigating to Google Slides: {SLIDES_URL}")
    
    try:
        # Try to use AppleScript to navigate in the current Chrome window
        script = f"""
        tell application "Google Chrome"
            activate
            open location "{SLIDES_URL}"
        end tell
        """
        subprocess.run(["osascript", "-e", script], check=True)
        print_status("Navigated to Google Slides using AppleScript")
        return True
    except Exception as e:
        print(f"AppleScript navigation failed: {e}")
        
        # Fallback to using webbrowser
        print_status("Trying fallback method to navigate...")
        try:
            webbrowser.open(SLIDES_URL)
            print_status("Opened Google Slides with webbrowser module")
            return True
        except Exception as e2:
            print(f"Navigation fallback failed: {e2}")
            return False

def main():
    """Main function to open Chrome and navigate to Google Slides."""
    print("\n" + "="*70)
    print("OPENING GOOGLE SLIDES".center(70))
    print("="*70)
    
    print("This script will open Chrome and navigate to the Google Slides presentation.")
    
    # Ask for confirmation
    try:
        input("Press Enter to continue (or Ctrl+C to abort)...")
    except (EOFError, KeyboardInterrupt):
        print("\nOperation aborted.")
        sys.exit(0)
    
    # Open Chrome
    if not open_chrome():
        print("Failed to open Chrome. Please open it manually.")
        sys.exit(1)
    
    # Give browser time to open
    print_status("Waiting for Chrome to initialize...")
    time.sleep(3)
    
    # Navigate to Google Slides
    if not navigate_to_slides():
        print("Failed to navigate to Google Slides. Please do it manually.")
        sys.exit(1)
    
    # Wait for page to load
    print_status("Waiting for Google Slides to load...")
    time.sleep(10)
    
    print("\n" + "="*70)
    print("GOOGLE SLIDES OPENED SUCCESSFULLY".center(70))
    print("="*70)
    
    print("""
Google Slides should now be open in Chrome.

Next steps:
1. Ensure you're logged into your Google account
2. Make sure the presentation is in edit mode (not presentation mode)
3. Wait for the presentation to fully load

When ready, you can:
- Run get_coordinates.py to capture slide element positions
- Run simple_update_slides.py to update slides
""")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())