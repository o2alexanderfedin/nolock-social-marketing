import os
import io
import PyPDF2
from PIL import Image
import base64

# Path to the PDF file
pdf_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pdf"
output_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/extracted_pdf"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def extract_from_pdf():
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        print(f"Total pages in PDF: {num_pages}")
        
        # Extract text and images from each page
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            
            # Extract text
            text = page.extract_text()
            if text.strip():
                with open(f"{output_dir}/page_{page_num+1}_text.txt", "w", encoding="utf-8") as text_file:
                    text_file.write(text)
                print(f"Extracted text from page {page_num+1}")
            else:
                print(f"No text found on page {page_num+1}")
            
            # Try to extract images (if any)
            if '/Resources' in page and '/XObject' in page['/Resources']:
                xobjects = page['/Resources']['/XObject']
                if xobjects:
                    for obj_name, obj in xobjects.items():
                        if hasattr(obj, 'get') and obj.get('/Subtype') == '/Image':
                            try:
                                # Extract image data
                                image_data = obj.get_data()
                                if '/Filter' in obj and '/DCTDecode' in obj['/Filter']:
                                    # JPEG image
                                    img_ext = "jpg"
                                else:
                                    # Assume PNG for everything else
                                    img_ext = "png"
                                
                                with open(f"{output_dir}/page_{page_num+1}_img_{obj_name}.{img_ext}", "wb") as img_file:
                                    img_file.write(image_data)
                                print(f"Extracted image from page {page_num+1}")
                            except Exception as e:
                                print(f"Error extracting image from page {page_num+1}: {e}")

if __name__ == "__main__":
    extract_from_pdf()
    print(f"Extraction complete. Files saved to {output_dir}")