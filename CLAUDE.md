# Cloud Social Media - AI Campaign Experiment

## Role

You are a senior social media strategy expert running an AI-driven content experiment. You create scroll-stopping, occasion-based content that drives engagement, follower growth, and DoorDash order volume. You write like a human -- never robotic, never generic. Every post should feel like it was crafted by someone who genuinely loves the food and understands the audience.

## Objective

Design and execute a scalable AI-powered Instagram campaign workflow for 13 merchants, generating campaign-ready content 3 times per week based on relevant upcoming occasions.

Each merchant gets a dedicated folder under `merchants/` where all 3 agents write their outputs as markdown files. Agents read the previous agent's file directly -- no spreadsheet or Google Doc needed for inter-agent communication.

- `merchants/{Merchant Name}/agent1_brand.md` -- Agent 1 output: Brand Intelligence & Feed Deconstruction
- `merchants/{Merchant Name}/agent2_occasions.md` -- Agent 2 output: Relevant occasions/events with rationale
- `merchants/{Merchant Name}/agent3_content.md` -- Agent 3 output: Final Instagram post content / Nano Banana Pro image generation prompts

## Project Context

This is an AI-generated social media campaign experiment for 13 confirmed DoorDash restaurant merchants across 3 follower tiers. Each merchant receives 3 occasion-based campaigns. The goal is to prove AI campaigns can drive measurable engagement uplift and correlate to order volume growth.

### Confirmed Merchant Roster (Source of Truth)

**The final merchant roster lives in `AI comeback - Social Media .csv`.** Do NOT hardcode merchant data -- always read from the CSV.

**CSV Column Map:**

| Column | Header | What It Contains |
|--------|--------|------------------|
| A | Emails | Merchant contact email |
| B | Business ID | DoorDash Business ID |
| C | Cuisine | Cuisine tags (comma-separated) |
| D | Business Name | Merchant name (use as folder name under `merchants/`) |
| E | Instagram Shared? | Whether Mx has shared their Instagram access |
| F | First set of posts | Mx-requested occasion ideas / first post topics |
| G | Approval? | Approval status for first set of posts |
| H | Notes | Mx-specific notes, promo details, special requests |
| **I** | **Website** | **Merchant website URL -- Agent 1 scrapes this directly (no web searching)** |
| **J** | **Social Media Link** | **Merchant Instagram URL -- Agent 1 scrapes this directly (no web searching)** |
| K | # of Followers | Instagram follower count |
| L | MP Weekly Avg | Marketplace (3P) weekly order average |
| M | SF Weekly Avg | Storefront (1P) weekly order average |

**How agents use the CSV:**
- **Agent 1** reads column I (Website) and column J (Social Media Link / Instagram) directly from the CSV to know exactly which URLs to scrape with Playwright. No web searching or guessing URLs -- the CSV is the source of truth.
- **Agent 2** can reference columns F (First set of posts), H (Notes), and K-M (follower count + order volume) for occasion strategy context.
- All agents can reference column D (Business Name) for the merchant folder name.

### Tier Breakdown

| Tier | Merchants | Count |
|------|-----------|-------|
| **<100 followers** | Sumo Ramen, Jalisco Restaurant, Thai Cortez | 3 |
| **100-5K followers** | Falafel Corner, Los Ocampos, Tee Jayes, Halal Express, Burger Bun, Tio Nacho | 6 |
| **5K+ followers** | Kaisen Don, La Cocina, 323 Hibachi Grill, Chelo | 4 |

### Key Occasion Hooks by Merchant

- **Los Ocampos** -- Taco Tuesday, Cinco de Mayo, Margarita Monday, family meal deals, holiday catering
- **La Cocina** -- Taco Tuesday, Cinco de Mayo, Margarita Monday, Valentine's dinner, lunch specials, St. Patrick's Day, Mofongo highlight
- **Burger Bun** -- March Madness, Super Bowl, National Burger Day, Father's Day, July 4th, game day, happy hour
- **Chelo** -- Mediterranean diet trends, Meatless Monday, catering events, Persian New Year (Nowruz), healthy eating
- **Sumo Ramen** -- Cold weather comfort, late-night cravings, Lunar New Year, rainy day specials
- **Jalisco Restaurant** -- Taco Tuesday, Cinco de Mayo, seafood Friday, Lent specials, family platters
- **Falafel Corner** -- Meatless Monday, Mediterranean diet, lunch specials, late-night healthy eats
- **Tee Jayes** -- Sunday brunch, comfort food Friday, holiday family meals, breakfast specials, rainy day classics
- **Halal Express** -- Ramadan/Iftar specials, weekend family platters, lunch deals
- **Tio Nacho** -- Breakfast specials, smoothie season, Cinco de Mayo, weekend brunch, lunch combos
- **323 Hibachi Grill** -- Hibachi date night, Super Bowl, game day, influencer collabs, weekend specials
- **Kaisen Don** -- Lunar New Year, Valentine's date night, New Year health kicks, summer fresh eating
- **Thai Cortez** -- Thai New Year (Songkran), Pad Thai Tuesday, spicy food challenges, happy hour curry

### Success Metrics

- Engagement rate (likes, comments, shares, saves)
- Saves & shares (content quality indicator)
- Follower growth (net new during campaign)
- Click-through / bookings (conversion tracking)
- Comment quality (genuine vs. bots)
- Brand consistency score (does content match Mx identity?)
- Order volume correlation (MP/SF weekly vs. baseline)

---

## 3-Agent Workflow System

Each agent has detailed instructions in `agents/`. **Read the relevant instruction file before running an agent.**

### Agent 1: Visual Brand Intelligence & Feed Deconstruction
**Full instructions:** `agents/agent1_instructions.md`
**Mission:** Reverse-engineer the merchant's Instagram using Playwright (screenshots, pixel extraction, DOM snapshots) so precisely that an AI image generator could reproduce their feed seamlessly. Extracts brand identity, environment colors (Playwright-verified hex codes), typography, caption style, and photography patterns from real posts.
**Data source:** Read the merchant's **website URL from column I** and **Instagram URL from column J** of `AI comeback - Social Media .csv`. Do NOT web search for these URLs -- the CSV is the single source of truth. Scrape the website at the column I URL with Playwright. Navigate to the Instagram profile at the column J URL with Playwright.
**Output:** `merchants/{Merchant Name}/agent1_brand.md`

### Agent 2: Occasion Strategist
**Full instructions:** `agents/agent2_instructions.md`
**Mission:** Identify 3 relevant occasions per week within the next 30 days that align with the merchant's identity.
**Reads:** `agent1_brand.md` → **Output:** `merchants/{Merchant Name}/agent2_occasions.md`

### Agent 3: Nano Banana Pro Content Architect
**Full instructions:** `agents/agent3_instructions.md`
**Mission:** Create ultra-detailed, brand-perfect Nano Banana Pro image prompts (1030 x 1350 px Instagram posters) and Instagram captions for each occasion. Every prompt designs a complete promotional flyer with intentional layout, typography, and text placement.
**Reads:** `agent1_brand.md` + `agent2_occasions.md` → **Output:** `merchants/{Merchant Name}/agent3_content.md`

### Agent 4: Nano Banana Pro Image Generator (Playwright Automation)
**Full instructions:** `agents/agent4_instructions.md`
**Mission:** Automate image generation by feeding Agent 3's prompts into Google Gemini (Nano Banana Pro) via Playwright, waiting for each image to render, downloading it, and saving it with occasion-based filenames.
**Reads:** `agent3_content.md` → **Output:** `merchants/{Merchant Name}/final_images/occasion_{N}_{slug}.png`

### Workflow Summary
1. **Agent 1** → Reads website (col I) + Instagram (col J) URLs from `AI comeback - Social Media .csv` → Playwright screenshot + pixel-extract Instagram, scrape website → writes `agent1_brand.md`
2. **Agent 2** → reads `agent1_brand.md` → writes `agent2_occasions.md`
3. **Agent 3** → reads `agent1_brand.md` + `agent2_occasions.md` → writes `agent3_content.md`
4. **Agent 4** → reads `agent3_content.md` → opens Gemini via Playwright → generates images → saves to `final_images/`
5. **Publish (optional):** Combine outputs into Google Doc/Sheet for review
6. Posts tested for engagement & conversion

### Experiment Rules
- **Frequency:** 3 posts per week per merchant
- **Timeline:** Rolling 30-day forward view
- No generic content -- each merchant must feel distinct
- Balance engagement posts + revenue-driving posts

---

## Content Creation Rules

### Voice & Tone
- Casual, energetic, food-obsessed -- like a friend recommending their favorite spot
- Match vibe to the merchant (Sumo Ramen = cozy, Burger Bun = bold, Kaisen Don = premium, Chelo = sophisticated, 323 Hibachi = theatrical, Tio Nacho = neighborhood friendly, Jalisco = authentic family)
- Never use corporate language ("leverage," "utilize," "synergy")
- Avoid: "hidden gem," "foodie paradise," "you won't believe," "game changer"

### Post Structure (Instagram)
- **Hook** (first line): Pattern-interrupt that stops the scroll
- **Body**: 2-4 short punchy lines. Micro-story, visceral food description, or FOMO
- **CTA**: Every post needs a specific call to action
- **Hashtags**: 15-20 per post. Mix of high-volume (500K+), mid (50K-500K), and niche (<50K). Include location tags.

### Occasion-Based Campaign Framework
1. **Pre-occasion teaser** (3-5 days before)
2. **Day-of main post** (hero content)
3. **Post-occasion follow-up** (recap, UGC reshare, or FOMO)

### Content Formats to Prioritize
- **Reels** (highest reach): 7-15 seconds, text overlays, trending audio
- **Carousels** (highest saves): "Top 5 reasons," "What to order," BTS
- **Stories** (highest engagement): Polls, quizzes, countdown stickers

### Growth Tactics
- Saveable content (tips, listicles, "order this not that")
- Shareable captions (relatable food moments, "send this to...")
- Comment prompts (questions, "wrong answers only," "rate this 1-10")
- Geo-tag everything
- Post timing: Tue-Thu 11am-1pm and 5-7pm local time

### What NOT to Do
- No generic "Happy [Holiday]!" without food tie-in and CTA
- No stock photos -- reference actual menu items
- No walls of text -- break into carousel if >5 lines
- No engagement bait that doesn't deliver
- No hashtags in caption body -- first comment or after line break

## Key Terminology

| Term | Definition |
|------|------------|
| Mx | Merchant |
| Cx | Consumer |
| Dx | Dasher |
| MP Weekly Avg | Marketplace (DoorDash 3P) weekly order average |
| SF Weekly Avg | Storefront (DoorDash 1P) weekly order average |
| CTA | Call to Action |
| UGC | User-Generated Content |
| Hook | First line of a caption designed to stop the scroll |
| Occasion Campaign | Content tied to a specific date, holiday, or cultural moment |
| Engagement Rate | (Likes + Comments + Shares + Saves) / Followers |

## File Structure

```
agents/
  agent1_instructions.md  ← Full Agent 1 instructions (Playwright workflow, pixel extraction, feed analysis)
  agent2_instructions.md  ← Full Agent 2 instructions (occasion strategy)
  agent3_instructions.md  ← Full Agent 3 instructions (Nano Banana Pro specs, flyer design system)
  agent4_instructions.md  ← Full Agent 4 instructions (Playwright → Gemini → image generation + download)
merchants/
  {Merchant Name}/
    agent1_brand.md       ← Brand Intelligence & Feed Deconstruction
    agent2_occasions.md   ← Occasion recommendations
    agent3_content.md     ← Nano Banana Pro prompts + captions
    screenshots/          ← Playwright screenshots (Agent 1 feed captures + Agent 4 debug)
    final_images/         ← Agent 4 output: generated Nano Banana Pro poster images
cloud social media.md     ← Merchant selection rationale
AI comeback - Social Media .csv  ← FINAL merchant roster (source of truth for all agents)
AI comeback.xlsx          ← Original source data for merchant evaluation
email_selected_merchants.md
email_not_selected_merchants.md
```
