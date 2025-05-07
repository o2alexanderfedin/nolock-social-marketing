#!/usr/bin/env python3

slide_info = [
    (1, "Title Slide", "NoLock Social - Rebuild Trust in the Digital Space"),
    (2, "Fragmentation Problem", "How social networks and services suffer from fragmentation and duplication"),
    (3, "Bad Actors", "Issues with spam, scam, propaganda, and content moderation"),
    (4, "Information Overload", "Services overflowed with bad quality information"),
    (5, "Our Vision", "Everyone creates their own immutable content with full control"),
    (6, "Trust Networks", "Reinforcing connections with trusted people"),
    (7, "Fragmentation", "The problem with fragmentation in digital services"),
    (8, "Content Structure", "How NoLock approaches content structure"),
    (9, "Content Foundation", "The foundation of content addressable storage"),
    (10, "Network Foundation", "The network foundation of NoLock Social"),
    (11, "Technology Stack", "The technology stack powering NoLock Social"),
    (12, "CAS Technology", "Content-Addressable Storage technology explanation"),
    (13, "DISOT Technology", "Decentralized Immutable Source Of Truth"),
    (14, "Trust Networks", "How Networks of Trust are built and function"),
    (15, "AI Foundation", "Ideal foundation for AI and DApps"),
    (16, "Technology Benefits", "Benefits of NoLock's technology approach"),
    (17, "Our Approach", "Creating a decentralized digital space"),
    (18, "Key Advantages", "Future-proof, offline functionality, verifiable content, personalized trust"),
    (19, "Innovations", "Unique data storage algorithm and content-addressable programming language"),
    (20, "Call to Action", "Join us in redefining digital trust, ownership, and connections"),
    (21, "Team", "The NoLock Social team")
]

# Generate the table header
table = """## Slides

| # | Title | Image | Description |
|---|------|-------|-------------|
"""

# Generate a row for each slide
for num, title, desc in slide_info:
    # Format the slide number with leading zero for all slide numbers
    slide_num = f"{num:02d}"
    table += f"| {num} | [{title}](slides/slide{slide_num}.md) | ![Slide {num} Thumbnail](images/slide{num}.png) | {desc} |\n"

# Print the table
print(table)

with open("slide_table.md", "w") as f:
    f.write(table)