# Xinhan — Tasks

## 🔴 CURRENT STATE

- `.ai/` protocol system initialized (2026-05-24)
- Website front page + auth pages built and deployed to stage.xinhan.org (2026-05-24)
- Awaiting Pedro's review on stage.xinhan.org
- Teaching materials audited; full catalog in `CONTENT_AUDIT.md`
- Trial-lesson hub live at `/trial-lesson` with 5 existing lessons arranged as a progressive trial cycle (2026-07-02)

---

## 📋 Backlog

- [ ] Get Pedro's review on front page design at stage.xinhan.org
- [ ] Get Pedro's review on sign-in / sign-up flow at stage.xinhan.org
- [ ] Get Pedro's review on trial-lesson hub at `/trial-lesson` (now shows 5 lessons in progressive order)
- [ ] Decide whether to fix ESLint setup (`npm run lint` prompts for config) or commit as-is
- [ ] Set up proper build tooling if needed (ask Pedro first)
- [ ] Clean up duplicate files across docs1/2/3 (ask Pedro first)
- [ ] Move non-educational/personal docs out of teaching folders (ask Pedro first)
- [ ] Decide which teaching materials to feature/publish publicly
- [x] Connect auth pages to real backend (done 2026-05-25 — real MongoDB auth with JWT)
- [x] Build universal pepe/claudino protocol system for all repos (done 2026-05-24 — v7.2 deployed to all GitHub repos)

---

## ✅ Completed

- [x] 2026-05-23 — Full content audit of docs1/2/3 completed (`CONTENT_AUDIT.md`)
- [x] 2026-05-24 — `.ai/` protocol system initialized
- [x] 2026-05-24 — Built front page (`index.html`) with HSK curriculum, themes, featured content
- [x] 2026-05-24 — Built sign-in page (`signin.html`) matching video-astrolaby auth model
- [x] 2026-05-24 — Built sign-up page (`signup.html`) matching video-astrolaby auth model
- [x] 2026-05-24 — Updated protocol v1.2 with explicit deployment infrastructure (stage.xinhan.org)
- [x] 2026-05-24 — Deployed all pages to `stage` branch → stage.xinhan.org
- [x] 2026-06-03 — Translated `BookletSpecificatoinsHainan.docx` to Chinese (中文翻译 .md + .docx)
- [x] 2026-06-03 — Created Meeting Report 2026-06-02 EN + CN (.docx) for Pedro Faria contract review
- [x] 2026-06-03 — Revised + translated WPR20250421_2.pdf to English (revised) + Chinese (.docx)
- [x] 2026-07-02 — Created new HSK 2–3 lesson deck "Mood & Weather" in `uncoveredDocs/HSKideas/16 Mood and Weather/` (HTML + PDF, drawings + pictures)
- [x] 2026-07-02 — Created new HSK 3 lesson deck "Many Ways to Say It" in `uncoveredDocs/HSKideas/15 Many Ways to Say It/` (HTML + PDF, drawings + pictures)
- [x] 2026-07-02 — Built trial-lesson selector hub (`app/trial-lesson/page.tsx`) and lesson player (`app/trial-lesson/[lessonId]/page.tsx`)
- [x] 2026-07-02 — Deployed 4 interactive trial lesson decks under `public/trial-lesson/`: `banjia`, `mood-weather`, `many-ways`, `mood-weather-v2`
- [x] 2026-07-02 — Restored original Luckin Coffee trial lesson at `/trial-lesson/luckin-coffee`
- [x] 2026-07-02 — Created progressive HSK 1–6 trial lesson cycle: `hsk-1` to `hsk-6` with level-appropriate vocabulary and grammar
- [x] 2026-07-02 — Reverted generic HSK 1–6 cycle; hub now uses the 5 existing lessons (`luckin-coffee`, `mood-weather`, `banjia`, `many-ways`, `mood-weather-v2`) in progressive order
- [x] 2026-07-02 — Added `.venv/` to `.gitignore` and removed virtualenv files from the repo
- [x] 2026-07-02 — Wired all trial lesson quizzes to `/api/lessons/attempt` and `/api/lessons/complete` for score persistence

---

## 📬 Reports to Maestro

- [2026-05-25] **Claude Code (Claudino)** — Implemented real auth for Xinhan
  - Files: `middleware.ts`, `lib/auth.ts`, `lib/auth-edge.ts`, `lib/mongodb.ts`, `app/api/auth/*`, `app/signin/`, `app/signup/`, `app/dashboard/`, `app/globals.css`, `app/layout.tsx`, `.env.local`
  - Commit: `fe8608e`
  - Status: done — build passes, pushed to `stage`
  - Handoff: **IMPORTANT** — Pedro must add `JWT_SECRET` to Vercel env vars for production. Value: `Bh9FgMEH/ZnrGzRa9K80XuxDZkG0yJVqZYvefaLWW3Q=`. Go to vercel.com → Xinhan project → Settings → Environment Variables → add `JWT_SECRET` for Preview + Production environments.
- [2026-07-02] **Kimi (Maestro)** — Built new HSK 2–3 "Mood & Weather" lesson deck
  - Files: `uncoveredDocs/HSKideas/16 Mood and Weather/xin-qing-he-tian-qi-lesson-deck.html`, `uncoveredDocs/HSKideas/16 Mood and Weather/xin-qing-he-tian-qi-lesson-deck.pdf`, `uncoveredDocs/HSKideas/convert_decks_to_pdf.py`
  - Source: `/Users/pedro/Downloads/level 2-3 心情和天气 new version mood and weather  English _20260626174543(2).pdf`
  - Status: done — HTML + PDF generated, includes SVG drawings, stock pictures, interactive quizzes, and lesson report
- [2026-07-02] **Kimi (Maestro)** — Built new HSK 3 "Many Ways to Say It" lesson deck
  - Files: `uncoveredDocs/HSKideas/15 Many Ways to Say It/many-ways-to-say-it-hsk3-lesson-deck.html`, `uncoveredDocs/HSKideas/15 Many Ways to Say It/many-ways-to-say-it-hsk3-lesson-deck.pdf`, `uncoveredDocs/HSKideas/convert_decks_to_pdf.py`
  - Source: `/Users/pedro/Documents/GitHub/Xinhan/uncoveredDocs/HSKideas/15 talking/many-ways-to-say-it-hsk3.pptx`
  - Status: done — HTML + PDF generated, includes SVG drawings, stock pictures, interactive quizzes, and lesson report
- [2026-07-02] **Kimi (Maestro)** — Built online trial-lesson hub
  - Files: `app/trial-lesson/page.tsx`, `app/trial-lesson/[lessonId]/page.tsx`, `public/trial-lesson/banjia/index.html`, `public/trial-lesson/mood-weather/index.html`, `public/trial-lesson/many-ways/index.html`, `public/trial-lesson/mood-weather-v2/index.html`, `build_trial_decks.py`
  - Features: JWT-gated selector page, iframe lesson player, interactive quizzes per deck, per-group scoring, end-of-lesson report, MongoDB persistence via `/api/lessons/attempt` and `/api/lessons/complete`
  - Status: done — `npm run build` passes; `npm run lint` still prompts for ESLint setup (pre-existing)
- [2026-07-02] **Kimi (Maestro)** — Restored Luckin Coffee lesson + built progressive HSK 1–6 cycle
  - Files: `public/trial-lesson/luckin-coffee/index.html`, `public/trial-lesson/hsk-1/index.html` … `public/trial-lesson/hsk-6/index.html`, `build_hsk_cycle.py`, `app/trial-lesson/page.tsx`, `app/trial-lesson/[lessonId]/page.tsx`
  - Features: original Luckin Coffee lesson moved to `/trial-lesson/luckin-coffee`; 6 new progressive HSK decks with level-appropriate vocab/grammar/quizzes; selector split into "Progressive HSK Cycle" and "More Trial Lessons"
  - Status: superseded — generic HSK 1–6 decks and `build_hsk_cycle.py` were removed after clarifying Pedro wants the 5 existing lessons arranged progressively
- [2026-07-02] **Kimi (Maestro)** — Finalized trial-lesson hub with 5 existing lessons in progressive order
  - Files: `app/trial-lesson/page.tsx`, `app/trial-lesson/[lessonId]/page.tsx`, `.gitignore`
  - Features: hub lists `luckin-coffee` → `mood-weather` → `banjia` → `many-ways` → `mood-weather-v2` as Step 1–5; player recognizes all 5 IDs; `.venv/` ignored
  - Status: done — `npm run build` passes; pushed to `stage`
