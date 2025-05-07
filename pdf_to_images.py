import os
from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = "/Users/alexanderfedin/Projects/nolock.social/marketing/REBUILD TRUST IN THE DIGITAL SPACEN LOCK•SOCIAL.pdf"
output_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/pdf_images"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def convert_pdf_to_images():
    try:
        # Convert PDF to images
        print(f"Converting PDF to images: {pdf_path}")
        images = convert_from_path(pdf_path, dpi=200)
        
        print(f"Total pages converted: {len(images)}")
        
        # Save images
        for i, image in enumerate(images):
            image_path = os.path.join(output_dir, f"page_{i+1}.png")
            image.save(image_path, "PNG")
            print(f"Saved page {i+1} to {image_path}")
            
        print(f"Conversion complete. Images saved to {output_dir}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")

if __name__ == "__main__":
    convert_pdf_to_images()