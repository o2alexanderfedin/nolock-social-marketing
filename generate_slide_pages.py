import os
import re

# Define paths
extracted_pdf_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/extracted_pdf"
slides_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/presentation/slides"

# Ensure slides directory exists
os.makedirs(slides_dir, exist_ok=True)

# Slide titles and descriptions (for slides we don't have yet)
slide_info = {
    2: {
        "title": "Fragmentation Problem",
        "description": "This slide highlights how social networks and services suffer from fragmentation and duplication, creating a disjointed user experience.",
        "key_points": [
            "Social networks and services begin with fragmentation and duplication",
            "Users must maintain multiple profiles across different platforms",
            "Content gets duplicated across different services",
            "Attention and data become scattered"
        ]
    },
    3: {
        "title": "Bad Actors",
        "description": "This slide discusses how bad actors post spam, scams, and propaganda, while some legitimate content from good actors gets banned.",
        "key_points": [
            "Bad actors spread spam, scams, and propaganda across platforms",
            "Content moderation struggles to identify harmful content",
            "Some legitimate content is incorrectly flagged and removed",
            "Trust in platform moderation diminishes"
        ]
    },
    4: {
        "title": "Information Overload",
        "description": "This slide explains how services become overflowed with low-quality information, and how some users are completely banned from access.",
        "key_points": [
            "Digital services are overwhelmed with low-quality information",
            "Signal-to-noise ratio continuously decreases",
            "Some legitimate users lose access entirely",
            "Information quality becomes harder to verify"
        ]
    },
    6: {
        "title": "Trust Networks",
        "description": "This slide explains how NoLock Social reinforces connections with trusted people while ignoring harmful information.",
        "key_points": [
            "Gradual reinforcement of connections with trusted people",
            "Natural filtering of untrusted information",
            "User control over information flow",
            "Trust replaces algorithmic content sorting"
        ]
    },
    7: {
        "title": "Fragmentation",
        "description": "This slide revisits the problem of fragmentation in social networks and digital services.",
        "key_points": [
            "Fragmentation creates barriers to effective communication",
            "Multiple platforms lead to inconsistent user experiences",
            "Content gets duplicated and loses context",
            "User attention becomes divided across services"
        ]
    },
    8: {
        "title": "Content Structure",
        "description": "This slide discusses how NoLock approaches content structure to solve fragmentation issues.",
        "key_points": [
            "Content-addressable approach to eliminate duplication",
            "Unified content structure across platforms",
            "User-controlled sharing and visibility",
            "Consistent content identification"
        ]
    },
    9: {
        "title": "Content Foundation",
        "description": "This slide explains the foundation of content addressable storage in the NoLock system.",
        "key_points": [
            "Content is addressed by what it is, not where it's stored",
            "Cryptographic validation ensures content integrity",
            "Immutable content creates a reliable foundation",
            "Decentralized storage eliminates single points of failure"
        ]
    },
    10: {
        "title": "Network Foundation",
        "description": "This slide outlines the network foundation of NoLock Social.",
        "key_points": [
            "Trust-based networking replaces algorithmic sorting",
            "Connection strength builds over time through interactions",
            "Network topology reflects genuine relationships",
            "Information flows through trusted channels"
        ]
    },
    11: {
        "title": "Technology Stack",
        "description": "This slide describes the technology stack powering NoLock Social.",
        "key_points": [
            "Three-layer architecture for complete solution",
            "Content storage, identity, and social layers working together",
            "Compatible with existing web technologies",
            "Designed for resilience and user control"
        ]
    },
    12: {
        "title": "CAS Technology",
        "description": "This slide provides a detailed explanation of the Content-Addressable Storage technology.",
        "key_points": [
            "Storage system unaware of content structure",
            "Address points to data through cryptographic hash functions",
            "Enables content verification and integrity",
            "Creates foundation for trustless content sharing"
        ]
    },
    13: {
        "title": "DISOT Technology",
        "description": "This slide explains the Decentralized Immutable Source Of Truth technology.",
        "key_points": [
            "Built on top of CAS for handling mutable data",
            "Uses digital signatures for verification",
            "Provides revision formats for content updates",
            "Maintains data integrity across changes"
        ]
    },
    14: {
        "title": "Trust Networks",
        "description": "This slide details how Networks of Trust are built and function in the NoLock ecosystem.",
        "key_points": [
            "Built on DISOT for verifiable connections",
            "Focuses on weighted subjective trust",
            "Reduces information noise through trust filtering",
            "Creates positive-sum interactions between users"
        ]
    },
    15: {
        "title": "AI Foundation",
        "description": "This slide explains how NoLock Social provides an ideal foundation for AI and decentralized applications.",
        "key_points": [
            "Digital rights framework ensures clear content ownership",
            "Enables collective ownership of AI resources",
            "Provides verifiable database as single source of truth",
            "Enhances data quality for machine learning"
        ]
    },
    16: {
        "title": "Technology Benefits",
        "description": "This slide outlines the key benefits of NoLock's technology approach.",
        "key_points": [
            "Improved data ownership and control",
            "Enhanced privacy through encryption options",
            "Better content discovery through trust networks",
            "Resilience against censorship and platform changes"
        ]
    },
    18: {
        "title": "Key Advantages",
        "description": "This slide presents the key advantages of the NoLock approach: future-proof design, offline functionality, verifiable content, and personalized trust.",
        "key_points": [
            "Future-Proof: Easy protocol and cryptography upgrades without data loss",
            "Offline Functionality: Works reliably without constant internet connectivity",
            "Verifiable Content: Data authenticity and integrity verification",
            "Personalized Trust: User-defined trust ratings based on individual networks"
        ]
    },
    19: {
        "title": "Innovations",
        "description": "This slide showcases NoLock's innovative unique data storage algorithm and content-addressable programming language.",
        "key_points": [
            "Unique data storage algorithm reduces storage space and network traffic",
            "Content-addressable programming language designed for efficient development",
            "FunctionalScript provides JavaScript compatibility",
            "Technical innovations create practical improvements for users"
        ]
    },
    20: {
        "title": "Call to Action",
        "description": "This slide invites viewers to join NoLock Social in redefining digital trust, ownership, and connections.",
        "key_points": [
            "Seeking partners to build on this foundation",
            "Invitation to join in redefining digital trust",
            "Multiple ways to connect and engage",
            "Vision for a collaborative ecosystem"
        ]
    },
    21: {
        "title": "Team",
        "description": "This slide introduces the NoLock Social team members.",
        "key_points": [
            "Diverse team with complementary skills",
            "Experience in blockchain, content systems, and security",
            "Commitment to rebuilding digital trust",
            "Open collaboration approach"
        ]
    }
}

# Generate all slide pages
for page_num in range(1, 22):
    # Skip slides we've already created manually
    if page_num in [1, 5, 17]:
        continue
        
    # Read the text content from the extracted PDF
    text_file = os.path.join(extracted_pdf_dir, f"page_{page_num}_text.txt")
    with open(text_file, 'r') as f:
        content = f.read().strip()
    
    # Get slide info
    slide_info_dict = slide_info.get(page_num, {
        "title": f"Slide {page_num}",
        "description": f"This is slide {page_num} of the NoLock Social presentation.",
        "key_points": ["Key information about this slide is being processed."]
    })
    
    # Create the slide markdown content
    slide_md = f"""# Slide {page_num}: {slide_info_dict['title']}

![Slide {page_num}](../../docs/assets/pdf_images/page_{page_num}.png)

## Content

```
{content}
```

## Description

{slide_info_dict['description']}

## Key Points

"""
    
    # Add key points
    for point in slide_info_dict.get('key_points', []):
        slide_md += f"- {point}\n"
    
    # Add navigation links
    slide_md += f"\n[Back to Index](../README.md)"
    
    if page_num > 1:
        slide_md += f" | [Previous Slide](slide{page_num-1:02d}.md)"
        
    if page_num < 21:
        slide_md += f" | [Next Slide](slide{page_num+1:02d}.md)"
    
    # Write the slide markdown to a file
    output_file = os.path.join(slides_dir, f"slide{page_num:02d}.md")
    with open(output_file, 'w') as f:
        f.write(slide_md)
    
    print(f"Created slide {page_num}")

print("All slide pages generated successfully!")