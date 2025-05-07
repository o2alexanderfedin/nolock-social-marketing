import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# URL of the Google Slides presentation
presentation_id = "1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU"
presentation_url = f"https://docs.google.com/presentation/d/{presentation_id}/edit?usp=sharing"
export_url = f"https://docs.google.com/presentation/d/{presentation_id}/export/pdf"

# Path to save the downloaded PDF
download_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/nolock_social_presentation.pdf"

def download_with_requests():
    """Try to download using direct requests to the export URL"""
    try:
        print(f"Attempting to download directly from: {export_url}")
        response = requests.get(export_url)
        
        if response.status_code == 200:
            with open(download_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded PDF to: {download_path}")
            return True
        else:
            print(f"Failed to download directly. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error in direct download: {e}")
        return False

def download_with_selenium():
    """Use Selenium to login and download the file"""
    print("Setting up Chrome browser...")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": os.path.dirname(download_path),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    })
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # First try to directly access the export URL
        print(f"Navigating to export URL: {export_url}")
        driver.get(export_url)
        
        # Wait to see if we get a direct download
        time.sleep(10)
        
        # Check if the file was downloaded
        if os.path.exists(download_path):
            print(f"Successfully downloaded PDF to: {download_path}")
            return True
            
        # If file wasn't downloaded, we'll need to use a different approach
        print("Direct export didn't work, trying a different approach...")
        
        # Go to the presentation URL
        driver.get(presentation_url)
        
        # Wait for the presentation to load
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # Wait a bit more for everything to initialize
        time.sleep(5)
        
        # Try to create a direct download link from the URL
        modified_export_url = f"https://docs.google.com/presentation/d/{presentation_id}/export/pdf"
        print(f"Trying modified export URL: {modified_export_url}")
        driver.get(modified_export_url)
        
        # Wait for download
        time.sleep(10)
        
        # Check if download succeeded
        if os.path.exists(download_path):
            print(f"Successfully downloaded PDF to: {download_path}")
            return True
        else:
            print("Failed to download using Selenium automated approach")
            return False
        
    except Exception as e:
        print(f"Error in Selenium approach: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Starting the download process...")
    
    # First try direct download with requests
    if download_with_requests():
        print("Direct download successful!")
    else:
        print("Direct download failed, trying with Selenium...")
        if download_with_selenium():
            print("Selenium download successful!")
        else:
            print("All download attempts failed.")
    
    print("Process completed.")