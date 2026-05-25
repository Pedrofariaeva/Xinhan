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

## 2026-05-24 — Universal Protocol Engineering

**What:** Built a single master protocol (`~/.pepe-template/.ai/protocol.md` v7.2) that auto-injects into all AI sessions across all repos via self-installing `pepe.sh`, Kimi `SessionStart` hooks, and Claude Code `CLAUDE.md`.

**Why it matters:** Pedro has 13+ repos. Previously, every new project required a "setup conversation" with AI agents to establish rules. Now `cd` into any folder and the protocol is already there. This eliminates ~5 minutes of boilerplate per session and prevents rule drift across projects.

**Key technical insights:**
1. **Self-installing heredoc scripts are the ultimate portability.** `pepe.sh` embeds all templates as heredocs. One `curl` → one `source` → fully configured system. No package managers, no dependencies beyond `sed` and `git`.
2. **Version detection protects custom protocols.** Astrolaby's v9.0 custom protocol was detected by `grep '^VERSION:'` and skipped during universal sync. Only `CLAUDE.md` was updated. This preserves project-specific rules.
3. **Kimi `SessionStart` hooks + Claude `CLAUDE.md` auto-read = zero-latency injection.** Kimi gets the protocol via shell hook output; Claude Code gets it via file read. Neither requires modifying the LLM binary.
4. **Preserve existing muscle memory.** Pedro's `cld`/`claudino` OpenCode launcher was left untouched. The new `claude-code` command is additive, not replacement.

**Validated by:** Successfully deployed to all 13+ repos in `~/Documents/GitHub/`. Pedro confirmed this is exactly what he wanted — zero setup, universal rules, project-specific overrides preserved.

---

## Template

```
## YYYY-MM-DD — <Pattern or Gotcha>

**What:** <description>

**Why it matters:** <impact>

**Validated by:** <how we confirmed this>
```
