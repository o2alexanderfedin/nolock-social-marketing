#!/usr/bin/env python3

"""
Open a web browser and navigate to a URL.
Usage: python open_browser.py URL
Example: python open_browser.py https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit
"""

import webbrowser
import sys
import time

if len(sys.argv) != 2:
    print("Usage: python open_browser.py URL")
    print("Example: python open_browser.py https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit")
    sys.exit(1)

url = sys.argv[1]

print(f"Opening browser and navigating to: {url}")
print("This may take a few seconds...")

# Open the URL in the default browser
webbrowser.open(url)

print("Browser should now be open.")
print("Done!")