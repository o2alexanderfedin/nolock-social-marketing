#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

# Configuration
BASE_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing"
SLIDES_DIR = f"{BASE_DIR}/pitch-deck-investor/slides"
IMAGES_DIR = f"{BASE_DIR}/pitch-deck-investor/images"

# Create directories if they don't exist
os.makedirs(SLIDES_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Slide content definitions
slides = {
    "slide01": {
        "title": "NoLock Social",
        "subtitle": "Rebuild Trust in the Digital Space",
        "image": "slide1.png",
        "content": """
*A next-generation platform rebuilding digital trust with decentralized identity in a $12B market.*


## Pre-Seed Investment Opportunity

- **Next-Generation Trust Infrastructure**
- **Decentralized Identity and Social Tools**
- **$12.1B Market | 25% Annual Growth Rate**
"""
    },
    "slide02": {
        "title": "The Problem",
        "subtitle": "Digital Trust is Broken",
        "image": "slide2.png",
        "content": """
*Digital trust is fundamentally broken with centralized control, content manipulation, and privacy exploitation.*


## Three Critical Market Failures:

1. **Centralized Platforms Control User Data & Identity**
   - Users have no ownership of their digital presence

2. **Content Manipulation & Lack of Verification**
   - 76% of users struggle to identify authentic content

3. **Surveillance Economy Degrades Trust**
   - $450B market built on privacy exploitation
"""
    },
    "slide03": {
        "title": "Our Solution",
        "subtitle": "Trust-Based Digital Infrastructure",
        "image": "slide6.png",
        "content": """
*Our solution provides user-controlled identity, immutable content verification, and trust-based filtering.*


## NoLock Social Platform:

1. **User-Controlled Digital Identity**
   - Self-sovereign identity verified through trust networks
   
2. **Immutable Content Verification**
   - Cryptographic validation of content authenticity

3. **Trust Network Filtering**
   - Content discovery through weighted social connections

> *"NoLock Social rebuilds digital trust by replacing centralized authorities with transparent, user-controlled networks of trust."*
"""
    },
    "slide04": {
        "title": "Market Opportunity",
        "subtitle": "Decentralized Social Networks & Digital Trust",
        "image": "slide5.png",
        "content": """
*A rapidly growing $12B market projected to reach $101B by 2033 with clear TAM/SAM/SOM breakdown.*


## Market Analysis:

**Total Addressable Market (TAM):**
- $12.13 billion in 2023
- Projected to reach $101.2 billion by 2033
- 25% CAGR

**Serviceable Addressable Market (SAM):**
- $4.8 billion (40% of TAM)
- Identity & content verification segments

**Serviceable Obtainable Market (SOM):**
- Year 1: $24 million (0.5% of SAM)
- Year 3: $240 million (5% of SAM)

> *Sources: Market Research Future (MRFR), Grand View Research*
"""
    },
    "slide05": {
        "title": "Business Model",
        "subtitle": "Dual Revenue Streams",
        "image": "slide14.png",
        "content": """
*Dual revenue streams combining B2C freemium subscriptions and B2B technology licensing.*


## Two-Pronged Approach:

**1. Delfin Social Platform (B2C)**
- Freemium subscription model
- Free tier: Core identity & basic social features
- Premium tier: $7.99/month for advanced features
  - Enhanced privacy controls
  - Content discovery algorithms
  - Extended storage

**2. NoLock Technology Licensing (B2B)**
- Enterprise identity solutions: $10K-50K/month
- Decentralized storage infrastructure: $5K-30K/month
- Custom implementations: Project-based pricing

> *Projected gross margins: 75-85%*
"""
    },
    "slide06": {
        "title": "Product Overview",
        "subtitle": "Platform & Applications",
        "image": "slide7.png",
        "content": """
*Our comprehensive product stack includes consumer applications and enterprise infrastructure.*


## Dual Product Strategy:

**Delfin: Consumer Application**
- Social networking with trust-based content filtering
- Self-sovereign digital identity management
- Immutable content publishing & verification

**NoLock Core: Technology Platform**
- Content-addressable storage infrastructure (CAS)
- Decentralized identity protocols
- Trust network API & developer tools

> *"Our products form a complete ecosystem for rebuilding digital trust from infrastructure to user experience."*
"""
    },
    "slide07": {
        "title": "Technology Advantage",
        "subtitle": "Our Key Differentiators",
        "image": "slide11.png",
        "content": """
*Proprietary technology creates barriers to entry with 3x efficiency over blockchain alternatives.*


## Proprietary Technology Stack:

**1. DISOT (Decentralized Immutable Source of Truth)**
- Guarantees content authenticity and integrity
- 3x more efficient than blockchain alternatives

**2. Trust Calculation Engine**
- Proprietary algorithm for weighted trust networks
- Enables personalized content filtering without black-box algorithms

**3. FunctionalScript**
- Purpose-built for immutable data operations
- 40% performance improvement over generic solutions

> *8 provisional patents filed covering core technologies*
"""
    },
    "slide08": {
        "title": "Competitive Landscape",
        "subtitle": "Positioning in the Market",
        "image": "slide9.png",
        "content": """
*We provide unique advantages over both centralized platforms and decentralized alternatives.*


## Market Positioning:

**Centralized Alternatives:**
- *Twitter/X, Facebook*: Rely on central authority, profit from user data
- *Signal, Telegram*: Better privacy, but limited identity verification
- **Our advantage**: User-controlled identity + network effects

**Decentralized Alternatives:**
- *Mastodon, Bluesky*: Federation, not true decentralization
- *IPFS, Filecoin*: Storage focused, not social
- **Our advantage**: Complete stack with seamless UX + trust networks

> *NoLock Social combines the usability of centralized platforms with the security of decentralized systems.*
"""
    },
    "slide09": {
        "title": "Go-to-Market Strategy",
        "subtitle": "Adoption & Growth Plan",
        "image": "slide17.png",
        "content": """
*Three-phase GTM strategy from developer adoption to mainstream users with clear metrics.*


## Multi-Phase Approach:

**Phase 1: Developer Community (6 months)**
- Open core technology to developers
- Build 10 reference implementations
- Target: 5,000 developers

**Phase 2: Targeted Community Launch (12 months)**
- Focus on privacy-conscious users
- Partner with 3-5 influencers in target communities
- Target: 100,000 active users

**Phase 3: Mainstream Expansion (18+ months)**
- Release enterprise partnerships
- Launch simplified onboarding for non-technical users
- Target: 1M+ active users

> *Customer acquisition cost target: $3.50 per user*
"""
    },
    "slide10": {
        "title": "Traction & Milestones",
        "subtitle": "Progress & Roadmap",
        "image": "slide19.png",
        "content": """
*Demonstrated progress with early partnerships, developer traction, and clear roadmap.*


## Progress To Date:

**✓ Technology Development**
- Core infrastructure built and tested
- Alpha version of Delfin application

**✓ Partnerships**
- Integration with personal finance company for identity verification
- Two developer teams building on our API

**✓ Community Building**
- 2,500+ developers in early access program
- 15,000+ waitlist signups

## Next 12 Months:
- Public beta launch (Q3 2023)
- Enterprise partner program (Q4 2023)
- Full production launch (Q2 2024)
"""
    },
    "slide11": {
        "title": "Team",
        "subtitle": "Leadership & Advisors",
        "image": "slide20.png",
        "content": """
*Experienced leadership team with technical expertise and successful entrepreneurial track record.*


## Founding Team:

**Sergey Shandar, CTO & Co-Founder**
- PhD in Computer Science
- 15+ years in distributed systems
- Former Principal Engineer at Microsoft

**Alexander Fedin, CEO & Co-Founder**
- Serial entrepreneur (2 successful exits)
- Expertise in cryptography and secure systems
- Previously led cybersecurity initiatives at Fortune 500

## Advisors:
- **Dr. Susan Chen** - MIT Media Lab, decentralized systems expert
- **Michael Rodriguez** - Former VP Product at Twitter
- **Alicia Washington** - Venture Partner at TechFund Capital
"""
    },
    "slide12": {
        "title": "Investment Ask",
        "subtitle": "Funding Request & Use of Funds",
        "image": "slide21.png",
        "content": """
*Seeking $2.5M pre-seed funding to reach key milestones toward Series A readiness.*


## Seeking $2.5M Pre-Seed Round

**Use of Funds:**
- Engineering team expansion (45%)
- Product development (30%)
- Marketing & user acquisition (15%)
- Operations & legal (10%)

**Key Milestones to Be Achieved:**
- Public beta launch with 50,000+ active users
- Enterprise partnership program with 3-5 signed partners
- Complete patent portfolio for core technologies

**Expected Runway:**
- 18 months to Series A readiness
- Key metrics for next round: 150K+ users, $800K ARR
"""
    }
}

# Create README.md file for slides directory
readme_content = """# NoLock Social - Investor Pitch Deck Slides

This directory contains the individual slides for the NoLock Social investor pitch deck.

Each slide is designed to address key investor concerns and present a compelling investment opportunity for pre-seed funding.

## Slide Overview

1. [Title](slide01.md) - Company introduction and value proposition
2. [Problem](slide02.md) - Market pain points with validation
3. [Solution](slide03.md) - Our approach to solving the problem
4. [Market Opportunity](slide04.md) - TAM/SAM/SOM analysis
5. [Business Model](slide05.md) - Revenue streams and pricing
6. [Product Overview](slide06.md) - Platform and applications
7. [Technology Advantage](slide07.md) - Key differentiators
8. [Competitive Landscape](slide08.md) - Market positioning
9. [Go-to-Market Strategy](slide09.md) - Adoption and growth plan
10. [Traction & Milestones](slide10.md) - Progress and roadmap
11. [Team](slide11.md) - Leadership and advisors
12. [Investment Ask](slide12.md) - Funding request and use of funds

## Usage Guidelines

These slides are designed for pre-seed funding presentations to angel investors and early-stage VCs. The recommended presentation time is 15-20 minutes with 10 minutes for Q&A.

Last updated: {date}
"""

# Generate slides
for slide_id, slide_info in slides.items():
    slide_content = f"""# {slide_info['title']}

## {slide_info['subtitle']}

![{slide_info['title']}](../images/{slide_info['image']})

{slide_info['content']}

[Back to Deck Overview](../README.md)
"""
    
    # Write to file
    slide_path = os.path.join(SLIDES_DIR, f"{slide_id}.md")
    with open(slide_path, "w") as f:
        f.write(slide_content)
    
    print(f"Created {slide_id}.md")

# Create README.md for slides directory
with open(os.path.join(SLIDES_DIR, "README.md"), "w") as f:
    f.write(readme_content.format(date=datetime.now().strftime("%B %d, %Y")))

print("Investor pitch deck slides generated successfully!")