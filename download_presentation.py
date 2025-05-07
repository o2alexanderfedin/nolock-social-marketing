import time
import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# URL of the Google Slides presentation
presentation_url = "https://docs.google.com/presentation/d/1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU/edit?usp=sharing"

# Path to save the downloaded PDF
download_dir = os.path.expanduser("~/Projects/nolock.social/marketing")
pdf_filename = "nolock_social_presentation.pdf"
full_path = os.path.join(download_dir, pdf_filename)

def download_presentation_as_pdf():
    print("Setting up Chrome browser...")
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    })
    
    # Use ChromeDriverManager to handle the driver installation
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        print(f"Opening the presentation URL: {presentation_url}")
        driver.get(presentation_url)
        
        # Wait for the presentation to load
        print("Waiting for the presentation to load...")
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)  # Additional wait to ensure full load
        
        # Trigger the File menu using keyboard shortcuts
        print("Initiating download process...")
        if os.name == 'posix':  # macOS
            # Press Cmd+Alt+Shift+P to download as PDF
            pyautogui.hotkey('command', 'option', 'shift', 'p')
        else:  # Windows/Linux
            # First press Alt+F to open the File menu
            pyautogui.hotkey('alt', 'f')
            time.sleep(1)
            # Navigate to "Download" in the menu
            pyautogui.press('d')
            time.sleep(1)
            # Select "PDF Document (.pdf)"
            pyautogui.press('p')
        
        # Wait for the download to complete
        print("Waiting for download to complete...")
        time.sleep(10)
        
        if os.path.exists(full_path):
            print(f"Successfully downloaded the presentation to: {full_path}")
        else:
            print(f"Download might have completed, but the file was not found at the expected location: {full_path}")
            print(f"Check your Downloads folder or the folder: {download_dir}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()

if __name__ == "__main__":
    print("Starting the download process...")
    download_presentation_as_pdf()
    print("Process completed.")