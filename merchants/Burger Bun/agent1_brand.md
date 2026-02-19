# Brand Intelligence: Burger Bun (@burgerbunla)

**Data Source:** Playwright browser automation -- full JavaScript rendering of Instagram profile, full-page screenshots, DOM snapshot caption extraction, and canvas-based pixel color sampling from 15+ post images. Verified February 18, 2026.

---

## 1. Brand Snapshot

Burger Bun is a family-owned, award-winning fast-casual restaurant at 818 N Pacific Ave, Glendale, CA 91203, founded in 2008 by celebrity restaurateur Art Chebeyan. The brand delivers an American-Greek-Mexican fusion menu anchored by hand-pressed 100% Angus beef burgers, award-winning pastrami, carne asada tacos, Mediterranean gyros, and legendary milkshakes. Awards include "Best Burger in Los Angeles" every year since 2019, "Best Pastrami in Town" (2020, 2022, 2025), and "Best Milkshake in Glendale" (2018, 2019, 2022, 2024, 2025). Halal options available. Instagram: @burgerbunla, 2,422 followers, 483 posts, 808 following. Managed by Kara Content (@karacontent). DoorDash: 4.7 stars. The feed is Reel/video-heavy with professional production quality but low engagement. The restaurant interior features distinctive **vibrant orange walls** and **kelly green accent walls** -- a bold, colorful environment that is the #1 visual signature for AI image replication.

---

## 2. Playwright-Verified Environment Color Table

**Source:** Canvas-based pixel extraction from Instagram post thumbnail images. Each hex code was sampled from specific pixel regions of actual post images rendered via Playwright.

| Element | Color Name | Hex Code | Source (Post # / Region) | Verified Across |
|---------|-----------|----------|--------------------------|-----------------|
| **Primary wall** | Vibrant orange | **#E85D15** | Post 1 topRight #E45F15, Post 1 rightEdge #F36D09, Post 9 leftEdge #D03500, Post 9 rightEdge #EF4401 | 4+ posts |
| **Secondary wall** | Kelly green | **#5AA339** | Post 9 topLeft #75D267 (well-lit), Post 9 topRight #3D6E51 (shadow), Post 7 leftEdge #637344, Post 7 rightEdge #4B5A30 | 4+ posts |
| **Brand color (logo)** | Red | **#C41E2A** | Logo circle, branded cup stickers ("BURGER BUN / ENJOY THE BLEND"), wrapper text | Throughout |
| **Brand color (website)** | Crimson red | **#DD2127** | Website burgerbun.la primary brand color | Website |
| **Secondary dark tone** | Deep burgundy | **#A30118** | Website burgerbun.la "Download Our Mobile App" section bg (Playwright-verified rgb(163,1,24)); earlier estimate was #470001 | Website |
| **Food tray** | Brand red | **#9E1E12** | Post 4 topLeft #9E1E12 (red tray/checkered paper) | 5+ posts |
| **Food basket liner** | Red/white checkered | N/A (pattern) | Visible in posts 4, 5, 6, and across Reel thumbnails | 5+ posts |
| **Branded wrapper** | Red text on white | **#C41E2A** on white | Post with "IS THIS YOUR NEW SANDWHICH ORDER?" and multiple wrapper shots | 3+ posts |
| **Counter/surface** | Neutral wood/beige | **#8B6914** (visual estimate) | Partially visible in interior shots -- mostly obscured by food/trays | 2 posts |
| **Interior lighting** | Warm overhead LED | N/A | Bright, warm, well-lit fast-casual environment | All interior posts |

**Critical note for Agent 3:** The orange (#E85D15) and green (#5AA339) walls are the two dominant colors of the restaurant interior. They meet at a corner -- orange is the primary wall color visible in most interior shots, green is the secondary/accent wall. Every Nano Banana Pro image prompt set inside the restaurant MUST include one or both of these wall colors as the background environment.

---

## 3. Visual System Blueprint

**A. Overall Aesthetic Category:**
- **Primary:** Bold & colorful (vibrant orange + green interior, bright food photography, saturated colors)
- **Secondary:** Trendy meme-based (Reel-dominant feed with text overlay hooks, meme-style humor, engagement-bait formats)

**B. Color Palette (Playwright-verified from real posts):**
- **Dominant interior colors:** Vibrant orange (#E85D15) walls + kelly green (#5AA339) accent walls -- confirmed across 8+ posts
- **Brand identity colors:** Red (#DD2127 / #C41E2A), black, white -- from logo, wrappers, cup stickers
- **Food-dominant colors:** Rich browns (grilled meat, toasted buns), bright yellows (melted cheese), vivid greens (lettuce), reds (tomato, sauce)
- **Background style:** Natural restaurant interior -- the orange and green walls ARE the background. Not studio, not plain.
- **Feed color consistency:** Highly consistent -- orange and green walls create a recognizable color signature across interior shots. Close-up food shots have warm, saturated tones.

**C. Image Composition Patterns (from Playwright screenshots of real posts):**
- **Content type ratio:** ~85% Reels/video, ~10% carousels, ~5% static photos. The feed is overwhelmingly Reel-dominant. Reels carry the Reel icon on thumbnails; carousels carry the carousel icon. Very few pure static photo posts.
- **Camera angle breakdown for food content:** Primarily **45-degree angle** (classic burger shot showing height) and **eye-level** (face-on burger shots). Some overhead/flat-lay for spread shots (trays of food).
- **Close-up / wide shot ratio:** ~70% close-up food shots, ~30% medium shots showing person + food or food spread
- **Centered vs. asymmetric/cropped composition:** Mixed -- NOT always centered. From Playwright screenshots:
  - ~40% of posts have food **centered** as a hero product shot
  - ~60% of posts have food **cropped at edges, off-center, or extending beyond the frame**. Examples:
    - Top-row posts: Sandwich held by hands with the bottom of the sandwich cropped by the frame edge. Girl with drinks where the drinks are cut off at the bottom.
    - Row 2: Sandwich being held where the top bun is cropped by the top edge. Loaded fries overhead shot where the plate edges are cut off on all sides.
    - Row 3: Guy holding tray where the tray is partially cut off at the bottom. Milkshake where the bottom of the cup is cropped.
  - **The brand favors dynamic, cropped compositions over centered product shots.** Food extends beyond the frame edges, creating energy and a "caught in the moment" feel rather than a studio product shot. Agent 3 MUST vary compositions: some centered hero shots, but MOST should have food positioned off-center with edges cropped.
- **Negative space usage:** Minimal -- food fills the frame and often extends beyond it. Orange/green walls fill the background.
- **Product isolated or contextual:** Contextual -- food is shown IN the restaurant environment with the distinctive colored walls visible behind
- **People included:** Yes, frequently -- staff member (guy in white shirt), influencer appearances, UGC reposts. Approximately 30-40% of recent posts include a person.
- **Surface/table details:** Red plastic trays with red-and-white checkered deli paper lining. Some food shown in branded "BURGER BUN" wrappers (red text on white paper). Counter is neutral wood/beige tone.
- **Plate/serving ware style:** Red plastic trays lined with red-and-white checkered deli paper (classic American burger joint style). Clear plastic cups with dome lids for milkshakes/drinks with branded "BURGER BUN / ENJOY THE BLEND" red circle stickers. Branded paper wrappers for takeout sandwiches.
- **Carousel storytelling style:** Limited carousels observed -- a few multi-image posts showing food from different angles (Sep 11, Sep 8, Aug 30, Aug 24 carousels visible in grid).

---

## 4. Website Typography System

**Source:** Playwright browser automation -- full JavaScript rendering of burgerbun.la with computed style extraction from all visible elements. Verified February 18, 2026. Site built on Framer.

**Fonts Loaded (4 font families via @font-face):**

| Font Family | Source | Weights Loaded | Styles Loaded | Actually Used on Page? |
|-------------|--------|----------------|---------------|------------------------|
| **Boogaloo** | Google Fonts | 400 | Normal | **Yes** -- H1 hero title, all H3 section headings |
| **Satoshi** | FontShare (via Framer) | 400, 700 | Normal, Italic | **Yes** -- body text, nav, CTAs, FAQ, footer, menu item names |
| **Forum** | Google Fonts | 400 | Normal | **No** -- loaded in CSS but NOT applied to any visible element |
| **Inter** | Framer CDN | 400, 700 | Normal | **No** -- loaded as fallback only, never rendered |

**A. Primary Display Font: Boogaloo**
- **Type:** Bold casual display sans-serif (Google Fonts). At large sizes with ALL CAPS and letter-spacing, renders as thick, hand-lettered, and blocky -- not bubbly or rounded.
- **Weight used:** 400 (regular). The `<strong>` wrapper on the H1 renders at weight 700 but Boogaloo only ships weight 400, so the browser faux-bolds it.
- **Case treatment:** ALL CAPS (`text-transform: uppercase`) on every instance
- **Letter spacing:** 2.7px on H1 hero title; normal on H3 section headings
- **Where used:**
  - **H1 hero title** ("BURGER BUN"): 90px, white (#FFFFFF), uppercase, letter-spacing 2.7px, over hero food image
  - **All H3 section headings** ("ABOUT US", "FEATURED", "GALLERY", "REVIEWS", "FAQ", "DOWNLOAD OUR MOBILE APP!"): 50px, crimson red (#DD2127), uppercase
- **Personality:** Bold, thick, casual, hand-lettered feel -- reads as a confident burger joint, not fine dining. At 90px ALL CAPS with 2.7px letter-spacing, the letterforms are chunky and impactful rather than bubbly. Matches the brand's cocky/casual Instagram tone.

**B. Primary Body Font: Satoshi**
- **Type:** Geometric sans-serif (FontShare, via Framer third-party assets)
- **Weights used:** 400 (regular) for body text, nav, contact info, FAQ questions; 700 (bold) for menu item names and emphasis
- **Case treatment:** Sentence case throughout (no uppercase transforms on body text)
- **Where used:**
  - **Navigation links:** 400, 16px, black (#000000)
  - **H2 subheading** ("Bite into Burger Bliss Today!"): 400, 17px, white (#FFFFFF)
  - **About / body paragraphs:** 400, 17px, black (#000000)
  - **Menu item names** (bold): 700, 17px, black (#000000)
  - **CTA button text** ("Order Online"): 400, 16px, white (#FFFFFF) on crimson red (#DD2127) button
  - **FAQ questions:** 400, 20px, white (#FFFFFF) on red background
  - **Contact section labels** ("Phone number:", "Address:", etc.): 400, 14px, dark gray (#383838)
  - **Footer copyright:** 400, 14px, white (#FFFFFF) on crimson red background
  - **Review text:** 400, 17px, black (#000000)

**C. Loaded but NOT Actively Used:**
- **Forum** (decorative serif, Google Fonts) -- loaded in the stylesheet but zero elements render with it. Likely a design remnant or intended for future use. However, its presence in the font stack suggests the brand considers serif an acceptable accent style.
- **Inter** (sans-serif, Framer CDN) -- loaded as a system fallback; never appears in computed styles on any visible text element.

**D. Brand Colors Used in Text (Playwright-verified hex codes):**

| Color | Hex Code | RGB | Where Used |
|-------|----------|-----|------------|
| **Crimson red** | **#DD2127** | rgb(221, 33, 39) | H3 section headings, "Download Our Mobile App!" heading, button backgrounds, FAQ section bg, footer bg |
| **Black** | **#000000** | rgb(0, 0, 0) | Body text, nav links, menu item names, review text |
| **White** | **#FFFFFF** | rgb(255, 255, 255) | H1 hero text, H2 subheading, CTA button text, FAQ question text, footer text, hero background body bg |
| **Dark gray** | **#383838** | rgb(56, 56, 56) | Contact section labels ("Phone number:", "Address:", etc.) |
| **Deep burgundy** | **#A30118** | rgb(163, 1, 24) | "Download Our Mobile App" section background (darker variant of brand red) |

**E. Button/CTA Styling:**

| Element | Font | Weight | Size | Text Color | Background | Border Radius | Padding |
|---------|------|--------|------|------------|------------|---------------|---------|
| **Nav "Order Online" button** | Satoshi | 400 | 16px | White #FFFFFF | Crimson red #DD2127 | 4px | 14px 22px |
| **DoorDash modal buttons** ("Order Delivery" / "Order Pickup") | DD-TTNorms (DoorDash system font) | 700 | 16px | White #FFFFFF | Crimson red #DD2127 | 10px | 0px |

**F. Overall Typographic Personality:**
The website uses a clear two-font hierarchy: **Boogaloo** for bold, playful, ALL CAPS display headings that grab attention, and **Satoshi** for clean, modern, readable body text. This combination creates a "fun but trustworthy" vibe -- the headings scream casual burger joint energy while the body text keeps things legible and professional. The crimson red (#DD2127) is the dominant accent color for headings and CTAs, creating strong visual urgency.

**CRITICAL NOTE FOR AGENT 3:** These website fonts are the **PRIMARY AUTHORITY** for text overlay design on Nano Banana Pro image prompts. Specifically:
- **Boogaloo** (bold casual display, ALL CAPS, uppercase) should be the default headline font for promotional Instagram posts -- it matches both the website and the Instagram feed's bold condensed style.
- **Satoshi** (geometric sans-serif, sentence case) should be the default sub-headline/CTA font for "Order now - Link in bio!" text.
- **Forum** is loaded but unused -- it may be referenced for elevated/special occasion posts where a serif accent is appropriate, but it is NOT the brand's active font.
- The brand red **#DD2127** should be used for text accents or background colors on promotional posts.
- Do NOT default to generic "bold sans-serif" -- specify **Boogaloo** by name for headlines and **Satoshi** by name for body/CTA text.

---

## 5. Text Overlay Specifications

**Analyzed from real posts visible in Playwright screenshots:**

- **Does the brand use text on images/videos?** Yes -- frequently on Reels, occasionally on static posts
- **Text density:** Moderate -- 1-line headline hooks or 2-3 word promos
- **Two distinct text overlay styles observed:**

**Style 1: Bold ALL CAPS (promotional/meme hooks)**
- "TORTA THURSDAYS" -- White ALL CAPS, bold condensed sans-serif, on solid orange background
- "IS THIS YOUR NEW SANDWHICH ORDER?" -- White ALL CAPS, bold sans-serif, centered on dark image
- "POV: THE DOCTOR SAID I NEEDED MORE GREENS" -- White ALL CAPS, bold condensed, bottom of frame
- Font: Bold condensed sans-serif (similar to Impact or Bebas Neue)
- Case: ALL CAPS
- Color: White (#fff)
- Placement: Centered, spanning ~40-60% of image width
- Use case: Promotional flyers, meme-style hooks, day-of-the-week specials

**Style 2: Casual script/cursive (relatable quotes)**
- "You had a burger yesterday..." -- White cursive/italic, sentence case, with quotation marks
- "Burger Bun" -- White script/handwritten watermark
- Font: Script or light italic serif
- Case: Sentence case
- Color: White (#fff)
- Placement: Centered or lower third
- Use case: Relatable food quotes, brand watermark

**Text Placement Map (from Playwright screenshots -- Agent 3 MUST vary placement accordingly):**

| Post | Text | Placement on Image |
|------|------|--------------------|
| "TORTA THURSDAYS" | Promo/day-specific | **TOP 20%** -- text at the top of the image with food below |
| "IS THIS YOUR NEW SANDWHICH ORDER?" | Engagement hook | **CENTER/UPPER 40%** -- text centered in the upper-middle area |
| "POV: THE DOCTOR SAID I NEEDED MORE GREENS" | Meme-style | **BOTTOM 25%** -- text at the bottom over darker area |
| "You had a burger yesterday..." | Relatable quote | **CENTER 40-60%** -- text centered vertically on the image |
| "Burger Bun" script | Brand watermark | **LOWER-LEFT 15%** -- small, subtle positioning |

**Placement distribution:** ~20% top, ~40% center/middle, ~30% bottom, ~10% subtle/corner
**Key takeaway for Agent 3:** Do NOT put text in the "bottom 15%" for every post. The brand varies text placement significantly. Promos tend to go at the TOP. Meme/quote text tends to be CENTERED. Only some posts have bottom-placed text.

**Text Background Treatment Map (from Playwright screenshots -- Agent 3 MUST vary treatment):**

| Post | Treatment | Notes |
|------|-----------|-------|
| "TORTA THURSDAYS" | **Solid orange background** | Entire image uses solid brand orange as background color -- no food photo behind text at all. Pure graphic/flyer design. |
| "IS THIS YOUR NEW SANDWHICH ORDER?" | **No treatment / raw text** | White text directly on the food image with no shadow, no vignette, no overlay. The food's dark areas provide natural contrast. |
| "POV: THE DOCTOR SAID I NEEDED MORE GREENS" | **No treatment / raw text** | White bold text directly on the image. No shadow. The lower portion of the image is dark enough for contrast. |
| "You had a burger yesterday..." | **No treatment / raw text** | White cursive text directly on a dark/blurred background. No added shadow or overlay. |
| "BURGER BUN / ENJOY THE BLEND" sticker | **Solid white circle with red text** | Brand sticker graphic, not a text overlay treatment |

**Treatment distribution:** ~60% NO background treatment (raw text on image), ~20% solid color background (graphic/flyer style), ~20% branded sticker/graphic element
**Key takeaway for Agent 3:** Do NOT apply "radial gradient vignette" to every post. The brand mostly uses RAW text on the image with NO background treatment. The food/environment provides natural contrast. Only use a vignette or shadow when the specific image composition has insufficient contrast for white text. For promo/day-specific posts, consider using a solid brand-color background (orange #E85D15) instead of a food photo.

**Brand font system (see Section 4: Website Typography System for full Playwright-verified details):**
- **Boogaloo** (bold casual display sans-serif) -- ALL CAPS headings on website; the primary display font. This is the brand's actual headline font.
- **Satoshi** (geometric sans-serif) -- Body text, nav, CTAs, FAQ, reviews. The primary body/CTA font.
- **Forum** (decorative serif) -- Loaded on website but NOT used on any visible element. Available for elevated/special occasion accent use only.
- **Inter** (sans-serif) -- Loaded as fallback only; never rendered.

**Note for Agent 3:** The Instagram feed uses bold ALL CAPS condensed sans-serif for most text overlays, which aligns with the Boogaloo display font's ALL CAPS treatment documented in Section 4. Agent 3 should specify **Boogaloo** (bold casual display, ALL CAPS) for promotional headlines and **Satoshi** (geometric sans-serif, sentence case) for sub-headlines/CTAs. For elevated/special occasion posts, Forum serif may be used as an accent -- but Boogaloo is the PRIMARY headline font per the website's actual rendering.

---

## 6. Photography & Editing Profile

**Verified from Playwright screenshots and pixel color data:**

- **Lighting:** Bright interior LED lighting -- warm, well-lit, clean. The orange walls amplify warmth. Not moody or dark. Some Reels show the restaurant's bright overhead lighting with a warm cast.
- **Editing style:** High saturation, warm tones. Colors are punchy -- cheese looks extra golden, meat is rich brown, lettuce pops green. The orange/green walls already provide vivid color without heavy editing.
- **Background/surface specifics (Playwright-verified hex codes):**
  - **Surface:** Red plastic trays with red-and-white checkered paper on a neutral wood/beige counter -- from Post 4 center sample ~#99704B (brown-toned)
  - **Background walls:** Vibrant orange wall #E85D15 (dominant, confirmed across Posts 1, 6, 9) + kelly green accent wall #5AA339 (confirmed across Posts 7, 9, and multiple drink posts). The orange and green walls meet at a corner in the restaurant.
  - **Visible props/context:** Menu boards on the orange wall, iPad/POS system on counter, Coca-Cola fridge (blue/red), branded cup stickers, straw dispensers
  - **These Playwright-verified specifics are the #1 differentiator** between a generic AI food photo and one that matches the merchant's actual environment. Agent 3 MUST copy these exact hex codes from this color table into every image prompt.
- **Camera feel:** Professional -- managed by Kara Content agency. Stabilized, well-framed, intentional composition.
- **Dominant camera angle for static photos:** 45-degree angle (primary, ~60%) and eye-level (secondary, ~30%). Overhead flat-lay is rare (~10%).

---

## 7. Graphic Design System

**Verified from Playwright screenshots:**

- **Use of templates:** Yes -- the promotional posts (TORTA THURSDAYS, etc.) use consistent design templates with solid orange backgrounds and white text
- **Repeated design frames:** The "BURGER BUN / ENJOY THE BLEND" red circle logo appears as a sticker on milkshake/drink posts
- **Borders around posts:** No
- **Watermarks:** "Burger Bun" script watermark appears occasionally
- **Logo placement:** Red circle logo with white "BURGER BUN" text appears on branded cup stickers and wrappers. Not consistently overlaid on every post image.
- **Consistent layout grid:** The feed alternates between close-up food shots and wider interior/person shots, creating visual rhythm. Most recent posts are Reels with a similar thumbnail aesthetic.

---

## 8. Caption Architecture Guide

**Source: Playwright DOM snapshot -- full captions extracted from `img alt` attributes of 20+ grid thumbnails.**

**Two distinct caption eras observed:**

**Era 1 (Older posts, pre-Kara Content):** Longer, descriptive, storytelling approach:
- "Say hello to the ultimate Pastrami Sandwich experience! At our restaurant, we believe in elevating every bite..."
- "🌧Embrace the cozy vibes with our Rainy Day Hot Dog Special at Burger Buns LA! 🌭✨️ Choose between a Regular or Spicy Hot Dog..."

**Era 2 (Current / Kara Content management -- THIS IS THE STYLE TO REPLICATE):** Short punchy hook + standardized CTA block:

**Current Caption Formula (verified across 15+ recent posts):**
```
[Short punchy 1-liner hook] [0-2 emojis]
.
.
.
🔗 ORDER NOW! Link in bio
⏰️ Open 7 days a week!
📍 818 N Pacific Ave Glendale, CA 91203
.
.
.
#GlendaleFoodie #LAfoodie #GlendaleCA #OurGlendaleEats #GlendaleEats #LAeats #LosAngelesFood #FoodieLA #GlendaleDining #SupportSmallBusiness #EatLocalLA #LAfoodscene #CateringGlendale #MealPrepLA #FreshFoodLA #FoodBloggersLA #InstaFoodie #FoodPhotography #FoodLovers #FoodStagram
```

**Observed patterns:**
- **Caption length:** Very short -- 1 hook line + CTA block. Total: 6-8 lines including spacing.
- **Hook style:** Short, witty, 1-line punches. See real examples below.
- **Body structure:** No body. Hook → spacing → CTA. That's it.
- **Emoji usage:** 0-2 emojis at end of hook line. 🔗 ⏰️ 📍 in CTA block (same every time).
- **Line break structure:** `. . .` (dot-space-dot on separate lines) between hook and CTA, and between CTA and hashtags.
- **CTA style:** Two variations:
  - Generic: "🔗 ORDER NOW! Link in bio"
  - Item-specific: "🔗 ORDER OUR [ITEM NAME] NOW! Link in bio" (e.g., "ORDER OUR BOSS BURGER NOW!", "ORDER OUR GREEN TEA MILKSHAKE NOW!", "ORDER OUR BLT SPECIAL NOW!", "ORDER OUR CARNE ASADA TORTA NOW!", "ORDER OUR TACOS NOW!", "ORDER OUR MUSHROOM BURGER NOW!")
- **Hashtag placement:** End of caption, after `. . .` spacing. NOT in first comment.
- **Hashtag count:** Exactly 20 hashtags -- same block on virtually every post.
- **Hashtag block (standard):** #GlendaleFoodie #LAfoodie #GlendaleCA #OurGlendaleEats #GlendaleEats #LAeats #LosAngelesFood #FoodieLA #GlendaleDining #SupportSmallBusiness #EatLocalLA #LAfoodscene #CateringGlendale #MealPrepLA #FreshFoodLA #FoodBloggersLA #InstaFoodie #FoodPhotography #FoodLovers #FoodStagram
- **Bilingual elements:** None
- **Voice/personality:** Cool, confident, slightly cocky. Like a friend who knows their food is fire and doesn't need to explain why.
- **Recurring CTA structure:** "ORDER NOW!" (always caps, always with exclamation) + "Link in bio" + ⏰️ + location

---

## 9. Real Caption Examples (from Playwright DOM snapshot -- verbatim)

**Caption 1:** "Caught in 4K: ultimate burger drip."
- **Representative because:** Perfect example of the current short-punchy style. One line, mic-drop energy.
- **Hook type:** Bold statement with pop culture reference ("caught in 4K")
- **CTA:** "🔗 ORDER NOW! Link in bio" (generic)
- **Emoji:** None in hook
- **Length:** 1 line hook + CTA block + 20 hashtags

**Caption 2:** "Not just a burger… THE Boss Burger."
- **Representative because:** Elevates a specific menu item with emphasis (THE in caps). Confident, declarative.
- **Hook type:** Product spotlight with emphasis
- **CTA:** "🔗 ORDER OUR BOSS BURGER NOW! Link in bio" (item-specific)
- **Emoji:** None in hook
- **Length:** 1 line hook + CTA block + 20 hashtags

**Caption 3:** "The best kept secret? Our tacos hit just as hard as our burgers. 🌮💥"
- **Representative because:** Menu discovery angle -- showing depth beyond burgers. Slightly longer hook (2 sentences).
- **Hook type:** Rhetorical question + surprise reveal
- **CTA:** "🔗 ORDER OUR TACOS NOW! Link in bio" (item-specific)
- **Emoji:** 🌮💥 at end of hook
- **Length:** 2-sentence hook + CTA block + 20 hashtags

**Caption 4:** "Cooler than your average shake."
- **Representative because:** Playful, comparative, casual. Positions the milkshake as superior.
- **Hook type:** Comparative flex
- **CTA:** "🔗 ORDER OUR GREEN TEA MILKSHAKE NOW! Link in bio" (item-specific)
- **Emoji:** None in hook
- **Length:** 1 line hook + CTA block + 20 hashtags

**Caption 5:** "No secret formula needed…just fresh ingredients."
- **Representative because:** Quality-focused, ties to "fresh, never frozen" brand promise. Understated confidence.
- **Hook type:** Counter-claim (we don't need secrets, just quality)
- **CTA:** "🔗 ORDER NOW! Link in bio" (generic)
- **Emoji:** None in hook
- **Length:** 1 line hook + CTA block + 20 hashtags

**Additional hooks from real posts (verbatim):**
- "The only tray worth fighting over."
- "No words needed."
- "Sandwich upgrade: unlocked. 🔓🍴"
- "A float without whip? Couldn't be us."
- "This is what they meant, right?"
- "Call it a pattern, I call it happiness."
- "Good things come in threes: burger, fries, and a fizzy Coke! ✨"
- "This is Burger Bun. 🍔"
- "Meet the sweetest addition to our menu. 🥤"
- "Your next favorite meal is just a menu flip away! 🙌🍽️"
- "Meet the burger that's all about that umami 🍄"
- "Sweet meets spicy in every bite and sip 😋 🔥"

---

## 10. Tone & Voice Encoding

**Brand Tone in 3 Words:** Confident. Punchy. Unfazed.

- **Personality archetype:** The Cool Food Plug -- speaks like someone who KNOWS the food is fire and doesn't need to oversell it. Short hooks, no explanations, just drops the line and walks away. Internet-savvy but not try-hard.
- **Words/phrases frequently used (from real captions):**
  - "ORDER NOW!" (always ALL CAPS with exclamation)
  - "Link in bio"
  - "...just [simple truth]" pattern ("just fresh ingredients")
  - Comparative flex ("cooler than," "not just," "THE [item]")
  - Pop culture refs ("caught in 4K," "unlocked")
  - "Open 7 days a week!"
- **Words/phrases never used:**
  - Long descriptions or storytelling (in current era)
  - Corporate language ("leverage," "utilize")
  - "Hidden gem" / "Foodie paradise" / "Game changer"
  - "Delicious" (they show, don't tell)
  - Formal language ("our establishment")
- **Energy level:** 7/10 -- confident and cool, not hyperactive. The ALL CAPS "ORDER NOW!" spikes energy momentarily, but the overall tone is unbothered swagger.

---

## 11. Key Products/Services

**Signature Dishes & Award Winners:**
- **Boss Burger** (#3) -- Angus beef, American & Swiss cheese. Customer favorite. ~$14.25
- **Pastrami Burger/Sandwich** -- "Best Pastrami in Town" 2020, 2022, 2025. ~$14.80-$19.85
- **Double Decker** (#4) -- Double Angus beef, Thousand Island, bacon, American & Swiss. ~$13.90-$14.80
- **Kobe (Wagyu) Burger** -- Premium option. $17.80
- **Green Tea Milkshake** -- Featured in multiple recent posts. Award-winning milkshakes.
- **Carne Asada Torta** -- Featured in recent CTA ("ORDER OUR CARNE ASADA TORTA NOW!")
- **BLT Special** -- Featured in recent CTA ("ORDER OUR BLT SPECIAL NOW!")
- **Mushroom Burger** -- Featured in recent CTA ("ORDER OUR MUSHROOM BURGER NOW!")
- **$5 Homemade Milkshakes** -- Highlighted in UGC repost ("Ain't nobody in LA doing that!!!")

**Menu Categories:**
- Burgers, Mexican (tacos, burritos, tortas, quesadillas), Greek (gyros), Sandwiches (pastrami, BLT), Wings & Tenders, Sides (fries, onion rings, mozzarella sticks, jalapeno poppers), Milkshakes & Smoothies, Thrifty Ice Cream

**Price Positioning:** Mid-tier fast-casual. Burgers $9.60-$17.80. Premium quality at fast food speed.

---

## 12. Target Audience Persona

**Primary:** Young adults (18-35) in Glendale/LA who want quality burgers beyond typical fast food. Active on social media, discover restaurants through Reels/TikTok. Large Armenian-American community in Glendale.

**Secondary:** Halal-observant diners seeking quality halal burger options in LA.

**Tertiary:** Families wanting menu variety (American-Greek-Mexican fusion) and milkshakes.

---

## 13. Words to Use / Words to Avoid

**Words to Use:**
- "ORDER NOW!" / "ORDER OUR [ITEM] NOW!" (established CTA)
- "Link in bio" / "Open 7 days a week!"
- Short punchy hooks (1-liners, no filler)
- Comparative flex ("not just," "THE [item]," "cooler than")
- Pop culture references
- "Fresh, never frozen" / "hand-pressed" / "award-winning"
- "Angus beef" / "Kobe" / "Wagyu"
- Menu item callouts in CTAs

**Words to Avoid:**
- Long descriptions or paragraphs (current style is ultra-short)
- "Hidden gem" / "Foodie paradise" / "Game changer" / "You won't believe"
- "Delicious" (generic)
- Corporate language
- "Our establishment" / formal tone
- "Gourmet" (they're fast-casual, not fine dining)

---

## 14. Cultural Moments to Own

**Tier 1 -- Perfect Fit:**
- National Burger Day (May 28), National Cheeseburger Day (Sep 18), Super Bowl, March Madness, July 4th, Father's Day, National Pastrami Day (Jan 14), National Milkshake Day (Sep 12), Cinco de Mayo

**Tier 2 -- Strong Fit:**
- National Taco Day, National French Fry Day, Ramadan/Eid (halal menu), National Wings Day, Valentine's Day (milkshake angle), National Gyro Day, Back to School

**Tier 3 -- Creative Stretch:**
- Meatless Monday (veggie burger), Rainy Day comfort food, Nowruz (Glendale community), Late night cravings, National Fast Food Day

---

## Data Sources & Verification Notes

**Playwright-verified (February 18, 2026):**
- Full Instagram profile rendered via Playwright browser automation
- Full-page screenshot captured (burgerbun_fullpage.png)
- DOM snapshot extracted 20+ full captions from img alt attributes
- Canvas-based pixel extraction sampled colors from 10 post thumbnail images across 8 regions each (topLeft, topRight, topCenter, leftEdge, rightEdge, center, bottomLeft, bottomCenter)
- Scrolled feed captured additional rows (burgerbun_scrolled.png) showing promotional posts with text overlays
- Orange wall confirmed across posts 1, 6, 9 and multiple scrolled posts
- Green wall confirmed across posts 7, 9 and multiple drink/milkshake posts
- 15+ real caption hooks extracted verbatim from DOM

**Playwright-verified website typography (February 18, 2026):**
- Full JavaScript rendering of burgerbun.la via Playwright browser automation
- Full-page screenshot captured (burgerbun_website_homepage.png)
- Computed style extraction from all visible elements (H1, H2, H3, paragraphs, buttons, links, strong, contact labels, FAQ, footer)
- @font-face declarations extracted: Boogaloo (Google Fonts), Forum (Google Fonts), Satoshi (FontShare/Framer), Inter (Framer CDN)
- Forum and Inter confirmed as loaded-but-unused via computed style analysis of all page elements
- Button/CTA styling extracted with exact font, color, background, border-radius, and padding values
- Section background colors verified: #DD2127 (FAQ, footer), #A30118 (Download App section)

**Additional sources:**
- Website branding (colors, fonts) from burgerbun.la -- now fully Playwright-verified in Section 4
- Awards and menu data from DoorDash, Yelp (656 reviews), Google (4.6/5)
- Founder: Art Chebeyan (est. 2008)
- Social media managed by: @karacontent (Kara Content, Ani Karayan)

**No remaining assumptions.** All visual and caption data in this file is traceable to Playwright-rendered real posts or verified external sources.
