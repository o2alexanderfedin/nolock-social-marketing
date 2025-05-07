# CLAUDE.md - NoLock Social Project Guide

## Project Overview

NoLock Social is building a decentralized digital ecosystem that enables users to own their content, establish trusted connections, and interact in a more authentic digital environment. The project focuses on rebuilding trust in the digital space through innovative approaches to content storage, identity, and social networking.

## Core Technology Components

1. **Universal Content-Addressable Storage (CAS)**
   - Secure, conflict-free data synchronization across devices
   - Content identified by cryptographic hash, not location
   - Immutable content foundation

2. **Decentralized Identity**
   - Verifiable content linked to user-controlled identities
   - Trusted timestamps for content verification
   - User ownership of digital identity

3. **Networks of Trust**
   - Personal social networks built on weighted subjective trust
   - Natural filtering of information through trusted connections
   - Positive-sum interactions between users

## Key Innovations

1. **Unique Data Storage Algorithm**
   - Significantly reduces storage space and network traffic
   - More efficient than traditional CAS systems
   - Enables practical everyday use of content-addressable storage

2. **FunctionalScript**
   - Content-addressable programming language
   - Compatible with JavaScript
   - Highly scalable for decentralized applications

## Project Products

1. **Blockset**
   - Core content-addressable storage technology
   - Developed by Sergey Shandar
   - Democratizes CAS for individual users

2. **Delfin**
   - Decentralized social network based on trust models
   - User-controlled content sharing and discovery
   - Progressive trust building

## Key Advantages

- **Future-Proof**: Easy protocol and cryptography upgrades without data loss
- **Offline Functionality**: Works reliably without constant internet connectivity
- **Verifiable Content**: Ensures data authenticity and integrity
- **Personalized Trust**: User-defined trust ratings based on individual networks

## Project Structure

- `/marketing/` - Marketing materials and documentation
  - `/docs/` - Core documentation
    - `/overview/` - Project introduction
    - `/vision/` - Vision and principles
    - `/problem/` - Problem statements
    - `/solution/` - Technical solutions
    - `/connect/` - Ways to get involved
    - `/assets/` - Images and resources
      - `/pdf_images/` - Original slide images from PDF
  - `/presentation-metadata/` - Detailed slide content and annotations
    - `/slides/` - Individual slide pages with metadata (slide01.md - slide21.md)
    - `/images/` - Slide images with consistent naming (slide1.png - slide21.png)
    - `README.md` - Index page with thumbnails and links to all slides
    - `nolock_social_presentation.pdf` - Full presentation PDF
  - `/pitch-deck/` - Professional presentation content
    - `/slides/` - Best-practice pitch content for each slide
    - `/images/` - Slide images for the pitch deck
    - `README.md` - Pitch deck structure and usage guidelines
    - `CUSTOMER_REVIEW.md` - Analysis from a customer perspective
    - `INVESTOR_REVIEW.md` - Analysis from an investor perspective
  - `/pitch-deck-investor/` - Investor-focused pitch deck
    - `/slides/` - Investor-tailored slide content (slide01.md - slide12.md)
    - `/images/` - Slide images for the investor deck
    - `README.md` - Investor pitch structure and guidelines
    - `INVESTOR_QA.md` - Investor requirements and specifications
    - `REVIEW_RESPONSE.md` - How this deck addresses investor feedback
    - `PRESENTATION_GUIDE.md` - Talking points and presentation tips
  - `/pitch-deck-investor-full/` - Comprehensive investor pitch deck
    - `/slides/` - Full investor slide content (slide01.md - slide21.md) 
    - `/images/` - Slide images for the comprehensive deck
    - `README.md` - Full investor pitch structure and guidelines

## Command Reference

When working with this project, the following commands may be useful:

```bash
# Navigate to project directory
cd /Users/alexanderfedin/Projects/nolock.social/marketing

# View presentation metadata
open presentation-metadata/README.md

# Extract text from PDF (if needed)
python3 extract_pdf.py

# Convert PDF to images (if needed)
python3 pdf_to_images.py

# Generate slide pages (if needed)
python3 generate_slide_pages.py

# Generate pitch deck slides (if needed)
python3 generate_pitch_slides.py

# Generate investor pitch deck slides (if needed)
python3 generate_investor_slides.py

# Generate full investor pitch deck slides (21 slides)
python3 generate_investor_slides_full.py
```

## Key Concepts and Terminology

- **Content-Addressable Storage (CAS)**: A storage mechanism where data is identified by its content rather than its location
- **DISOT (Decentralized Immutable Source Of Truth)**: Built on CAS, uses digital signatures for mutable data
- **Weighted Subjective Trust**: Trust ratings based on individual relationships, not algorithms
- **Immutable Content**: Content that cannot be altered once created
- **Trusted Timestamps**: Verification of when content was created
- **Networks of Trust**: Social connections based on real-world trust relationships

## Important Links

- **Website**: [https://nolock.social/](https://nolock.social/)
- **Discord**: [https://discord.gg/QdatyarG94](https://discord.gg/QdatyarG94)
- **Bluesky**: [https://bsky.app/profile/nolock-social.bsky.social](https://bsky.app/profile/nolock-social.bsky.social)
- **Email**: [info@nolock.social](mailto:info@nolock.social)

## Team Members

- **Sergey** - Creator of Blockset & FunctionalScript
- **Alex** - Strategy and user experience
- **Gela** - Architecture and systems design
- **Rodion** - Network security and protocols
- **Denis** - Distributed systems and data integrity
- **Vladimir, Nikita, Eldar** - Software development

## Key Files and Resources

- **Complete Presentation**: `/marketing/docs/assets/nolock_social_presentation.pdf`
- **Presentation Metadata**: `/marketing/presentation-metadata/README.md`
- **Documentation Root**: `/marketing/docs/README.md`

---

*This CLAUDE.md file serves as a comprehensive guide to the NoLock Social project for Claude's reference.*