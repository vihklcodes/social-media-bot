# Agent 1: Brand Replication Blueprint — Shamrocks Ale House

**Date:** 2026-02-25
**Business ID:** 80215
**Instagram:** @shamrocksalehouse
**Website:** shamrocksalehouse.com (DoorDash Online Ordering storefront)
**Location:** 7805 Temple Terrace Hwy, Tampa, FL 33637

---

## 1. Brand Snapshot

Shamrocks Ale House is a neighborhood sports bar and ale house in Temple Terrace, Florida, serving classic American pub fare — wings, burgers, fish and chips, shepherd's pie — alongside cold draft beers and specialty cocktails. The brand identity is rooted in Irish-American pub culture with a strong sports-bar lean (Tampa Bay Lightning, Bucs, college football). The vibe is casual, unpretentious, and community-driven — a regular's bar where everyone knows your name. Their tagline is "Where Every Sip Tells a Story" and their branding emphasizes "Great Food · Great Sports · Great Fun." The Instagram presence is low-frequency (122 posts over 5+ years) with minimal production value — this is a bar that communicates through short announcements, not polished content.

---

## 2. Playwright-Verified Environment Color Table

| Element | Color Name | Hex Code | Source (Post # / Region) | Verified Across |
|---------|-----------|----------|--------------------------|-----------------|
| Interior walls (dark) | Dark maroon/red | #481414 | Post 1 (football) topLeft, leftEdge, bottomLeft | 3 regions in 1 post |
| Interior accent (dark green) | Dark forest green | #2D4339 | Post 1 topRight; Post 9 (beer taps) leftEdge #323D33 | 2 posts |
| Brand green (logo/website) | Shamrock dark green | #004225 | Website header, buttons — Playwright CSS extraction | Throughout website |
| Bar counter/wood surface | Warm dark brown | #3B2815 | Post 4 (cocktail) bottomCenter; Post 3 (cocktail) bottomCenter #1D1811 | 2 posts |
| Bar lighting ambience | Dark moody warm | #261A0F | Post 4 bottomLeft | Multiple posts |
| Specials flyer background | Near-black charcoal | #121318 | Post 6 (specials) topLeft, topRight, leftEdge, rightEdge, bottomLeft | 5 regions — verified |
| Specials flyer text area | Warm cream/beige | #E2D5D2 | Post 6 center | 1 post (designed flyer) |
| Cocktail/drink warm tone | Warm peach/amber | #B29477 | Post 3 (cocktail) center; Post 4 center #A26F53 | 2 posts |
| Tampa Bay Lightning blue | Bold blue | #192F9E | Post 7 (Lightning) topLeft through bottomCenter | Verified across 8 regions |
| Neon purple (karaoke) | Deep purple/violet | #6B2B8A | Post 2 (karaoke) center | 1 post — event-specific |
| Profile picture green | Olive/shamrock green | #5E6547 | Profile pic center; branding post #5E6446 center | 2 images |
| White (text/accents) | Clean white | #FFFFFF | Profile pic corners; branding post corners | Multiple |

**Note:** The interior is DARK — dark maroon/red walls, dark wood surfaces, low warm lighting. This is a classic dimly-lit sports bar interior, not a bright restaurant. Most food/drink photos have a warm, dark, moody ambient quality from the bar lighting. The brand green (#004225) appears on the logo, website, and signage but is NOT the dominant wall color — the walls lean dark red/maroon.

---

## 3. Visual System Blueprint

**Primary aesthetic:** Dark & moody sports bar
**Secondary aesthetic:** UGC-heavy / iPhone casual

- **Feed consistency:** Very inconsistent. No cohesive color theme, no grid planning, no visual templates. Posts include cocktail close-ups, neon signs, sports team graphics, specials flyers, beer tap photos, food photos, and community/memorial posts — all with different visual treatments.
- **Color palette:** The feed reads dark overall — lots of deep reds, dark greens, browns, and blacks from the bar interior. Bright pops come from neon lighting (purple/blue karaoke sign), sports team colors (Lightning blue, Bucs red), and cocktail colors (peach/amber drinks).
- **Feed is NOT color-consistent.** Each post has a different dominant color based on subject matter. There is no curated aesthetic.
- **Background style:** Natural background (bar interior) in most shots. The specials flyer uses a solid dark charcoal background. Sports posts use team-branded graphics.

---

## 4. Website Typography System

**IMPORTANT NOTE:** The website is a **DoorDash Online Ordering (DDOO) storefront template**, NOT a custom-designed merchant website. All typography is DoorDash's system fonts, not the merchant's own brand fonts.

| Element | Font Family | Size | Weight | Color | Case |
|---------|-----------|------|--------|-------|------|
| H1 (Hero headline) | DD Norms (sans-serif) | 60px | 700 (Bold) | rgb(25, 25, 25) #191919 | Sentence case |
| H2 (Section headers) | DD Norms | 32px | 700 (Bold) | rgb(25, 25, 25) #191919 | ALL CAPS (manually) |
| Body text | DD Norms | 16px | 500 (Medium) | rgb(25, 25, 25) #191919 | Sentence case |
| CTA buttons | DD Norms | 16px | 400 | White #FFFFFF on green #004225 | Sentence case |
| Button style | Pill-shaped (border-radius: 9999px) | — | — | Green bg #004225, white text | — |

**Since the website is a DDOO template, Agent 3 should NOT use DD Norms.** Instead, derive font direction from:
- The **Shamrocks logo** uses a bold, blocky serif/slab font with an Irish character — heavy, traditional, pub-style lettering
- The **specials flyer** (Post 6) uses bold, condensed uppercase text for the "SHAMROCK'S ALE HOUSE" header and price callouts
- **Recommended font direction for Agent 3:** Bold, heavy, pub-style serif or slab-serif for headlines (think Playfair Display Bold, Bitter Bold, or a heavy Irish-pub style). Clean sans-serif for body/prices (Roboto, Open Sans). This matches the logo's traditional pub character.

**Rendered appearance at display size:** The logo text is THICK, heavy-stroked, blocky serif with tight letter spacing — it reads as sturdy, traditional, masculine. At 60-80px it would appear as chunky, high-contrast serif letterforms with minimal decorative flourish.

---

## 5. Text Overlay Specifications

**Does the brand use text on images?** Sometimes (~25% of posts)

**Posts with text overlays observed:**
1. **Post 1 (football):** Team name graphics — "INDIANA HOOSIERS" / "MIAMI HURRICANES" — white text, sports broadcast style, centered
2. **Post 2 (karaoke):** Neon sign design — "Karaoke NIGHT" — stylized neon font, centered, purple/blue glow
3. **Post 6 (specials flyer):** Dense promotional flyer — "SHAMROCK'S ALE HOUSE - LIMITED TIME ONLY SPECIALS" — bold white/cream text on dark charcoal background, multiple font sizes for hierarchy (header, item names, prices)
4. **Post 12 (branding):** "Great Food · Great Sports · Great Fun / SHAMROCK'S ALE HOUSE" — circular text arrangement around logo, green and gold on white

**Text placement map:**
- 50% of text-overlay posts: Text CENTERED on image (karaoke, branding)
- 25% of text-overlay posts: Text spanning FULL image (specials flyer — text everywhere)
- 25% of text-overlay posts: Text integrated into graphic (football game info)
- **NO consistent "bottom third" or "top banner" pattern**

**Text background treatment map:**
- 50%: Solid color background behind text (specials flyer on charcoal, branding on white)
- 25%: No treatment — neon sign is the text itself
- 25%: Sports graphic template with built-in text areas

**Font style in overlays:** Bold, uppercase, condensed — no script, no thin, no decorative. The specials flyer uses a bold sans-serif for item names and a bolder condensed for the header.

**Text color:** White or cream on dark backgrounds. Green and gold on the branding post.

---

## 6. Photography & Editing Profile

**Lighting:** Dark, warm, ambient bar lighting. Most photos have a yellow/amber cast from interior bar lighting. No natural light, no studio lighting. The cocktail photos (Posts 3, 4) show warm backbar lighting with soft bokeh. The beer tap photo (Post 9) shows dark, moody lighting with the taps illuminated.

**Editing style:** Minimal to none. Photos appear unedited — straight from iPhone camera. No filters, no color grading, no cropping adjustments. Some photos are slightly underexposed due to dark bar environment.

**Background/surface specifics (Playwright-verified):**
- **Surface:** Dark wood bar counter — warm brown tones #3B2815 to #1D1811. Visible in cocktail photos where drinks sit on the bar.
- **Background walls:** Dark maroon/red walls #481414 visible behind the bar area. Dark green accents #2D4339 also present.
- **Visible props/context:** Beer taps (PBR, Guinness, Coors — Post 9), neon signs, TVs in background, bar stools, condiments, cocktail garnishes (lime, cherry, straw)
- **Serving ware:** Standard barware — pint glasses, cocktail glasses with straws, standard pub plates. No branded serving ware visible.

**Camera feel:** 100% iPhone casual. No professional photography whatsoever.

**Dominant camera angle for static photos:**
- Cocktails: ~45-degree angle, close-up with blurred bar background (~30%)
- Straight-on for signs, taps, and specials flyers (~40%)
- Eye-level for food items (~20%)
- No overhead/flat-lay shots observed (~0%)
- No food fully isolated — always contextual with bar environment visible

**Edge-cropping:** Minimal. Most subjects are centered in frame. Cocktails are typically centered with bar background filling the edges. No intentional dynamic framing or edge-cropping observed.

---

## 7. Graphic Design System

- **Use of templates?** No consistent templates. The specials flyer (Post 6) appears to be a one-off design, not a recurring template.
- **Repeated design frames?** No
- **Borders around posts?** No
- **Watermarks?** No
- **Logo placement:** The Shamrocks logo (green shield with shamrock and "SHAMROCK'S ALE HOUSE" text) appears in the profile picture and the branding post. It is NOT overlaid on regular posts.
- **Consistent layout grid?** No grid planning whatsoever. The feed has no visual cohesion.

---

## 8. Caption Architecture Guide

**Caption length:** Very short — 1-2 sentences, typically 15-40 words. The longest caption observed is the Super Bowl post at ~35 words. No multi-paragraph captions, no storytelling.

**Hook style:** Direct announcement opener. The most common pattern is "Join us..." (4 out of 12 posts). Other openers: "Beat the heat...", "Check our...", "We now have...", "Come join us..."

**Body structure:** Single run-on announcement. No line breaks, no bullet points, no emoji separation. Combines the what (event/special), when (date/time), and price in one sentence.

**Emoji usage:** ZERO. Not a single emoji observed in any of the 12 analyzed captions. This is a deliberate (or default) choice — the brand communicates purely through plain text.

**Line break structure:** No line breaks. Everything is a single block of text.

**CTA style:** Implicit — the "Join us" opener IS the CTA. No "Order now," "Link in bio," or "Comment below." The closest to an explicit CTA is "Large parties, please make reservations prior to Sunday."

**Hashtag placement:** NO hashtags observed in any caption. Zero hashtag strategy.

**Bilingual elements:** None.

**Voice/personality in captions:** Sounds like the bartender or owner writing a quick announcement — no-frills, matter-of-fact, friendly but not performative. Zero marketing polish. The tone is "hey, here's what's happening tonight."

**Recurring phrases/patterns:**
- "Join us" — appears in 4/12 posts (33%)
- Price callouts with specific dollar amounts ($6.49, $14.99, $19.99, $2.99, 94¢, 99cent)
- Event + time + deal structure: "[Event] at [time]. Enjoy [deal] from [time] to close."
- "Dine-in only" qualifier
- References to specific days/dates rather than general timeframes

---

## 9. Real Caption Examples

### Caption 1: Game Night Wing Special
> "Join us tonight for the Miami @ Indiana at 7:30 PM. Enjoy 94¢ bone-in wings from 6:30 PM to close!"
- **Representative because:** Classic Shamrocks formula — sports event + time + wing deal + time window
- **Hook:** "Join us tonight" — direct, time-sensitive
- **CTA:** Implicit invitation
- **Emoji:** None
- **Length:** 1 sentence, 24 words
- **Tone:** Bartender announcing tonight's deal

### Caption 2: Summer Cocktail Feature
> "Beat the heat and enjoy a refreshing summer specialty cocktail. Today , we have fresh hand crafted Old Man by the Sea for $6.49"
- **Representative because:** Product feature with price — simple, descriptive, price-forward
- **Hook:** "Beat the heat" — seasonal hook
- **CTA:** None — just states the product and price
- **Emoji:** None
- **Length:** 2 sentences, 26 words
- **Tone:** Friendly bartender recommendation

### Caption 3: Super Bowl Party
> "Join Shamrock's Superb Owl Party this Sunday, February 9th. Enjoy 99cent wings, bone-in, boneless fried, or grilled 6pm to close. (Dine-in only) Large parties, please make reservations prior to Sunday."
- **Representative because:** The LONGEST caption in the sample — still only 3 sentences. Shows their "big event" format with multiple details crammed into short text.
- **Hook:** "Join Shamrock's Superb Owl Party" — playful name twist ("Superb Owl" vs Super Bowl)
- **CTA:** "please make reservations" — the only direct CTA observed
- **Emoji:** None
- **Length:** 3 sentences, 35 words
- **Tone:** Slightly playful with the "Superb Owl" pun, but still matter-of-fact

### Caption 4: Thanksgiving Dinner
> "Come join us at Shamrock's Ale House noon to midnight Thanksgiving Day. Try our $14.99 Full Turkey Dinner and finish with a slice of Pumpkin Pie for $3.99. If you've had enough of the festivities or need some time away stop in for a drink."
- **Representative because:** Shows the "holiday event" format and reveals the brand personality — they position themselves as a refuge ("need some time away"), acknowledging their audience isn't looking for a fancy holiday dinner but a chill alternative.
- **Hook:** "Come join us" — warm invitation
- **CTA:** Implicit
- **Emoji:** None
- **Length:** 3 sentences, 48 words (longest observed)
- **Tone:** Understanding, empathetic — "we get it, holidays are a lot"

### Caption 5: Daily Beer Special
> "We now have $2.99 PBR all day, everyday. Join us for a pint."
- **Representative because:** The most minimal caption — just a price point and an invitation. This is their default voice at its purest.
- **Hook:** Price-first ("$2.99 PBR")
- **CTA:** "Join us for a pint" — simple invitation
- **Emoji:** None
- **Length:** 2 sentences, 14 words
- **Tone:** Straight to the point. No sell, just info.

---

## 10. Tone & Voice Encoding

**Brand tone in 3 words:** Neighborly, No-Frills, Sports-Focused

**Personality archetype:** The Regular's Bartender — knows your name, tells you what's on special tonight, doesn't waste your time with marketing speak. A local institution, not a brand.

**Words/phrases frequently used (from real captions):**
- "Join us" (33% of posts)
- "Enjoy" (appears in multiple posts)
- Specific prices ($6.49, $2.99, 94¢, $14.99)
- Specific times (7:30 PM, 6:30 PM, 6pm to close, noon to midnight)
- Team/game references (Lightning, Panthers, Miami, Indiana)

**Words/phrases NEVER used:**
- No emojis — ever
- No hashtags — ever
- No "link in bio," "order now," "tag a friend"
- No "delicious," "amazing," "incredible," "must-try"
- No marketing buzzwords whatsoever
- No "foodie" language

**Energy level:** 3/10 — calm, low-key, matter-of-fact. Zero hype energy.

---

## 11. Key Products/Services

**Signature dishes (from website + Instagram + reviews):**
1. **Bone-In Wings** — The #1 featured item. Multiple wing promotions (94¢ wings, 99¢ wings, All You Can Eat $19.99). Choice of sauces: BBQ, cajun, ranch, General Tso's, citrus, honey, heat levels, plain, teriyaki, South of the Border
2. **Sweeney's Shepherd's Pie** — Freshly oven-baked, beef with mixed vegetables, topped with mashed potatoes and cheddar jack cheese
3. **Flanagans Fish and Chips** — Beer-battered white fish with fries and homemade coleslaw. Praised as "best in Tampa" by Yelp reviewers
4. **Loaded Potato Skins** — Idaho potato skins with smoked bacon and cheddar jack cheese, topped with scallions
5. **Specialty Cocktails** — Rotating seasonal cocktails ($6.49 — Palomas, Old Man by the Sea)
6. **$2.99 PBR Draft** — All day, everyday. Also carry Guinness, Coors, Outlaw Draft

**Price positioning:** Budget-friendly / mid-tier pub pricing. Wing specials under $1, entrees $10-$20, cocktails ~$6.50, draft beers ~$3.

### Daily Specials (IN-HOUSE ONLY — Do NOT feature in online ordering campaigns)
| Day | Special | Price | Notes |
|-----|---------|-------|-------|
| Monday | Quarter Pounder Burger w/ Cheese, crispy onions, fries | $8.99 | In-house only |
| Tuesday | Spaghetti with Meat Sauce | $9.99 | In-house only |
| Tuesday | Euchre Night | — | Starts 6:30 PM |
| Wednesday | 94¢ Wings (bone-in & boneless) | $0.94 | In-house only |
| Wednesday | Trivia Night | — | 8 PM, $80 prizes, FREE to play |
| Thursday | Shepherd's Pie Night (beef or chicken) | $10.99 | In-house only |
| Friday | BBQ Pork Friday (potato, quesadilla, platter, sandwich) | varies | In-house only |
| Friday | Live Music | — | 1st & 3rd Friday, 6 PM |
| Friday | Karaoke Night | — | 2nd & 4th Friday, 9 PM |
| Saturday | All You Can Eat Wings (bone-in & boneless) + sides | — | Noon-9 PM |
| Sunday | Schnitzel and 1 side | $12.99 | Dine-in only |

### Popular Menu Items (Available for Online Ordering Campaigns)
**Starters:** Quinn's Quesadilla
**Salads:** Buffalo Chicken Salad, Bacon Cheeseburger Salad (no carb salad)
**Wings:** 10 Jumbo Wings
**Sandwiches:** Willy Cheese Steak, Irish Cuban, Pork Roll Sandwich
**Wraps:** Buffalo Chicken Wrap, Buffalo Cauliflower Wrap (vegetarian option)
**Entrees:** Sweeney's Shepherd's Pie, Hans' Homemade Schnitzel, Flanagan's Fish N Chips
**Burgers:** Bacon Cheeseburger, Double/Triple Cheeseburger
**Specialty Burgers:** Big Texas Burger, Buffalo Chicken Cheeseburger, Black & Bleu Burger, Bacon Lovers Burger

---

## 12. Target Audience Persona

**Primary:** Local regulars (30-60 years old) — Temple Terrace residents who come multiple times a week for drinks, wings, and sports. They know the staff by name. They care about value (94¢ wings) and convenience.

**Secondary:** Sports fans — People looking for a spot to watch Tampa Bay Lightning, Bucs, college football, Super Bowl. They want TVs, wings, and cold beer, not a fancy atmosphere.

**Tertiary:** Budget-conscious families/couples — People drawn by the hearty comfort food (shepherd's pie, fish and chips, turkey dinner) at affordable prices. Not "foodies" — people who want a solid, filling meal.

---

## 13. Words to Use / Words to Avoid

**USE:**
- "Join us" (their signature opener)
- Specific prices with cent symbols (94¢, $2.99, $6.49)
- Specific times and days
- "Bone-in wings," "cold pint," "draft"
- Local references: Temple Terrace, Tampa, Go Bolts
- "Tonight," "today," "this Sunday"
- "All day, everyday"
- "Dine-in only" when applicable

**AVOID:**
- Emojis (the brand never uses them — adding them would feel off-brand)
- Hashtags in captions (they've never used them — add only as first comment if needed for reach)
- "Link in bio," "tap to order," "swipe up"
- Performative enthusiasm ("OMG," "you NEED to try this," "insane flavor")
- Long-form storytelling (keep it to 1-3 sentences max)
- Marketing jargon ("limited time offer," "exclusive deal," "don't miss out")
- Fine dining language ("artisanal," "curated," "hand-selected")

---

## 14. Cultural Moments to Own

1. **NFL Season / Tampa Bay Bucs games** — Wing specials + game watch parties (confirmed from feed)
2. **NHL Season / Tampa Bay Lightning games** — Playoff watch parties (confirmed: Lightning @ Panthers post)
3. **College Football** — Game-day promotions (confirmed: Indiana vs Miami post)
4. **Super Bowl Sunday** — Their biggest promotional event (confirmed: "Superb Owl Party")
5. **St. Patrick's Day** — An absolute natural fit for "Shamrocks" — surprisingly NO St. Patrick's Day content found in feed. This is a massive untapped opportunity.
6. **Thanksgiving** — Alternative holiday gathering spot (confirmed: turkey dinner post)
7. **Karaoke Nights** — Entertainment events (confirmed from feed)
8. **National Wings Day / National Beer Day** — Natural product tie-ins
9. **March Madness** — College basketball tournament watch parties
10. **Summer cocktail season** — Rotating specialty cocktails (confirmed: Old Man by the Sea, Palomas)
11. **Fourth of July** — Patriotic holiday + summer BBQ vibes
12. **Fish Fry Fridays / Lenten Fridays** — Fish and chips promotion opportunity

---

## Post Frequency & Engagement Summary

| Metric | Value |
|--------|-------|
| Total posts | 122 |
| Posts in 2025-2026 | ~10 (extremely low frequency) |
| Average likes per post | 1-4 (very low engagement) |
| Highest engagement observed | 7 likes (hack apology post, 2021) |
| Comments | Near-zero across all posts |
| Posting frequency | ~1 post per month (very sporadic) |
| Last post date | January 19, 2026 |
| Content gap before that | December 26, 2025 (3+ weeks) |

**Key insight for Agent 3:** This account has EXTREMELY low engagement and posting frequency. The AI campaign represents a massive uplift opportunity — going from ~1 post/month to 3 posts/week will be transformative. The content style should respect the brand's no-frills personality while introducing more visual polish and engagement hooks that the current feed completely lacks. The challenge is making content feel authentically "Shamrocks" (plain-spoken, price-forward, sports-focused) while being Instagram-worthy enough to drive engagement.
