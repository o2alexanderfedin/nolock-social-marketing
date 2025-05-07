#!/usr/bin/env python3

import os
import re
import time
import json
import pickle
import markdown
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Configuration
PRESENTATION_ID = '1nB_qDZdPiVAA8KbGzatFYnzW24-rE5NSAamyvGgxrcU'
INVESTOR_SLIDES_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck-investor-full/slides"
SLIDES_ORDER = [f"slide{i:02d}.md" for i in range(1, 22)]  # slide01.md to slide21.md

# Google API scopes
SCOPES = ['https://www.googleapis.com/auth/presentations']

def parse_markdown_slide(file_path):
    """Extract title, subtitle, summary and content from a markdown slide file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Remove navigation links and separators
    content = re.sub(r'\[← Previous\].+?\[Next →\].+?---', '', content, flags=re.DOTALL)
    content = re.sub(r'---\s+\[← Previous\].+?\[Next →\].*$', '', content, flags=re.DOTALL)
    
    # Extract title, subtitle, and summary
    title_match = re.search(r'# (.+)', content)
    subtitle_match = re.search(r'## (.+)', content)
    summary_match = re.search(r'\*([^*]+)\*', content)
    
    title = title_match.group(1) if title_match else ""
    subtitle = subtitle_match.group(1) if subtitle_match else ""
    summary = summary_match.group(1).strip() if summary_match else ""
    
    # Extract content (everything after the summary)
    if summary_match:
        content_section = content.split(f"*{summary}*", 1)[1].strip()
    else:
        content_section = content.split('##', 2)[2] if len(content.split('##')) > 2 else ""
    
    # Extract bullet points and other content
    content_lines = []
    bullet_points = []
    
    for line in content_section.split('\n'):
        line = line.strip()
        if line and not line.startswith('[Back to'):
            if line.startswith('-') or line.startswith('*') or re.match(r'^\d+\.', line):
                # This is a bullet point
                bullet_points.append(line)
            elif line.startswith('> '):
                # This is a quote
                content_lines.append(line[2:])  # Remove the '> ' prefix
            elif line.startswith('#'):
                # This is a heading
                heading_level = len(re.match(r'^#+', line).group(0))
                content_lines.append(line[heading_level:].strip())
            else:
                # Regular text
                content_lines.append(line)
    
    # Convert markdown to html for certain elements (no need for full conversion)
    content_html = content_section  # We'll use the raw markdown for now
    
    return {
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "content_lines": content_lines,
        "bullet_points": bullet_points,
        "content_html": content_html
    }

def get_google_slides_service():
    """Get an authorized Google Slides API service instance."""
    creds = None
    
    # Check if token file exists
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    # Refresh the token if expired or get new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # You need to have a credentials.json file from the Google Cloud Console
            # When creating a new project, enable the Google Slides API and download the credentials
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for future runs
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    # Return the Google Slides service
    return build('slides', 'v1', credentials=creds)

def update_presentation(service, slides_data):
    """Update the Google Slides presentation with the provided data."""
    # Get the presentation
    presentation = service.presentations().get(presentationId=PRESENTATION_ID).execute()
    slides = presentation.get('slides', [])
    
    # Ensure we have enough slides
    if len(slides) < len(slides_data):
        print(f"Warning: Presentation has {len(slides)} slides, but we have data for {len(slides_data)} slides.")
    
    # Prepare requests for batch update
    requests = []
    
    # Update each slide
    for i, slide_data in enumerate(slides_data):
        if i >= len(slides):
            break  # Don't try to update slides that don't exist
        
        slide = slides[i]
        slide_id = slide.get('objectId')
        
        # Update title
        title_element = next((element for element in slide.get('pageElements', []) 
                             if element.get('shape', {}).get('shapeType') == 'TEXT_BOX' 
                             and 'title' in element.get('objectId', '').lower()), None)
        
        if title_element and slide_data["title"]:
            title_object_id = title_element.get('objectId')
            requests.append({
                'deleteText': {
                    'objectId': title_object_id,
                    'textRange': {
                        'type': 'ALL'
                    }
                }
            })
            requests.append({
                'insertText': {
                    'objectId': title_object_id,
                    'text': slide_data["title"],
                    'insertionIndex': 0
                }
            })
        
        # Update subtitle
        subtitle_element = next((element for element in slide.get('pageElements', []) 
                               if element.get('shape', {}).get('shapeType') == 'TEXT_BOX' 
                               and 'subtitle' in element.get('objectId', '').lower()), None)
        
        if subtitle_element and slide_data["subtitle"]:
            subtitle_object_id = subtitle_element.get('objectId')
            requests.append({
                'deleteText': {
                    'objectId': subtitle_object_id,
                    'textRange': {
                        'type': 'ALL'
                    }
                }
            })
            requests.append({
                'insertText': {
                    'objectId': subtitle_object_id,
                    'text': slide_data["subtitle"],
                    'insertionIndex': 0
                }
            })
        
        # Update content (for simplicity, just replace the first content element)
        content_element = next((element for element in slide.get('pageElements', []) 
                              if element.get('shape', {}).get('shapeType') == 'TEXT_BOX' 
                              and not ('title' in element.get('objectId', '').lower() 
                                      or 'subtitle' in element.get('objectId', '').lower())), None)
        
        if content_element:
            content_object_id = content_element.get('objectId')
            
            # Prepare content text
            content_text = slide_data["summary"] + "\n\n" if slide_data["summary"] else ""
            
            # Add bullet points
            if slide_data["bullet_points"]:
                for point in slide_data["bullet_points"]:
                    content_text += point + "\n"
            
            # Add other content lines
            if slide_data["content_lines"]:
                content_text += "\n".join(slide_data["content_lines"])
            
            # Replace content
            requests.append({
                'deleteText': {
                    'objectId': content_object_id,
                    'textRange': {
                        'type': 'ALL'
                    }
                }
            })
            requests.append({
                'insertText': {
                    'objectId': content_object_id,
                    'text': content_text,
                    'insertionIndex': 0
                }
            })
    
    # Execute batch update
    if requests:
        body = {
            'requests': requests
        }
        response = service.presentations().batchUpdate(
            presentationId=PRESENTATION_ID, body=body).execute()
        print(f"Updated {len(response.get('replies', []))} elements in the presentation.")
    else:
        print("No updates to make.")

def main():
    """Main function to update Google Slides."""
    # Load slide data
    slides_data = []
    for slide_file in SLIDES_ORDER:
        file_path = os.path.join(INVESTOR_SLIDES_DIR, slide_file)
        if os.path.exists(file_path):
            slide_data = parse_markdown_slide(file_path)
            slides_data.append(slide_data)
            print(f"Processed {slide_file}")
        else:
            print(f"Warning: Could not find {file_path}")
    
    # Initialize the Slides API
    try:
        service = get_google_slides_service()
        update_presentation(service, slides_data)
        print("Slides update completed!")
    except Exception as e:
        print(f"Error during slides update: {e}")

if __name__ == "__main__":
    main()