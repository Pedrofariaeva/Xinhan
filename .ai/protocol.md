# Xinhan Protocol — Single Source of Truth (v1.2)
# Last updated: 2026-05-24
# Applies to: Kimi (Maestro) for Xinhan Chinese Language School

---

## 🔴 RED LINES — ABSOLUTE PROHIBITIONS

1. **NEVER delete or move teaching materials** from `docs1/`, `docs2/`, `docs3/` without Pedro's explicit approval. These are the school's content archive.

2. **NEVER push to `main` without Pedro saying "push to main"** — `main` = xinhan.org (production). Work on `stage` branch.

3. **NEVER commit without updating `.ai/` files** — `history.md`, `tasks.md`, `plan.txt` minimum. Every session.

4. **NEVER assume when you have a doubt — ASK PEDRO FIRST.**
   If uncertain about ANYTHING (which doc folder to use, how to structure the site, what content to publish) — STOP. Ask. Do NOT guess.

5. **NEVER modify `.env.local` or Vercel environment variables** — ask first, every time.

6. **NEVER start work without doing the Startup Protocol first.** No exceptions, not even for "quick fixes".

---

## 🚀 DEPLOYMENT RULES — READ THIS EVERY TIME

### Infrastructure (must be checked every session)

| Environment | Branch | Domain |
|-------------|--------|--------|
| **Staging / Preview** | `stage` | `stage.xinhan.org` |
| **Production** | `main` | `xinhan.org` |

**Pedro does NOT test locally.** The only way he reviews work is via `stage.xinhan.org`.

### The Rule
After completing work:
1. Commit to the current branch.
2. **Merge or push to `stage` branch.**
3. Vercel auto-deploys `stage` → `stage.xinhan.org`.
4. Tell Pedro: "Deployed to stage.xinhan.org."

**NEVER end a session without pushing to `stage`.** A commit that is not on `stage` does not exist for Pedro.

### Production Deployment — Explicit Approval Required
You may ONLY deploy to production (`main` branch / `xinhan.org`) if Pedro uses **one of these exact phrases** (or unmistakably equivalent intent):

- "yes you can deploy"
- "ok" (in direct response to a deploy request)
- "deploy to production"
- "push to main"
- "go ahead and deploy"
- "ship it"

**Anything else = NO.** Examples that are NOT approval:
- "looks good" (feedback on code, not deploy approval)
- "thanks" (acknowledgment, not approval)
- "let's see" (unclear intent — ask again)
- silence / no response

### Deployment Decision Tree
```
Work completed?
  ├── Commit to current branch
  ├── Push / merge to `stage`
  ├── Vercel deploys to stage.xinhan.org
  └── Is Pedro's last message an EXPLICIT production approval phrase?
        ├── YES → push to main, Vercel deploys to xinhan.org
        └── NO  → STOP. Do NOT touch main.
```

---

## ✅ Startup Protocol (EVERY session, in order)

Run these commands first:
```sh
git branch --show-current       # confirm branch
git log --oneline -5            # see what changed recently
```

Then read in order:
1. `.ai/protocol.md` — this file (you are reading it now ✅)
2. `.ai/context.md` — **deployment infrastructure, staging/production domains, branch mapping**
3. `.ai/plan.txt` — current roadmap and priorities
4. `.ai/tasks.md` — what is pending and in progress
5. `.ai/history.md` (last 30 lines) — what happened last session
6. `.ai/decisions.md` — architectural decisions already made
7. `.ai/learnings.md` — patterns discovered, gotchas, validated rules

Then **confirm with Pedro** before touching anything:
> "I'm on branch `<branch>`. Last commit: `<message>`. Ready for instructions."

**Do NOT start coding before Pedro responds to this confirmation.**

---

## ✅ Before You Write Any Code — Mandatory Pre-Coding Check

Before writing a single line of implementation:

1. **State what you understood** — repeat back what Pedro asked for, in your own words
2. **State what files you will change** — list them explicitly
3. **State any assumptions you are making** — if you have ANY assumption, that is a question you must ask Pedro instead
4. **Wait for Pedro to say "yes, go ahead"** or correct you

---

## ✅ Before Every Commit — Mandatory Pre-Commit Checklist

```
[ ] Committing to the correct branch (NOT main unless Pedro explicitly said so)
[ ] Pushing to stage after commit so Pedro can review on stage.xinhan.org
[ ] .ai/history.md updated with what was done and why
[ ] .ai/tasks.md updated (completed items moved, new items added)
[ ] .ai/plan.txt updated (completed steps marked [x])
[ ] No files with secrets added (.env, credentials)
[ ] git add lists only the files I intentionally changed
[ ] Teaching materials in docs1/2/3 were NOT accidentally moved or deleted
```

---

## 🚀 Push to stage is MANDATORY after every commit — no exceptions

After every commit, immediately run:
```sh
git push origin stage
```

**Never end a coding session without pushing to `stage`.**
A commit that is not on `stage` does not exist for Pedro.
Do NOT ask "should I push?" — just push. Always. Every time. To `stage`.

**BUT:** ONLY push to `main` if Pedro gave **explicit production approval**.

---

## ✅ Exit Protocol — Triggered by "cld", "claudino", "exit", or "stop"

When Pedro says any of these words (as the whole message or clear intent):

1. Append to `.ai/history.md` — dated entry, bullet points of what was done and why
2. Update `.ai/tasks.md` — move completed items, add newly discovered tasks
3. Update `.ai/plan.txt` — mark completed steps `[x]`, update status
4. Update `.ai/decisions.md` — record any architectural decisions made
5. Update `.ai/learnings.md` — record any new patterns or gotchas discovered

Then reply: **"✓ Session saved."** and stop.

---

## Branches

| Branch | Domain | Push allowed? | When to use |
|--------|--------|---------------|-------------|
| `stage` | stage.xinhan.org | ✅ Default. Always push here. | Every session |
| `main` | xinhan.org (production) | 🚫 Pedro's EXPLICIT approval ONLY | When Pedro explicitly says to deploy |

---

## Commit Format

```sh
git add <specific files>          # NEVER "git add -A" blindly
git commit -m "type(scope): what happened and why"
git push origin stage             # always stage, never main unless approved
```

Types: `feat | fix | refactor | style | test | docs | chore`

---

## When You Are Unsure — ASK (RED LINE #4)

**Any doubt = full stop. Do not proceed until Pedro answers.**

This includes:
- Which teaching materials to feature on the site
- How to organize the docs folders
- Whether to publish specific content publicly
- Design or branding decisions
- Which branch to push to
- Whether to deploy to production
- Anything where you catch yourself writing "I'll assume…" or "probably…" or "I think…"

---

## `.ai/` Files — Update Every Session

| File | When to update |
|------|----------------|
| `history.md` | After every session — append dated entry |
| `tasks.md` | Mark completed tasks, add newly discovered tasks |
| `plan.txt` | Mark completed steps `[x]`, update status |
| `decisions.md` | Record any architectural or design decision made |
| `learnings.md` | Add patterns, gotchas, validated rules |

These are Pedro's memory across all AI tools. Stale files = broken context = wasted sessions.
