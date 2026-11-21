# Detector report – sample – 2026-11-21
Summary: 2 critical, 1 medium, 0 minor. Words: n/a (design sample, D9 skipped). TO-VERIFY: 1.
| Bug ID | Check | Line | Severity | Problem | Suggested fix |
|---|---|---|---|---|---|
| BUG-sample-01 | D1 | 12 | critical | Latin "David" (font name) in Hebrew text not wrapped | גופן \textenglish{David} בגודל 12 נקודות |
| BUG-sample-02 | D13 | 14 | critical | Maqaf ־ joins prefix ו to a \textenglish run ("ו־\textenglish{LoRA}"); order renders reversed (INC-001 pattern) | Add RLM (U+200F) after the maqaf and after the closing brace of the preceding run: ...\textenglish{IP-Adapter}‏ ו־‏\textenglish{LoRA} ... (check the PDF) |
| BUG-sample-03 | D10 | 14 | medium | "IP-Adapter" and "LoRA" used on first use without a Hebrew term and parentheses | Add a Hebrew gloss in parentheses on first use, e.g. ושיטות כגון \textenglish{IP-Adapter} (מתאם תמונה) ו־‏\textenglish{LoRA} (התאמה קלה של מודל קיים); gloss wording to be confirmed by the writer |

Notes (not bugs):
- D2 BIDI-JOIN: no hits. D3 REF: tab:sample has one matching \ref (line 15). D4 CAPTION: caption above the table (line 19, tabular line 21), correct. D5 CITE: no \cite in file. D6 VOICE: the only first-person form (שלנו, line 30) is inside directornote, allowed. D7 GENERIC: no hits. D8 TODO: 1 [TO-VERIFY] (line 15), 0 FIGURE PENDING.
- D1 check on the other Latin runs: Text-to-Video (line 13), Tool A/B/C (lines 23-25) and brandHighlight (line 34) are wrapped. brandHighlight is a color identifier, not a glossable term, so no D10 entry.
- D12 BUILD: build/sample.log has no "!" errors and no Overfull hbox. Two Underfull \hbox (badness 10000) at log lines 1264 and 1269, both at the chapter heading (line 8). Not a D12 trigger; information only.
- D5 note: bib/references.bib and docs/sources.md are both empty (0 bytes), so any future \cite would fail D5.
