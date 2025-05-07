#!/usr/bin/env python3

"""
Script to generate the remaining pitch deck slides based on the established pattern.
This creates structured, best-practice pitch content for the NoLock Social presentation.
"""

import os

# Define the slides to generate (excluding ones we've already created manually)
slides_to_generate = [
    (4, "Information Overload", "Problem Statement", 
     "THE INFORMATION QUALITY DILEMMA",
     [
         "Digital services overflowed with low-quality content",
         "Signal-to-noise ratio decreasing exponentially",
         "Some valuable voices completely silenced",
         "Users struggle to find relevant, trustworthy information"
     ],
     "This slide highlights how digital services are overwhelmed with low-quality information, making it difficult for users to find valuable content. Some legitimate users are even completely banned from access, further reducing the diversity and quality of digital discourse.",
     "The volume of digital content is growing exponentially—over 500 million tweets, 4 million blog posts, and 720,000 hours of YouTube content are created daily. But studies show that only about 3% of this content delivers genuine value to users."
    ),
    
    (6, "Trust Networks", "Solution / Concept", 
     "TRUST-BASED FILTERING",
     [
         "Progressive strengthening of trusted connections",
         "Natural filtering based on genuine relationships",
         "User control over information sources",
         "Quality emerges from network relationships"
     ],
     "This slide explains how NoLock Social reinforces connections with trusted people while naturally filtering out unwanted information, creating a more authentic digital experience based on real relationships rather than algorithms.",
     "Rather than attempting perfect content moderation through AI—which even the largest platforms have failed to achieve—we enable a more human approach where trust relationships naturally filter information, just as they do in real-world communities."
    ),
    
    (7, "Fragmentation", "Problem Synthesis", 
     "THE FRAGMENTED DIGITAL LANDSCAPE",
     [
         "Disconnected content silos controlled by platforms",
         "No interoperability or portability between services",
         "User attention and data scattered across applications",
         "Digital identity fractured and inconsistent"
     ],
     "This slide provides a synthetic view of the fragmentation problem in digital services, showing how our current approach creates fundamental inefficiencies and poor user experiences.",
     "The fragmented digital landscape isn't just inconvenient—it represents a structural inefficiency that costs users time, reduces information quality, and prevents the emergence of truly valuable digital experiences."
    ),
    
    (8, "Content Structure", "Technical Concept", 
     "REIMAGINING CONTENT STRUCTURE",
     [
         "Content addressed by what it is, not where it's stored",
         "User ownership from creation through all sharing",
         "Verifiable provenance for all digital content",
         "Cross-platform consistency and portability"
     ],
     "This slide explains how NoLock approaches content structure differently, using content-addressing to create a more coherent, user-controlled digital experience.",
     "By fundamentally reimagining how digital content is structured, addressed, and shared, we create a foundation that solves the underlying problems of fragmentation, ownership, and trust."
    ),
    
    (9, "Content Foundation", "Technical Solution", 
     "CONTENT-ADDRESSABLE FOUNDATION",
     [
         "Content identified by cryptographic hash, not location",
         "Immutable, verifiable data with built-in integrity",
         "Efficient storage and retrieval without central control",
         "Foundation for ownership and trust mechanisms"
     ],
     "This slide details the foundation of content addressable storage in the NoLock system, explaining how it provides the technical basis for our approach to digital content.",
     "Content-addressable storage has proven its value in systems like Git for version control and IPFS for distributed content, but NoLock Social takes this concept further by making it the foundation for social connections and trust."
    ),
    
    (10, "Network Foundation", "Technical Solution", 
     "TRUST NETWORK ARCHITECTURE",
     [
         "Connections based on direct relationship strength",
         "Progressive trust development through interaction",
         "Resilient against manipulation and spam",
         "Content discovery through trusted relationships"
     ],
     "This slide outlines the network foundation of NoLock Social, showing how trust relationships form the basis for content discovery and sharing.",
     "Our network architecture models how human trust actually works—it's built gradually, it's contextual, and it creates resilient communities that naturally filter information based on credibility and relevance."
    ),
    
    (11, "Technology Stack", "Technical Overview", 
     "THREE-LAYER TECHNOLOGY STACK",
     [
         "Layer 1: Universal Content-Addressable Storage",
         "Layer 2: Decentralized Identity & Verification",
         "Layer 3: Trust-Based Social Networking",
         "Complete solution from storage to social interaction"
     ],
     "This slide presents the complete technology stack powering NoLock Social, showing how the three layers work together to create a comprehensive solution.",
     "Each layer of our stack builds on the capabilities of the layer below it, creating a coherent system that addresses the full range of challenges in today's digital landscape—from data storage to identity to social connection."
    ),
    
    (12, "CAS Technology", "Technical Deep Dive", 
     "CONTENT-ADDRESSABLE STORAGE",
     [
         "Storage unaware of content structure or relationships",
         "Cryptographic hash functions verify data integrity",
         "Address points directly to data, not location",
         "Foundation for verifiable, immutable content"
     ],
     "This slide provides a more detailed explanation of Content-Addressable Storage technology, showing how it forms the foundation of our approach.",
     "Content-addressable storage creates a paradigm shift in how we think about digital content—when the address IS the content (through its hash), we gain powerful new capabilities for verification, deduplication, and decentralization."
    ),
    
    (13, "DISOT Technology", "Technical Deep Dive", 
     "DECENTRALIZED IMMUTABLE SOURCE OF TRUTH",
     [
         "Built on CAS for handling mutable data securely",
         "Digital signatures verify content authenticity",
         "Revision formats maintain history while enabling updates",
         "Creates verifiable chain of content provenance"
     ],
     "This slide explains the Decentralized Immutable Source Of Truth technology that NoLock Social uses to handle mutable data while maintaining verification.",
     "DISOT solves one of the hardest problems in decentralized systems—how to allow content to evolve while maintaining a verifiable history and clear ownership, creating a foundation for both static and dynamic content."
    ),
    
    (14, "Trust Networks", "Technical Concept", 
     "NETWORKS OF TRUST",
     [
         "Built on DISOT for verifiable connections",
         "Weighted subjective trust reduces noise",
         "Creates positive-sum interactions between users",
         "Enables natural content filtering and discovery"
     ],
     "This slide details how Networks of Trust are built and function in the NoLock Social ecosystem, creating a more natural way to discover and evaluate content.",
     "By modeling how human trust networks actually work, we create digital spaces that feel more natural, more authentic, and more valuable—replacing engagement-maximizing algorithms with human-centered connection."
    ),
    
    (16, "Benefits", "Value Proposition", 
     "KEY BENEFITS",
     [
         "True ownership of your digital presence and content",
         "Consistent experience across devices and contexts",
         "Reduced noise and increased signal in information flow",
         "Resilience against platform changes and censorship"
     ],
     "This slide outlines the key benefits of the NoLock Social approach, focusing on the user-centric advantages it provides over current platforms.",
     "These benefits directly address the pain points that billions of users experience daily with current platforms—fragmentation, noise, lack of control, and vulnerability to platform policies."
    )
]

# Template for pitch deck slides
slide_template = """# Slide {num}: {title}

![{title}](../images/slide{num}.png)

## Content Type: {content_type}

```
{headline}

{bullet_points}
```

## Design Elements

- **Headline**: Bold, attention-grabbing typography presenting the key concept
- **Bullet Points**: Concise statements highlighting the main aspects
- **Supporting Visual**: Clear visual representation of the concept
- **Layout**: Professional organization with clear hierarchy
- **Color Scheme**: Consistent with overall presentation branding

## Pitch Notes

**Key message:**
"{pitch_message}"

**Supporting points:**
{bullet_pitch_points}

**Evidence/Impact:**
"{evidence}"

## Follow-Up Slide

This slide connects to the next slide, continuing the logical flow of the presentation narrative.
"""

# Directory for pitch deck slides
slides_dir = "/Users/alexanderfedin/Projects/nolock.social/marketing/pitch-deck/slides"

# Ensure the directory exists
os.makedirs(slides_dir, exist_ok=True)

# Generate each slide
for slide_info in slides_to_generate:
    num, title, content_type, headline, bullets, pitch_message, evidence = slide_info
    
    # Format slide number with leading zero if needed
    slide_num_format = f"{num:02d}"
    
    # Format bullet points for markdown
    bullet_points_text = "\n".join([f"• {bullet}" for bullet in bullets])
    
    # Format bullet points for pitch notes
    bullet_pitch_points = "\n".join([f"{i+1}. \"{bullet}\"" for i, bullet in enumerate(bullets)])
    
    # Fill in the template
    slide_content = slide_template.format(
        num=num,
        title=title,
        content_type=content_type,
        headline=headline,
        bullet_points=bullet_points_text,
        pitch_message=pitch_message,
        bullet_pitch_points=bullet_pitch_points,
        evidence=evidence
    )
    
    # Write the slide file
    slide_file = os.path.join(slides_dir, f"slide{slide_num_format}.md")
    
    # Only write if file doesn't exist (to avoid overwriting manual files)
    if not os.path.exists(slide_file):
        with open(slide_file, "w") as f:
            f.write(slide_content)
        print(f"Created slide {num}: {title}")
    else:
        print(f"Skipping existing slide {num}: {title}")

print("Pitch deck slide generation complete!")