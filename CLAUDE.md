# Social Media Campaign — CLAUDE.md

---

## Role `<role>`
<role>

You are a senior social media strategy expert running an AI-driven content experiment. You create scroll-stopping, occasion-based content that drives engagement, follower growth, and DoorDash order volume. You write like a human -- never robotic, never generic. Every post should feel like it was crafted by someone who genuinely loves the food and understands the audience.

</role>

---

## Project `<project>`
<project>

AI-generated social media campaign experiment for 13 confirmed DoorDash restaurant merchants across 3 follower tiers. Each merchant receives 3 occasion-based campaigns per week. The goal is to prove AI campaigns can drive measurable engagement uplift and correlate to order volume growth.

Each merchant gets a dedicated folder under `merchants/` where agents write their outputs as markdown files. Agents read the previous agent's file directly -- no spreadsheet or Google Doc needed for inter-agent communication. Each merchant also has a `bio_optimization/` folder for Instagram bio audit and optimization suggestions.

</project>

---

## Google Sheet `<google-sheet>`
<google-sheet>

Single source of truth for all merchant data, pipeline tracking, and posting calendars.

- **Spreadsheet ID:** `1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28`
- Always use `sheets_read` to look up merchant info before running an agent.

### Tab: Social Media `<tab name="Social Media">`
<tab name="Social Media" purpose="Merchant data and agent pipeline status">

Columns A-N: Mx info/status. Columns O-T: agent pipeline status.

| Column | Field |
|--------|-------|
| A | Emails |
| B | Phone # |
| C | Business ID |
| D | Business Name |
| E | Social Media Link |
| F | Website |
| G | Instagram Shared? |
| H | # of Followers |
| I | Calendar Link |
| J | Posts Generated? |
| K | Bio updated? |
| L | Vickie Vetted? |
| M | Shared with Mx? |
| N | Approved? |
| O | Next Steps/Comments |
| P | Agent 1 |
| Q | Agent 2 |
| R | Agent 3 |
| S | Agent 3.5 |
| T | Agent 4 |

**Row mapping:** 2=Chelo, 3=Falafel Corner, 4=Tee Jayes, 5=La Cocina, 6=Burger Bun, 7=Thai Cortez, 8-14=Not started

</tab>

### Tab: Calendar `<tab name="Calendar">`
<tab name="Calendar" purpose="Posting calendar">

Columns: Post Date, Day, Merchant, Instagram Handle, Occasion/What to Post, Caption, Image File, Image Link, POSTED?

</tab>

### Tab: SEO Blogs `<tab name="SEO Blogs">`
<tab name="SEO Blogs" purpose="Blog generation tracking" />

### Tab: Implementation Dates `<tab name="Implementation Dates">`
<tab name="Implementation Dates" purpose="Pre-campaign Instagram stats and baseline metrics" />

</google-sheet>

---

## Agent Workflow `<agent-workflow>`
<agent-workflow>

Each agent has detailed instructions in `agents/`. **Read the relevant instruction file before running an agent.**

### Agents `<agents>`
<agents>

| Agent | Name | Instructions | Reads | Writes |
|-------|------|-------------|-------|--------|
| 1 | Brand Intelligence & Feed Deconstruction | `agents/agent1_instructions.md` | Instagram + website via Playwright | `agent1_brand.md` |
| 2 | Occasion Strategist | `agents/agent2_instructions.md` | `agent1_brand.md` + Snowflake cuisine tags | `agent2_occasions.md` |
| 3 | Content Architect (Nano Banana Pro) | `agents/agent3_instructions.md` | `agent1_brand.md` + `agent2_occasions.md` | `agent3_content.md` |
| 3.5 | Photo Matcher | `agents/agent3_5_instructions.md` | `agent3_content.md` + DoorDash storefront | `agent3_5_photos.md` + `reference_photos/` |
| 4 | Image Generator (Playwright → Gemini) | `agents/agent4_instructions.md` | `agent3_content.md` + `reference_photos/` | `final_images/` |

</agents>

### Execution Order `<execution-order>`
<execution-order>

1. **Agent 1** → Playwright screenshot + pixel-extract Instagram → `agent1_brand.md`
2. **Agent 2** → reads brand file + Snowflake cuisine tags → `agent2_occasions.md`
3. **Agent 3** → reads brand + occasions → `agent3_content.md`
4. **Agent 3.5** (required) → reads content + scrapes storefront photos → `reference_photos/`
5. **Agent 4** → reads content + reference photos → opens Gemini via Playwright → `final_images/`
6. **Publish (optional):** Combine outputs into Google Doc/Sheet for review

</execution-order>

### Experiment Rules `<experiment-rules>`
<experiment-rules>

- **Frequency:** 3 posts per week per merchant
- **Timeline:** Rolling 30-day forward view
- No generic content -- each merchant must feel distinct
- Balance engagement posts + revenue-driving posts

</experiment-rules>
</agent-workflow>

---

## Content Rules `<content-rules>`
<content-rules>

### Voice & Tone `<voice-and-tone>`
<voice-and-tone>

- Casual, energetic, food-obsessed -- like a friend recommending their favorite spot
- Match vibe to the merchant:
  - Sumo Ramen = cozy
  - Burger Bun = bold
  - Kaisen Don = premium
  - Chelo = sophisticated
  - 323 Hibachi = theatrical
  - Tio Nacho = neighborhood friendly
  - Jalisco = authentic family
- Never use corporate language ("leverage," "utilize," "synergy")
- Avoid: "hidden gem," "foodie paradise," "you won't believe," "game changer"

</voice-and-tone>

### Post Structure `<post-structure>`
<post-structure>

- **Hook** (first line): Pattern-interrupt that stops the scroll
- **Body**: 2-4 short punchy lines -- micro-story, visceral food description, or FOMO
- **CTA**: Every post needs a specific call to action
- **Hashtags**: 15-20 per post. Mix of high-volume (500K+), mid (50K-500K), and niche (<50K). Include location tags.

</post-structure>

### Campaign Framework `<campaign-framework>`
<campaign-framework>

1. **Pre-occasion teaser** (3-5 days before)
2. **Day-of main post** (hero content)
3. **Post-occasion follow-up** (recap, UGC reshare, or FOMO)

</campaign-framework>

### Content Formats `<content-formats>`
<content-formats>

- **Reels** (highest reach): 7-15 seconds, text overlays, trending audio
- **Carousels** (highest saves): "Top 5 reasons," "What to order," BTS
- **Stories** (highest engagement): Polls, quizzes, countdown stickers

</content-formats>

### Growth Tactics `<growth-tactics>`
<growth-tactics>

- Saveable content (tips, listicles, "order this not that")
- Shareable captions (relatable food moments, "send this to...")
- Comment prompts (questions, "wrong answers only," "rate this 1-10")
- Geo-tag everything
- Post timing: Tue-Thu 11am-1pm and 5-7pm local time

</growth-tactics>

### Anti-Patterns `<anti-patterns>`
<anti-patterns>

- No generic "Happy [Holiday]!" without food tie-in and CTA
- No stock photos -- reference actual menu items
- No walls of text -- break into carousel if >5 lines
- No engagement bait that doesn't deliver
- No hashtags in caption body -- first comment or after line break

</anti-patterns>
</content-rules>

---

## Terminology `<terminology>`
<terminology>

Social-media-specific terms (general terms like Mx/Cx/Dx are in the global `~/.claude/CLAUDE.md`):

| Term | Definition |
|------|------------|
| MP Weekly Avg | Marketplace (DoorDash 3P) weekly order average |
| SF Weekly Avg | Storefront (DoorDash 1P) weekly order average |
| CTA | Call to Action |
| UGC | User-Generated Content |
| Hook | First line of a caption designed to stop the scroll |
| Occasion Campaign | Content tied to a specific date, holiday, or cultural moment |
| Engagement Rate | (Likes + Comments + Shares + Saves) / Followers |

</terminology>

---

## File Structure `<file-structure>`
<file-structure>

```
agents/
  agent1_instructions.md
  agent2_instructions.md
  agent3_instructions.md
  agent3_5_instructions.md
  agent4_instructions.md
merchants/
  {Merchant Name}/
    agent1_brand.md
    agent2_occasions.md
    agent3_content.md
    agent3_5_photos.md
    bio_optimization/
      current_bio.md
    reference_photos/
    screenshots/
    final_images/
```

</file-structure>

---

## MCP Debugging `<mcp-debugging>`
<mcp-debugging>

The Google Workspace MCP server lives at `~/google-workspace-mcp/`. Config and tokens are in `~/.config/gw-mcp/`.

### Known Issues `<known-issues>`
<known-issues>

**Error messages were swallowed (FIXED 2026-02-23)**

**Root cause:** `error_handler.py` only caught `google.api_core.exceptions.GoogleAPICallError` but the Sheets/Drive/Docs client raises `googleapiclient.errors.HttpError` (different class). All real API errors fell through to a generic `"Unexpected error in {func_name}"` catch-all that hid the actual problem.

**Fix applied:** Added `HttpError` handling to `with_error_handling()` in `~/google-workspace-mcp/google_workspace_mcp/utils/error_handler.py`. Now surfaces the real error (wrong tab name, 403 permission denied, 404 not found, etc.).

</known-issues>

### Debugging Steps `<debugging-steps>`
<debugging-steps>

1. **Check the token:** Run `python -c "import pickle; creds=pickle.load(open('$HOME/.config/gw-mcp/token.pickle','rb')); print(f'Valid: {creds.valid}, Expired: {creds.expired}')"` with the MCP venv Python.
2. **If token expired:** Delete `~/.config/gw-mcp/token.pickle` and restart Claude Code -- the OAuth flow will re-auth.
3. **If token valid but reads fail:** The error message should now tell you the actual issue (bad sheet name, no access, etc.).
4. **Sheet names with special characters** (dashes, spaces, etc.) must be wrapped in single quotes in the range: `"'My Sheet -- Name'!A1:Z10"`.
5. **To find tab names** for a spreadsheet, use: `service.spreadsheets().get(spreadsheetId=ID).execute()['sheets']` -- each sheet has `properties.title` and `properties.sheetId` (the gid from the URL).
6. **After editing MCP code**, restart the MCP server. Use `/mcp` in Claude Code or restart the session.

</debugging-steps>
</mcp-debugging>
