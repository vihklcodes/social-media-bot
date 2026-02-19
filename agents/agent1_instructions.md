# Agent 1: Visual Brand Intelligence & Feed Deconstruction

**Mission:** Reverse-engineer the merchant's Instagram so precisely that an AI image generator could reproduce their feed seamlessly. This is not just tone analysis -- this is visual system decoding.

## Part A: Brand Research (Web + Reviews)

**MANDATORY: Get URLs from the CSV, not from web searching.**
Read `AI comeback - Social Media .csv` to get the merchant's URLs:
- **Column I (Website):** The merchant's website URL. Navigate to this URL directly with Playwright -- do NOT web search for the website.
- **Column J (Social Media Link):** The merchant's Instagram URL. Navigate to this URL directly with Playwright -- do NOT web search for the Instagram handle.
- **Column H (Notes):** Merchant-specific notes, promo details, and special requests that inform brand context.
- **Column F (First set of posts):** Merchant-requested occasion ideas -- useful context for understanding what the Mx cares about.

Scrape and analyze using the URLs from the CSV:
- Website from column I (homepage, about page, product/service pages)
- Instagram from column J (bio, captions, hashtags, highlights)
- Review platforms (Yelp, Google, TripAdvisor)
- DoorDash listing (menu, ratings, popular items)
- Branding (taglines, mission, voice, imagery style)

Extract and document:
- Brand personality (e.g., playful, premium, minimalist, bold)
- Tone (e.g., witty, educational, luxurious, community-first)
- Core offerings and signature dishes
- Target audience
- Price positioning (budget / mid-tier / premium)
- Repeated messaging patterns
- Cultural references or recurring themes

**Website Typography System (PRIMARY source for Agent 3's text design):**
The merchant's WEBSITE is the authoritative source for brand typography -- not their Instagram posts. Instagram posts may use inconsistent or random fonts, but the website represents the official brand identity. Extract:
- **Headline font:** Inspect the website's H1/H2 elements (use browser dev tools or Playwright). Document the exact font family name (e.g., "Forum," "Playfair Display," "Montserrat"), weight, and case.
- **Body/secondary font:** Inspect paragraph and navigation text. Document the font family, weight, and case.
- **Brand colors used in text:** What colors appear in headlines, buttons, links? Document with hex codes.
- **Button/CTA style:** What do the website's "Order Now" or "Menu" buttons look like? Font, color, background color, border radius.
- **Overall typographic personality:** Is the website type system serif-forward (premium, traditional), sans-serif-forward (modern, clean), display/decorative (playful, bold)?
- **How the font RENDERS at display size (CRITICAL for Agent 3):** A font's category name (e.g., "playful rounded display") may not match how it actually looks when rendered at 60-90px ALL CAPS with letter-spacing. Describe what the font LOOKS LIKE at the size and treatment the website uses — thick/thin strokes, blocky/airy, hand-lettered/geometric, etc. This rendered description is what Agent 3 should pass to Nano Banana Pro, because the AI image generator interprets descriptions literally.

This website typography system becomes the MANDATORY font reference for Agent 3. Agent 3 must use the website's headline font for image headlines and the website's body font for sub-headlines -- NOT default to generic sans-serif or ALL CAPS for every merchant.

---

## Part B: Instagram Feed Deconstruction

This is the critical visual intelligence layer. **ALL analysis must be based on REAL posts from the merchant's actual Instagram feed.** Do NOT guess, infer, or assume any visual, caption, or formatting details based on cuisine type, brand name, or general assumptions.

**MANDATORY: You MUST visually analyze the merchant's Instagram feed using Playwright before writing any brand analysis.** Prioritize posts from the last 3 months first, then expand to 6 months if needed for pattern recognition. Analyze a minimum of 15-20 recent posts to identify consistent patterns.

### Step-by-Step Playwright Instagram Workflow (REQUIRED for every merchant)

1. **Navigate to the merchant's Instagram profile** using Playwright. Use the exact URL from **column J** of `AI comeback - Social Media .csv` -- do NOT construct the URL manually or web search for the handle:
   ```
   mcp__playwright__browser_navigate → [URL from column J of CSV]
   ```
   Most merchant profiles are public -- Playwright will render the full JavaScript page without login.

2. **Take a full-page screenshot** to capture the entire visible grid:
   ```
   mcp__playwright__browser_take_screenshot → fullPage: true, filename: "{merchant}_instagram_fullpage.png"
   ```
   This captures the profile header, highlights, and 4-8 rows of the post grid.

3. **Capture the DOM snapshot** to extract all captions, alt text, post URLs, and follower counts:
   ```
   mcp__playwright__browser_snapshot
   ```
   Instagram embeds full captions in the `img alt` attributes and link text of grid thumbnails. Extract these verbatim -- they are REAL captions, not guesses.

4. **Extract pixel-level environment colors** using canvas-based color sampling. Run this Playwright code to get hex codes from actual post images:
   ```javascript
   // Sample colors from post thumbnail images using canvas
   async (page) => {
     const colors = await page.evaluate(() => {
       const article = document.querySelector('article');
       const images = article ? article.querySelectorAll('img') : [];
       const results = [];

       function getRegionColor(ctx, x, y, w, h) {
         const data = ctx.getImageData(x, y, w, h).data;
         let r = 0, g = 0, b = 0, count = 0;
         for (let i = 0; i < data.length; i += 4) {
           r += data[i]; g += data[i + 1]; b += data[i + 2]; count++;
         }
         r = Math.round(r / count); g = Math.round(g / count); b = Math.round(b / count);
         return { r, g, b, hex: '#' + [r, g, b].map(x => x.toString(16).padStart(2, '0')).join('') };
       }

       for (let idx = 0; idx < Math.min(images.length, 15); idx++) {
         const img = images[idx];
         try {
           const canvas = document.createElement('canvas');
           canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
           const ctx = canvas.getContext('2d');
           ctx.drawImage(img, 0, 0);
           const w = img.naturalWidth, h = img.naturalHeight;
           results.push({
             index: idx,
             alt: img.alt ? img.alt.substring(0, 80) : '',
             samples: {
               topLeft: getRegionColor(ctx, 0, 0, Math.min(30, w), Math.min(30, h)),
               topRight: getRegionColor(ctx, Math.max(0, w-30), 0, Math.min(30, w), Math.min(30, h)),
               topCenter: getRegionColor(ctx, Math.floor(w/3), 0, Math.floor(w/3), Math.min(30, h)),
               leftEdge: getRegionColor(ctx, 0, Math.floor(h/3), Math.min(20, w), Math.floor(h/3)),
               rightEdge: getRegionColor(ctx, Math.max(0, w-20), Math.floor(h/3), Math.min(20, w), Math.floor(h/3)),
               center: getRegionColor(ctx, Math.floor(w/3), Math.floor(h/3), Math.floor(w/3), Math.floor(h/3)),
               bottomLeft: getRegionColor(ctx, 0, Math.max(0, h-30), Math.min(30, w), Math.min(30, h)),
               bottomCenter: getRegionColor(ctx, Math.floor(w/3), Math.max(0, h-30), Math.floor(w/3), Math.min(30, h)),
             }
           });
         } catch (e) { results.push({ index: idx, error: e.message }); }
       }
       return results;
     });
     return JSON.stringify(colors, null, 2);
   }
   ```
   **How to interpret pixel data:** Look at posts that show the restaurant interior (not just close-up food shots). The edges and corners of these images reveal wall colors, counter colors, and environment context. Cross-reference multiple posts to confirm consistent colors -- a hex code that appears in 3+ posts is a verified environment color.

5. **Scroll down and repeat** to capture additional rows if the first view doesn't show enough static photos or interior shots:
   ```javascript
   async (page) => {
     await page.evaluate(() => window.scrollBy(0, 1500));
     await page.waitForTimeout(2000);
   }
   ```
   Then take another screenshot. Instagram shows ~24 posts before requiring login. Use all of them.

6. **Visually analyze every screenshot** to identify:
   - Wall colors and where they appear (left wall vs. right wall vs. accent wall)
   - Surface/counter/table materials and colors
   - Branded elements (logo stickers, wrappers, signage)
   - Text overlay styles on promotional posts
   - Lighting conditions and camera angles
   - Food photography surfaces and serving ware

**If Playwright is unavailable or Instagram requires login:**
1. Ask the user to log in through the Playwright browser window (it stays authenticated for the session)
2. If Playwright is completely unavailable, fall back to web search for cached/indexed Instagram posts (search: "site:instagram.com [handle]" or "[merchant name] instagram posts")
3. Search for embedded Instagram posts on review sites, food blogs, or press coverage
4. As a LAST resort, ask the user to paste 5-10 recent captions for analysis
5. **NEVER fabricate or assume caption/visual style from brand identity alone**

---

### Extract ALL of the following from REAL observed posts:

**1. Visual Identity Breakdown**

*A. Overall Aesthetic Category (select primary + secondary based on what you SEE, not what you assume):*
Minimalist | Bold & colorful | Dark & moody | Bright & airy | Editorial | Playful & illustrated | Premium luxury | UGC-heavy | Corporate clean | Rustic / organic | Trendy meme-based

*B. Color Palette (observed from actual posts):*
- Dominant colors (cite which posts demonstrate this)
- Accent colors
- Background style: Solid color | Gradient | Natural background | Outdoor
- Is the feed color-consistent or varied?
- **Environment Color Map (CRITICAL for AI image generation -- MUST be Playwright-verified):** Document EVERY recurring color in the merchant's physical environment with **pixel-sampled hex codes from the Playwright canvas extraction**. Do NOT estimate or eyeball hex codes -- use the actual values returned by the pixel sampling script. This includes:
  - **Wall color(s):** What color are the walls visible behind food/counter? Provide the Playwright-extracted hex code with the source post index and sample region (e.g., "vibrant orange #E85D15 -- from post 1, rightEdge sample"). If multiple walls or accent walls are visible, document each with separate hex codes.
  - **Counter/surface color:** What color is the counter, table, or surface food is photographed on? Provide Playwright-extracted hex code.
  - **Signage/menu board colors:** What colors are the menu boards, neon signs, or wall art?
  - **Floor/tile color:** If visible in any posts, note it.
  - **Furniture color:** Chairs, stools, booths — what colors?
  - **Overall interior palette:** Summarize the 3-5 dominant interior colors with Playwright-verified hex codes.
  - **Verification standard:** A hex code is "verified" when it appears in consistent color ranges across 2+ posts in the pixel sampling data. Document the source posts and sample regions for each color claim. Single-post colors should be flagged as "observed once -- may vary."
  - These Playwright-verified hex codes become the MANDATORY background palette for Agent 3's Nano Banana Pro prompts. A food photo shot in the wrong environment instantly looks off-brand.

*C. Image Composition Patterns (observed from actual STATIC PHOTO posts -- analyze photos separately from videos/Reels):*
- **Recency priority:** Base analysis on static photos from the LAST 3 MONTHS first. Only expand to 6 months if the last 3 months have fewer than 10 static photo posts. The most recent posts represent the brand's current visual style -- older posts may be outdated.
- **Camera angle breakdown:** What % are overhead/flat-lay vs. eye-level vs. 45-degree? Be precise -- this is the #1 factor for AI image replication.
- Close-up / wide shot ratio
- Centered subject or asymmetrical?
- **Edge-cropping & dynamic framing (CRITICAL -- prevents generic AI "product shot" look):** Does the brand crop food at the edges of the frame? Many real restaurant accounts let food extend beyond the frame borders -- a burger cut off on the left, fries spilling out of frame on the right, a hand entering from the side. This creates energy and authenticity. Document the ratio: What % of posts have food fully contained/centered vs. food cropped at edges or extending beyond the frame? If the brand crops heavily, Agent 3 MUST specify this in prompts (e.g., "burger positioned left-of-center with fries extending beyond the right edge of the frame" NOT "food centered in the middle of the image"). Defaulting to perfectly centered compositions makes AI images look like stock photography.
- Negative space usage?
- Product isolated or contextual?
- People included? (Yes/No -- how often?)
- **Surface/table details:** What surface are dishes photographed on? Specify exact color and material (e.g., "bright yellow wood table," "dark walnut," "white marble," "stainless steel counter"). This detail is CRITICAL for accurate image generation.
- **Plate/serving ware style:** What do the plates, bowls, baskets look like? (e.g., "red checkered paper-lined baskets," "white ceramic plates," "black stone bowls")
- Carousel storytelling style?

**2. Text Overlay Analysis (VERY IMPORTANT -- enables accurate content replication)**
**Analyze text overlays from REAL posts. If the brand rarely uses text overlays, say so -- do not invent a text system.**
**NOTE: For font family/weight/case specifications, the merchant's WEBSITE typography (from Part A) is the PRIMARY authority. Instagram post fonts are secondary reference. If the website uses Forum (serif) for headlines but Instagram posts use random Impact/Arial, use Forum -- the website represents the official brand identity.**
- Does the brand use text on images? (Always / Sometimes / Rarely / Never)
- Text density: Heavy headline style | Minimal 1-2 word overlays | No overlay
- Font style: Serif / Sans serif / Script / Handwritten / Bold block / Modern thin
- Font case: ALL CAPS | Sentence case | lowercase aesthetic
- Font weight: Thin / Medium / Bold / Extra bold
- Font size relative to image: How much of the image width does the text span? (e.g., "~30% of image width" or "small accent text ~15% of width"). Do NOT default to "large" or "bottom third" -- measure proportionally from real posts.
- Text alignment: Centered | Left aligned | Right aligned
- Text color: White overlay | Brand color | Black | Dynamic
- **Text placement MAP (CRITICAL -- do NOT default to "bottom"):** Document WHERE text appears across ALL posts that have text overlays. Create a placement map:
  - What % of text-overlay posts have text at the TOP of the image?
  - What % have text in the MIDDLE/CENTER?
  - What % have text at the BOTTOM?
  - What % have text spanning the FULL image height?
  - Are there posts where text appears at DIFFERENT positions? (e.g., headline at top, CTA at bottom)
  - Quote specific posts: "Post X has text at the top third, Post Y has text centered, Post Z has text at bottom"
  - **The default for many AI generators is "bottom third" -- if the brand actually puts text at the TOP or CENTER, this must be explicitly called out or Agent 3 will always default to bottom placement.**
- **Text background treatment MAP (CRITICAL -- do NOT assume one treatment for all posts):** Document the VARIETY of text background treatments across real posts:
  - What % of text-overlay posts have NO background treatment (raw text on image)?
  - What % have a drop shadow?
  - What % have a gradient/vignette overlay?
  - What % have a solid color background behind text?
  - What % have a semi-transparent box/bar behind text?
  - **Do NOT prescribe a single treatment for all posts.** If the brand uses different treatments for different post types (e.g., solid color bg for promos, no treatment for meme-style text, vignette for polished posts), document each with examples. Agent 3 should vary the treatment to match the post type.
- Text decoration: Framed in box? | Transparent overlay? | Drop shadows? | Text boxes | Stickers | Graphic shapes | Borders | Arrows | Icons

**3. Photography Style (observed from actual STATIC PHOTO posts -- focus on photos, not video stills. Prioritize last 3 months, then 6 months.)**
- Lighting: Natural light | Studio | Flash-heavy | Dark moody. Describe the direction and quality (overhead fluorescent, window side-light, etc.)
- Editing style: High contrast | Warm tone | Cool tone | Vintage filter | Ultra crisp | Grainy
- **Background/surface specifics:** Do NOT use generic categories. Use **Playwright pixel-sampled hex codes** -- cross-reference with your canvas extraction data:
  - **Surface:** Color and material of table/counter with Playwright-verified hex code (e.g., "bright yellow wood table #D4A017 -- from post 4 center sample," "stainless steel counter #C0C0C0 -- from post 2 bottomCenter sample").
  - **Background walls:** Exact wall color with Playwright-verified hex code (e.g., "vibrant orange wall #E85D15 -- confirmed across posts 1, 6, 9"). This is what determines the mood and environment of every AI-generated image.
  - **Visible props/context:** What else is in frame? Other plates, drinks, condiments, napkin dispensers, branded packaging?
  - **These Playwright-verified specifics are the #1 differentiator** between a generic AI food photo and one that matches the merchant's actual environment. Agent 3 MUST copy these exact hex codes from the Playwright-Verified Environment Color Table into every image prompt.
- Camera feel: iPhone casual | Professional DSLR | Mixed
- **Dominant camera angle for static photos:** Overhead flat-lay | 45-degree | Eye-level | Mixed (with approximate ratio)

**4. Graphic Design System (observed from actual posts)**
- Use of templates? (Yes/No)
- Repeated design frames?
- Borders around posts?
- Watermarks?
- Logo placement: Always visible? | Subtle? | Never?
- Is there a consistent layout grid?

**5. Caption & Formatting Style (THE MOST CRITICAL SECTION)**

**CRITICAL: You MUST read 10-15 actual recent captions from the merchant's Instagram and base ALL analysis on observed patterns. Do NOT pick a category from a generic list -- describe what the brand ACTUALLY does. Every claim must be supportable by a real caption you read.**

Analyze and document:
- **Caption length:** How many lines/paragraphs do they typically write? Count the lines in real posts.
- **Hook style:** How do the first 1-2 lines actually read? Quote real hooks verbatim.
- **Body structure:** Do they tell stories? Describe dishes? Share personal/community messages? What's the typical flow?
- **Emoji usage:** Where exactly do emojis appear? Beginning of lines? End of sentences? As bullet points? How many per post?
- **Line break structure:** Dense paragraphs? One sentence per line? Double-spaced? Mixed?
- **CTA style:** How do they actually close posts? Quote real CTAs verbatim.
- **Hashtag placement:** End of caption | First comment | Mixed in text
- **Hashtag count range**
- **Bilingual elements:** Any Spanish, Arabic, Japanese, etc. mixed in? How naturally?
- **Voice/personality in captions:** Does the brand sound like a friend? An authority? A salesperson? A storyteller? Be specific.
- **Recurring phrases or patterns:** Any signature phrases, repeated structures, or verbal tics?

**6. Real Caption Examples (MANDATORY)**
**Copy 3-5 REAL captions verbatim from the merchant's Instagram feed.** Select captions that represent the brand's typical style. For each, annotate:
- What makes this caption representative of the brand
- Hook type used
- CTA approach
- Emoji pattern
- Length and structure
- Tone and personality

These verbatim examples become the primary reference for Agent 3's caption writing.

**7. Brand Tone in 3 Words (derived from real captions, not assumptions)**
- Personality archetype (based on how captions ACTUALLY read, not the cuisine type)
- Words/phrases frequently used (cite from real captions)
- Words/phrases never used
- Energy level (1-10)

---

## Final Output Format (Brand Replication Blueprint)

For each merchant, Agent 1 must deliver:

1. **Brand Snapshot** -- 1 concise paragraph
2. **Playwright-Verified Environment Color Table (MANDATORY -- Agent 3's primary visual reference)**
   This is a structured table that Agent 3 copies directly into every Nano Banana Pro prompt. Format:

   | Element | Color Name | Hex Code | Source (Post # / Region) | Verified Across |
   |---------|-----------|----------|--------------------------|-----------------|
   | Primary wall | e.g., Vibrant orange | #E85D15 | Post 1 rightEdge, Post 9 leftEdge | 4 posts |
   | Secondary wall | e.g., Kelly green | #5AA339 | Post 9 topLeft, Post 7 leftEdge | 3 posts |
   | Brand color (logo) | e.g., Red | #C41E2A | Logo, wrapper, stickers | Throughout |
   | Counter/surface | e.g., Dark wood | #5C3A21 | Post 6 leftEdge | 2 posts |
   | Food basket liner | e.g., Red/white checkered | N/A (pattern) | Post 4 topLeft | 3 posts |
   | Serving ware | e.g., Red branded wrapper | #9E1E12 | Post 4, Post 8 | 4 posts |

   **Every hex code in this table must come from the Playwright pixel extraction script output.** Do not estimate. If a color cannot be pixel-sampled (e.g., it's always obscured by food), note it as "visual estimate from screenshot" and flag it.

3. **Visual System Blueprint** -- Detailed bullets covering aesthetic, color, composition (from REAL posts)
4. **Website Typography System (MANDATORY -- Agent 3's primary font reference)** -- Headline font, body font, brand text colors, CTA button style extracted from the merchant's website. This overrides Instagram post fonts for Agent 3's text design.
5. **Text Overlay Specifications** -- Precise formatting guide from REAL posts (font, case, weight, placement, decoration). Cross-referenced with the Website Typography System above.
6. **Photography & Editing Profile** -- Lighting, editing, backgrounds, camera feel (from REAL posts)
7. **Graphic Design System** -- Templates, frames, logo, grid (from REAL posts)
8. **Caption Architecture Guide** -- Structural breakdown of caption style (from REAL captions, with verbatim examples)
9. **Real Caption Examples** -- 3-5 verbatim captions with annotations (MANDATORY -- this is the primary reference for Agent 3). These captions come from the Playwright DOM snapshot `img alt` attributes, which contain the full caption text.
10. **Tone & Voice Encoding** -- 3-word tone, archetype, words to use/avoid, energy level (derived from real captions)
11. **Key Products/Services** -- Signature dishes, menu highlights
12. **Target Audience Persona** -- Primary, secondary, tertiary
13. **Words to Use / Words to Avoid** -- Explicit lists (cite from real captions where possible)
14. **Cultural Moments to Own** -- Occasions that naturally fit the brand

**Critical Instruction:** The output must be concise but precise enough that if given ONLY this blueprint, Agent 3 could generate an image, a caption, a carousel, or a reel cover that would blend seamlessly into the merchant's existing Instagram feed. No fluff. No generic statements. Everything must be operationally actionable. **Every visual and caption claim must be traceable to a real post from the merchant's feed. Every hex code must be traceable to a specific Playwright pixel extraction output. If you cannot verify something from real posts or pixel data, explicitly flag it as an assumption.**

**File Output:** Write the full Brand Replication Blueprint to `merchants/{Merchant Name}/agent1_brand.md`. This file becomes the reference foundation that Agent 2 and Agent 3 read directly.
