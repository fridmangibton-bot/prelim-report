# Market data for chapter 4 (collected by the team, 2026-11-21)

> Source of truth for the competitor table, the radar chart and the scatter chart.
> Prices = public pricing pages, MONTHLY billing, USD (re-checked 2026-11-21; annual billing is cheaper and is not used). "Not found" = not stated on the public pages / could not be tested on the free tier.

## 1. Competitor comparison table (ch4)

| Product | Cheapest paid plan | Plan needed for consistent characters | Consistent characters | Series / episodes | Hebrew | End-to-end AI video | Main weakness (team test) |
|---|---|---|---|---|---|---|---|
| LTX Studio | $15 (Lite); $35 Standard; $125 Pro | Standard, $35 | Yes (saved "elements") | Not found | Not found (needs payment to test) | Yes | Cannot be tried without paying |
| OpenArt | $14 (Starter); $34 Plus; $56 Pro; $240 Wonder | Starter, $14 (~13 characters; ~353 on Wonder). Starter has no commercial-use license | Yes | Not found | Not found (needs payment to test) | Yes | Loaded for a long time and produced no result |
| LongStories.ai | $59 (Pro); $99 Creator; $199 Creator Max; free tier without video | Pro, $59 | Yes ("Universes") | **Yes** – a follow-up video becomes episode 1 of a series automatically | Not found (needs payment to test) | Yes | Cannot be tried without paying |
| Atlabs | Lite $19; Pro $39; Plus $79; Max $249 (verified on atlabs.ai/pricing, team screenshot 2026-11-22) | Pro, $39 ("Cast Characters & maintain consistency"); Lite does not include it. Translation to 40+ languages only on Max | Yes | Not found | **Yes, paid plans only** (confirmed in a chat with Atlabs support) | Yes | Hebrew only behind a paywall |
| CapCut (manual process) | $19.99 Pro (69.9 ILS in Israel), according to a secondary source (official pricing page could not be opened) [TO-VERIFY: CapCut footnote] | – | No (manual editing) | No | **Yes** (interface in Hebrew) | No – editing only, other AI tools needed | Desktop download required; everything manual |

Team finding for the report: none of the four AI video tools could be tested in Hebrew on a free tier; only one (Atlabs) states Hebrew support, and only on paid plans. This supports the claim that there is no accessible Hebrew-first tool for creators.

## 2. Scatter chart (ch4) – replace the old cost-per-minute chart

The team has no reliable cost-per-finished-minute data, so the scatter uses verifiable values:
- **X axis:** monthly price (USD) of the cheapest plan that includes consistent characters.
- **Y axis:** capability coverage = how many of the 4 key capabilities the product has: (1) consistent characters, (2) series/episodes, (3) Hebrew, (4) end-to-end AI video.

| Product | X: price (USD) | Y: capabilities (0–4) | Which |
|---|---|---|---|
| LTX Studio | 35 | 2 | consistent characters, end-to-end |
| OpenArt | 14 | 2 | consistent characters, end-to-end |
| LongStories.ai | 59 | 3 | consistent characters, series, end-to-end |
| Atlabs | 39 | 3 | consistent characters, Hebrew (paid), end-to-end |
| CapCut (manual) | 19.99 | 1 | Hebrew |
| Our solution (design target) | target range 20–30, marked as target | 4 | all four |

Draw "our solution" as a target marker (different style, labelled "יעד תכנון"), not as a measured product.

## 3. Radar chart (ch4) – team assessment, scale 1–5

Basis: the documented features above. Show the 4 competitors that matter most + our design target. OpenArt stays in the table only.

| Axis | LTX Studio | LongStories.ai | Atlabs | CapCut (manual) | Our solution (target) |
|---|---|---|---|---|---|
| עקביות דמות | 4 | 4 | 4 | 1 | 4 |
| עלות נמוכה | 3 | 2 | 3 | 4 | 4 |
| תמיכה בעברית | 1 | 1 | 3 | 4 | 5 |
| רציפות עלילתית | 2 | 4 | 2 | 1 | 5 |
| קלות שימוש | 3 | 4 | 3 | 2 | 5 |
| שליטת היוצר | 5 | 2 | 3 | 5 | 4 |

Rationale (one line each, for the chapter text):
- Consistency: all AI tools offer saved characters; CapCut has none.
- Low cost: follows the entry price for the consistency feature (cheaper = higher): CapCut $19.99 and our target $20–30 = 4; LTX Studio $35 and Atlabs $39 = 3; LongStories.ai $59 = 2. Ours is a design target.
- Hebrew: Atlabs = paid only (3); CapCut = Hebrew UI but no Hebrew generation (4); others not found (1).
- Narrative continuity: only LongStories has an explicit series feature (4); none keeps a story memory with contradiction checks – our innovation (5).
- Ease of use: LTX and OpenArt could not be tried; LongStories auto-builds episodes; CapCut needs many manual steps.
- Creator control: LTX (storyboard + camera control) and CapCut (full manual editing) are highest.

Caption note for both charts: "הערכת צוות על בסיס תכונות מוצהרות בדפי המוצר, נבדק ב-21-22.11.2026".

## Verification log (2026-11-21)
- LTX Studio $15/$35/$125 and saved Elements on Standard: confirmed on ltx.studio pricing and LTX plans blog.
- OpenArt: the partner's figures were old annual prices; corrected to current monthly $14/$34/$56/$240; ~13 / ~353 consistent characters confirmed.
- LongStories.ai: Pro $59 confirmed; Creator is $99 (the $199 plan is Creator Max) – corrected.
- Atlabs (2026-11-22): all four prices verified on atlabs.ai/pricing (team screenshot): Lite $19, Pro $39, Plus $79, Max $249. Consistency starts at Pro.
- CapCut: price from a secondary source; official page could not be opened (kept with asterisk, "לפי מקור משני").

## Team test findings and selection criteria (2026-11-23)
- None of the four AI tools could be used in Hebrew on a free plan; only Atlabs states Hebrew support, on paid plans (per its support team).
- Only LongStories.ai offers an explicit series feature.
- In a review of the product pages, no product presents plot-contradiction detection.
- Selection criteria: (1) AI video tools with persistent/consistent characters for story videos; (2) public self-serve price; (3) relevance to the Israeli market (Atlabs states Hebrew support; LTX Studio is Israeli, Lightricks); (4) the manual process (CapCut + separate tools) as today's baseline.
