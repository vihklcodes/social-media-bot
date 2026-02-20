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

### Confirmed Merchant Roster

| # | Merchant | Cuisine | Instagram | Followers | Tier | MP Wkly | SF Wkly | Notes |
|---|----------|---------|-----------|-----------|------|---------|---------|-------|
| 1 | Los Ocampos | Mexican | @losocamporestaurants | 2,840 | 100-5K | 960.8 | 190.9 | Influencer videos, photos. Multi-location. |
| 2 | La Cocina | Mexican | @lacocina_nj | 8,598 | 5K+ | 231.0 | 9.1 | Posts daily, boosted content, hasn't cracked the code. |
| 3 | Burger Bun | Burgers/American | @burgerbunla | 2,422 | 100-5K | 283.9 | 4.1 | High quality videos, low engagement. |
| 4 | Chelo | Mediterranean/Middle Eastern | @tasteofchelo | 7,391 | 5K+ | 24.2 | 0.3 | Good to work with, wants to share, gets catering. |
| 5 | Sumo Ramen Market City | Japanese/Ramen | @sumoramenmarketcity | 88 | <100 | 157.0 | 1.0 | Only 2 posts, no engagement. Blank canvas. |
| 6 | Jalisco Restaurant | Mexican/Seafood | @jaliscoscatering | 66 | <100 | 100.7 | 0.8 | Photos and vids, low engagement. |
| 7 | Falafel Corner | Mediterranean | @falafelcornerdowntown | 445 | 100-5K | 1,806.0 | 129.1 | Highest MP weekly in dataset. |
| 8 | Tee Jayes Country Place | Comfort Food/Deli | @teejayescountryplace | 1,035 | 100-5K | 951.2 | 70.9 | Updates, promos, some menu items. |
| 9 | Halal Express | Halal/Fast Food | @halalexpressnj | 1,281 | 100-5K | 337.0 | 13.3 | Great food-focused videos, zero engagement. |
| 10 | Tio Nacho | Mexican/Breakfast | @tionacho_nyc | 207 | 100-5K | 105.5 | 5.6 | Engaged merchant, interested in pilot. |
| 11 | 323 Hibachi Grill | Japanese/Hibachi | @323hibachigrill | 15,800 | 5K+ | 286.5 | 13.6 | Already Med/High engagement. Influencer posts. |
| 12 | Kaisen Don | Japanese/Poke | @kaisendon1939 | 15,700 | 5K+ | 272.0 | 153.7 | Influencer marketing. Huge dormant audience. |
| 13 | Thai Cortez | Thai | @thai.cortez | 64 | <100 | 41.2 | 40.7 | Friendly Mx, needs help, posts food vids occasionally. |

---

## 3-Agent Workflow System

Each agent has detailed instructions in `agents/`. **Read the relevant instruction file before running an agent.**

### Agent 1: Visual Brand Intelligence & Feed Deconstruction
**Full instructions:** `agents/agent1_instructions.md`
**Mission:** Reverse-engineer the merchant's Instagram using Playwright (screenshots, pixel extraction, DOM snapshots) so precisely that an AI image generator could reproduce their feed seamlessly. Extracts brand identity, environment colors (Playwright-verified hex codes), typography, caption style, and photography patterns from real posts.
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
1. **Agent 1** → Playwright screenshot + pixel-extract Instagram → writes `agent1_brand.md`
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
AI comeback.xlsx          ← Source data for merchant evaluation
email_selected_merchants.md
email_not_selected_merchants.md
```
