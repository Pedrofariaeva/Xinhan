# Xinhan — Claude Code Instructions

> **Read `.ai/protocol.md` first. That file contains all the rules.**
> This file only adds Claude Code-specific context on top.

---

## Startup Protocol (EVERY session, in order)

Run these commands first:
```sh
git branch --show-current
git log --oneline -5
```

Then read in order:
1. `.ai/protocol.md` ← THE RULES (start here, every session)
2. `.ai/context.md` ← Project overview, stack, key paths
3. `.ai/plan.txt` ← Current roadmap and priorities
4. `.ai/tasks.md` ← Pending / in-progress / completed tasks
5. `.ai/history.md` (last 30 lines) ← What happened last session
6. `.ai/decisions.md` ← Architectural decisions already made
7. `.ai/learnings.md` ← Patterns, gotchas, validated rules

Then **confirm with Pedro** before touching anything:
> "I'm on branch `<branch>`. Last commit: `<message>`. Ready for instructions."

**Do NOT start coding before Pedro responds to this confirmation.**

---

## Agent Reporting Rule

You are NOT the lead agent. **Kimi is the Maestro.**

After every session, you MUST:
1. Write session summary to `.ai/history.md`
2. Update `.ai/tasks.md`
3. Add a note in `.ai/tasks.md` under `## 📬 Reports to Maestro`
4. Notify Kimi of what you did

---

## RED LINES (from protocol.md)

- NEVER push or merge to `main` without Pedro explicitly saying "push to main"
- NEVER push broken builds — run quality checks before every commit
- NEVER commit without updating `.ai/` files
- NEVER assume when you have a doubt — ASK PEDRO FIRST
- NEVER modify `.env` files without asking first
- NEVER start coding without doing the Startup Protocol first

---

## Before You Write Any Code — Mandatory Pre-Coding Check

1. **State what you understood** — repeat back what Pedro asked for
2. **State what files you will change** — list them explicitly
3. **State any assumptions** — if you have ANY, that is a question for Pedro
4. **Wait for Pedro to say "yes, go ahead"**

---

## Before Every Commit — Mandatory Pre-Commit Checklist

- [ ] Committing to the correct branch (NOT main unless Pedro said so)
- [ ] `.ai/history.md` updated with what was done and why
- [ ] `.ai/tasks.md` updated (completed items moved, new items added)
- [ ] `.ai/plan.txt` updated (completed steps marked [x])
- [ ] No files with secrets added
- [ ] `git add` lists only files I intentionally changed

---

## Exit Protocol — Triggered by "exit" or "stop"

When Pedro says to stop:
1. Append to `.ai/history.md`
2. Update `.ai/tasks.md`
3. Update `.ai/plan.txt`
4. Update `.ai/decisions.md` (if architectural choices made)
5. Update `.ai/learnings.md` (if new patterns discovered)

Then reply: **"✓ Session saved."** and stop.
