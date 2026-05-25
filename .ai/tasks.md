# Xinhan — Tasks

## 🔴 CURRENT STATE

- `.ai/` protocol system initialized (2026-05-24)
- Website front page + auth pages built and deployed to stage.xinhan.org (2026-05-24)
- Awaiting Pedro's review on stage.xinhan.org
- Teaching materials audited; full catalog in `CONTENT_AUDIT.md`

---

## 📋 Backlog

- [ ] Get Pedro's review on front page design at stage.xinhan.org
- [ ] Get Pedro's review on sign-in / sign-up flow at stage.xinhan.org
- [ ] Set up proper build tooling if needed (ask Pedro first)
- [ ] Clean up duplicate files across docs1/2/3 (ask Pedro first)
- [ ] Move non-educational/personal docs out of teaching folders (ask Pedro first)
- [ ] Decide which teaching materials to feature/publish publicly
- [x] Connect auth pages to real backend (done 2026-05-25 — real MongoDB auth with JWT)

---

## ✅ Completed

- [x] 2026-05-23 — Full content audit of docs1/2/3 completed (`CONTENT_AUDIT.md`)
- [x] 2026-05-24 — `.ai/` protocol system initialized
- [x] 2026-05-24 — Built front page (`index.html`) with HSK curriculum, themes, featured content
- [x] 2026-05-24 — Built sign-in page (`signin.html`) matching video-astrolaby auth model
- [x] 2026-05-24 — Built sign-up page (`signup.html`) matching video-astrolaby auth model
- [x] 2026-05-24 — Updated protocol v1.2 with explicit deployment infrastructure (stage.xinhan.org)
- [x] 2026-05-24 — Deployed all pages to `stage` branch → stage.xinhan.org

---

## 📬 Reports to Maestro

- [2026-05-25] **Claude Code (Claudino)** — Implemented real auth for Xinhan
  - Files: `middleware.ts`, `lib/auth.ts`, `lib/auth-edge.ts`, `lib/mongodb.ts`, `app/api/auth/*`, `app/signin/`, `app/signup/`, `app/dashboard/`, `app/globals.css`, `app/layout.tsx`, `.env.local`
  - Commit: `fe8608e`
  - Status: done — build passes, pushed to `stage`
  - Handoff: **IMPORTANT** — Pedro must add `JWT_SECRET` to Vercel env vars for production. Value: `Bh9FgMEH/ZnrGzRa9K80XuxDZkG0yJVqZYvefaLWW3Q=`. Go to vercel.com → Xinhan project → Settings → Environment Variables → add `JWT_SECRET` for Preview + Production environments.
