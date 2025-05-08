#!/usr/bin/env python3

"""
NoLock Social Slides Launcher

This script serves as a central entry point for all slide update tools.
It detects available tools and dependencies, then presents the user with
appropriate options for updating the Google Slides presentation.

Features:
- Dependency checking (PyAutoGUI availability)
- All-in-one launcher for various update methods
- Clear instructions and guidance
- Quick access to all update tools
"""

import os
import sys
import subprocess
import importlib.util
import shutil

# ANSI color codes for terminal output
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def color_text(color, text):
    """Return colored text for terminal output."""
    return f"{color}{text}{Colors.ENDC}"

def print_status(message):
    """Print status messages with a consistent format."""
    print(f"{Colors.BLUE}[STATUS]{Colors.ENDC} {message}")

def print_warning(message):
    """Print warning messages with a consistent format."""
    print(f"{Colors.YELLOW}[WARNING]{Colors.ENDC} {message}")

def print_error(message):
    """Print error messages with a consistent format."""
    print(f"{Colors.RED}[ERROR]{Colors.ENDC} {message}")

def print_header(message):
    """Print header messages with a consistent format."""
    width = shutil.get_terminal_size().columns
    padding = max(0, width - len(message) - 4)
    
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * (width)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}= {message}{' ' * padding}={Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * (width)}{Colors.ENDC}\n")

def check_pyautogui():
    """Check if PyAutoGUI is available."""
    try:
        import pyautogui
        return True
    except ImportError:
        return False

def check_script_exists(script_name):
    """Check if a script exists in the current directory."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    return os.path.exists(script_path)

def run_script(script_name, args=[]):
    """Run a Python script with arguments."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
    
    if not os.path.exists(script_path):
        print_error(f"Script not found: {script_name}")
        return False
    
    cmd = [sys.executable, script_path] + args
    print_status(f"Running: {' '.join(cmd)}")
    
    try:
        return subprocess.call(cmd) == 0
    except Exception as e:
        print_error(f"Error running script: {e}")
        return False

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    """Show help information about updating Google Slides."""
    print_header("GOOGLE SLIDES UPDATE HELP")
    
    print("This launcher provides access to various tools for updating the NoLock Social Google Slides presentation.")
    print("The tools are organized into different categories based on your needs and the available dependencies.")
    
    print("\n" + color_text(Colors.BOLD, "AVAILABLE UPDATE METHODS:"))
    print("\n1. Interactive Mode")
    print("   - Displays slide content for reference")
    print("   - You manually update the slides in Google Slides")
    print("   - No automation dependencies required")
    
    print("\n2. Assisted Mode")
    print("   - Provides step-by-step guidance")
    print("   - Helps with keyboard shortcuts and coordination")
    print("   - No automation dependencies required")
    
    print("\n3. Semi-Automated Mode")
    print("   - Uses PyAutoGUI to automate some tasks")
    print("   - Requires confirmation for each action")
    print("   - Requires PyAutoGUI library")
    
    print("\n4. Fully Automated Mode")
    print("   - Uses PyAutoGUI to update slides automatically")
    print("   - Minimal user interaction required")
    print("   - Requires PyAutoGUI library")
    
    print("\n" + color_text(Colors.BOLD, "REQUIREMENTS:"))
    print("- For automated modes: PyAutoGUI library (pip install pyautogui)")
    print("- Google Slides presentation must be accessible")
    print("- Exported slide content files must be available")
    
    print("\n" + color_text(Colors.BOLD, "TIPS:"))
    print("- Always verify slides after updating")
    print("- Keep hands off mouse and keyboard during automated updates")
    print("- Move mouse to upper-left corner to abort automated scripts")
    print("- Use slower speeds for more reliable automation")
    
    input("\nPress Enter to return to the main menu...")

def show_main_menu(pyautogui_available):
    """Show the main menu and get the user's choice."""
    clear_screen()
    print_header("NOLOCK SOCIAL SLIDES LAUNCHER")
    
    print(f"This launcher helps you update the NoLock Social Google Slides presentation.")
    
    if pyautogui_available:
        print(f"PyAutoGUI is {color_text(Colors.GREEN, 'AVAILABLE')} - All update methods are supported.\n")
    else:
        print(f"PyAutoGUI is {color_text(Colors.YELLOW, 'NOT AVAILABLE')} - Only manual methods are supported.")
        print(f"To enable automated methods, install PyAutoGUI: {color_text(Colors.CYAN, 'pip install pyautogui')}\n")
    
    print(f"{color_text(Colors.BOLD, 'SLIDE VIEWING OPTIONS:')}")
    print(f"1. Display Slides (Interactive Browsing)")
    print(f"   View slides content without changes\n")
    
    print(f"{color_text(Colors.BOLD, 'MANUAL UPDATE OPTIONS:')}")
    print(f"2. Manual Update with Instructions")
    print(f"   Guided step-by-step manual updating\n")
    
    if pyautogui_available:
        print(f"{color_text(Colors.BOLD, 'AUTOMATED UPDATE OPTIONS:')}")
        print(f"3. Update Single Slide (Semi-automated)")
        print(f"   Update one slide with automation assistance\n")
        
        print(f"4. Update Multiple Slides (Fully automated)")
        print(f"   Update a range of slides automatically\n")
    
    print(f"{color_text(Colors.BOLD, 'OTHER OPTIONS:')}")
    print(f"h. Help - Detailed information on update methods")
    print(f"q. Quit")
    
    while True:
        choice = input("\nEnter your choice: ").lower().strip()
        
        valid_choices = ['1', '2', 'h', 'q']
        if pyautogui_available:
            valid_choices.extend(['3', '4'])
            
        if choice in valid_choices:
            return choice
        else:
            print_warning("Invalid choice. Please try again.")

def main():
    """Main function for the NoLock Social Slides Launcher."""
    # Check if PyAutoGUI is available
    pyautogui_available = check_pyautogui()
    
    # Show main menu
    while True:
        choice = show_main_menu(pyautogui_available)
        
        if choice == '1':
            # Display Slides (Interactive Browsing)
            run_script("display_slides_auto.py")
        
        elif choice == '2':
            # Manual Update with Instructions
            run_script("update_slides_interactive_improved.py")
        
        elif choice == '3' and pyautogui_available:
            # Update Single Slide (Semi-automated)
            slide_num = input("Enter slide number to update (1-21): ").strip()
            if slide_num.isdigit() and 1 <= int(slide_num) <= 21:
                run_script("simple_update_slides.py", [slide_num])
            else:
                print_error("Invalid slide number. Must be between 1 and 21.")
                input("Press Enter to continue...")
        
        elif choice == '4' and pyautogui_available:
            # Update Multiple Slides (Fully automated)
            run_script("update_all_slides.py")
        
        elif choice == 'h':
            # Show help
            show_help()
        
        elif choice == 'q':
            # Quit
            print_status("Exiting NoLock Social Slides Launcher.")
            break
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user (KeyboardInterrupt)")
        sys.exit(1)
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
        sys.exit(1)