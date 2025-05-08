#!/usr/bin/env python3

"""
Interactive Google Slides Updater (Improved)

This script provides an interactive interface for updating NoLock Social's
Google Slides presentation with content from markdown files. It focuses on
clarity, user guidance, and proper content formatting.

Features:
- Color-coded content display
- Preview mode for seeing content before updating
- Navigation between slides with keyboard shortcuts
- Step-by-step instructions for manual updates
- Support for both automatic and manual workflows
"""

import os
import re
import time
import webbrowser
import json
import sys
import datetime

# Try to import PyAutoGUI, but make the script work even if it's not available
try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except ImportError:
    PYAUTOGUI_AVAILABLE = False

# Configuration
SLIDES_URL = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit"
EXPORT_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/slides_export"
TOTAL_SLIDES = 21

# ANSI color codes for terminal output
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_color(color, text):
    """Print text in color."""
    print(f"{color}{text}{Colors.ENDC}")

def print_status(message):
    """Print status messages with a consistent format."""
    print(f"{Colors.BLUE}[STATUS]{Colors.ENDC} {message}")

def print_instruction(message):
    """Print instruction messages with a consistent format."""
    print(f"{Colors.GREEN}[INSTRUCTION]{Colors.ENDC} {message}")

def print_warning(message):
    """Print warning messages with a consistent format."""
    print(f"{Colors.YELLOW}[WARNING]{Colors.ENDC} {message}")

def print_error(message):
    """Print error messages with a consistent format."""
    print(f"{Colors.RED}[ERROR]{Colors.ENDC} {message}")

def print_header(message):
    """Print header messages with a consistent format."""
    print(f"\n{Colors.BOLD}{message}{Colors.ENDC}\n")

def load_slide_data(slide_number):
    """Load slide data from the exported markdown file."""
    file_path = os.path.join(EXPORT_DIR, f"slide{slide_number:02d}_export.md")
    
    if not os.path.exists(file_path):
        print_warning(f"Could not find {file_path}")
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract the sections
    title_match = re.search(r'## Title\n(.*?)(?=\n\n)', content, re.DOTALL)
    subtitle_match = re.search(r'## Subtitle\n(.*?)(?=\n\n)', content, re.DOTALL)
    summary_match = re.search(r'## Summary\n(.*?)(?=\n\n)', content, re.DOTALL)
    
    # Extract bullet points section
    bullet_points = ""
    if "## Bullet Points" in content:
        bp_match = re.search(r'## Bullet Points\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if bp_match:
            bullet_points = bp_match.group(1).strip()
    
    # Extract quotes
    quotes = ""
    if "## Quotes" in content:
        q_match = re.search(r'## Quotes\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if q_match:
            quotes = q_match.group(1).strip()
    
    # Extract sources
    sources = ""
    if "## Sources" in content:
        s_match = re.search(r'## Sources\n(.*?)(?=\n\n(?:##|$))', content, re.DOTALL)
        if s_match:
            sources = s_match.group(1).strip()
    
    return {
        "title": title_match.group(1).strip() if title_match else "",
        "subtitle": subtitle_match.group(1).strip() if subtitle_match else "",
        "summary": summary_match.group(1).strip() if summary_match else "",
        "bullet_points": bullet_points,
        "quotes": quotes,
        "sources": sources
    }

def display_slide_content(slide_number):
    """Display the content of a slide in a well-formatted, readable way."""
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        print_error(f"No data found for slide {slide_number}")
        return False
    
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the slide header with slide number
    print_header(f"===== SLIDE {slide_number}/{TOTAL_SLIDES} =====")
    
    # Print each section with color coding and clear labels
    print_color(Colors.BOLD, "=== TITLE ===")
    print(f"{slide_data['title']}\n")
    
    print_color(Colors.BOLD, "=== SUBTITLE ===")
    print(f"{slide_data['subtitle']}\n")
    
    print_color(Colors.BOLD, "=== SUMMARY ===")
    print(f"{slide_data['summary']}\n")
    
    if slide_data['bullet_points']:
        print_color(Colors.BOLD, "=== BULLET POINTS ===")
        print(slide_data['bullet_points'] + "\n")
    
    if slide_data['quotes']:
        print_color(Colors.BOLD, "=== QUOTES ===")
        print(slide_data['quotes'] + "\n")
    
    if slide_data['sources']:
        print_color(Colors.BOLD, "=== SOURCES ===")
        print(slide_data['sources'] + "\n")
    
    # Print navigation instructions
    print_color(Colors.YELLOW, "----------------------------------------------")
    print_color(Colors.YELLOW, "NAVIGATION:")
    print_color(Colors.YELLOW, "  Press Enter: Continue to next slide")
    print_color(Colors.YELLOW, "  Type a number: Jump to that slide")
    print_color(Colors.YELLOW, "  Type 'q': Quit the program")
    print_color(Colors.YELLOW, "----------------------------------------------")
    
    return True

def display_slide_with_instructions(slide_number):
    """Display slide content with instructions for manual updates."""
    slide_data = load_slide_data(slide_number)
    if not slide_data:
        print_error(f"No data found for slide {slide_number}")
        return False
    
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the slide header with slide number
    print_header(f"===== SLIDE {slide_number}/{TOTAL_SLIDES} =====")
    
    # Print each section with clear instructions
    print_color(Colors.BOLD, "=== TITLE ===")
    print(f"{slide_data['title']}\n")
    print_instruction("1. Click the title text box in Google Slides")
    print_instruction("2. Press Cmd+A to select all text")
    print_instruction("3. Copy and paste the title above")
    print_instruction("4. Press Escape when done\n")
    
    print_color(Colors.BOLD, "=== SUBTITLE ===")
    print(f"{slide_data['subtitle']}\n")
    print_instruction("1. Click the subtitle text box")
    print_instruction("2. Press Cmd+A to select all text")
    print_instruction("3. Copy and paste the subtitle above")
    print_instruction("4. Press Escape when done\n")
    
    print_color(Colors.BOLD, "=== MAIN CONTENT ===")
    # Combine all content sections
    main_content = []
    if slide_data['summary']:
        main_content.append(slide_data['summary'])
    if slide_data['bullet_points']:
        main_content.append(slide_data['bullet_points'])
    if slide_data['quotes']:
        main_content.append(slide_data['quotes'])
    if slide_data['sources']:
        main_content.append(slide_data['sources'])
    
    print("\n".join(main_content) + "\n")
    
    print_instruction("1. Click the main content text box")
    print_instruction("2. Press Cmd+A to select all text")
    print_instruction("3. Copy and paste the main content above")
    print_instruction("4. Press Escape when done\n")
    
    # Print navigation instructions
    print_color(Colors.YELLOW, "----------------------------------------------")
    print_color(Colors.YELLOW, "NAVIGATION:")
    print_color(Colors.YELLOW, "  Press Enter: Continue to next slide")
    print_color(Colors.YELLOW, "  Type a number: Jump to that slide")
    print_color(Colors.YELLOW, "  Type 'q': Quit the program")
    print_color(Colors.YELLOW, "----------------------------------------------")
    
    return True

def open_google_slides():
    """Open Google Slides presentation in the browser."""
    print_status(f"Opening Google Slides: {SLIDES_URL}")
    webbrowser.open(SLIDES_URL)
    
    # Wait for the browser to open
    print_status("Waiting 5 seconds for browser to open...")
    time.sleep(5)

def navigate_slides_manually(start_slide=1, with_instructions=True):
    """Navigate through slides manually with interactive controls."""
    # Ask if user wants to open Google Slides
    if input("Open Google Slides in browser? (y/n): ").lower().strip() == 'y':
        open_google_slides()
        print_status("Make sure the Google Slides presentation is visible.")
        input("Press Enter when you're ready to start...")
    
    # Start from the specified slide
    slide_num = start_slide
    
    # Display slides one by one
    while slide_num <= TOTAL_SLIDES:
        # Show slide content with or without detailed instructions
        success = (display_slide_with_instructions(slide_num) if with_instructions 
                  else display_slide_content(slide_num))
        
        if not success:
            # If there was a problem loading the slide, ask what to do
            choice = input("Skip to next slide? (y/n, default: y): ").lower().strip()
            if choice == 'n':
                continue
            else:
                slide_num += 1
                continue
        
        # Get user input for navigation
        user_input = input("Command: ").strip().lower()
        
        if user_input == 'q':
            # Quit
            print_status("Exiting program.")
            break
        elif user_input.isdigit():
            # Jump to specific slide
            new_slide = int(user_input)
            if 1 <= new_slide <= TOTAL_SLIDES:
                slide_num = new_slide
            else:
                print_warning(f"Invalid slide number. Must be between 1 and {TOTAL_SLIDES}")
                time.sleep(1)
        else:
            # Continue to next slide
            slide_num += 1
    
    print_status("\nAll done! You can continue editing the slides in your browser.")

def show_keyboard_shortcuts():
    """Show helpful keyboard shortcuts for Google Slides."""
    print_header("GOOGLE SLIDES KEYBOARD SHORTCUTS")
    
    shortcuts = [
        ("Navigation", ""),
        ("Home", "Go to first slide"),
        ("End", "Go to last slide"),
        ("Left/Right arrows", "Previous/Next slide"),
        ("", ""),
        ("Editing", ""),
        ("Cmd+A", "Select all text in box"),
        ("Cmd+C", "Copy selected text"),
        ("Cmd+V", "Paste text"),
        ("Cmd+Z", "Undo"),
        ("Cmd+Shift+Z", "Redo"),
        ("Escape", "Finish editing text"),
        ("", ""),
        ("Formatting", ""),
        ("Cmd+B", "Bold"),
        ("Cmd+I", "Italic"),
        ("Cmd+U", "Underline"),
    ]
    
    # Print shortcuts in a nicely formatted table
    max_shortcut_len = max(len(shortcut) for shortcut, _ in shortcuts)
    for shortcut, description in shortcuts:
        if shortcut:
            print(f"{Colors.BOLD}{shortcut.ljust(max_shortcut_len)}{Colors.ENDC}  {description}")
        else:
            print()  # Empty line

def show_main_menu():
    """Show the main menu and get the user's choice."""
    print_header("NOLOCK SOCIAL INTERACTIVE SLIDES UPDATER")
    
    print("This tool helps you update Google Slides with content from markdown files.")
    print("Choose an option:\n")
    
    print(f"{Colors.BOLD}1. Simple Preview Mode{Colors.ENDC}")
    print("   Display slide content for reference while you update manually\n")
    
    print(f"{Colors.BOLD}2. Guided Update Mode{Colors.ENDC}")
    print("   Step-by-step instructions for updating each slide\n")
    
    print(f"{Colors.BOLD}3. View Keyboard Shortcuts{Colors.ENDC}")
    print("   Show helpful Google Slides keyboard shortcuts\n")
    
    print(f"{Colors.BOLD}q. Quit{Colors.ENDC}")
    
    while True:
        choice = input("\nEnter your choice (1-3, q): ").lower().strip()
        if choice in ['1', '2', '3', 'q']:
            return choice
        else:
            print_warning("Invalid choice. Please enter 1, 2, 3, or q.")

def main():
    """Main function for the NoLock Social Interactive Slides Updater."""
    # Parse command line arguments
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        start_slide = int(sys.argv[1])
        if start_slide < 1 or start_slide > TOTAL_SLIDES:
            print_error(f"Invalid slide number. Must be between 1 and {TOTAL_SLIDES}")
            return 1
        
        # If a slide number is provided, start directly in guided mode
        navigate_slides_manually(start_slide, with_instructions=True)
        return 0
    
    # If no command line arguments, show the menu
    choice = show_main_menu()
    
    if choice == '1':
        # Simple preview mode
        slide_num = 1
        try:
            slide_input = input("Enter slide number to start with (1-21, default: 1): ").strip()
            if slide_input and slide_input.isdigit():
                slide_num = int(slide_input)
                if slide_num < 1 or slide_num > TOTAL_SLIDES:
                    print_warning(f"Invalid slide number. Using default: 1")
                    slide_num = 1
        except ValueError:
            print_warning("Invalid input. Using default: 1")
        
        navigate_slides_manually(slide_num, with_instructions=False)
    
    elif choice == '2':
        # Guided update mode
        slide_num = 1
        try:
            slide_input = input("Enter slide number to start with (1-21, default: 1): ").strip()
            if slide_input and slide_input.isdigit():
                slide_num = int(slide_input)
                if slide_num < 1 or slide_num > TOTAL_SLIDES:
                    print_warning(f"Invalid slide number. Using default: 1")
                    slide_num = 1
        except ValueError:
            print_warning("Invalid input. Using default: 1")
        
        navigate_slides_manually(slide_num, with_instructions=True)
    
    elif choice == '3':
        # Show keyboard shortcuts
        show_keyboard_shortcuts()
        input("\nPress Enter to return to main menu...")
        main()  # Return to main menu
    
    else:  # choice == 'q'
        print_status("Exiting program.")
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user (KeyboardInterrupt)")
        sys.exit(1)
    except Exception as e:
        print_error(f"An error occurred: {e}")
        sys.exit(1)