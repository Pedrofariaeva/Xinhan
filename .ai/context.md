# Xinhan — Project Context

- **Name:** Xinhan Chinese Language School
- **Type:** Static website + teaching content archive
- **Stack:** Vanilla HTML (currently), deployed on Vercel
- **Domain:** Production on Vercel (main branch)

## Project Structure

```
Xinhan/
├── .ai/                  # AI protocol & memory files
├── docs1/                # Teaching materials (PPTX, DOCX, PDF) — primary
├── docs2/                # Teaching materials + 2018 archive + personal docs
├── docs3/                # Teaching materials — largest collection
├── index.html            # Landing page ("Coming soon")
├── README.md             # Project readme
├── CONTENT_AUDIT.md      # Full audit of all teaching materials (130+ files)
├── .vercel/              # Vercel deployment config
├── .env.local            # Environment variables (sensitive)
└── .gitignore
```

## Key Facts

- **Content audit completed:** 2026-05-23. See `CONTENT_AUDIT.md` for full catalog.
- **~62 unique educational documents** across HSK 1–6, plus English/TOEIC materials.
- **Current site:** Single `index.html` with "Coming soon". Needs full website build.
- **No build system yet** — plain HTML. May expand to a framework later (ask Pedro first).

## Important Paths

| Path | Description |
|------|-------------|
| `docs1/`, `docs2/`, `docs3/` | Teaching content archives — DO NOT delete or reorganize without Pedro's approval |
| `CONTENT_AUDIT.md` | Complete catalog of all teaching materials with quality ratings |
| `index.html` | Current landing page |
| `.env.local` | Vercel/environment secrets |

## Current State

- Website is a placeholder. Full build is pending.
- Teaching materials are organized but duplicated across folders.
- `CONTENT_AUDIT.md` contains a detailed gap analysis and recommendations for curriculum development.
