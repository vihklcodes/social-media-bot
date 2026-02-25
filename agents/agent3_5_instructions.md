# Agent 3.5: Photo Matcher

**Mission:** Scan the merchant's available food photos, match them to each occasion's hero food item from Agent 3's output, and write a photo-to-occasion mapping file that Agent 4 reads to optionally upload real photos alongside Nano Banana Pro generation prompts.

## Prerequisites

- Agent 3 must have already run for the target merchant -- `merchants/{Merchant Name}/agent3_content.md` must exist.
- The merchant's **Business ID** must be available in the Google Sheet `1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28`, tab "Social Media", column C.

---

## Photo Source Locations

Check these locations **in priority order**:

1. **DoorDash Storefront (primary):** `https://order.online/business/{BUSINESS_ID}`
   - Uses the merchant's Business ID from the Google Sheet to navigate to their DoorDash online ordering page.
   - Scrapes all menu item food photos with their item names via Playwright.
   - This is the richest photo source — typically 50-100+ menu items with 1200x1200 CDN images.
   - See **Phase 2** below for the full scraping workflow.
2. **Per-merchant folder (backup):** `merchants/{Merchant Name}/photos/`
3. **Shared project library (backup):** `Total New Images/`
4. **If ALL sources are empty or unavailable:** write all occasions as `NO_MATCH` and log: "No photo sources found for {Merchant Name} (storefront scrape returned 0 images, no local folders). All occasions will use text-only generation."

Always start with the storefront scrape. If a specific occasion gets `NO_MATCH` from the storefront, check local folders as a backup before finalizing as `NO_MATCH`.

---

## Step-by-Step Workflow

### Phase 1: Parse Agent 3 Content

1. **Read** `merchants/{Merchant Name}/agent3_content.md`.

2. **Identify every occasion block.** Occasions follow the pattern:
   ```
   ## Occasion N: {Occasion Title}
   ```

3. **For each occasion, extract:**
   - `occasion_number` -- the number N from the heading (e.g., `1`, `2`, `13A`)
   - `occasion_title` -- the descriptive title after the colon
   - `food_description` -- the full text of the **"Food photography:"** line from the Nano Banana Pro prompt (blockquoted section under `### A.`). This describes the hero food item, camera angle, composition, and plating.
   - `hero_food_keywords` -- extract the specific menu item name(s) from the food description. Examples:
     - "45-degree angle hero shot of a loaded Combo Platter" → keywords: **Combo Platter, chicken**
     - "Falafel Wrap cut in half to reveal the cross-section" → keywords: **Falafel Wrap, falafel**
     - "a plate of golden Shawarma Fries" → keywords: **Shawarma Fries**
     - "Chicken Wings arranged on a plate" → keywords: **Chicken Wings**
   - `camera_angle` -- extract the specified angle from the food description: "overhead" / "45-degree" / "eye-level" / "flat lay"

4. **Build an ordered list** of `{occasion_number, occasion_title, food_description, hero_food_keywords, camera_angle}` entries.

5. **Log:** "Parsed {N} occasions from agent3_content.md for {Merchant Name}."

---

### Phase 2: Scrape Photos from DoorDash Storefront (Primary)

This is the primary photo source. Scrapes real food photos from the merchant's DoorDash online ordering page using Playwright.

#### Step 2.1: Navigate to the Storefront

1. Get the merchant's **Business ID** from column C of the Google Sheet (use `sheets_read` on `Social Media!C1:D14`, match on Business Name in column D).
2. Navigate to `https://order.online/business/{BUSINESS_ID}` using Playwright (`browser_navigate`).
3. The page will redirect to the actual store URL (e.g., `https://order.online/store/365067?pickup=true`). Wait 3 seconds for the page to fully render.

#### Step 2.2: Pull the Merchant Logo

Before scrolling, grab the merchant's logo from the top of the page. The logo is an `img` element with `alt="logo"` and a CDN URL containing `fit=contain`.

```javascript
async (page) => {
  await page.waitForTimeout(3000);
  const logo = await page.evaluate(() => {
    const img = document.querySelector('img[alt="logo"]');
    return img ? img.src : null;
  });
  return logo;
}
```

If found, record it as a special inventory entry: `{ name: "LOGO", src: "{logo_url}" }`. Download and save it to:
```
merchants/{Merchant Name}/reference_photos/logo.png
```

This logo file is always staged regardless of occasion matching — Agent 4 can use it whenever a Nano Banana Pro prompt calls for the merchant's logo on the poster.

#### Step 2.3: Scroll and Collect Menu Item Images

The storefront lazy-loads menu items as you scroll — items only render when their section enters the viewport. You **must scroll incrementally and collect images at each scroll position** to capture everything.

Use `browser_run_code` with the following approach:

```javascript
async (page) => {
  await page.waitForTimeout(3000);

  // Accumulate items as we scroll — Map prevents duplicates
  const allItems = new Map();

  const collectImages = async () => {
    const items = await page.evaluate(() => {
      const imgs = document.querySelectorAll('img');
      return Array.from(imgs)
        .filter(img => {
          const src = img.src || '';
          const alt = img.alt || '';
          return src.includes('cdn4dd') && alt && alt !== 'logo' && alt !== 'Loading' && alt !== '';
        })
        .map(img => ({ name: img.alt, src: img.src }));
    });
    for (const item of items) {
      if (!allItems.has(item.name)) {
        allItems.set(item.name, item.src);
      }
    }
  };

  // Collect at initial position
  await collectImages();

  // Scroll incrementally (400px steps, 600ms pause) and collect at each step
  const scrollHeight = await page.evaluate(() => document.body.scrollHeight);
  for (let y = 0; y <= scrollHeight; y += 400) {
    await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
    await page.waitForTimeout(600);
    await collectImages();
  }

  // Return as array of {name, src} objects
  return JSON.stringify(Array.from(allItems.entries()).map(([name, src]) => ({ name, src })));
}
```

#### Step 2.4: Build the Storefront Photo Inventory

The returned data is an array of `{name, src}` objects where:
- **`name`** = the menu item name from the `img` alt text (e.g., "Mofongo de Camarones", "Bistec sandwich", "Pernil")
- **`src`** = the CDN image URL (format: `https://img.cdn4dd.com/p/fit=cover,width=1200,height=1200,format=auto,quality=90/media/photosV2/{uuid}-retina-large.jpg`)

Build an inventory list organized by item name. The image URLs are 1200x1200 resolution — suitable for poster generation.

**Log:** "Storefront scrape for {Merchant Name} (Business ID: {ID}): {N} unique menu items with photos found."

#### Step 2.5: Download Matched Photos

For each occasion that gets a MATCH or PARTIAL_MATCH against the storefront inventory (Phase 3), download the matched image:

1. Use Playwright to navigate to the image URL directly, or use `browser_run_code` to fetch and save:
   ```javascript
   async (page) => {
     const response = await page.goto('{IMAGE_URL}');
     const buffer = await response.body();
     require('fs').writeFileSync('{SAVE_PATH}', buffer);
   }
   ```
2. Save to `merchants/{Merchant Name}/reference_photos/occasion_{N}_{food_slug}.jpg`

This is the primary path for staging photos into `reference_photos/`.

---

### Phase 2B: Scan Local Photo Folders (Backup)

Use this **only for occasions that got NO_MATCH from the storefront scrape.** Check if local folders have a photo that the storefront didn't.

1. **Glob for all image files** in the backup folder(s):
   ```
   Glob: merchants/{Merchant Name}/photos/**/*.png
   Glob: merchants/{Merchant Name}/photos/**/*.jpg
   Glob: Total New Images/**/*.png
   Glob: Total New Images/**/*.jpg
   ```

2. **Build a photo inventory** organized by subfolder name. The subfolder structure is typically:
   ```
   {Category}/{Item Name}/{number}.png
   ```

3. **Re-run Phase 3 matching** for any NO_MATCH occasions against this local inventory. If a match is found, upgrade it from NO_MATCH to MATCH or PARTIAL_MATCH.

4. If no local folders exist or they're empty, skip this phase entirely.

---

### Phase 3: Match Occasions to Photos

For each occasion extracted in Phase 1:

#### Step 3a: Keyword Matching

Compare the occasion's `hero_food_keywords` against the photo inventory. Match against the storefront inventory's `name` field (menu item alt text) first. For any NO_MATCH occasions that fall through to Phase 2B local folders, match against subfolder names (the `{Item Name}` level).

Use **case-insensitive keyword overlap** for both:

| Prompt Keywords | Inventory Item | Match Type |
|----------------|----------------|------------|
| "Combo Platter" + "chicken" | `Platter Chicken/` OR "Chicarron de pollo sin hueso" | **MATCH** (exact item) |
| "Falafel Wrap" | `Platter Falafel/` | **PARTIAL_MATCH** (same protein, different format -- platter vs wrap) |
| "Shawarma Fries" | `Shawarma Fries/` | **MATCH** (exact item) |
| "Mofongo" | "Mofongo de Camarones" or "Mofongo de Pollo" | **MATCH** (exact item — pick the variant closest to the prompt's description) |
| "Chicken Wings" | `Chicken Wings/` | **MATCH** (exact item) |
| "Pernil" | "Pernil" or "Pernil with Rice" | **MATCH** (exact item) |
| "Gyro Wrap" | (no match in inventory) | **NO_MATCH** |

**Matching rules:**
- **MATCH**: The inventory item directly corresponds to the menu item in the prompt (same food type AND presentation)
- **PARTIAL_MATCH**: The inventory item contains the same protein/food type but in a different format (platter vs wrap, fries vs bowl, "with rice" vs "with tostone", etc.)
- **NO_MATCH**: No inventory item contains food related to the prompt's hero item
- **Do NOT match unrelated food types.** A chicken platter photo should never match a falafel occasion or vice versa.
- **For storefront matches with multiple variants** (e.g., "Mofongo de Pollo", "Mofongo de Camarones", "Mofongo de Res"), pick the variant that best matches the prompt's specific description. If the prompt says "shrimp mofongo," match "Mofongo de Camarones."

#### Step 3b: Visual Selection (when a match is found)

**Storefront photos (primary):** Each menu item has exactly one photo (its CDN image). If multiple storefront items match the same occasion keyword (e.g., "Mofongo de Pollo" and "Mofongo de Camarones" both match "mofongo"), use Playwright to take a screenshot of each candidate item on the page, visually compare, and select the one that best matches the prompt's description.

**Local folder photos (backup, Phase 2B only):** If a matching folder has **multiple photos**, visually inspect candidates:

1. **Read 3-5 candidate images** using the Read tool (which can view images natively).
2. **Score each candidate** against the occasion's prompt requirements:
   - **Angle match** (highest priority): Does the photo's camera angle match what the prompt specifies?
   - **Composition match**: Is the food centered? Is the full plate/platter visible?
   - **Quality**: Sharpness, lighting warmth, color saturation.
   - **Background**: Solid color backgrounds integrate more naturally into poster gradients.
3. **Select the single best photo** for this occasion.

#### Step 3c: Record the Match

For each occasion, record:
- `match_status`: `MATCH`, `PARTIAL_MATCH`, or `NO_MATCH`
- `photo_path`: Absolute path to the selected photo file (or `None`)
- `rationale`: 1-2 sentences explaining the selection or why no match was found

---

### Phase 4: Stage Reference Photos for Agent 4

Copy each matched photo into a standardized folder so Agent 4 can always find them without re-running Agent 3.5:

1. **Create the folder:** `merchants/{Merchant Name}/reference_photos/`
   - If the folder already exists, **clear it first** (delete all files inside) to avoid stale photos from a previous run.
   - **Always stage the logo** (from Step 2.2) as `reference_photos/logo.png`, regardless of occasion matching. Agent 4 uses this whenever a Nano Banana Pro prompt includes the merchant's logo on the poster.

2. **For each occasion with a MATCH or PARTIAL_MATCH**, stage the photo into `reference_photos/` with a predictable occasion-based filename:
   ```
   reference_photos/occasion_{N}_{food_slug}.jpg
   ```
   - `{N}` = occasion number (e.g., `1`, `2`, `13a`)
   - `{food_slug}` = short slugified hero food name (lowercase, underscores, max 40 chars). Examples:
     - Fisherman's Platter → `fishermans_platter`
     - Pancake Breakfast → `pancake_breakfast`
     - Turkish Bacon Swiss → `turkey_bacon_swiss`
   - **Dual-hero occasions** (two photos): Use suffix `a` and `b`:
     ```
     occasion_6a_turkey_bacon_swiss.jpg
     occasion_6b_reuben.jpg
     ```
   - **Storefront source (typical):** Download the CDN image using Phase 2 Step 2.5 and save directly to `reference_photos/`.
   - **Local folder source (backup):** Copy the file. Preserve the original — do not move.

3. **For NO_MATCH occasions**, do not create a file. Agent 4 will detect the absence and use text-only generation.

4. **Log:** "Staged {count} reference photos to merchants/{Merchant Name}/reference_photos/."

---

### Phase 5: Write Output

Write the mapping file to `merchants/{Merchant Name}/agent3_5_photos.md`:

```markdown
# Agent 3.5: Photo Matches -- {Merchant Name}

**Date:** {today's date}
**Photo Source:** {path(s) scanned — e.g., "DoorDash Storefront (Business ID: 14600429)" or "merchants/La Cocina/photos/"}
**Logo:** {Saved to reference_photos/logo.png | Not found on storefront}
**Total Occasions:** {N}
**Matched:** {count} | **Partial:** {count} | **No Match:** {count}

---

## Occasion 1: {Occasion Title}
**Hero Food Item:** {extracted menu item name from prompt}
**Match Status:** MATCH
**Photo Path:** `/absolute/path/to/photo.png`
**Rationale:** Overhead chicken combo platter with rice, pita, hummus -- matches the "loaded Combo Platter" described in the prompt. Photo has warm lighting and red background that blends with brand gradient.

## Occasion 2: {Occasion Title}
**Hero Food Item:** {extracted menu item name}
**Match Status:** NO_MATCH
**Photo Path:** None
**Rationale:** No falafel wrap photos found. Closest available: Platter Falafel (shows falafel in a platter, not a wrap). Agent 4 should use text-only generation.

## Occasion 3: {Occasion Title}
**Hero Food Item:** {extracted menu item name}
**Match Status:** PARTIAL_MATCH
**Photo Path:** `/absolute/path/to/photo.png`
**Rationale:** Falafel platter photo available but prompt describes a falafel wrap. Same protein, different presentation. Photo may still improve the output as a food reference.
```

Log the summary: "Agent 3.5 complete for {Merchant Name}: {matched} matches, {partial} partial, {no_match} no match out of {total} occasions."

---

## Matching Guidelines

### Do Match
- Prompt says "Chicken Combo Platter" and folder is `Platter Chicken/` → **MATCH**
- Prompt says "Shawarma Fries loaded with toppings" and folder is `Shawarma Fries/` → **MATCH**
- Prompt says "falafel balls on a side plate" and folder is `Platter Falafel/` → **PARTIAL_MATCH** (falafel present but in platter format)

### Do NOT Match
- Prompt describes a chicken dish but only falafel photos available → **NO_MATCH**
- Prompt describes a drink/beverage but only food photos available → **NO_MATCH**
- Prompt describes a dessert but only savory food photos available → **NO_MATCH**

### Photo Selection Priority (when multiple candidates)
1. Camera angle matches prompt specification
2. Food is centered and fully visible in frame (not cropped at edges)
3. Warm lighting, high color saturation
4. Solid-color background (especially red/warm tones) over busy backgrounds
5. Clean plating with all components visible

---

## Error Handling

| Scenario | Action |
|----------|--------|
| `agent3_content.md` not found | Stop and tell user to run Agent 3 first |
| Storefront page fails to load or redirects to error | Log the error, fall back to local folders (Phase 2B). If no local folders either, write all as NO_MATCH |
| Storefront scrape returns 0 images | Log: "Storefront has no menu photos for Business ID {ID}." Write all occasions as NO_MATCH |
| Business ID not found in Google Sheet | Stop and ask user for the Business ID |
| Cannot read/view an image file | Skip that photo, try next candidate |
| Cannot download a storefront CDN image | Log the failed URL, mark that occasion as NO_MATCH |
| agent3_content.md has no parseable occasions | Stop and report parsing failure |

---

## File Output

**Reads:** `merchants/{Merchant Name}/agent3_content.md` + photo source folder(s) OR DoorDash storefront via Playwright
**Reads:** Google Sheet `1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28`, tab "Social Media" (for Business ID, column C)
**Writes:** `merchants/{Merchant Name}/agent3_5_photos.md`
**Writes:** Staged reference photos to `merchants/{Merchant Name}/reference_photos/`

---

## Important Notes

- **Do NOT modify `agent3_content.md`** -- it is read-only input.
- **Do NOT move, rename, or modify any photo files** -- read-only access to the photo library.
- **Agent 3.5 is required.** Always run Agent 3.5 before Agent 4. If Agent 3.5 has not been run, pause and run it before proceeding with image generation.
- **Re-running Agent 3.5** will overwrite the previous `agent3_5_photos.md` and re-stage `reference_photos/`. This is expected if Agent 3 content changes or new photos are added.
- **Photo paths must be absolute** in the output file so Agent 4 can use them directly with `browser_file_upload`.
- **The `reference_photos/` folder is the handoff to Agent 4.** Agent 4 reads from this folder directly — it does not need to parse `agent3_5_photos.md` to find photos. The mapping file is for human reference and debugging.
