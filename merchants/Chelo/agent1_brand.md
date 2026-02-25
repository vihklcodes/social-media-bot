# Agent 1: Brand Replication Blueprint — Chelo (@tasteofchelo)

**Date:** 2026-02-23
**Source:** Playwright Instagram feed analysis + website typography extraction + pixel sampling

---

## 1. Brand Snapshot

Chelo — "Taste of Persia" — is a Persian-Mediterranean fast-casual restaurant in Van Nuys, CA, led by Executive Chef Saeed Mastoory (30+ years culinary experience). The brand positions itself as premium-casual: scratch-made kabobs grilled per order, fresh pita bread spun in-house, and house-made sides like saffron pistachio ice cream and multiple hummus varieties. The Instagram feed (133 posts, 7,403 followers) is heavily catering-focused — about half the visible posts showcase wedding receptions, event spreads, and charcuterie boards. The visual identity balances elegant script branding (gold/bronze tones) with warm, abundant food photography. Halal-certified. The brand voice is proud, hospitable, and heritage-forward — "Bringing the heart of Persia to every plate."

---

## 2. Playwright-Verified Environment Color Table

| Element | Color Name | Hex Code | Source (Post # / Region) | Verified Across |
|---------|-----------|----------|--------------------------|-----------------|
| Food warm golden | Golden-brown (kabobs/grilled meat) | #D2A76C | Post 0 bottomCenter | 4+ posts |
| Food warm brown | Rich brown (grilled kabob surface) | #A86F5D | Post 0 center | 3 posts |
| Deep amber/saffron | Saffron-rice golden | #C79C54 | Post 4 leftEdge | 3 posts |
| Dark food brown | Deep roasted brown | #894C1C | Post 4 center | 2 posts |
| Warm orange-brown | Grilled meat accent | #BE5E0B | Post 4 bottomLeft | 2 posts |
| Light beige/cream | Tablecloth/surface | #CEBEA2 | Post 0 topRight | 3 posts |
| Warm earth beige | Table/platter surface | #B1A181 | Post 3 bottomLeft | 2 posts |
| Warm dusty rose | Food/environment mid-tone | #B38E74 | Post 5 center | 3 posts |
| Catering grey/silver | Graphic design background | #EEEFF1 | Post 2 topLeft, topCenter | 1 post (graphic) |
| Dark charcoal | Text/graphic dark tone | #3D3B38 | Post 2 bottomCenter | 1 post (graphic) |
| Twilight blue | Evening event sky | #24478B | Post 11 topLeft | 2 posts |
| Warm peachy-salmon | Food highlight | #DF986C | Post 9 topCenter | 2 posts |
| Soft blue-grey | Wedding/event ambiance | #BDC6D2 | Post 6 topCenter | 2 posts |
| Brand gold (website) | Logo/heading gold | #BD8644 | Website H1, H2, body text | Throughout website |
| CTA button orange | Order/Catering buttons | #FCB25A | Website CTA buttons | Throughout website |

**Note:** Chelo's Instagram feed is dominated by warm golden-brown food tones and neutral beige/cream surfaces. There is no single dominant wall color — most shots are either close-up food, catering spreads on white tablecloths, or outdoor event venues. The brand gold #BD8644 from the website is the anchor brand color.

---

## 3. Visual System Blueprint

**Overall Aesthetic Category:** Premium casual + Catering showcase | Secondary: UGC-heavy (influencer/food blogger reels)

**Color Palette (observed):**
- **Dominant:** Warm golds, amber, and browns from grilled kabobs and saffron rice (#D2A76C, #C79C54, #A86F5D)
- **Accent:** Brand gold/bronze #BD8644, CTA orange #FCB25A
- **Backgrounds:** White tablecloths for catering, cream/beige surfaces (#CEBEA2), occasional grey for graphics (#EEEFF1)
- **Evening events:** Twilight blue (#24478B), soft blue-grey (#BDC6D2)
- **Feed color consistency:** Moderately varied — food posts are warm-toned, event posts shift to blue/evening tones, graphics use grey/silver

**Image Composition Patterns (from 12 visible posts):**
- **Content mix:** 7/12 visible posts are Reels, 5/12 are photo carousels. Heavy video content.
- **Camera angle breakdown:** ~50% eye-level (event/catering shots), ~30% 45-degree (food close-ups), ~20% overhead (spreads)
- **Close-up vs. wide:** Mixed — food-focused posts are medium close-ups, catering posts are wide establishing shots
- **Centered vs. asymmetrical:** Mostly centered, especially for single-plate food shots. Catering spreads are wide/symmetrical.
- **Edge-cropping:** Minimal. Food is typically fully visible and centered. Chelo prefers showing the complete plate/platter presentation.
- **Negative space:** Low — frames are filled with food abundance. Catering spreads fill the entire frame.
- **People included:** Yes, ~30% of posts. Chef Saeed appears, influencers eating, wedding guests.
- **Surface/table details:** White tablecloths (catering), white ceramic plates (restaurant), stainless steel buffet trays (events)
- **Plate/serving ware:** White square plates with clean presentation, stainless steel chafing dishes for catering, wooden boards for charcuterie

---

## 4. Website Typography System (PRIMARY font reference for Agent 3)

**Headline font:** `belinda-w00-regular` (script/handwritten family)
- Weight: 400 (regular)
- Case: Mixed case (flows naturally, not ALL CAPS)
- Color: #BD8644 (warm gold/bronze)
- Size: 43px on website
- **Rendered appearance at display size (CRITICAL):** Flowing, elegant, connected cursive script with moderate thick-thin stroke contrast. Looks hand-lettered with a calligraphy pen — graceful loops on descenders, smooth flowing connections between letters. NOT blocky, NOT geometric. Think "elegant wedding invitation" script at large size. When rendered at 60-80px for poster headlines, it reads as premium, sophisticated, heritage-proud.

**Section heading font:** `dinneuzeitgroteskltw01-_812426` (DIN Neuzeit Grotesk, sans-serif)
- Weight: 400
- Case: ALL CAPS for section heads ("LOCATION & CONTACT", "OPENING HOURS", "ADDRESS")
- Color: #BD8644 (warm gold/bronze) or white on dark backgrounds
- Size: 45px on website
- **Rendered appearance:** Clean, geometric, modernist sans-serif with even stroke width. Tall letterforms with wide spacing. At ALL CAPS display size it reads as architectural, clean, European-modern. Good contrast to the script headline.

**Body/description font:** `Georgia, Palatino, "Book Antiqua", serif`
- Weight: 400
- Case: Sentence case
- Color: #BD8644 (warm gold/bronze) on light backgrounds
- Size: 15px body text

**CTA button style:**
- Background: #FCB25A (warm orange-gold)
- Text: Black (#000000)
- Shape: Pill/rounded (60px border-radius)
- Text: ALL CAPS ("ORDER ONLINE", "CALL NOW", "ORDER CATERING")

**Typographic personality:** Dual-font system — elegant script for brand identity/headlines paired with clean geometric sans-serif for functional text. This creates a premium-but-approachable feel that matches the "fast casual with chef-driven quality" positioning.

---

## 5. Text Overlay Specifications

**Text overlay frequency:** Sometimes (~25% of posts). Most posts are pure food/event photography. Text overlays appear mainly on:
- The "Chelo Catering" promotional graphic (Post 2): Elegant script "Chelo Catering" + serif "EVENTS. WEDDINGS. PARTIES & MORE. CONTACT US."
- Reel text overlays: Simple white text, casual placement

**Text placement MAP:**
- Top: 10% of text-overlay posts
- Center: 60% (especially the "Chelo Catering" graphic where text is centered)
- Bottom: 30% (Reel captions/subtitles)

**Text background treatment:**
- 80% NO treatment (text directly on image/video, relying on contrast)
- 20% Subtle natural contrast (light grey background on the Catering graphic)
- No gradient overlays, no drop shadows observed

**Font style in overlays:** Script (matching the Belinda website headline font) for brand-name overlays; simple white sans-serif for Reel caption text

---

## 6. Photography & Editing Profile

**Lighting:** Warm, natural-looking. Indoor restaurant shots use bright overhead lighting that casts warm tones on food. Catering/event shots range from warm indoor (golden chandeliers) to blue-hour outdoor evening lighting.

**Editing style:** Warm-toned, slightly saturated. Food colors are enhanced — saffron rice pops bright yellow, grilled meats look rich golden-brown. Not heavily filtered — natural feel with warm color grading.

**Background/surface specifics:**
- **Restaurant plates:** White square ceramic plates on neutral surfaces. Clean, minimal backgrounds.
- **Catering spreads:** White tablecloths (#FFFFFF or near-white), stainless steel chafing dishes, wooden charcuterie boards
- **Event venues:** Outdoor evening settings with string lights, black-and-white checkered dance floors, white chairs with gold accents

**Camera feel:** Mix of professional DSLR (catering/event photography) and iPhone-quality (Reels, casual food shots). ~60% iPhone casual, ~40% professional.

**Dominant camera angle for static photos:** 45-degree for single-plate food | Eye-level for catering spreads/events

---

## 7. Graphic Design System

- **Templates:** No consistent template. The "Chelo Catering" graphic (Post 2) is the closest to a branded template — grey/silver background, script font, serif subtext.
- **Repeated design frames:** None
- **Borders/watermarks:** None
- **Logo placement:** Rarely visible in feed posts. Logo appears in profile picture (circular mark with "CHELO TASTE OF PERSIA" and a musical instrument motif in gold on peach background).
- **Consistent layout grid:** No — feed is organic/varied

---

## 8. Caption Architecture Guide

**Caption length:** Short to medium. Most captions are 2-4 lines. Catering posts are shorter (1-2 lines + CTA). Food description posts are slightly longer.

**Hook style:** Statement-first, often using sparkle emoji. Examples:
- "Boards done right. Now catering ✨"
- "All I want for Christmas is food that hits ✨"
- "Bringing the heart of Persia to every plate"

**Body structure:** Direct and warm. Either a quick food description or a sentiment about heritage/quality. No storytelling paragraphs.

**Emoji usage:** Moderate. Sparkle ✨ is the signature emoji. Also uses 🍽️ (plate), 💐 (events), 📍 (location), 😍 (love). Emojis at end of sentences or as line-openers.

**Line break structure:** Single-spaced, short lines. No double-spacing. No bulleted lists.

**CTA style:** Direct and simple. "Contact us for catering inquiries." "Order now." Brief, not pushy.

**Hashtag placement:** End of caption, in the caption body (not first comment)

**Hashtag count:** 5-8 per post. Mix: #persianfood #iranianfood #persianrestaurant #LosAngeles #TasteOfChelo #CharcuterieBoard #EventCatering #authenticeats

**Voice/personality:** Proud, hospitable, heritage-first. Speaks like a proud chef sharing their craft. Not salesy. Not casual/slang. Warm but with quiet confidence.

---

## 9. Real Caption Examples (from Playwright DOM snapshot)

**Caption 1:** "Boards done right. Now catering ✨ @tasteofchelo #CharcuterieBoard #LosAngeles #TasteOfChelo #FoodReels #EventCatering"
- **Representative because:** Short, confident, CTA for catering. Uses ✨ signature emoji.
- **Hook:** Bold statement ("Boards done right.")
- **CTA:** Implicit (tagging for inquiries)
- **Emoji:** ✨ only — restrained
- **Length:** 1 line + hashtags

**Caption 2:** "As a picky eater, I'd never recommend it if I didn't actually love it 😍 The kabobs were perfectly marinated, and perfect sides to go with it! 📍 Chelo Restaurant #persianfood #iranianfood #persian #iran #invite"
- **Representative because:** UGC/influencer repost. Testimonial voice. Location pin. Persian-focused hashtags.
- **Hook:** First-person endorsement ("As a picky eater...")
- **CTA:** Location tag serves as CTA
- **Emoji:** 😍 📍 — minimal

**Caption 3:** "All I want for Christmas is food that hits ✨ Saffron lemon chicken + beef kabobs = holiday perfection 🎄🍽️. . . . . . . . . . #persianfood #foodstagram #cateringservice #authenticeats #merrychristmaseveryone"
- **Representative because:** Occasion tie-in (Christmas), specific menu items named, dot separators before hashtags.
- **Hook:** Pop culture reference + food
- **CTA:** None (engagement-focused)
- **Emoji:** ✨ 🎄 🍽️

**Caption 4:** "Bringing the heart of Persia to every plate — authentic flavors, made from scratch, just like home. 💫 Big thanks to @jtdacomic for stopping by and showing love. Always a pleasure serving real food to real foodies! 🍽️ #PersianCuisine #MadeFromScratch #AuthenticEats #TasteOfTradition #FoodieLove"
- **Representative because:** Heritage pride, community/influencer shoutout, key phrases ("heart of Persia," "made from scratch," "real food to real foodies").
- **Hook:** Heritage statement
- **CTA:** Implicit (community engagement)
- **Emoji:** 💫 🍽️

**Caption 5:** "The Details! We enjoyed catering this wonderful wedding & celebrating love. 💐 You give us a vision, and we make it come to life. 🍽️ Contact us to cater at your next event!"
- **Representative because:** Catering CTA pattern. Warm, service-oriented. Direct contact invitation.
- **Hook:** "The Details!" (excitement)
- **CTA:** "Contact us to cater at your next event!"

---

## 10. Tone & Voice Encoding

**Brand tone in 3 words:** Proud, Warm, Heritage-Driven

**Personality archetype:** The Proud Chef — shares their craft with quiet confidence, heritage pride, and genuine hospitality. Not flashy, not salesy. Lets the food and tradition speak.

**Words/phrases frequently used:** "heart of Persia," "authentic," "made from scratch," "catering," "fresh," "grilled," "real," sparkle ✨
**Words/phrases never used:** "lowkey," "no cap," "fire" (slang), "best kept secret," "hidden gem," "you won't believe"

**Energy level:** 6/10 — Warm and confident, not hyper. Sophisticated without being stiff.

---

## 11. Key Products/Services

**Signature dishes:**
- Kabobs (beef, chicken saffron lemon, koobideh) — grilled fresh per order
- Fresh pita bread — made in spinning oven in front of customers
- Saffron rice
- Hummus varieties (traditional, sundried tomato, avocado)
- Charcuterie/grazing boards (newer offering, heavily promoted)

**Specialty items (scratch-made):**
- Persian saffron pistachio ice cream
- Saffron rice pudding (Sholeh Zard)
- Shirazi salad
- Yogurt sauces (Mast Khiar, Mast Moosir)
- Persian drinks: Doogh, cucumber lemonade, saffron drink

**Services:**
- Dine-in (counter-service, Van Nuys location)
- Catering (weddings, corporate, events — on-site grilling, bartenders, servers)
- Online ordering via DoorDash/Clover
- Gift cards

---

## 12. Target Audience Persona

**Primary:** Persian/Iranian-American community in LA (30-55), seeking authentic home-style Persian food + catering for cultural events (Nowruz, weddings, family gatherings)

**Secondary:** LA food enthusiasts (25-40), attracted by "authentic eats" positioning, follow food bloggers, try diverse cuisines

**Tertiary:** Corporate/event planners looking for unique catering options in the San Fernando Valley area

---

## 13. Words to Use / Words to Avoid

**Use:** authentic, fresh, grilled, scratch-made, Persian, Mediterranean, saffron, kabob, tradition, heritage, craft, family, celebrate, catering, from our kitchen to your table

**Avoid:** cheap, deal, discount (conflicts with premium positioning), fast food, generic terms like "yummy" or "delish," slang, hidden gem, foodie paradise, game changer

---

## 14. Cultural Moments to Own

- **Nowruz (Persian New Year, ~Mar 20)** — THE cultural moment for their core audience
- **Eid celebrations** — halal-certified, resonates with broader Middle Eastern/Muslim community
- **Yalda Night (Dec 21)** — Persian winter solstice celebration
- **Wedding season (spring/summer)** — massive catering opportunity, already heavily promoted
- **National Kebab Day / food holidays** — natural fit for their hero product
- **LA food/cultural festivals** — community presence
- **Lent (if applicable)** — seafood options for observant customers
- **International Women's Day** — celebrating the women in the kitchen
- **Super Bowl / game day** — catering platters and group orders
