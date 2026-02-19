# Agent 4: Nano Banana Pro Image Generator (Playwright Automation)

**Mission:** Automate image generation by feeding Agent 3's Nano Banana Pro prompts into Google Gemini via Playwright, waiting for each image to render, downloading it, and saving it to `merchants/{Merchant Name}/final_images/` with occasion-based filenames.

## Prerequisites

- Agent 3 must have already run for the target merchant -- `merchants/{Merchant Name}/agent3_content.md` must exist.
- Playwright MCP server must be configured and running (see `.mcp.json`).
- The user must be signed into a Google account with Gemini access in the Playwright browser. Agent 4 will check for this and pause if sign-in is needed.

---

## Step-by-Step Playwright Workflow

### Phase 0: Parse Agent 3 Prompts

Before touching the browser, extract all Nano Banana Pro image prompts from `agent3_content.md`:

1. **Read** `merchants/{Merchant Name}/agent3_content.md`.
2. **Identify every occasion block.** Occasions follow the pattern:
   ```
   ## Occasion N: {Occasion Title}
   ```
   Each occasion contains a section headed `### A. Nano Banana Pro Image Generation Prompt` (or similar). The prompt is the blockquoted text (`> ...`) under that heading, ending before `### B.` (the Instagram Caption section).
3. **For each occasion, extract:**
   - `occasion_number` -- the number N from the heading (e.g., `1`, `2`, `13A`)
   - `occasion_title` -- the descriptive title after the colon (e.g., "Ramadan Begins + Ash Wednesday -- Dual Religious Observance")
   - `prompt_text` -- the full Nano Banana Pro prompt (all blockquoted lines under section A, stripped of `>` prefixes and markdown bold markers)
   - `filename_slug` -- a filesystem-safe slug derived from the occasion title: lowercase, spaces to underscores, strip special characters, max 80 chars. Example: `occasion_1_ramadan_begins_ash_wednesday.png`
4. **Build an ordered list** of `{occasion_number, occasion_title, prompt_text, filename_slug}` entries.
5. **Log the count:** "Found {N} Nano Banana Pro prompts for {Merchant Name}."

---

### Phase 1: Open Gemini & Authenticate

1. **Navigate to Gemini:**
   ```
   mcp__playwright__browser_navigate → https://gemini.google.com/app
   ```

2. **Wait for page load** (2-3 seconds), then take a snapshot:
   ```
   mcp__playwright__browser_snapshot
   ```

3. **Check authentication status.** Look for these signals in the DOM snapshot:
   - **Signed in:** User avatar/profile icon in the top-right corner, OR the chat input placeholder says "Ask Gemini" without a prominent "Sign in" button.
   - **Not signed in:** A "Sign in" button is visible in the top-right, OR the page redirected to `accounts.google.com`.

4. **If NOT signed in:**
   - Take a screenshot for the user:
     ```
     mcp__playwright__browser_take_screenshot → filename: "gemini_signin_required.png"
     ```
   - **STOP and ask the user** to sign in manually through the Playwright browser window. Say:
     > "Gemini requires Google sign-in. Please sign in through the Playwright browser window. I'll wait and continue once you're authenticated."
   - After the user confirms they've signed in, navigate back to `https://gemini.google.com/app` and re-verify.

5. **If signed in:** Proceed to Phase 2.

---

### Phase 2: Set Model to "Pro" (Nano Banana Pro)

Nano Banana Pro image generation requires the "Pro" model, not "Fast."

1. **Check the current model** in the DOM snapshot. The model selector is near the bottom-right of the chat input area. It displays either "Pro" or "Fast."

2. **If the model shows "Fast":**
   - Click the model selector dropdown:
     ```
     mcp__playwright__browser_click → element: the model selector button (shows "Fast" or "Pro" text near the send button)
     ```
   - Select "Pro" from the dropdown options:
     ```
     mcp__playwright__browser_click → element: the "Pro" option in the dropdown
     ```
   - Verify the selector now shows "Pro" by taking a snapshot.

3. **If already on "Pro":** Continue.

---

### Phase 3: Generate Images (Loop Per Occasion)

For each occasion prompt extracted in Phase 0, execute the following sequence:

#### Step 3a: Start a Fresh Chat

Before each prompt (except the first, which already starts fresh), open a new chat to avoid Gemini treating prompts as a conversation thread:

- Click the "New chat" button (pencil/compose icon in the left sidebar, or navigate fresh):
  ```
  mcp__playwright__browser_navigate → https://gemini.google.com/app
  ```
- Wait 2 seconds for the page to load:
  ```
  mcp__playwright__browser_wait_for → timeout: 2000
  ```

#### Step 3b: Enter the Prompt

1. **Click the chat input area** (the text field with placeholder "Ask Gemini 3" or similar):
   ```
   mcp__playwright__browser_click → element: the main chat textarea/input
   ```

2. **Type the full prompt.** Because prompts are long (500-2000+ characters), use `browser_fill_form` for reliability instead of `browser_type`:
   ```
   mcp__playwright__browser_fill_form → values: [{selector: the chat textarea, value: "{full prompt text}"}]
   ```
   **IMPORTANT:** Before pasting the prompt, prepend this instruction line to ensure the correct output dimensions:
   ```
   Generate a 1030 x 1350 px Instagram poster, portrait orientation. This is a promotional flyer.\n\n
   ```
   Then append the full Agent 3 prompt text.

3. **Send the prompt** by clicking the send button (blue arrow icon to the right of the input):
   ```
   mcp__playwright__browser_click → element: the send/submit button (arrow icon)
   ```

#### Step 3c: Wait for Image Generation

Image generation takes 15-60 seconds depending on complexity. The agent must wait patiently.

1. **Poll for completion.** Check every 10 seconds for up to 120 seconds:
   ```
   mcp__playwright__browser_wait_for → timeout: 10000
   mcp__playwright__browser_snapshot
   ```

2. **Detect completion signals in the snapshot:**
   - **Image generated:** An `<img>` element appears in the Gemini response area containing the generated image. The response may also show "Show thinking (Nano Banana Pro)" text.
   - **Still generating:** A loading spinner, "Generating..." text, or animated dots are visible.
   - **Error/refusal:** Gemini may refuse to generate certain content. Look for error messages like "I can't generate that image" or safety warnings.

3. **If generation succeeds** (image visible in response): Proceed to Step 3d.

4. **If generation fails or is refused:**
   - Take a screenshot for debugging:
     ```
     mcp__playwright__browser_take_screenshot → filename: "{merchant}_occasion_{N}_error.png"
     ```
   - Save the screenshot to `merchants/{Merchant Name}/screenshots/`.
   - Log the error: "Occasion {N} ({title}) -- image generation failed. Screenshot saved. Skipping to next occasion."
   - Continue to the next occasion.

5. **If timeout (120 seconds) with no image and no error:**
   - Take a screenshot, save it, log the timeout, and move to the next occasion.

#### Step 3d: Download the Generated Image

Once the image appears in Gemini's response:

1. **Take a full screenshot** of the page showing the generated image for reference:
   ```
   mcp__playwright__browser_take_screenshot → filename: "{merchant}_occasion_{N}_fullpage.png"
   ```
   Save this to `merchants/{Merchant Name}/screenshots/` as a record of the generation.

2. **Extract the generated image.** Use one of these methods (try in order):

   **Method A -- Right-click download (preferred):**
   - Hover over the generated image in the response:
     ```
     mcp__playwright__browser_hover → element: the generated image in Gemini's response
     ```
   - Look for a download/share button that appears on hover (Gemini shows action icons on image hover). Take a snapshot to find clickable elements.
   - If a download button exists, click it and let the browser save the file.

   **Method B -- Extract image source URL via JavaScript:**
   ```
   mcp__playwright__browser_evaluate →
     const imgs = document.querySelectorAll('img[src*="blob:"], img[src*="data:image"], img[src*="lh3.googleusercontent"]');
     const responseImgs = [...imgs].filter(img => img.closest('[data-message-id]') || img.width > 400);
     return responseImgs.length > 0 ? responseImgs[responseImgs.length - 1].src : null;
   ```
   If a URL is returned, use `browser_evaluate` with fetch to download the image data, or use `browser_run_code` to save it.

   **Method C -- Canvas-based screenshot crop (fallback):**
   If the image cannot be downloaded directly, take a targeted screenshot of just the image element. First identify the image element's bounding box via the snapshot, then:
   ```
   mcp__playwright__browser_evaluate →
     const img = document.querySelector('[data-message-id]:last-child img[src*="blob:"], [data-message-id]:last-child img[width]');
     if (img) {
       const rect = img.getBoundingClientRect();
       return {x: rect.x, y: rect.y, width: rect.width, height: rect.height};
     }
     return null;
   ```
   Then use a targeted screenshot with clip coordinates to capture just the image.

   **Method D -- Direct Blob download via JavaScript (most reliable for blob URLs):**
   ```javascript
   mcp__playwright__browser_evaluate →
     async () => {
       const imgs = document.querySelectorAll('img');
       const genImg = [...imgs].filter(i => i.src.startsWith('blob:') && i.width > 300).pop();
       if (!genImg) return null;
       const response = await fetch(genImg.src);
       const blob = await response.blob();
       const reader = new FileReader();
       return new Promise(resolve => {
         reader.onload = () => resolve(reader.result);
         reader.readAsDataURL(blob);
       });
     }
   ```
   This returns a base64 data URL that can be written to a file.

3. **Save the image** to the final images folder:
   ```
   merchants/{Merchant Name}/final_images/{filename_slug}
   ```
   Example: `merchants/Falafel Corner/final_images/occasion_1_ramadan_begins_ash_wednesday.png`

4. **Verify the save** -- read/check that the file exists and has a reasonable file size (>10KB for a real image).

#### Step 3e: Log Progress

After each occasion (success or failure), log:
```
[{occasion_number}/{total}] {occasion_title} -- {SUCCESS | FAILED | TIMEOUT}
  → Saved: merchants/{Merchant Name}/final_images/{filename_slug}
```

#### Step 3f: Repeat

Loop back to Step 3a for the next occasion. Continue until all occasions are processed.

---

### Phase 4: Generate Summary Report

After processing all occasions, create a summary at the top of a log file or output it directly:

```markdown
# Agent 4: Image Generation Report -- {Merchant Name}
**Date:** {today's date}
**Total Occasions:** {N}
**Successful:** {count}
**Failed:** {count}
**Timed Out:** {count}

| # | Occasion | Status | Filename |
|---|----------|--------|----------|
| 1 | Ramadan Begins + Ash Wednesday | SUCCESS | occasion_1_ramadan_begins_ash_wednesday.png |
| 2 | First Lenten Friday | SUCCESS | occasion_2_first_lenten_friday.png |
| ... | ... | ... | ... |
```

---

## File Naming Convention

All generated images go into `merchants/{Merchant Name}/final_images/` with this naming pattern:

```
occasion_{N}_{slugified_title}.png
```

Rules for slug generation:
- Lowercase everything
- Replace spaces with underscores
- Remove special characters (colons, dashes used as separators, parentheses, apostrophes, ampersands)
- Replace ` + ` or ` -- ` with `_`
- Collapse multiple underscores to single
- Truncate to 80 characters max (before `.png`)
- Examples:
  - `## Occasion 1: Ramadan Begins + Ash Wednesday -- Dual Religious Observance` → `occasion_1_ramadan_begins_ash_wednesday_dual_religious_observance.png`
  - `## Occasion 7: National Snack Day -- Shawarma Fries & Sides` → `occasion_7_national_snack_day_shawarma_fries_sides.png`
  - `## Occasion 13A: March Madness First Round` → `occasion_13a_march_madness_first_round.png`
  - `## Occasion 14: Falafel Friday (Recurring Weekly)` → `occasion_14_falafel_friday_recurring_weekly.png`

---

## Folder Structure (per merchant, after Agent 4 runs)

```
merchants/{Merchant Name}/
  agent1_brand.md          ← Agent 1 output
  agent2_occasions.md      ← Agent 2 output
  agent3_content.md        ← Agent 3 output (prompts + captions)
  screenshots/             ← Playwright screenshots (Agent 1 + Agent 4 debug)
    {merchant}_occasion_{N}_fullpage.png
    {merchant}_occasion_{N}_error.png (if failed)
  final_images/            ← Agent 4 output: generated Nano Banana Pro images
    occasion_1_{slug}.png
    occasion_2_{slug}.png
    ...
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Google sign-in required | Pause, ask user to sign in, wait, retry |
| Model set to "Fast" not "Pro" | Switch to Pro before generating |
| Gemini refuses to generate image | Screenshot the error, log it, skip to next occasion |
| Generation times out (>120s) | Screenshot, log timeout, skip to next occasion |
| Image download fails (blob extraction fails) | Fall back to canvas screenshot crop method |
| `agent3_content.md` not found | Stop and tell user to run Agent 3 first |
| No prompts extracted | Stop and report parsing failure -- agent3_content.md format may have changed |
| Gemini rate-limits requests | Wait 30 seconds between prompts; if rate-limited, wait 60 seconds and retry once |
| Browser crashes or disconnects | Report error, note which occasion was last completed, so the user can resume |

---

## Timing & Rate Limiting

- **Wait 5 seconds** after page load before interacting with elements.
- **Wait 3 seconds** after clicking send before polling for results.
- **Poll every 10 seconds** for image generation completion, up to 120 seconds.
- **Wait 5 seconds** between completing one occasion and starting the next to avoid rate limits.
- If Gemini shows any rate-limit messaging, **wait 60 seconds** before the next attempt.

---

## Important Notes

- **Do NOT modify `agent3_content.md`** -- it is read-only input for Agent 4.
- **Do NOT skip occasions** unless they fail. Generate every prompt, even recurring ones (Falafel Friday, Meatless Monday, etc.).
- **Each prompt gets its own fresh Gemini chat.** Do not chain prompts in a single conversation -- Gemini may carry context from previous prompts and distort the output.
- **Screenshot everything** -- both successes (fullpage proof) and failures (error state). These go in `screenshots/`, NOT `final_images/`.
- **The `final_images/` folder should ONLY contain the clean, generated poster images** -- no debug screenshots, no fullpage captures.
- If a merchant has an existing `final_images/` folder with prior runs, **do NOT delete existing images.** Generate new ones alongside them. If a filename conflicts, append `_v2`, `_v3`, etc.
- The generated images will NOT be exactly 1030x1350 pixels -- Gemini generates at its own resolution. The prompts specify the target dimensions and 3:4 aspect ratio, but the actual output size may vary. This is expected.

---

## File Output

**Reads:** `merchants/{Merchant Name}/agent3_content.md`
**Writes:** Generated images to `merchants/{Merchant Name}/final_images/`
**Writes:** Debug screenshots to `merchants/{Merchant Name}/screenshots/`
