# Sources whitelist

> The ONLY sources the report may cite. Each line: bib key – what it supports – verified status.
> Verified on 2026-11-21 (papers: venue checked on the publisher/proceedings page; market numbers: checked on the publisher page).

## Academic papers (chapter 3)

| Bib key | Paper | Venue | Use in report | Verified |
|---|---|---|---|---|
| zhao2025moviedreamer | MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences | ICLR 2025 | **FLAGSHIP PAPER.** Narrative coherence + character identity across a long video (autoregressive planning + diffusion rendering, multimodal script) | ✔ ICLR 2025 proceedings |
| hu2024storyagent | StoryAgent: Customized Storytelling Video Generation via Multi-Agent Collaboration | arXiv 2411.04925 (2024) | Multi-agent "production crew" (agent manager, story designer, storyboard generator, video creator, observer) – closest to our architecture | ✔ arXiv (cite as preprint) |
| lin2023videodirectorgpt | VideoDirectorGPT: Consistent Multi-scene Video Generation via LLM-Guided Planning | arXiv 2309.15091 (2023, rev. 2024) | LLM as "director": video plan with scenes, entities and consistency groups | ✔ arXiv (cite as preprint) |
| guo2025lct | Long Context Tuning for Video Generation | ICCV 2025, pp. 17281–17291 | Scene-level consistency across multiple shots | ✔ ICCV 2025 open access |
| zhou2024storydiffusion | StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation | NeurIPS 2024 | Consistent character across a story image sequence, then video | ✔ (arXiv 2405.01434) |
| tewel2024consistory | Training-Free Consistent Text-to-Image Generation (ConsiStory) | ACM Transactions on Graphics (SIGGRAPH 2024) | Same subject across images without retraining (NVIDIA + Tel Aviv University) | ✔ (arXiv 2402.03286) |
| liu2024grimm | Intelligent Grimm – Open-ended Visual Storytelling via Latent Diffusion Models | CVPR 2024 | Auto-regressive visual storytelling conditioned on previous frames + StorySalon dataset | ✔ CVPR 2024 open access |

**Knowledge gap (one sentence, for ch3):** המחקרים והמוצרים הקיימים שומרים על עקביות חזותית של דמויות ועולם, ולעיתים גם בין פרקים, אך אף אחד מהם אינו מנהל זיכרון של העלילה עצמה (אירועים, יחסים ומצב הדמויות) ואינו מזהה סתירות עלילתיות בין פרקים, ואף אחד אינו נגיש כמערכת קצה-לקצה ליוצרים בעברית.

Careful wording note: LongStories.ai keeps cast, voices and world across episodes, so the report must NOT claim that no product keeps characters across episodes. The gap is plot memory + contradiction detection + Hebrew.

## Market size (chapter 1 and 4)

| Bib key | Figure | Source | Verified |
|---|---|---|---|
| fbi2026aivideo | AI video generator market: USD 716.8M (2025) → USD 847M (2026) → USD 3,350M (2034), CAGR 18.8% **for 2026–2034**; North America 41% share (2025) | Fortune Business Insights, report FBI110060, updated Oct 2026 – https://www.fortunebusinessinsights.com/ai-video-generator-market-110060 | ✔ |
| mnm2023t2v | Text-to-video AI market: USD 0.1B (2022) → USD 0.9B (2027), CAGR 37.1% (older, narrower definition – use only for comparison) | MarketsandMarkets, report TC 8580, Feb 2023 – https://www.marketsandmarkets.com/Market-Reports/text-to-video-ai-market-236764144.html | ✔ (note: the partner's original link was a different URL; use this one) |
| goldman2023creator | Creator economy TAM ≈ USD 250B (2023) → ≈ USD 480B (2027); only ~4% of creators are professionals (> USD 100K/year) | Goldman Sachs Research, 2023 – https://www.goldmansachs.com/insights/pages/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027 | ✔ |

Note for ch4: market reports disagree strongly (definitions differ). The report presents a range, not one number.

## Competitor products (chapter 4) – accessed 2026-11-21 by the team

| Bib key | Product | URL |
|---|---|---|
| ltxstudio | LTX Studio (Lightricks) | https://ltx.studio |
| openart | OpenArt | https://openart.ai |
| longstories | LongStories.ai | https://longstories.ai |
| atlabs | Atlabs | https://www.atlabs.ai |
| capcut | CapCut | https://www.capcut.com |

Competitor data (prices, features, Hebrew) is in `docs/market-data.md`.
