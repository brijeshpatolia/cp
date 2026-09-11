# bfre-risk-desk

Working materials for **THE RISK DESK** — a single-player game whose only purpose is to make one
person capable of rebuilding the BlackRock Fundamental Risk for Equities (BFRE) model from a blank
page.

The game is played in a chat session. This directory holds the things a chat session cannot keep:
the game-master prompt, a page-indexed transcription of the source paper, the hand-computable
datasets each level runs on, and the save files that carry progress between sessions.

## Layout

| Path | What's in it |
|---|---|
| `prompt/RISK_DESK.md` | The game-master prompt. Paste into a fresh chat alongside the paper, then say "Begin." |
| `notes/` | Page-indexed transcription of the BFRE paper — equations, tables, numbers, and methodological choices, keyed to PDF page. |
| `datasets/` | The datasets for each level, small enough to compute by hand, with the exact arithmetic worked out. |
| `gm/` | Game-master reference: BFRE anchor map, vocabulary, the Level 12 critique dossier, the analogy bank, and the playbook. |
| `tools/` | Scripts that produced or verify the above. |
| `saves/` | Save files. `SAVE_TEMPLATE.md` is the blank; each session appends a dated save. |

## Why `notes/` exists

The source PDF is a **scan** — 65 pages, one JPEG per page, no text layer at all. `pdftotext` on it
returns 1,421 characters of nothing. Every equation, table cell and number in `notes/` was read off
the page images and then re-read by a second pass that checked it digit by digit against the same
images.

Anything the scan could not resolve is marked `[UNREADABLE: ...]` rather than guessed. That marker
is load-bearing: the game's rules forbid teaching from a number whose origin cannot be traced, so a
value that cannot be read must be visibly missing rather than quietly invented.

To regenerate the page images from your own copy of the PDF:

```bash
pip install pypdf pillow
python bfre-risk-desk/tools/extract_pages.py BFRE_paper.pdf bfre-risk-desk/img/
```

The PDF itself is not committed — it is a third-party document. `.gitignore` excludes `*.pdf` and
`img/`.

## Verifying the datasets

Every number a level shows the player has to trace back to arithmetic already on the table. The
scripts in `tools/` recompute each dataset in exact rational arithmetic, so a teaching example can
never drift:

```bash
python bfre-risk-desk/tools/verify_coldopen.py      # the 60-second cold open
python bfre-risk-desk/tools/verify_level0_boss.py   # Level 0 boss round
python bfre-risk-desk/tools/verify_level1.py        # Level 1 derivation + boss round
python bfre-risk-desk/tools/verify_level2.py        # Level 2 balance condition + sabotage boss
python bfre-risk-desk/tools/verify_level3.py        # Level 3 two-column normal equations
python bfre-risk-desk/tools/verify_level4.py        # Level 4 collinearity + Frisch-Waugh
```

## The four victory conditions

The game is won only when all four hold:

1. **Wiki test** — any question about the model answered from structure, not memory.
2. **Passing test** — 20 minutes with a professional quant reveals no gap in background.
3. **Origin test** — every formula derived from scratch, including where standard errors and
   denominators come from.
4. **Rebuild test** — given only returns and characteristics, build `X`, estimate factor returns,
   build `F`, build `D`, assemble `V = XFXᵀ + D`, and compute a portfolio's risk, alone.
