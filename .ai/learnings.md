# Xinhan — Learnings & Gotchas

## 2026-05-24 — Deployment Workflow (Pedro-validated)

**What:** Pedro does NOT test websites locally. The ONLY way he reviews work is via a live Vercel preview URL. Therefore, after every coding session, the default action must be to commit and push to a non-`main` branch (which auto-deploys a preview URL). Production deployment (`main`) requires explicit verbal approval using specific phrases.

**Why it matters:** If code sits uncommitted or unpushed, Pedro cannot review it. If it gets pushed to `main` without approval, it goes live on xinhan.com prematurely.

**Validated by:** Pedro explicitly stated this after repeated protocol breaches across multiple sessions.

---

## 2026-05-24 — Exact Production Approval Phrases

**What:** Only the following phrases (or unmistakably equivalent intent) count as permission to deploy to production (`main`):
- "yes you can deploy"
- "ok" (in direct response to deploy request)
- "deploy to production"
- "push to main"
- "go ahead and deploy"
- "ship it"

**Why it matters:** Vague acknowledgments like "looks good" or "thanks" have been mistakenly interpreted as deploy approval, causing friction.

**Validated by:** Pedro's direct instruction during protocol correction session.

---

## Template

```
## YYYY-MM-DD — <Pattern or Gotcha>

**What:** <description>

**Why it matters:** <impact>

**Validated by:** <how we confirmed this>
```
