# Xinhan — Architectural Decisions

## 2026-05-24 — Preview-First Deployment Workflow

**Context:** Pedro does not review code locally. He needs a live URL to see changes. Repeated miscommunication occurred about when and where to deploy.

**Decision:**
1. All work is committed to a feature branch (NOT `main`).
2. After every commit, push to that branch immediately.
3. Vercel auto-generates a preview URL for non-`main` branches.
4. Pedro reviews via the preview URL.
5. ONLY after Pedro gives explicit production approval (using one of the listed phrases) may `main` be updated.

**Consequences:**
- Pedro always has a live URL to review.
- Production is protected from accidental deployments.
- Slightly more branch management, but worth the safety.

**Agent:** Kimi (Maestro), per Pedro's instruction.

---

## 2026-05-24 — Static HTML First, Framework Later

**Context:** Xinhan needs a client-reviewable website quickly. The long-term plan may involve a framework (Next.js, etc.) but Pedro needs something static to show now.

**Decision:** Build static HTML/CSS/JS pages (`index.html`, `signin.html`, `signup.html`) for immediate client review. Migrate to a framework only when Pedro explicitly asks for it.

**Consequences:**
- Fast to build and deploy.
- No build step required.
- Future migration to a framework will require a rewrite.

**Agent:** Kimi (Maestro), per Pedro's instruction.

---

## 2026-05-24 — Unified Pepe/Claudino Protocol System (v7.2)

**Context:** Pedro has 13+ repos across GitHub. Each had fragmented or outdated protocol files (v6.1, v9.0, none at all). Setting up protocols for new projects required manual copying and conversation with AI agents.

**Decision:**
1. Create a single universal master protocol at `~/.config/claudino/templates/protocol.md` (v7.2).
2. Make `pepe.sh` fully self-installing — it creates templates, Kimi hooks, and claudino templates on first run.
3. `pep` launches Kimi with auto-injected protocol via `SessionStart` hook.
4. `claude-code` launches Claude Code with `CLAUDE.md` auto-generated from the master protocol.
5. Pedro's existing `cld`/`claudino` OpenCode launcher is preserved untouched.
6. All repos share the same protocol source. Update once → all LLMs everywhere get it.

**Consequences:**
- Zero setup for new projects. `cd` into any folder → protocol auto-scaffolds.
- No more "setup conversation" with AI agents.
- Risk: updating the master protocol overwrites project-specific rules in generic repos. Astrolaby's v9.0 custom protocol is protected by version detection.

**Agent:** Kimi (Maestro)

---

## Template

```
## YYYY-MM-DD — <Decision Title>

**Context:** <what problem were we solving>

**Decision:** <what we decided to do>

**Consequences:** <trade-offs, what this enables or prevents>

**Agent:** <who made the decision>
```
