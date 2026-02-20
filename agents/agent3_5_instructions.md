# Agent 3.5: Photo Matcher

**Mission:** Scan the merchant's available food photos, match them to each occasion's hero food item from Agent 3's output, and write a photo-to-occasion mapping file that Agent 4 reads to optionally upload real photos alongside Nano Banana Pro generation prompts.

## Prerequisites

- Agent 3 must have already run for the target merchant -- `merchants/{Merchant Name}/agent3_content.md` must exist.
- At least one photo source folder must exist (see Photo Source Locations below).

---

## Photo Source Locations

Check these locations **in order**. Use the first one that exists and contains image files:

1. **Per-merchant folder (preferred):** `merchants/{Merchant Name}/photos/`
2. **Shared project library (fallback):** `Total New Images/`
3. **If neither exists** or both are empty: write all occasions as `NO_MATCH` and log: "No photo source folders found for {Merchant Name}. All occasions will use text-only generation."

If both locations exist, scan **both** and merge the inventories (per-merchant photos take priority over shared library when the same food category appears in both).

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

### Phase 2: Scan Available Photos

1. **Glob for all image files** in the photo source folder(s):
   ```
   Glob: {photo_source}/**/*.png
   Glob: {photo_source}/**/*.jpg
   Glob: {photo_source}/**/*.jpeg
   ```

2. **Build a photo inventory** organized by subfolder name. The subfolder structure is typically:
   ```
   {Category}/{Item Name}/{number}.png
   ```
   Example inventory:
   ```
   Platters/Platter Chicken/  → 25 photos (1.png through 30.png with gaps)
   Platters/Platter Falafel/  → 4 photos (1.png through 4.png)
   Mediterranean Fries/Shawarma Fries/ → 2 photos (9.png, 39.png)
   Mediterranean Fries/Badmash Fries/  → 1 photo (10.png)
   Chicken & Sandwich/Chicken Nuggets/ → 2 photos (14.png, 21.png)
   Chicken & Sandwich/Chicken Wings/   → 1 photo (44.png)
   Appetizer/Quesadilla/              → 1 photo (1.png)
   ```

3. **Log the inventory:** "{N} total photos found across {M} categories in {photo_source_path}."

---

### Phase 3: Match Occasions to Photos

For each occasion extracted in Phase 1:

#### Step 3a: Keyword Matching

Compare the occasion's `hero_food_keywords` against the photo inventory's subfolder names (the `{Item Name}` level). Use case-insensitive keyword overlap:

| Prompt Keywords | Matching Folder | Match Type |
|----------------|----------------|------------|
| "Combo Platter" + "chicken" | `Platter Chicken/` | **MATCH** (exact item) |
| "Falafel Wrap" | `Platter Falafel/` | **PARTIAL_MATCH** (same protein, different format -- platter vs wrap) |
| "Shawarma Fries" | `Shawarma Fries/` | **MATCH** (exact item) |
| "Chicken Wings" | `Chicken Wings/` | **MATCH** (exact item) |
| "Gyro Wrap" | (no gyro folder) | **NO_MATCH** |
| "Hummus bowl" | (no hummus folder) | **NO_MATCH** |

**Matching rules:**
- **MATCH**: The folder name directly corresponds to the menu item in the prompt (same food type AND presentation)
- **PARTIAL_MATCH**: The folder contains the same protein/food type but in a different format (platter vs wrap, fries vs bowl, etc.)
- **NO_MATCH**: No folder contains food related to the prompt's hero item
- **Do NOT match unrelated food types.** A chicken platter photo should never match a falafel occasion or vice versa.

#### Step 3b: Visual Selection (when a folder matches)

If a matching folder has **multiple photos**, visually inspect candidates to select the best one:

1. **Read 3-5 candidate images** using the Read tool (which can view images natively).
2. **Score each candidate** against the occasion's prompt requirements:
   - **Angle match** (highest priority): Does the photo's camera angle match what the prompt specifies? Overhead prompt → prefer overhead photo. 45-degree prompt → prefer 45-degree photo.
   - **Composition match**: Is the food centered? Is the full plate/platter visible? Is the framing clean?
   - **Quality**: Sharpness, lighting warmth, color saturation. Prefer bright, warm, high-saturation photos that match the brand's studio aesthetic.
   - **Background**: Photos with solid color backgrounds (especially red, warm tones) integrate more naturally into the poster gradient backgrounds.
3. **Select the single best photo** for this occasion.
4. If the folder has only 1 photo, use it (no comparison needed).

#### Step 3c: Record the Match

For each occasion, record:
- `match_status`: `MATCH`, `PARTIAL_MATCH`, or `NO_MATCH`
- `photo_path`: Absolute path to the selected photo file (or `None`)
- `rationale`: 1-2 sentences explaining the selection or why no match was found

---

### Phase 4: Write Output

Write the mapping file to `merchants/{Merchant Name}/agent3_5_photos.md`:

```markdown
# Agent 3.5: Photo Matches -- {Merchant Name}

**Date:** {today's date}
**Photo Source:** {path(s) scanned}
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
| No photo source folders exist | Write all occasions as NO_MATCH, log the issue |
| Photo folder exists but is empty | Same as above -- all NO_MATCH |
| Cannot read/view an image file | Skip that photo, try next candidate in folder |
| agent3_content.md has no parseable occasions | Stop and report parsing failure |

---

## File Output

**Reads:** `merchants/{Merchant Name}/agent3_content.md` + photo source folder(s)
**Writes:** `merchants/{Merchant Name}/agent3_5_photos.md`

---

## Important Notes

- **Do NOT modify `agent3_content.md`** -- it is read-only input.
- **Do NOT move, rename, or modify any photo files** -- read-only access to the photo library.
- **Agent 3.5 is optional.** If it has not been run, Agent 4 proceeds with text-only generation (backward compatible).
- **Re-running Agent 3.5** will overwrite the previous `agent3_5_photos.md`. This is expected if Agent 3 content changes or new photos are added.
- **Photo paths must be absolute** in the output file so Agent 4 can use them directly with `browser_file_upload`.
