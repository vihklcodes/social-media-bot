# Social Media Bot

AI-powered Instagram campaign engine that generates occasion-based content for DoorDash restaurant merchants. A 4-agent pipeline analyzes each merchant's brand, identifies timely occasions, writes image prompts + captions, and generates ready-to-post promotional flyers via Google Gemini.

## How It Works

The system runs a sequential 4-agent workflow for each merchant:

```
Agent 1 (Brand Intel)  →  Agent 2 (Occasions)  →  Agent 3 (Content)  →  Agent 4 (Image Gen)
```

| Agent | What It Does | Output |
|-------|-------------|--------|
| **Agent 1** | Scrapes the merchant's website and Instagram via Playwright. Extracts brand colors (hex-verified), typography, photography style, caption voice, and cultural identity. | `agent1_brand.md` |
| **Agent 2** | Identifies 3 relevant occasions per week for the next 30 days — holidays, cultural moments, menu highlights, Mx-requested promos. | `agent2_occasions.md` |
| **Agent 3** | Writes detailed Nano Banana Pro image generation prompts (1030x1350px flyer specs) and Instagram captions for each occasion. | `agent3_content.md` |
| **Agent 4** | Feeds prompts into Google Gemini to generate the final poster images. Can run via Playwright automation or the `generate_image.py` script. | `final_images/*.png` |

Each agent reads the previous agent's output — no external tools needed for inter-agent communication.

## Merchant Roster

13 confirmed DoorDash merchants across 3 follower tiers:

| Tier | Merchants |
|------|-----------|
| **< 100 followers** | Sumo Ramen, Jalisco Restaurant, Thai Cortez |
| **100 – 5K** | Falafel Corner, Los Ocampos, Tee Jayes, Halal Express, Burger Bun, Tio Nacho |
| **5K+** | Kaisen Don, La Cocina, 323 Hibachi Grill, Chelo |

The source of truth for merchant data (emails, cuisine, Instagram URLs, website URLs, follower counts, order volume) lives in `AI comeback - Social Media .csv`.

## Setup

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (runs the agent workflow)
- [Node.js](https://nodejs.org/) (for Playwright MCP server)
- Python 3.10+ (for the standalone image generation script)

### Install

```bash
# Clone the repo
git clone https://github.com/vihklcodes/social-media-bot.git
cd social-media-bot

# Set up Python environment (for generate_image.py)
python3 -m venv .venv
source .venv/bin/activate
pip install google-genai python-dotenv

# Create .env with your Gemini API key
echo "GEMINI_API_KEY=your-api-key-here" > .env
```

Get a Gemini API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

The Playwright MCP server is configured in `.mcp.json` and launches automatically when Claude Code runs.

## Running the Agents

Open Claude Code in the project directory and run agents per merchant:

```
# Run all 4 agents for a merchant
> run the agents for La Cocina

# Run a specific agent
> run agent 1 for Burger Bun
> run agent 3 for Falafel Corner
```

Agents read their instructions from `agents/agent{N}_instructions.md` and write outputs to `merchants/{Merchant Name}/`.

### Standalone Image Generation

You can also generate images directly with the Python script (bypasses Agent 4's Playwright automation):

```bash
# Generate from a direct prompt
python generate_image.py "Your prompt here" -o output.png

# Generate from a merchant's agent3_content.md
python generate_image.py --merchant "La Cocina" --occasion 1

# Generate all occasions for a merchant
python generate_image.py --merchant "Burger Bun"
```

## Project Structure

```
├── AI comeback - Social Media .csv   # Merchant roster (source of truth)
├── CLAUDE.md                         # Agent instructions & project rules
├── generate_image.py                 # Standalone Gemini image generation script
├── .mcp.json                         # Playwright MCP server config
├── .env                              # Gemini API key (not committed)
├── agents/
│   ├── agent1_instructions.md        # Brand intelligence & feed deconstruction
│   ├── agent2_instructions.md        # Occasion strategy
│   ├── agent3_instructions.md        # Nano Banana Pro prompt & caption creation
│   └── agent4_instructions.md        # Playwright → Gemini image generation
└── merchants/
    └── {Merchant Name}/
        ├── agent1_brand.md           # Brand analysis output
        ├── agent2_occasions.md       # Occasion calendar output
        ├── agent3_content.md         # Image prompts + captions output
        ├── screenshots/              # Playwright screenshots (brand research)
        └── final_images/             # Generated poster images
```

## Content Rules

- 3 posts per week per merchant
- Every post is occasion-based (holidays, cultural moments, menu highlights)
- Bilingual where appropriate (matches merchant's audience)
- Each post includes: scroll-stopping hook, body copy, CTA, 15-20 hashtags
- Images are 1030x1350px promotional flyers designed for Instagram feed

## Success Metrics

- Engagement rate (likes, comments, shares, saves)
- Follower growth during campaign
- Order volume correlation (DoorDash MP/SF weekly averages vs. baseline)
- Brand consistency (does AI content match the merchant's identity?)
