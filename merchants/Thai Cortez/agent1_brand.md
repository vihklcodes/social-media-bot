# Agent 1: Brand Replication Blueprint — Thai Cortez (@thai.cortez)

**Date:** 2026-02-23
**Source:** Playwright Instagram feed analysis + website typography extraction + pixel sampling

---

## 1. Brand Snapshot

Thai Cortez is an award-winning Thai restaurant in Cortez, Colorado, specializing in authentic Northern Thai cuisine. With only 19 posts and 64 followers, this is a small-but-passionate account with well-crafted content that punches above its weight. The feed is 100% food-focused — close-up Reels of signature dishes like Khao Soi, Drunken Noodles, Green Curry, and "Mimi's Special" weekly features. The brand identity centers on deep red and gold (traditional Thai colors), scratch-cooked authenticity, and a warm small-town hospitality. The account uses descriptive, educational captions with authentic Thai dish names (Gai Him Ma Parn, Nam Prik Ong, Khao Mun Gai) alongside English descriptions. Photography is casual iPhone-quality but well-composed — warm lighting, tight food close-ups on white plates with fresh herb garnishes.

---

## 2. Playwright-Verified Environment Color Table

| Element | Color Name | Hex Code | Source (Post # / Region) | Verified Across |
|---------|-----------|----------|--------------------------|-----------------|
| Curry golden/amber | Warm curry sauce color | #CB9848 | Post 2 leftEdge, Post 2 rightEdge | 4+ posts |
| Food warm golden | Saffron/golden stir-fry | #B1885B | Post 0 center | 3 posts |
| Deep golden-brown | Rich cooked brown | #BA8334 | Post 1 bottomLeft | 3 posts |
| Food warm brown | Grilled/stir-fried tone | #8D5A36 | Post 1 center | 4 posts |
| Deep red-brown | Chili/sauce accent | #9E4709 | Post 1 topCenter | 2 posts |
| Dark maroon (food) | Deep red sauce/meat | #5B1304 | Post 1 topLeft | 2 posts |
| Cream/beige plate edge | White plate highlight | #D3C1A3 | Post 2 topLeft | 4 posts |
| Warm beige surface | Table/surface | #D6B79B | Post 3 topLeft | 3 posts |
| Light warm cream | Plate/background | #CABCB3 | Post 11 topLeft | 3 posts |
| Dark warm brown (table) | Dark table surface | #34291F | Post 3 bottomCenter | 2 posts |
| Green (curry/herbs) | Thai curry green | #715A16 | Post 0 leftEdge | 2 posts |
| Fresh green (herbs) | Cilantro/basil green | #5E924E | Post 9 leftEdge | 2 posts |
| Brand dark red (website) | Header/logo red | #730101 | Website header | Throughout |
| Brand gold (website) | Nav/accent gold | #E7B103 | Website nav links | Throughout |
| Brand dark gold | Section heading gold | #826401 | Website H2 headings | Throughout |

**Note:** Thai Cortez food photos are dominated by warm golden/amber curry tones and cream/beige plate surfaces. The restaurant interior is not prominently visible in posts — most shots are tight food close-ups. The brand identity colors (deep red #730101 + gold #E7B103) from the website do NOT currently appear in Instagram posts but should be incorporated into promotional posters as the anchor brand palette.

---

## 3. Visual System Blueprint

**Overall Aesthetic Category:** Casual food-forward | Secondary: Educational/descriptive (authentic Thai dish names)

**Color Palette (observed):**
- **Dominant:** Warm golden/amber curry tones (#CB9848, #B1885B, #BA8334) — Thai curries and stir-fries
- **Accent (food):** Deep reds from chili/sauce (#9E4709, #5B1304), fresh greens from herbs (#5E924E)
- **Surfaces:** Cream/beige plate edges (#D3C1A3, #D6B79B), dark wood table (#34291F)
- **Brand colors (website, NOT yet on Instagram):** Deep maroon red #730101 + bright gold #E7B103
- **Feed color consistency:** Moderately consistent — warm-toned food on white/cream plates. No graphic design or branded templates.

**Image Composition Patterns (from 12 visible posts):**
- **Content mix:** 9/12 visible posts are Reels, 3/12 are photo carousels. Very heavy video content.
- **Camera angle breakdown:** ~70% 45-degree angle (dominant — looking down at plate from slight angle), ~20% overhead flat-lay, ~10% eye-level
- **Close-up vs. wide:** Tight close-ups dominate. Food fills 70-80% of the frame in most shots.
- **Centered vs. asymmetrical:** Mostly centered, with plate/bowl positioned center-frame.
- **Edge-cropping:** Minimal to moderate. Some plates are cropped at the edges (bowl not fully visible), but food itself is typically fully shown.
- **Negative space:** Low — plates fill the frame. Background is minimal.
- **People included:** Rarely (1 Halloween photo with people, 10/12 posts are food-only)
- **Surface/table details:** Dark wood table visible in edges of some shots. White round plates and white bowls are primary serving ware.
- **Plate/serving ware:** White round ceramic plates (most dishes), white bowls (soups/curries), dark wok/pan visible in Drunken Noodles shot

---

## 4. Website Typography System (PRIMARY font reference for Agent 3)

**Headline font:** `PT Serif` (serif family)
- Weight: 400 (regular)
- Case: ALL CAPS for site title and section headings ("THAI CORTEZ", "REVIEWS")
- Color: #826401 (dark gold/mustard) for H2 headings, #404040 (dark grey) for H1
- Size: 36px for site title, 18px for section headings
- Letter-spacing: 1px
- **Rendered appearance at display size (CRITICAL):** Classic, traditional serif with moderate thick-thin stroke contrast. At ALL CAPS with 1px letter-spacing, it reads as elegant, traditional, slightly formal — like a fine dining menu. Serifs are refined but not decorative. When rendered at 60-80px for poster headlines, it has a timeless, premium quality that suits the "authentic Thai" positioning. NOT blocky, NOT modern geometric — think traditional book typography.

**Body font:** `PT Serif` (same font as headlines)
- Weight: 400
- Case: Sentence case
- Color: #404040 (dark grey)
- Size: 16px

**CTA button style:**
- Background: Red (DoorDash widget default)
- Text: White
- Shape: Rounded pill ("Order Delivery" / "Order Pickup")
- Additional CTA: "Order Online" banner in dark red

**Nav link style:**
- Color: #E7B103 (bright golden yellow) on dark red header (#730101)
- Font: PT Serif, 18px, sentence case

**Typographic personality:** Single-font system (PT Serif throughout). Traditional serif conveys authenticity, heritage, and quality. The deep red + gold color scheme is quintessential Thai restaurant branding — regal, warm, traditional.

---

## 5. Text Overlay Specifications

**Text overlay frequency:** Sometimes (~40% of posts). Reels use text overlays for dish names and location tags.

**Text styles observed on Reels:**
- **Dish name overlay:** White text, medium weight, positioned center-bottom of frame. Examples: "Seafood Green Curry 🥣", "Gai Him Ma Parn ⭐", "#Fried Calamari", "#Tom Kha Soup", "#Mango Sticky Rice"
- **Location tag:** "📍THAI CORTEZ" in white text, always below the dish name
- **Hashtag-style labels:** "#Fried Calamari" — black text on beige/cream semi-transparent label background

**Text placement MAP:**
- Top: 0% (no text at top observed)
- Center-bottom: 70% of text-overlay posts (dish name + location)
- Bottom: 30% (hashtag labels)

**Text background treatment:**
- 60% NO treatment (white text directly on food, relying on video contrast)
- 30% Subtle semi-transparent cream/beige label behind hashtag text
- 10% Instagram native text tools
- No gradient overlays, no drop shadows

**Font in overlays:** Simple sans-serif (Instagram's native text tool), not matching website PT Serif

---

## 6. Photography & Editing Profile

**Lighting:** Warm, indoor restaurant lighting. Overhead warm-toned light that creates golden highlights on food. Slightly dim/moody ambiance — not bright and airy. Consistent warm color temperature across all food posts.

**Editing style:** Minimal editing. Warm-toned but not heavily filtered. Slight saturation boost on food colors — curries look rich golden, greens pop, reds are vibrant. Natural feel overall.

**Background/surface specifics:**
- **Surface:** Dark wood table, occasionally visible at edges (#34291F). Most of the frame is plate + food.
- **Plates:** White round ceramic plates and bowls — the primary "background" in most shots. Clean, simple presentation.
- **Props/context:** Fresh herb garnishes (cilantro, Thai basil, lime wedges, red chili) are consistent across posts. Occasionally visible: chopsticks, small sauce bowls.

**Camera feel:** iPhone casual. Not professional DSLR. Consistent quality across posts — someone (likely the owner/chef "Mimi") shoots all content in the same style.

**Dominant camera angle:** 45-degree for plated dishes (70%), overhead for spread/ingredient shots (20%)

---

## 7. Graphic Design System

- **Templates:** None. No branded templates or designed graphics observed.
- **Repeated design frames:** None
- **Borders/watermarks:** None
- **Logo placement:** Never in feed posts. Logo only in profile picture (red rooster/chicken silhouette with "Thai Cortez" script on cream background).
- **Consistent layout grid:** No — organic/casual feed. All food, no curated color grid.

---

## 8. Caption Architecture Guide

**Caption length:** Medium (3-6 lines + hashtags). Descriptive — each caption explains the dish in detail. Often includes price.

**Hook style:** Emoji + dish name with sparkle/flair. Examples:
- "✨ Khao Soi with Crispy Roasted Duck ✨"
- "🧡 Mimi's Special"
- "🌟 Ingredient Sunday 🌟"
- "It's cold outside ❄️"

**Body structure:** Descriptive food writing — names the dish with authentic Thai name, describes ingredients and flavors, sometimes includes price. Educational but not dry — enthusiastic and inviting.

**Emoji usage:** Moderate-to-heavy. Multiple emojis per post. Food-relevant emojis: 🍲 🔥 🐙 🍽️ ✨ 🥥 🍜 🦆 🧡 🌶️ 🥦 🍅 🇹🇭. Emojis appear at start of hooks, end of sentences, and between lines.

**Line break structure:** Double-spaced between hook and body. Single-spaced within body. Clean formatting.

**CTA style:** Soft — "Stop by Thai Cortez and treat yourself!" "Come warm up with a bowl of our Tom Kha." Not pushy. Invitation-style.

**Hashtag placement:** End of caption, separated by line break

**Hashtag count:** 6-14 per post. Mix: #ThaiCortez #CortezColorado #CortezCO #ThaiFood #TasteOfThailand #EatLocal + dish-specific tags

**Bilingual elements:** Yes — authentic Thai dish names in parentheses: "Gai Him Ma Parn (Thai Cashew Chicken)", "Khao Mun Gai", "Nam Prik Ong". This is educational and establishes authenticity.

**Voice/personality:** Warm, passionate, educational. Like a proud Thai mom sharing her cooking. Uses "our" language (possessive pride). Describes flavors vividly. Friendly small-town hospitality.

---

## 9. Real Caption Examples (from Playwright DOM snapshot)

**Caption 1:** "It's cold outside ❄️ Warm your day with our creamy, spicy Seafood Green Curry packed with shrimp, scallops, mussels, and squid. 🍲🔥 #ThaiCortez #SeafoodGreenCurry #GreenCurry #ThaiFood #CortezColorado"
- **Representative because:** Weather tie-in hook, detailed ingredient list, emoji-rich, location hashtag.
- **Hook:** Situational ("It's cold outside ❄️")
- **CTA:** Implicit (food description = CTA)
- **Emoji:** ❄️ 🍲 🔥
- **Length:** 3 lines + 5 hashtags

**Caption 2:** "✨ Khao Soi with Crispy Roasted Duck ✨ Dive into comfort with our Northern Thai classic with a twist! Familiar and rich Khao Soi Curry with Rice Noodles topped with Crispy Roasted Duck. Finished with crunchy noodles, red onions, and lime. $24.95 🥥🍜🦆 #ThaiCortez #KhaoSoi #RoastedDuck #DuckNoodles #ThaiCurry #NorthernThaiCuisine #CortezColorado #EatLocal #FoodieFiles #ThaiFoodLover #ComfortFood #CurrySeason #TasteOfThailand"
- **Representative because:** Sparkle frame hook, authentic dish name, detailed description, PRICE INCLUDED, Northern Thai positioning, 13 hashtags.
- **Hook:** ✨ Dish name ✨ (sparkle frame)
- **CTA:** None (description-focused)
- **Emoji:** ✨ 🥥 🍜 🦆

**Caption 3:** "🧡 Mimi's Special Northern Thailand's soul food on a plate 😋 Ground pork simmered with tomato, chili, and herbs. Served with rice noodles and broccoli $19.95 🍅🥦✨ #MimisSpecial #ThaiCortez #NamPrikOng #NorthernThaiFlavors #ThaiComfortFood #TasteOfThailand #EatThaiBeHappy"
- **Representative because:** "Mimi's Special" branded series, vivid food description, price, emoji-heavy.
- **Hook:** 🧡 Mimi's Special (series branding)
- **CTA:** None (description-focused)

**Caption 4:** "🌟 Ingredient Sunday 🌟 Sweet, tangy, and full of depth Tamarind brings that perfect balance of sour and sweet that makes Thai dishes pop. It is used in our Pad Thai and our house Tamarind Sauce 😋 #ThaiCortez #IngredientSunday #TamarindTwist #TasteOfThailand #CortezEats #ThaiFlavors #PadThaiLove #SweetAndTangy #AuthenticThai #EatLocalCortez #ThaiSauceMagic #SpiceAndSoul"
- **Representative because:** "Ingredient Sunday" educational series, teaches audience about Thai ingredients.
- **Hook:** 🌟 Ingredient Sunday 🌟 (series branding)
- **CTA:** None (educational)

**Caption 5:** "Mimi's Special 💫 Drunken Noodles with Seafood: Stir-fried ramen noodles tossed with shrimp, scallops, mussels, and squid — packed with veggies, Thai basil, and a punch of young black pepper. $24.95 🌶️🔥 A bold, seafood twist on our classic Drunken Noodles! #MimisSpecial #ThaiCortez #SeafoodDrunkenNoodles #TasteOfThailand #SpicyLover #thaifood"
- **Representative because:** Detailed ingredient description, price, flavor adjectives ("bold", "punch"), emphasis on signature preparation.

---

## 10. Tone & Voice Encoding

**Brand tone in 3 words:** Warm, Authentic, Educational

**Personality archetype:** The Proud Thai Mom — passionate about sharing authentic Northern Thai recipes, educates while inviting, speaks with pride about ingredients and traditions. Small-town warmth, big-city flavor ambition.

**Words/phrases frequently used:** "authentic," "comfort," "Northern Thai," "fresh," "Mimi's Special," "packed with," "our," "treat yourself," "soul food," ✨ sparkle framing
**Words/phrases never used:** "lit," "fire" (slang), "cheap," "fast food," "hidden gem," corporate language

**Energy level:** 7/10 — Warm and inviting with genuine enthusiasm about the food. Slightly more energetic than Chelo due to emoji usage and exclamation points.

---

## 11. Key Products/Services

**Signature dishes:**
- Khao Soi (Northern Thai curry noodle soup — with duck twist)
- Green Curry (seafood version with shrimp, scallops, mussels, squid)
- Drunken Noodles (pad kee mao — seafood version is "Mimi's Special")
- Gai Him Ma Parn (Thai Cashew Chicken)
- Tom Kha (coconut galangal soup)
- Pad Thai
- Nam Prik Ong (Northern Thai chili dip with pork)
- Khao Mun Gai (Thai chicken rice — "Mimi's Special")
- Mango Sticky Rice (dessert)
- Fried Calamari

**Recurring series:**
- "Mimi's Special" — weekly featured dish (appears to be a signature series)
- "Ingredient Sunday" — educational ingredient spotlight

**Services:**
- Dine-in (Cortez, Colorado location)
- Online ordering via DoorDash (both delivery and pickup)
- Seating for large groups (mentioned in reviews)

---

## 12. Target Audience Persona

**Primary:** Cortez/Montezuma County locals (25-55) looking for a quality restaurant alternative to fast food and American chains in a rural Colorado town. "Don't let the outside fool you" — travelers and locals discovering a gem.

**Secondary:** Mesa Verde National Park tourists stopping through Cortez for meals — road trippers, families on vacation, adventure travelers seeking authentic local food.

**Tertiary:** Thai food enthusiasts in the Four Corners region who appreciate authentic Northern Thai cuisine (rare in rural Colorado).

---

## 13. Words to Use / Words to Avoid

**Use:** authentic, Northern Thai, comfort, homemade, fresh, scratch-made, Mimi's, signature, Thai basil, curry, spicy, creamy, award-winning, Cortez, Colorado, tradition

**Avoid:** fast food, generic, cheap, basic, Americanized, fusion (unless Mimi specifically uses it), hidden gem, game changer, foodie paradise

---

## 14. Cultural Moments to Own

- **Songkran (Thai New Year, April 13-15)** — THE cultural moment for Thai restaurants
- **Loy Krathong (November)** — Thai festival of lights
- **National Thai Food Day** — natural tie-in
- **Lunar New Year** — broad Asian celebration, relevant
- **Winter/cold weather** — already leveraged ("It's cold outside ❄️") — huge for soup/curry promotion in mountain Colorado
- **Ski/snowboard season** — après-ski comfort food for travelers passing through Cortez area
- **Mesa Verde tourist season (spring/summer)** — drive tourist traffic
- **National Noodle Day / Curry Day** — specific food holidays
- **Spicy food challenges / National Hot & Spicy Day** — fits the brand's chili/spice identity
- **Small Business Saturday / Support Local** — small-town angle
