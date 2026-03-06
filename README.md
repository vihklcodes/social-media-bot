# AI Social Media Campaign Bot

**DoorDash Pro/Enterprise Strategy & Ops** | Vickie Hua | Feb-Mar 2026

An AI-driven social media content pipeline that generates occasion-based Instagram posts for DoorDash restaurant merchants. Built with Claude Code, Playwright, Snowflake, and Gemini — no manual design work required.

---

## What This Is

An experiment to prove that AI-generated social media campaigns can drive measurable engagement uplift and correlate to DoorDash order volume growth for 3P marketplace merchants.

- **13 merchants** across 3 follower tiers (micro, small, medium)
- **3 posts per week** per merchant — occasion-based, brand-matched content
- **5-agent pipeline** that takes a merchant from zero context to ready-to-post images + captions
- **Baseline metrics captured** pre-campaign to measure lift

## The 5-Agent Pipeline

Each agent reads the previous agent's output as markdown files. No databases, no APIs between agents — just files.

```
Agent 1: Brand Intelligence          → agent1_brand.md
    ↓
Agent 2: Occasion Strategist         → agent2_occasions.md
    ↓
Agent 3: Content Architect           → agent3_content.md
    ↓
Agent 3.5: Photo Matcher             → agent3_5_photos.md + reference_photos/
    ↓
Agent 4: Image Generator             → final_images/
```

| Agent | What It Does | Key Tools |
|-------|-------------|-----------|
| **1 — Brand Intelligence** | Scrapes merchant's Instagram + website via Playwright. Pixel-extracts hex colors from real posts. Builds a 14-section Brand Replication Blueprint. | Playwright, canvas pixel sampling |
| **2 — Occasion Strategist** | Queries Snowflake for cuisine tags, then maps relevant occasions (holidays, food days, local events) to the next 30 days. | Snowflake `dimension_store` |
| **3 — Content Architect** | Writes 2-3 caption variations + ultra-detailed image generation prompts (1030x1350 Instagram posters) per occasion. Uses brand colors, fonts, and tone from Agent 1. | — |
| **3.5 — Photo Matcher** | Scrapes DoorDash storefront photos as reference images for each occasion's hero food. Stages matched photos locally. **Required before Agent 4.** | Playwright, DoorDash storefront |
| **4 — Image Generator** | Opens Gemini via Playwright, uploads reference photos, pastes prompts, downloads generated images. Fully automated. | Playwright → Gemini Pro |

## Current Status (Mar 2026)

### Pipeline Progress

| Merchant | Agent 1 | Agent 2 | Agent 3 | Agent 3.5 | Agent 4 | Bio Audit | Images |
|----------|:-------:|:-------:|:-------:|:---------:|:-------:|:---------:|-------:|
| **Chelo** | Done | Done | Done | Done | Done | Done | 13 |
| **Falafel Corner** | Done | Done | Done | Done | Done | Done | 15 |
| **Burger Bun** | Done | Done | Done | Done | Done | Done | 14 |
| **Thai Cortez** | Done | Done | Done | Done | Done | Done | 12 |
| **La Cocina** | Done | Done | Done | Done | Done | Done | 11+ |
| **Jalisco** | Done | Done | Done | Done | Done | Done | 13 |
| **Shamrocks Ale House** | Done | Done | Done | Done | Done | Done | 14 |
| **Tio Nacho** | Done | Done | Done | Done | Done | — | 14 |
| **Tee Jayes** | Done | Done | Done | Done | — | Done | — |
| Merchants 10-13 | — | — | — | — | — | — | — |

**9 of 13 merchants** have completed the full agent pipeline. **8 merchants** have final images generated and ready to post.

### Pre-Campaign Baselines

Scraped via Instaloader on Feb 23, 2026:

| Merchant | Followers | Avg Likes | Eng. Rate | MP Weekly Orders | SF Weekly Orders |
|----------|----------:|----------:|----------:|-----------------:|-----------------:|
| Burger Bun | **2,418** | 9.4 | **0.49%** | 283.9 | 4.1 |
| Chelo | **7,409** | 174.8 | **2.44%** | 24.2 | 0.3 |
| Falafel Corner | **134** | 0.7 | **0.50%** | 1,806.0 | 129.1 |
| La Cocina | **8,739** | 88.8 | **1.10%** | 231.0 | 9.1 |
| Tee Jayes | **1,029** | 2.2 | **0.23%** | 951.2 | 70.9 |
| Thai Cortez | **64** | 5.6 | **9.24%** | 41.2 | 40.7 |

**Biggest opportunities:** Tee Jayes (0.23% engagement) and Falafel Corner (1,806 orders/wk but only 134 followers).

## Project Structure

```
social-media/
├── CLAUDE.md                  # Agent instructions + project rules
├── README.md                  # This file
├── midpoint-reachout.md       # Mx communication templates
├── agents/                    # Detailed instructions for each agent
│   ├── agent1_instructions.md
│   ├── agent2_instructions.md
│   ├── agent3_instructions.md
│   ├── agent3_5_instructions.md
│   └── agent4_instructions.md
├── merchants/                 # One folder per merchant
│   └── {Merchant Name}/
│       ├── agent1_brand.md        # Brand Replication Blueprint
│       ├── agent2_occasions.md    # Occasion recommendations
│       ├── agent3_content.md      # Captions + image prompts
│       ├── agent3_5_photos.md     # Photo matching results
│       ├── bio_optimization/      # Instagram bio audit
│       ├── reference_photos/      # Storefront photos (Agent 3.5)
│       └── final_images/          # Generated posters (Agent 4)
├── pre-post-stats/            # Baseline metrics + scraping scripts
├── scripts/                   # Google Sheets automation (Python)
└── workspace/                 # Playwright test workspace
```

## Tracking

All merchant data, pipeline status, and posting calendars live in a single Google Sheet:
- **Social Media tab** — merchant info + agent pipeline status (columns P-T)
- **Calendar tab** — posting schedule with captions, image links, and posted status
- **Implementation Dates tab** — pre-campaign Instagram baselines

## Key Design Decisions

1. **File-to-file agent communication** — agents read/write markdown directly instead of using APIs or databases. Simple, debuggable, and version-controllable.
2. **Pixel-level brand matching** — Agent 1 extracts actual hex codes from merchant Instagram posts via Playwright canvas sampling, so generated images match the merchant's real aesthetic.
3. **Photo Matcher (Agent 3.5) is mandatory** — scraping real DoorDash storefront photos as references dramatically improves Gemini's output quality vs. text-only prompts.
4. **Every post ties to an occasion** — no generic filler content. Each post maps to a holiday, food day, local event, or cultural moment relevant to the merchant's cuisine.
5. **CTAs drive online ordering** — all campaigns push DoorDash orders, not in-house dining.

## How to Run

Agents are invoked via Claude Code skills (`/brand-intel`, `/occasions`, `/content`, `/generate_images`) or by asking Claude directly. Each agent reads its instruction file from `agents/` before executing.

```
# Example: run the full pipeline for a merchant
/brand-intel Chelo
/occasions Chelo
/content Chelo
# Agent 3.5 runs automatically before Agent 4
/generate_images Chelo
```

Requires:
- Claude Code with Playwright MCP
- Google Workspace MCP (for Sheets read/write)
- Snowflake access (for Agent 2 cuisine tags)
- Gemini Pro access (for Agent 4 image generation)
