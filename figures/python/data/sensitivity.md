# Sensitivity check (weighted decision matrix)

Each weight is moved by +/-0.1; the other weights are rescaled proportionally so the sum stays 1.0.

| Criterion | Change | New weight | A | B | C | Winner | Winner changed? |
|---|---|---|---|---|---|---|---|
| base | - | - | 2.85 | 3.05 | 3.50 | C | no |
| quality | -0.1 | 0.15 | 2.96 | 2.92 | 3.57 | C | no |
| quality | +0.1 | 0.35 | 2.74 | 3.18 | 3.43 | C | no |
| cost | -0.1 | 0.10 | 2.83 | 3.18 | 3.44 | C | no |
| cost | +0.1 | 0.30 | 2.87 | 2.92 | 3.56 | C | no |
| hebrew | -0.1 | 0.10 | 2.83 | 3.06 | 3.44 | C | no |
| hebrew | +0.1 | 0.30 | 2.87 | 3.04 | 3.56 | C | no |
| dev_time | -0.1 | 0.05 | 3.07 | 2.82 | 3.56 | C | no |
| dev_time | +0.1 | 0.25 | 2.63 | 3.28 | 3.44 | C | no |
| vendor | -0.1 | 0.00 | 2.61 | 3.28 | 3.56 | C | no |
| vendor | +0.1 | 0.20 | 3.09 | 2.82 | 3.44 | C | no |
| privacy | -0.1 | 0.00 | 2.61 | 3.17 | 3.44 | C | no |
| privacy | +0.1 | 0.20 | 3.09 | 2.93 | 3.56 | C | no |

Base winner: C. The winner does not change in any of 12 scenarios.

Scores are the team's assessment (see weights.json), not sourced facts.
