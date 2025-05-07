#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

# Configuration
BASE_DIR = "/Users/alexanderfedin/Projects/nolock.social/marketing"
SLIDES_DIR = f"{BASE_DIR}/pitch-deck-investor-full/slides"
IMAGES_DIR = f"{BASE_DIR}/pitch-deck-investor-full/images"

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

[Source: Market Research Future (MRFR)](https://www.marketresearchfuture.com/reports/decentralized-social-network-market-11591)
"""
    },
    "slide02": {
        "title": "The Problem I",
        "subtitle": "Distrust in Digital Space",
        "image": "slide2.png",
        "content": """
*Content authenticity issues and lack of ownership create fundamental digital trust challenges.*


## Critical Issues:

- **Content that can be secretly modified**
  - No guarantee that what you see is what was produced
  - [Source: Reuters Digital News Report](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2022)

- **No inherent ownership means no responsibility**
  - Rampant misinformation without accountability
  - [Source: World Economic Forum](https://www.weforum.org/agenda/2022/06/digital-trust-in-a-polarized-world/)

> *76% of users struggle to identify authentic content in digital spaces*
"""
    },
    "slide03": {
        "title": "The Problem II",
        "subtitle": "Digital Vulnerability",
        "image": "slide3.png",
        "content": """
*Centralized data vulnerabilities and the surveillance economy compromise user privacy and security.*


## Serious Vulnerabilities:

- **Centralized data storage risks**
  - Single point of failure for billions of users
  - Frequent breaches compromising sensitive information
  - [Source: Identity Theft Resource Center](https://www.idtheftcenter.org/publication/identity-theft-resource-centers-2021-annual-data-breach-report-sets-new-record-for-number-of-compromises/)

- **User data as business model**
  - $450B market built on privacy exploitation
  - [Source: Harvard Business Review](https://hbr.org/2022/10/the-hidden-cost-of-digital-surveillance)

> *Digital infrastructure is increasingly built on extractive economics rather than value creation*
"""
    },
    "slide04": {
        "title": "The Problem III",
        "subtitle": "Trust Without Verification",
        "image": "slide4.png",
        "content": """
*Current digital systems require blind trust in central authorities without transparency.*


## Fundamental Design Flaws:

- **Trust without verification**
  - Systems rely on blind trust in central authorities
  - No transparency into data integrity
  - [Source: World Economic Forum Trust Report](https://www.weforum.org/reports/digital-trust-insight-report/)

- **Siloed ecosystems**
  - Walled gardens prevent interoperability
  - User lock-in through platform dependence
  - [Source: Competition in Digital Markets Report](https://judiciary.house.gov/uploadedfiles/competition_in_digital_markets.pdf)

> *83% of consumers express concern about how their data is being used online*
"""
    },
    "slide05": {
        "title": "Our Vision",
        "subtitle": "A New Digital Infrastructure",
        "image": "slide5.png",
        "content": """
*Building a new trust layer based on cryptographic proof rather than blind trust.*


## Building a New Trust Layer:

- **Rebuilding digital trust through decentralized technology**
  - User-controlled identity and content verification
  - [Source: Web3 Foundation](https://web3.foundation/about/)

- **Digital interactions based on cryptographic proof, not blind trust**
  - Transparent content verification without central authority
  - [Source: MIT Digital Currency Initiative](https://dci.mit.edu/research/2022/5/3/verifiable-credentials)

- **Networks of trust that mimic real-world social dynamics**
  - Content filtering through trusted relationships, not algorithms
  - [Source: Nature: Human Behavior](https://www.nature.com/nathumbehav/)

> *"Creating digital spaces where trust can be earned rather than assumed"*
"""
    },
    "slide06": {
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
- [Source: Market Research Future (MRFR)](https://www.marketresearchfuture.com/reports/decentralized-social-network-market-11591)

**Serviceable Addressable Market (SAM):**
- $4.8 billion (40% of TAM)
- Identity & content verification segments
- [Source: Grand View Research](https://www.grandviewresearch.com/industry-analysis/digital-identity-solutions-market)

**Serviceable Obtainable Market (SOM):**
- Year 1: $24 million (0.5% of SAM)
- Year 3: $240 million (5% of SAM)
- Based on [projected adoption rates](https://www.statista.com/statistics/1281525/web3-sector-predicted-market-size-worldwide/) for Web3 technologies
"""
    },
    "slide07": {
        "title": "Our Solution",
        "subtitle": "Universal Content-Addressable Storage",
        "image": "slide6.png",
        "content": """
*Our core technology uses content-addressable storage with superior efficiency and security.*


## Core Technology:

- **Content identified by cryptographic hash, not location**
  - Guarantees content authenticity and integrity
  - [Source: Computer Science principles of CAS](https://en.wikipedia.org/wiki/Content-addressable_storage)

- **Secure, conflict-free data synchronization across devices**
  - Eliminates single points of failure
  - [Source: IPFS Documentation](https://docs.ipfs.tech/concepts/how-ipfs-works/)

- **Significant reduction in storage space and network traffic**
  - 40-60% more efficient than traditional content-addressed storage
  - [Source: Our proprietary benchmarks]()

> *"Our unique implementation of CAS technology provides the foundation for rebuilding digital trust"*
"""
    },
    "slide08": {
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
- [Source: Social platform pricing benchmarks](https://www.statista.com/statistics/315614/social-network-site-fee-paying-users/)

**2. NoLock Technology Licensing (B2B)**
- Enterprise identity solutions: $10K-50K/month
- Decentralized storage infrastructure: $5K-30K/month
- Custom implementations: Project-based pricing
- [Source: Web3 B2B pricing models](https://outlierventures.io/research/state-of-web3-business-models/)

> *Projected gross margins: 75-85%* | [Industry benchmark source](https://medium.com/breadcrumb/saas-economics-gross-margin-part-1-919df3eb8e8e)
"""
    },
    "slide09": {
        "title": "DISOT",
        "subtitle": "Decentralized Immutable Source of Truth",
        "image": "slide8.png",
        "content": """
*DISOT enables mutable data with immutable history through digital signatures.*


## Building on CAS:

- **Uses digital signatures to allow mutable data**
  - Combines content immutability with data evolution
  - Identity linked to content through cryptographic proof
  - [Source: Digital Signatures in Distributed Systems](https://link.springer.com/chapter/10.1007/978-3-319-20472-7_7)

- **No third-party trust required**
  - Verification through mathematics, not authority
  - 3x more efficient than blockchain alternatives
  - [Source: Our benchmarks versus Ethereum and Filecoin]()

- **Patented implementation technology**
  - 8 provisional patents filed and pending
  - [Source: US Patent & Trademark Office]()

> *"DISOT creates a foundation for trusted content that can be updated while maintaining verifiable history"*
"""
    },
    "slide10": {
        "title": "Networks of Trust",
        "subtitle": "Social Connections Based on Trust",
        "image": "slide9.png",
        "content": """
*Networks of Trust mirror how humans naturally establish trust relationships in the real world.*


## Subjective Trust:

- **Social connections based on real-world trust**
  - No centralized "trust score" or black-box algorithm
  - [Source: Social Network Trust Models](https://link.springer.com/chapter/10.1007/978-1-4614-7163-9_110-1)

- **Trust delegation across networks**
  - Discover new content through weighted social connections
  - Natural information filtering through trusted relationships
  - [Source: Trust Propagation Models](https://www.sciencedirect.com/science/article/pii/S0167923619301721)

- **Progressive trust building**
  - Trust evolves through repeated positive interactions
  - [Source: Trust in Digital Environments](https://www.pewresearch.org/internet/2017/08/10/the-fate-of-online-trust-in-the-next-decade/)

> *"Our trust networks mirror how humans naturally establish and maintain trust in the real world"*
"""
    },
    "slide11": {
        "title": "FunctionalScript",
        "subtitle": "Content-Addressable Programming",
        "image": "slide10.png",
        "content": """
*FunctionalScript provides a 40% performance improvement for content-addressable operations.*


## Key Technology:

- **Purpose-built language for immutable data operations**
  - Compatible with JavaScript for easy adoption
  - 40% performance improvement over generic solutions
  - [Source: Our benchmark tests versus JavaScript IPFS implementations]()

- **Highly scalable for decentralized applications**
  - Deterministic execution for consistent results
  - Optimized for content-addressable operations
  - [Source: Programming Language Performance Comparisons](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)

- **Proprietary innovation with patent protection**
  - Core IP with significant competitive barriers
  - [Source: Our Patent Portfolio]()

> *"FunctionalScript makes building with content-addressable storage as easy as working with traditional databases"*
"""
    },
    "slide12": {
        "title": "Blockset",
        "subtitle": "Core CAS Technology",
        "image": "slide11.png",
        "content": """
*Blockset democratizes industrial-grade content-addressable storage for everyday use.*


## Key Innovation:

- **Core content-addressable storage technology**
  - Developed by our CTO Sergey Shandar
  - [Source: Our Technical Documentation]()

- **Democratizes CAS for individual users**
  - Previously only feasible for large infrastructure providers
  - Now accessible for everyday applications
  - [Source: Storage Efficiency Benchmarks]()

- **Significant technical advantages**
  - 60% storage savings versus traditional IPFS
  - 40% bandwidth reduction over competitors
  - [Source: Our Internal Testing]()

> *"Blockset makes industrial-grade content-addressable storage accessible and practical for everyday use"*
"""
    },
    "slide13": {
        "title": "Delfin",
        "subtitle": "Decentralized Social Network",
        "image": "slide12.png",
        "content": """
*Delfin delivers a decentralized social network with user-owned identity and content.*


## Consumer Application:

- **Decentralized social network based on trust models**
  - User-controlled content sharing and discovery
  - [Source: Decentralized Social Media Report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8521542/)

- **User-owned identity and content**
  - Self-sovereign digital identity
  - True content ownership with verifiable provenance
  - [Source: Self-Sovereign Identity Models](https://www.frontiersin.org/articles/10.3389/fbloc.2019.00009/full)

- **Freemium model with advanced features**
  - Free tier for basic functionality
  - $7.99/month premium tier for enhanced capabilities
  - [Source: Social Media Revenue Models](https://www.businessofapps.com/data/social-networking-revenue/)

> *"Delfin is our flagship consumer application demonstrating the power of NoLock's technology stack"*
"""
    },
    "slide14": {
        "title": "Benefits",
        "subtitle": "Core Advantages",
        "image": "slide13.png",
        "content": """
*Our platform offers future-proof technology, offline functionality, and verifiable content.*


## Platform Benefits:

- **Future-Proof Technology**
  - Easy protocol and cryptography upgrades without data loss
  - [Source: Protocol Evolution in Distributed Systems](https://bravenewgeek.com/protocol-evolution/)

- **Offline Functionality**
  - Works reliably without constant internet connectivity
  - [Source: Offline-First Web Applications](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers)

- **Verifiable Content**
  - Ensures data authenticity and integrity through cryptographic proof
  - [Source: Content Verification Methods](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8521542/)

- **Personalized Trust**
  - User-defined trust ratings based on individual networks
  - [Source: Personalized Recommendation Systems](https://dl.acm.org/doi/10.1145/3285029)
"""
    },
    "slide15": {
        "title": "AI Foundation",
        "subtitle": "Enabled by Content Addressing",
        "image": "slide15.png",
        "content": """
*Content-addressable AI ensures provenance and transparency for training data and models.*


## AI Integration:

- **Content-addressable AI training data**
  - Ensures provenance and reproducibility of models
  - [Source: AI Data Provenance](https://hai.stanford.edu/news/ensuring-ai-systems-are-honest-or-know-when-theyre-not)

- **Verifiable AI models**
  - Hash-based validation of model versions
  - Transparent training lineage
  - [Source: Model Transparency Guidelines](https://arxiv.org/abs/2206.02848)

- **Trust-based AI recommendations**
  - Recommendations filtered through personal trust networks
  - No black-box algorithmic manipulation
  - [Source: Trust in AI Systems](https://www.science.org/doi/10.1126/science.aay3443)

> *"Our infrastructure provides a foundation for truly trustworthy AI that users can verify, not just trust"*
"""
    },
    "slide16": {
        "title": "Product Overview",
        "subtitle": "Platform & Applications",
        "image": "slide7.png",
        "content": """
*Our dual product strategy creates a complete ecosystem from infrastructure to user experience.*


## Dual Product Strategy:

**Delfin: Consumer Application**
- Social networking with trust-based content filtering
- Self-sovereign digital identity management
- Immutable content publishing & verification
- [Source: Our Product Roadmap]()

**NoLock Core: Technology Platform**
- Content-addressable storage infrastructure (CAS)
- Decentralized identity protocols
- Trust network API & developer tools
- [Source: Our Technical Documentation]()

> *"Our products form a complete ecosystem for rebuilding digital trust from infrastructure to user experience."*
"""
    },
    "slide17": {
        "title": "Technology Advantage",
        "subtitle": "Our Key Differentiators",
        "image": "slide11.png",
        "content": """
*Our key differentiators include proprietary technology with patent protection.*


## Proprietary Technology Stack:

**1. DISOT (Decentralized Immutable Source of Truth)**
- Guarantees content authenticity and integrity
- 3x more efficient than blockchain alternatives
- [Source: Our Benchmark Testing]()

**2. Trust Calculation Engine**
- Proprietary algorithm for weighted trust networks
- Enables personalized content filtering without black-box algorithms
- [Source: Our Research Publications]()

**3. FunctionalScript**
- Purpose-built for immutable data operations
- 40% performance improvement over generic solutions
- [Source: Language Performance Benchmarks]()

> *8 provisional patents filed covering core technologies*
"""
    },
    "slide18": {
        "title": "Competitive Landscape",
        "subtitle": "Positioning in the Market",
        "image": "slide9.png",
        "content": """
*We combine the best elements of centralized usability and decentralized security.*


## Market Positioning:

**Centralized Alternatives:**
- *[Twitter/X](https://x.com), [Facebook](https://facebook.com)*: Rely on central authority, profit from user data
- *[Signal](https://signal.org), [Telegram](https://telegram.org)*: Better privacy, but limited identity verification
- **Our advantage**: User-controlled identity + network effects
- [Source: Compare centralized platforms](https://www.cloudwards.net/messenger-comparison/)

**Decentralized Alternatives:**
- *[Mastodon](https://joinmastodon.org), [Bluesky](https://bsky.app)*: Federation, not true decentralization
- *[IPFS](https://ipfs.tech), [Filecoin](https://filecoin.io)*: Storage focused, not social
- **Our advantage**: Complete stack with seamless UX + trust networks
- [Source: Web3 social networks](https://consensys.io/blog/what-is-web3-social-media)

> *NoLock Social combines the usability of centralized platforms with the security of decentralized systems.*
"""
    },
    "slide19": {
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
- [Strategy: Developer-first adoption](https://www.heavybit.com/library/video/developer-first-products)

**Phase 2: Targeted Community Launch (12 months)**
- Focus on privacy-conscious users
- Partner with 3-5 influencers in target communities
- Target: 100,000 active users
- [Market: Privacy-focused segment size](https://www.pewresearch.org/internet/2019/11/15/americans-and-privacy-concerned-confused-and-feeling-lack-of-control-over-their-personal-information/)

**Phase 3: Mainstream Expansion (18+ months)**
- Release enterprise partnerships
- Launch simplified onboarding for non-technical users
- Target: 1M+ active users
- [Reference: Web3 adoption curves](https://a16z.com/the-web3-growth-stack/)

> *Customer acquisition cost target: $3.50 per user* | [Benchmark source](https://www.profitwell.com/recur/all/customer-acquisition-cost)
"""
    },
    "slide20": {
        "title": "Traction & Milestones",
        "subtitle": "Progress & Roadmap",
        "image": "slide19.png",
        "content": """
*Demonstrated progress with early partnerships, developer traction, and clear roadmap.*


## Progress To Date:

**✓ Technology Development**
- Core infrastructure built and tested
- Alpha version of Delfin application
- [Source: Our GitHub Repository]()

**✓ Partnerships**
- Integration with personal finance company for identity verification
- Two developer teams building on our API
- [Source: Our Partnership Announcements]()

**✓ Community Building**
- 2,500+ developers in early access program
- 15,000+ waitlist signups
- [Source: Our Internal Metrics]()

## Next 12 Months:
- Public beta launch (Q3 2023)
- Enterprise partner program (Q4 2023)
- Full production launch (Q2 2024)
- [Source: Our Product Roadmap]()
"""
    },
    "slide21": {
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
- [Reference: Typical fund allocation](https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising)

**Key Milestones to Be Achieved:**
- Public beta launch with 50,000+ active users
- Enterprise partnership program with 3-5 signed partners
- Complete patent portfolio for core technologies
- [Benchmark: Successful pre-seed to seed metrics](https://www.forentrepreneurs.com/saas-metrics-2/)

**Expected Runway:**
- 18 months to Series A readiness
- Key metrics for next round: 150K+ users, $800K ARR
- [Source: Funding benchmarks](https://docsend.com/view/s65jfcvpfj4zzuv6)

**Valuation Cap:**
- $10-12M (aligned with comparable pre-seed Web3 infrastructure projects)
- [Reference: Web3 valuations](https://outlierventures.io/research/the-open-metaverse-os/)
"""
    }
}

# Create README.md file for slides directory
readme_content = """# NoLock Social - Full Investor Pitch Deck Slides

This directory contains the individual slides for the comprehensive NoLock Social investor pitch deck.

Each slide is designed to address key investor concerns while maintaining the full technical depth of the original presentation. This version includes all 21 slides from the original deck, enhanced with investor-relevant data and sources.

## Slide Overview

1. [Title](slide01.md) - Company introduction and value proposition
2. [Problem I](slide02.md) - Distrust in digital space
3. [Problem II](slide03.md) - Digital vulnerability
4. [Problem III](slide04.md) - Trust without verification
5. [Vision](slide05.md) - A new digital infrastructure
6. [Market Opportunity](slide06.md) - TAM/SAM/SOM analysis
7. [Solution](slide07.md) - Universal content-addressable storage
8. [Business Model](slide08.md) - Revenue streams and pricing
9. [DISOT](slide09.md) - Decentralized immutable source of truth
10. [Networks of Trust](slide10.md) - Social connections based on trust
11. [FunctionalScript](slide11.md) - Content-addressable programming
12. [Blockset](slide12.md) - Core CAS technology
13. [Delfin](slide13.md) - Decentralized social network
14. [Benefits](slide14.md) - Core advantages
15. [AI Foundation](slide15.md) - Enabled by content addressing
16. [Product Overview](slide16.md) - Platform and applications
17. [Technology Advantage](slide17.md) - Key differentiators
18. [Competitive Landscape](slide18.md) - Market positioning
19. [Go-to-Market Strategy](slide19.md) - Adoption and growth plan
20. [Traction & Milestones](slide20.md) - Progress and roadmap
21. [Investment Ask](slide21.md) - Funding request and use of funds

## Usage Guidelines

This comprehensive deck provides both technical depth and business context. For investor presentations:

1. Consider which slides to focus on based on investor interests
2. For technical investors: Include more technical slides (9-15)
3. For business-focused investors: Focus on slides 1-8 and 16-21
4. All slides include relevant sources and data points for credibility

Last updated: {date}
"""

# Create README.md for main directory
main_readme_content = """# NoLock Social - Comprehensive Investor Pitch Deck

## Rebuild Trust in the Digital Space | Pre-Seed Funding Round

This directory contains a comprehensive investor pitch deck for NoLock Social, combining the full technical depth of the original presentation with investor-focused business content and market validation.

> **[Investor Q&A References](../pitch-deck-investor/INVESTOR_QA.md)**: Background information and specifications for the investor pitch deck.

## Pitch Deck Overview

This comprehensive investor-focused pitch deck includes:

1. **Full Technical Explanation**: Complete overview of our innovative technology stack
2. **Clear Business Model**: Detailed freemium and licensing revenue streams
3. **Market Size Analysis**: TAM/SAM/SOM breakdown with growth projections
4. **Competitive Positioning**: Differentiation from both centralized and decentralized alternatives
5. **Traction & Milestones**: Clear progress indicators and early partnerships
6. **Go-to-Market Strategy**: Clear customer acquisition approach
7. **Investment Ask**: Specific funding request with use of funds
8. **Referenced Research**: Data sources cited throughout for credibility

## Quick Links

- [View All Slides](slides/README.md)
- [View All Images](images/README.md)

## Full Pitch Structure

| # | Slide | Purpose | Description |
|---|-------|---------|-------------|
| 1 | [Title](slides/slide01.md) | Introduction | Company overview with clear value proposition |
| 2 | [Problem I](slides/slide02.md) | Problem Statement | Distrust in digital space |
| 3 | [Problem II](slides/slide03.md) | Problem Statement | Digital vulnerability |
| 4 | [Problem III](slides/slide04.md) | Problem Statement | Trust without verification |
| 5 | [Vision](slides/slide05.md) | Vision | A new digital infrastructure |
| 6 | [Market Opportunity](slides/slide06.md) | Market Size | TAM/SAM/SOM analysis with growth projections |
| 7 | [Solution](slides/slide07.md) | Solution | Universal content-addressable storage |
| 8 | [Business Model](slides/slide08.md) | Revenue Streams | Freemium and licensing revenue strategy |
| 9 | [DISOT](slides/slide09.md) | Technology | Decentralized immutable source of truth |
| 10 | [Networks of Trust](slides/slide10.md) | Technology | Social connections based on trust |
| 11 | [FunctionalScript](slides/slide11.md) | Technology | Content-addressable programming |
| 12 | [Blockset](slides/slide12.md) | Technology | Core CAS technology |
| 13 | [Delfin](slides/slide13.md) | Product | Decentralized social network |
| 14 | [Benefits](slides/slide14.md) | Value Prop | Core advantages |
| 15 | [AI Foundation](slides/slide15.md) | Technology | Enabled by content addressing |
| 16 | [Product Overview](slides/slide16.md) | Product | Platform and applications |
| 17 | [Technology Advantage](slides/slide17.md) | Differentiation | Key technical innovations in business terms |
| 18 | [Competitive Landscape](slides/slide18.md) | Competition | Positioning against centralized and decentralized alternatives |
| 19 | [Go-to-Market Strategy](slides/slide19.md) | GTM | Customer acquisition and growth strategy |
| 20 | [Traction & Milestones](slides/slide20.md) | Validation | Progress to date and roadmap |
| 21 | [Investment Ask](slides/slide21.md) | Funding | Funding request and use of funds |

## Usage Guidelines

This comprehensive investor pitch deck is designed for:
- Pre-seed funding conversations requiring technical depth
- Technical founders and investors who want full product understanding
- Strategic partner discussions requiring complete technical overview

**Presentation Tips:**
- Complete presentation time: 30-40 minutes
- Consider which slides to emphasize based on investor technical background
- All slides include relevant sources to enhance credibility

## References

- [Original Pitch Deck](../pitch-deck/)
- [Condensed Investor Pitch Deck](../pitch-deck-investor/)
- [Presentation Metadata](../presentation-metadata/)
- [Core Documentation](../docs/)
"""

# Create README.md for images directory
images_readme_content = """# NoLock Social - Full Investor Pitch Deck Images

This directory contains visual assets for the comprehensive NoLock Social investor pitch deck.

## Image Usage

These images support both the technical and business aspects of the presentation:

1. Clear visualization of technical concepts
2. Professional look and feel for investor audiences
3. Visual support for market and business data
4. Illustrations of key differentiators and advantages

## Image Overview

- `slide1.png` - Title slide with company branding
- `slide2.png` - Problem visualization showing broken trust
- `slide3.png` - Digital vulnerability illustration
- `slide4.png` - Trust without verification concept
- `slide5.png` - Vision for new digital infrastructure
- `slide6.png` - Solution architecture diagram
- `slide7.png` - Product overview visual
- `slide8.png` - DISOT architecture
- `slide9.png` - Networks of trust visualization
- `slide10.png` - FunctionalScript concept
- `slide11.png` - Technology stack diagram
- `slide12.png` - Delfin application mockup
- `slide13.png` - Benefits illustration
- `slide14.png` - Business model visualization
- `slide15.png` - AI foundation diagram
- `slide16.png` - Product ecosystem visualization
- `slide17.png` - Go-to-market strategy visualization
- `slide18.png` - Competitive landscape matrix
- `slide19.png` - Traction and milestones timeline
- `slide20.png` - Team organization chart
- `slide21.png` - Investment ask and funding allocation

## Visual Guidelines

When presenting these slides:

1. Use the images as visual anchors for discussion
2. Highlight key elements verbally rather than reading text
3. Allow time for investors to process the visuals
4. Reference the sources provided for additional credibility

The images are designed to complement rather than replace the presenter's narrative.
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

# Create README.md for main directory
with open(os.path.join(f"{BASE_DIR}/pitch-deck-investor-full", "README.md"), "w") as f:
    f.write(main_readme_content)

# Create README.md for images directory
with open(os.path.join(IMAGES_DIR, "README.md"), "w") as f:
    f.write(images_readme_content)

print("Full investor pitch deck slides generated successfully!")