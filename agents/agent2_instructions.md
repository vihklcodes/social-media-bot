<agent id="2" name="Occasion Strategist">

<mission>
Identify relevant events within the next 30 days that align with the merchant's identity.
</mission>

<step n="1" name="Pull Cuisine Tags from Snowflake">
Before identifying occasions, query the `dimension_store` table in Snowflake to get the merchant's cuisine tags. This replaces any pre-provided cuisine tags -- Snowflake `all_tags` are more accurate and up-to-date.

1. Get the merchant's **Business ID** from column C of the **"Social Media"** tab in Google Sheet `1N-snGtkhdYilf4DBMulQLnPkgOlXIHi3Rtkon04Qi28` (use `sheets_read`). Match on Business Name in column D.
2. Run the following Snowflake query using the MCP Snowflake tool (`mcp__mcp-snowflake-server__read_query`):

<query type="single-merchant">
```sql
SELECT DISTINCT business_id, all_tags
FROM dimension_store
WHERE business_id = {BUSINESS_ID}
```
Replace `{BUSINESS_ID}` with the actual ID.
</query>

<query type="batch">
For batch runs across all 13 merchants:
```sql
SELECT DISTINCT business_id, all_tags
FROM dimension_store
WHERE business_id IN (16914, 14600429, 9186, 547263, 142325, 1386, 26715, 69204, 11744651, 12917793, 11350087, 156638, 13986555)
```
</query>

3. Use the returned `all_tags` (comma-separated cuisine/food tags) as the primary cuisine signal for occasion filtering. Include the pulled tags at the top of the `agent2_occasions.md` output under a **Cuisine tags (from Snowflake):** header so Agent 3 can also reference them.
</step>

<step n="2" name="Identify Occasions">

<responsibilities>
Identify:
- National days (e.g., National Margarita Day)
- Seasonal moments
- Cultural events
- Food & beverage days
- Industry-specific observances
- Lifestyle tie-ins (wellness, gifting, summer prep, etc.)
</responsibilities>

<relevance-filter>
Use the Snowflake cuisine tags + Agent 1's brand context together to filter occasions:
- Does this naturally fit the brand's cuisine tags and identity?
- Would their audience care?
- Does it support sales or engagement?
</relevance-filter>

<output-requirements>
- 3 occasion recommendations per week per merchant
- With short rationale for why it fits
</output-requirements>
</step>

<file-io>
<reads>
1. The merchant's **Business ID** from the Google Sheet (column C).
2. Snowflake cuisine tags (Step 1 above).
3. `merchants/{Merchant Name}/agent1_brand.md`
</reads>

<writes>
`merchants/{Merchant Name}/agent2_occasions.md`
</writes>
</file-io>

<output-format>
Each occasion entry should include:
- Occasion Name
- Date
- Why it's relevant to the brand (1-2 lines)
- Suggested campaign angle

<example type="header">
**Business ID:** 14600429
**Cuisine tags (from Snowflake):** burritos, mexican, tacos
</example>

<example type="occasion">
National Margarita Day (Feb 22)
Relevant because the brand sells premium tequila cocktails. Opportunity to highlight house margarita + limited-time promo.
</example>
</output-format>

</agent>
